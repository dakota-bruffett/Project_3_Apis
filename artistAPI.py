import requests 
import os
from pprint import pprint

artistName1 = 'bad bunny'
def main(name):
    infoReturn = get_Artist(name)
    return extract_artist_info(infoReturn);

def get_Artist(artistName):
    #search for the artist
    searchArt = f'https://musicbrainz.org/ws/2/artist?query={artistName}&fmt=json'
    try:
        responseArtist = requests.get(searchArt).json()
        return responseArtist
    except Exception as exc:
        print(exc)
        print('The artist was not found, sorry!')
        return None


def extract_artist_info(jsonData):
    if jsonData == None:
        return None
    else:
        realName = jsonData['artists'][0]['aliases'][0]['sort-name']
        return realName
