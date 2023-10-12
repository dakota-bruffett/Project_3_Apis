from flask import Flask, render_template, request
import requests
from artistAPI import main as req_musicbrainz_info

from spotifyAPI import get_spotify_artist_info

app = Flask(__name__)


@app.route('/')  # home page
def homepage():
    return render_template('index.html')


@app.route('/get_artist')  # will get the artist info from the API
def get_artist_info_route():
    # safer - return None if no username
    artist = request.args.get('artist-Input')

    # Using different API modules and passing in users' artist input value for the call

    # Musicbrainz will return information
    musicbrainz_information = req_musicbrainz_info(artist)
    # Spotify will currently return information for artist's Stage name, followers count, artist image,albums w/images, and top tracks w/images
    spotify_information = get_spotify_artist_info(artist)

    # Checking if all information on artist is  not found for both api calls, return no artist found message template, else render template with their information
    if spotify_information is None and musicbrainz_information is None:
        return render_template('artist.html', artistName='No artist found.')

    else:
        return render_template('artist.html', musicbrainz_information=musicbrainz_information, spotify_information=spotify_information)

    # if returnUser == None:
    #     return render_template('artist.html', artistName='No artist found.')
    # else:
    #     # render our data, and send it to the html file to display.
    #     return render_template('artist.html', artistName=returnUser)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
