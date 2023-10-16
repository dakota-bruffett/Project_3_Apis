import requests 
import os
from pprint import pprint

BioList = [];

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


#Extract the info of the artist to do a Bio
def extract_artist_info(jsonData):

    if jsonData == None:
        return None
    else:
        BioList.clear()

        # data : Getting all the data for the Bio and save it in a list.
        realName = jsonData['artists'][0]['aliases'][0]['sort-name']
        Artist_country = jsonData['artists'][0]['area']['name']
        Artist_City = jsonData['artists'][0]['begin-area']['name']
        Artist_gender = jsonData['artists'][0]['gender']
        artist_Birthday = jsonData['artists'][0]['life-span']['begin']
        Music_Type = jsonData['artists'][0]['tags'][0]['name']

        BioList.extend((realName,Artist_country,Artist_City,Artist_gender,artist_Birthday,Music_Type))

        return BioList


