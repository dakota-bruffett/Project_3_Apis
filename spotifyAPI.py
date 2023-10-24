import requests
import os
import time
from pprint import pprint
import logging
from dotenv import load_dotenv

# Note: Need to make a spotify dev account and create app to be able have access to client id and secret key.


# Logging set up
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.INFO)


# Spotify API keys for API calls interaction

class Spotify_API:
    # Spotify API endpoint calls URL
    SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
    ALBUMS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/albums'
    TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

    def __init__(self):

        load_dotenv()
        # Spotify Client ID
        self.SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']

        # Spotify Secret Client ID
        self.SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

        # Access token that is needed for every api call
        self.access_token = None

        # Token Expires in 1 hour
        self.token_expiration = None

        self.refresh_Spotify_access_token()

        # Make sure you have both client id and secret id set up first. Logging should give corresponding key pair values if set up correctly for environment variables
        logging.info(f"Client ID: {self.SPOTIFY_CLIENT_ID}")
        logging.info(f"Secret ID: {self.SPOTIFY_CLIENT_SECRET}")

    # # A new auth key is required every time after the key expires in 1 hour.
    # Need to send a request to spotify token end point to get a new access token and also providing necessary data to the URL such as client ID and secret key

    def refresh_Spotify_access_token(self):
        # Spotify's token endpoint URL
        SPOTIFY_TOKEN_ENDPOINT = 'https://accounts.spotify.com/api/token'

        # Make a post request to Token endpoint and get necessary return for an access token
        # Example curl request that requests  and uses data needed for a valid access  token
        # curl -X POST "https://accounts.spotify.com/api/token" \
        #  -H "Content-Type: application/x-www-form-urlencoded" \
        #  -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"
        token_response = requests.post(SPOTIFY_TOKEN_ENDPOINT, data={
            'grant_type': 'client_credentials',
            'client_id': self.SPOTIFY_CLIENT_ID,
            'client_secret': self.SPOTIFY_CLIENT_SECRET,
        })

        # From the response, the data that will be received are, access_token, token_type, and expires_in with their values. Need access token value from those object variables in order to use the API calls.

        token_data = token_response.json()

        # Extracting the access token
        self.access_token = token_data.get('access_token')

        # Set expiration time for token from JSON response (In seconds) Example - "expires_in": 3600
        # time.time() returns the current time in seconds since the Epoch
        self.token_expiration = time.time() + token_data.get('expires_in')

    # Handling and checking the time for access token expiration
    def check_token_expiration(self):
        if self.token_expiration is None:
            return True  # Return true if token have expired

        # Check current time is over the expiration time
        return time.time() > self.token_expiration

    # Providing additional information for request
    # Handling authorization, what type of  application data format is accepted for client and can process, and  what content format is parsed to users, which is JSON.
    def get_headers(self):
        return {
            'Accept': 'application/json',
            'ContentType': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

    def get_Artist(self, artist_Name):

        # Check if token expired (Over time limit), then get a new access token before using access token to call Artist data
        if self.token_expiration:
            self.refresh_Spotify_access_token()

        headers = self.get_headers()

        params = {

            'q': artist_Name,
            'type': 'artist',
            'limit': '1'

        }

        try:
            # Searching for the artists
            response_Artist = requests.get(
                self.SEARCH_ENDPOINT, headers=headers, params=params)

            if response_Artist.status_code != 200:
                print('Error:', response_Artist.status_code)
                print('Response:', response_Artist.text)

                self.refresh_Spotify_access_token()

                response_Artist = requests.get(
                    self.SEARCH_ENDPOINT, headers=headers, params=params)

            return response_Artist.json()

        except Exception as e:
            logging.exception(e)

            print(f'Error fetching Spotify\'s artist API')

    def extract_artist_info(self, json_Data):

        # Additional information used for req
        headers = self.get_headers()

        if not json_Data or 'artists' not in json_Data or not json_Data['artists']['items']:
            print('Artists not found or invalid response')
            pprint(json_Data)  # Should print in the json res why
            return None

        try:

            # Artists required JSON DATA Extraction
            artist = json_Data['artists']['items'][0]

            # If the first artist is found with that name, get their necessary  credentials
            if artist:
                # Need artist id for searching their information, spotify uses artist id to find that artist  in their db
                artistID = artist.get('id')

                # Stage name
                artist_Name = artist.get('name')

                # Information about the followers  count of the artist.
                artist_Followers = artist.get('followers').get('total')
                # Cover photo from spotify, 'May need to use MusicBrainz for more pictures'
                images = artist.get('images')

                if images:
                    # URL of first image (Only image)
                    artist_Picture = images[0]['url']

                else:
                    # In the render part, may need to render a default picture if no artist picture is provided
                    return None

            # Lists of Albums from requested artist
            response_From_Albums_EndPoint = requests.get(
                self.ALBUMS_ENDPOINT.format(id=artistID), headers=headers)

            list_Of_Artists_Albums = [{'album_name': album['name'],
                                       'image': album['images'][0]['url'] if album['images'] else None}
                                      for album in response_From_Albums_EndPoint.json()['items']]

            # Top tracks

            params = {
                'market': 'US'
            }

            response_From_Artists_Top_Tracks = requests.get(
                self.TOP_TRACKS_ENDPOINT.format(id=artistID), headers=headers, params=params)

            response_From_Artists_Top_Tracks.raise_for_status()

            # Artists' top tracks JSON response
            top_Tracks = response_From_Artists_Top_Tracks.json().get('tracks', [])

            # Extracting artists' top tracks and their images
            artists_Top_Tracks = [
                {'track_name': track['name'], 'image': track['album']
                    ['images'][0]['url'] if track['album']['images'] else None}
                for track in top_Tracks if track.get('name')]

            Spotify_Artist_Info = {
                'Name': artist_Name,
                'picture': artist_Picture,
                'followers': artist_Followers,
                'albums': list_Of_Artists_Albums,
                'top tracks': artists_Top_Tracks,
            }
            pprint(Spotify_Artist_Info)

            return Spotify_Artist_Info  # Dictionary full of artist's information

        except Exception as err:
            logging.exception(err)

            print('Error Processing Artist')

    def main(self, name):
        artist_info = self.get_Artist(name)
        return self.extract_artist_info(artist_info)


Spotify_API = Spotify_API()


def get_spotify_artist_info(name):
    return Spotify_API.main(name)

# pprint(Spotify_API.main('Justin Bieber'))
