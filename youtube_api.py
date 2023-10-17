from googleapiclient.discovery import build
import os
from pprint import pprint

api_key = os.environ['YOUTUBE_API_KEY']
api_name = 'youtube'
api_version = 'v3'

artist_name = input('Artist name? ')#TEMPORARY INPUT FOR TESTING
def singer_video():#category needed here?
     
    try:
        yt_response = build(api_name, api_version, developerKey=api_key)#build() creates a service object takes api name and api version as arguments
        request = yt_response.search().list(
            part='snippet',#string, always will be snippet?
            maxResults=1,#unsigned integer
            order='relevance',#string, params are: date, rating, relevance, title, videoCount, or viewCount
            q=artist_name,#string, q is query term to search for
            type='video',#string, only retrieves a particular type of resource: channel, playlist, or video
            relevanceLanguage='en',#string
            safeSearch='moderate'#string, could be moderate, strict, or none
        )#no .execute here?
        # print(response)
        # print(search_response)
        response = request.execute()
        pprint(response)
    except:#refine try-except later
        print('err')


singer_video()#TEMPORARY FOR STARTING PROGRAM FOR TESTING





