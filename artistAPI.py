import requests
import os
from pprint import pprint
# Create out empty list 
BioList = []
listKeys = ['name','country','city','gender','birthday','music']
NoInfo = ['not found','not found','not found','not found','not found','not found']
# Our main method will call the other methods, and will return all the info that we required.
def main(name):
    infoReturn = get_Artist(name)
    listofArtist = extract_artist_info(infoReturn)

    if listofArtist is None:   #If that info is not valid, we will return a None
        DataArtist = create_BioDictionary(listKeys, NoInfo)
        return DataArtist
    else:
        DataArtist = create_BioDictionary(listKeys,listofArtist)
        return DataArtist

def get_Artist(artistName):
    #search for the artist in our API musicbrainz
    searchArt = f'https://musicbrainz.org/ws/2/artist?query={artistName}&fmt=json'
    try:
        responseArtist = requests.get(searchArt).json()
        tryGetNameArtist = responseArtist['artists'][0]['aliases'][0]['sort-name'] # try to get an Artist from the data. if not we retunr the error.

        return responseArtist
    # if artist is not found, we will send an excepction and return None
    except Exception as exc:
        print(exc)
        print('The artist was not found, sorry!')
        return None


#Extract the info of the artist to do a Bio
def extract_artist_info(jsonData):
    if jsonData is not None:
        BioList.clear()
        try:
                # data : Getting all the data for the Bio and save it in a list.
            realName = jsonData['artists'][0]['aliases'][0]['sort-name']
            Artist_country = jsonData['artists'][0]['area']['name']
            Artist_City = jsonData['artists'][0]['begin-area']['name']

            artist_Birthday = jsonData['artists'][0]['life-span']['begin']
            Music_Type = jsonData['artists'][0]['tags'][0]['name']
            # if the artist is a band we will not have a gender 
            if (jsonData['artists'][0]['gender'] is not None):
                Artist_gender = jsonData['artists'][0]['gender']
            BioList.extend((realName,Artist_country,Artist_City,Artist_gender,artist_Birthday,Music_Type))
        # Here we return the info in our list 
            return BioList
        except Exception as exc:
            print(exc)
            print('ERROR')
            Artist_gender = 'band'
            BioList.extend((realName,Artist_country,Artist_City,Artist_gender,artist_Birthday,Music_Type))
            return BioList
    else: 
        return None


def create_BioDictionary(keys, values):
    BioResult = {} 
    for key, value in zip(keys, values):
        BioResult[key] = value
    return BioResult

