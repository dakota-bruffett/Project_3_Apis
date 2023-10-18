from flask import Flask, render_template, request
import requests
from artistAPI import main as req_musicbrainz_info

from spotifyAPI import get_spotify_artist_info

app = Flask(__name__)


@app.route('/')  # home page
def homepage():
    return render_template('index.html')

@app.route('/get_artist') # will get the artist info from the API
def get_artist_info_route():
    # safer - return None if no username
    artist = request.args.get('artist-Input') # safer - return None if no username

    # Using different API modules and passing in users' artist input value for the call
    returnUser = req_musicbrainz_info(artist)
    # Spotify will currently return information for artist's Stage name, followers count, artist image,albums w/images, and top tracks w/images
    spotify_information = get_spotify_artist_info(artist)

    # Checking if all information on artist is  not found for both api calls, return no artist found message template, else render template with their information
    if spotify_information is None and returnUser == None: # If we get a None , we should display a no info found on our template.
         return render_template('artist.html', artistName= 'No info found.')
    else:
        #  Here we will return all the info that we get to create our Bio
         return render_template('artist.html', artistName= returnUser[0], artistCountry = returnUser[1], artistCity = returnUser[2],
                                artistGender = returnUser[3],  artistBirth = returnUser[4], artistMusic = returnUser[5],
                                 spotify_information=spotify_information ) # render our data, and send it to the html file to display.\
    
    # if returnUser == None:
    #     return render_template('artist.html', artistName='No artist found.')
    # else:
    #     # render our data, and send it to the html file to display.
    #     return render_template('artist.html', artistName=returnUser)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
