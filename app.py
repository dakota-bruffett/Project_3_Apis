from flask import Flask, render_template, request
import requests
from artistAPI import main as req_musicbrainz_info

from spotifyAPI import get_spotify_artist_info

from youtube_api import get_youtube_videos

app = Flask(__name__)


@app.route('/')  # home page
def homepage():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    print(data)
    value = "{{Music.data}}"
    name = "Music.db"
    value = request.form.get('Music.db')
    return 'saved'


@app.route('/get_artist')  # will get the artist info from the API
def get_artist_info_route():
    # safer - return None if no username
    # safer - return None if no username
    artist = request.args.get('artist-Input')

    # Using different API modules and passing in users' artist input value for the call
    returnUser = req_musicbrainz_info(artist)
    # Spotify will currently return information for artist's Stage name, followers count, artist image,albums w/images, and top tracks w/images
    spotify_information = get_spotify_artist_info(artist)

    artist_video = get_youtube_videos(artist)

    # Checking if all information on artist is  not found for both api calls, return no artist found message template, else render template with their information

    # If we get a None , we should display a no info found on our template.
    if spotify_information is None and returnUser is None:
        return render_template('artist.html', returnUser=returnUser, spotify_information=spotify_information)
    else:
        #  Here we will return all the info that we get to create our Bio

        return render_template('artist.html', returnUser=returnUser, spotify_information=spotify_information,  artist_video=artist_video)  # render our data, and send it to the html file to display.\

    # if returnUser == None:
    #     return render_template('artist.html', artistName='No artist found.')
    # else:
    #     # render our data, and send it to the html file to display.
    #     return render_template('artist.html', artistName=returnUser)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
