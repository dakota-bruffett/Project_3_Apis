import requests 
import os
from pprint import pprint
# Create out empty list 
BioList = [];
# Our main method will call the other methods, and will return all the info that we required.
def main(name):
    infoReturn = get_Artist(name)
    if infoReturn == None:   #If that info is not valid, we will return a None
        return None
    else:
        return extract_artist_info(infoReturn);

def get_Artist(artistName):
    #search for the artist in our API musicbrainz
    searchArt = f'https://musicbrainz.org/ws/2/artist?query={artistName}&fmt=json'
    try:
        responseArtist = requests.get(searchArt).json()
        return responseArtist
    # if artist is not found, we will send an excepction and return None
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
        try:
            # data : Getting all the data for the Bio and save it in a list.
            realName = jsonData['artists'][0]['aliases'][0]['sort-name']
            Artist_country = jsonData['artists'][0]['area']['name']
            Artist_City = jsonData['artists'][0]['begin-area']['name']
            Artist_gender = jsonData['artists'][0]['gender']
            artist_Birthday = jsonData['artists'][0]['life-span']['begin']
            Music_Type = jsonData['artists'][0]['tags'][0]['name']
            BioList.extend((realName,Artist_country,Artist_City,Artist_gender,artist_Birthday,Music_Type))
        # Here we return the info in our list 
            return BioList
        except Exception as exc:
            # If there is any error in getting any info, we will retunr a NONE, and print an error
            print(exc)
            print("Error in gettign info")
            return None
        


