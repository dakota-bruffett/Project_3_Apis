import unittest
from unittest.mock import patch, Mock
from youtube_api import get_youtube_videos

class TestYouTubeAPI(unittest.TestCase):
    @patch('youtube_api.build')
    def test_successful_request(self, mock_build):# Create a mock response for build()
        #Arrange?
        mock_response = Mock()#empty or initialized build object?
        mock_execute = Mock(return_value={'items': [{'snippet': {'title': 'Video Title 1', 'thumbnails': {'high': {'url': 'image_url'}}}, 'id': {'videoId': '123'}}]})# Create a mock execute()
        #Act??
        mock_response.search().list().execute = mock_execute
        mock_build.return_value = mock_response#create the mocked build object?

        result = get_youtube_videos('Artist Name') #Call the function with an artist name

        #Assert?
        expected_result = [{'title': 'Video Title 1', 'video_id': '123', 'url': 'image_url'}]# Check if the result contains the expected data
        self.assertEqual(result, expected_result)