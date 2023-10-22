from googleapiclient.discovery import build
import os
from pprint import pprint

api_key = os.environ['YOUTUBE_API_KEY']
api_name = 'youtube'
api_version = 'v3'

def singer_video(artist):
    try:
        yt_response = build(api_name, api_version, developerKey=api_key)#build() creates a service object takes api name and api version as arguments
        request = yt_response.search().list(
            part='snippet',#string, always will be snippet?
            maxResults=5,#unsigned integer
            order='relevance',#string, params are: date, rating, relevance, title, videoCount, or viewCount
            q=artist,#string, q is query term to search for
            type='video',#string, only retrieves a particular type of resource: channel, playlist, or video
            relevanceLanguage='en',#string
            safeSearch='moderate'#string, could be moderate, strict, or none
        )#no .execute() here?
        response = request.execute()#response will be the json turned into a python dictionary?
        
        # pprint(response)#FOR (SOLO) TESTING
        
        title = response['items'][0]['snippet']['title']#pulling out the titles of the videos
        
        video_id = response['items'][0]['id']['videoId']#will unique identify videos
        
        # print('---------------')#FOR (SOLO) TESTING
        five_video_list = []#create empty list to hold the five videos

        for item in response.get('items', []):#loop to return the value associated with the key 'items', which is a list of dictionaries. Otherwise returns empty list so it won't crash
            title = item['snippet']['title']#drilling down to pull out the title and video id, and high thumbnail parameters 
            video_id = item['id']['videoId']
            high_height = item['snippet']['thumbnails']['high']['height']#could choose betweeen default, high, or medium thumnails, which differ in size and img quality.
            high_url = item['snippet']['thumbnails']['high']['url']
            high_width = item['snippet']['thumbnails']['high']['width']
            five_video_list.append({'title': title, 
                                    'video_id': video_id, 
                                    'height': high_height, 
                                    'url': high_url, 
                                    'width': high_width})#package these items into dictionaries and add them all to the list 
        # pprint(five_video_list)#FOR (SOLO) TESTING
        return five_video_list#send back list of parameters to itentify videos

    except:#refine try-except later
        print('err')

if __name__ == '__main__':#allows module to be run solo
    singer_video(input('Artist name? '))