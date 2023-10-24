from googleapiclient.discovery import build
import os
from pprint import pprint
from googleapiclient.errors import HttpError
import logging
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(#set up logging settings
    level=logging.DEBUG,
    filename='youtube_api.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

api_key = os.environ['YOUTUBE_API_KEY']
api_name = 'youtube'
api_version = 'v3'

def get_youtube_videos(artist):
    try:
        yt_response = build(api_name, api_version, developerKey=api_key)#build() creates a service object takes api name and api version as arguments
        request = yt_response.search().list(
            part='snippet',#string, always will be snippet?
            maxResults=20,#unsigned integer
            order='relevance',#string, params are: date, rating, relevance, title, videoCount, or viewCount
            q=artist,#string, q is query term to search for
            type='video',#string, only retrieves a particular type of resource: channel, playlist, or video
            relevanceLanguage='en',#string
            safeSearch='moderate'#string, could be moderate, strict, or none
        )#no .execute() here?
        response = request.execute()#response will be the json turned into a python dictionary?
        # pprint(response)#FOR (SOLO) TESTING
        # print('---------------')#FOR (SOLO) TESTING
        five_video_list = extract_video_info(response)#send the json to function for parsing
        
        return five_video_list#send back list of parameters to identify videos

    except HttpError as e:# Handles related HTTP errors such trying to access unauthorized resources, server errors, connetion problems and many more...
        logging.exception(e)
        print('An http related error has occured.')
    except KeyError as e:# Handles errors related to missing dictionary keys or incorrectly formatted JSON responses
        logging.exception(e)
        print('The returned data is not in expected format.')
    except Exception as e:# Handle other unexpected exceptions
        logging.exception(e)
        print('An uexpected error has occured.')

def extract_video_info(response):
    five_video_list = []#create empty list to hold the five videos

    for item in response.get('items', []):#loop to return the value associated with the key 'items', which is a list of dictionaries. Otherwise returns empty list so it won't crash
        title = item['snippet']['title']#pulling out the titles of the videos
        video_id = item['id']['videoId']#will unique identify videos
        high_height = item['snippet']['thumbnails']['high']['height']
        high_url = item['snippet']['thumbnails']['high']['url']#could choose betweeen default, high, or medium thumnails, which differ in size and img quality.
        high_width = item['snippet']['thumbnails']['high']['width']
        five_video_list.append({'title': title, 
                                'video_id': video_id, 
                                'height': high_height, 
                                'url': high_url, 
                                'width': high_width})#package these items into dictionaries and add them all to the list 
        pprint(five_video_list)#FOR (SOLO) TESTING
    return five_video_list

if __name__ == '__main__':#allows module to be run solo
    get_youtube_videos(input('Artist name? '))