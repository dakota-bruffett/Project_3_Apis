import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from unittest.mock import patch

import spotifyAPI


class TestSpotify(TestCase):

    # Setting up an instance
    def setUp(self):
        # Run the instance
        self.spotify = spotifyAPI.Spotify_API()

    # Test get spotify artist information gateway function using mock values to send
    @patch('spotifyAPI.get_spotify_artist_info')
    def test_get_spotify_artist_info_gateway(self, mock_spotify_info_data):

        # Mock data to test with and setting the return value to this data
        mock_spotify_info_data.return_value = {'Name': 'The Weeknd',
                                               'albums': [{'album_name': 'Starboy (Deluxe)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2738ad8f5243d6534e03b656c8b'},
                                                          {'album_name': 'Live At SoFi Stadium',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273308f9319a3d6f6737f43b3fc'},
                                                          {'album_name': 'Avatar: The Way of Water (Original Motion Picture '
                                                           'Soundtrack)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273c8044633efdd0e991224e197'},
                                                          {'album_name': 'Dawn FM (Alternate World)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273ade87e5f9c3764f0a1e5df64'},
                                                          {'album_name': 'Dawn FM',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2734ab2520c2c77a1d66b9ee21d'},
                                                          {'album_name': 'After Hours (Deluxe)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273ef017e899c0547766997d874'},
                                                          {'album_name': 'After Hours',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36'},
                                                          {'album_name': 'My Dear Melancholy,',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2731f6a2a40bb692936879db730'},
                                                          {'album_name': 'Starboy',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452'},
                                                          {'album_name': 'Beauty Behind The Madness',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2737fcead687e99583072cc217b'},
                                                          {'album_name': 'Kiss Land',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2730cc6c8a864d2d16a2bc507d4'},
                                                          {'album_name': 'Trilogy',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273b5d7c1fb40878285bc547649'},
                                                          {'album_name': 'Echoes Of Silence (Original)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b27336fb79728dbb379579cef97e'},
                                                          {'album_name': 'Thursday (Original)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273e01c2631218e2de27765b7d5'},
                                                          {'album_name': 'House Of Balloons (Original)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273274b406a7e18acebcf743079'},
                                                          {'album_name': 'Another One Of Me (feat. 21 Savage)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b2730b976123dcdaf4d60fb7ca2c'},
                                                          {'album_name': 'K-POP',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273893489768de0c42b4d217b82'},
                                                          {'album_name': 'K-POP (Chopped & Screwed)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b273dd8912dfae6121b0e25bcaec'},
                                                          {'album_name': 'The Idol Episode 5 Part 2 (Music from the HBO '
                                                           'Original Series)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b27338b9ba68af98c3c0855b47ee'},
                                                          {'album_name': 'The Idol Episode 5 Part 1 (Music from the HBO '
                                                           'Original Series)',
                                                           'image': 'https://i.scdn.co/image/ab67616d0000b27337a61e7106ce1b3628e4af8d'}],
                                               'followers': 73324485,
                                               'picture': 'https://i.scdn.co/image/ab6761610000e5eb214f3cf1cbe7139c1e26ffbb',
                                               'top_tracks': [{'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452',
                                                               'popularity': 94,
                                                               'preview_link': None,
                                                               'track_name': 'Starboy'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b273a048415db06a5b6fa7ec4e1a',
                                                               'popularity': 90,
                                                               'preview_link': None,
                                                               'track_name': 'Die For You'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b2734c8f092adc59b4bf4212389d',
                                                               'popularity': 93,
                                                               'preview_link': None,
                                                               'track_name': 'Popular (with Playboi Carti & Madonna) - Music '
                                                               'from the HBO Original Series'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b27313e54d6687e65678d60466c2',
                                                               'popularity': 93,
                                                               'preview_link': None,
                                                               'track_name': "Creepin' (with The Weeknd & 21 Savage)"},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36',
                                                               'popularity': 92,
                                                               'preview_link': None,
                                                               'track_name': 'Blinding Lights'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b2738ad8f5243d6534e03b656c8b',
                                                               'popularity': 84,
                                                               'preview_link': None,
                                                               'track_name': 'Die For You (with Ariana Grande) - Remix'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b273a048415db06a5b6fa7ec4e1a',
                                                               'popularity': 88,
                                                               'preview_link': None,
                                                               'track_name': 'Stargirl Interlude'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36',
                                                               'popularity': 89,
                                                               'preview_link': None,
                                                               'track_name': 'Save Your Tears'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452',
                                                               'popularity': 89,
                                                               'preview_link': None,
                                                               'track_name': 'Reminder'},
                                                              {'image': 'https://i.scdn.co/image/ab67616d0000b273893489768de0c42b4d217b82',
                                                               'popularity': 87,
                                                               'preview_link': 'https://p.scdn.co/mp3-preview/011ff5d71b1fad87bc1f4bed5a1abab3e0500426?cid=c572c383999a4c658ee57597e802d157',
                                                               'track_name': 'K-POP'}]}

        # Call
        retrieve_Spotify_artist_data = spotifyAPI.get_spotify_artist_info(
            'The Weeknd')

        # # Expected results
        expected_artist_data = {'Name': 'The Weeknd',
                                'albums': [{'album_name': 'Starboy (Deluxe)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2738ad8f5243d6534e03b656c8b'},
                                           {'album_name': 'Live At SoFi Stadium',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273308f9319a3d6f6737f43b3fc'},
                                           {'album_name': 'Avatar: The Way of Water (Original Motion Picture '
                                            'Soundtrack)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273c8044633efdd0e991224e197'},
                                           {'album_name': 'Dawn FM (Alternate World)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273ade87e5f9c3764f0a1e5df64'},
                                           {'album_name': 'Dawn FM',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2734ab2520c2c77a1d66b9ee21d'},
                                           {'album_name': 'After Hours (Deluxe)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273ef017e899c0547766997d874'},
                                           {'album_name': 'After Hours',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36'},
                                           {'album_name': 'My Dear Melancholy,',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2731f6a2a40bb692936879db730'},
                                           {'album_name': 'Starboy',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452'},
                                           {'album_name': 'Beauty Behind The Madness',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2737fcead687e99583072cc217b'},
                                           {'album_name': 'Kiss Land',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2730cc6c8a864d2d16a2bc507d4'},
                                           {'album_name': 'Trilogy',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273b5d7c1fb40878285bc547649'},
                                           {'album_name': 'Echoes Of Silence (Original)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b27336fb79728dbb379579cef97e'},
                                           {'album_name': 'Thursday (Original)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273e01c2631218e2de27765b7d5'},
                                           {'album_name': 'House Of Balloons (Original)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273274b406a7e18acebcf743079'},
                                           {'album_name': 'Another One Of Me (feat. 21 Savage)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b2730b976123dcdaf4d60fb7ca2c'},
                                           {'album_name': 'K-POP',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273893489768de0c42b4d217b82'},
                                           {'album_name': 'K-POP (Chopped & Screwed)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b273dd8912dfae6121b0e25bcaec'},
                                           {'album_name': 'The Idol Episode 5 Part 2 (Music from the HBO '
                                            'Original Series)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b27338b9ba68af98c3c0855b47ee'},
                                           {'album_name': 'The Idol Episode 5 Part 1 (Music from the HBO '
                                            'Original Series)',
                                            'image': 'https://i.scdn.co/image/ab67616d0000b27337a61e7106ce1b3628e4af8d'}],
                                'followers': 73324485,
                                'picture': 'https://i.scdn.co/image/ab6761610000e5eb214f3cf1cbe7139c1e26ffbb',
                                'top_tracks': [{'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452',
                                                'popularity': 94,
                                                'preview_link': None,
                                                'track_name': 'Starboy'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b273a048415db06a5b6fa7ec4e1a',
                                                'popularity': 90,
                                                'preview_link': None,
                                                'track_name': 'Die For You'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b2734c8f092adc59b4bf4212389d',
                                                'popularity': 93,
                                                'preview_link': None,
                                                'track_name': 'Popular (with Playboi Carti & Madonna) - Music '
                                                'from the HBO Original Series'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b27313e54d6687e65678d60466c2',
                                                'popularity': 93,
                                                'preview_link': None,
                                                'track_name': "Creepin' (with The Weeknd & 21 Savage)"},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36',
                                                'popularity': 92,
                                                'preview_link': None,
                                                'track_name': 'Blinding Lights'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b2738ad8f5243d6534e03b656c8b',
                                                'popularity': 84,
                                                'preview_link': None,
                                                'track_name': 'Die For You (with Ariana Grande) - Remix'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b273a048415db06a5b6fa7ec4e1a',
                                                'popularity': 88,
                                                'preview_link': None,
                                                'track_name': 'Stargirl Interlude'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36',
                                                'popularity': 89,
                                                'preview_link': None,
                                                'track_name': 'Save Your Tears'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452',
                                                'popularity': 89,
                                                'preview_link': None,
                                                'track_name': 'Reminder'},
                                               {'image': 'https://i.scdn.co/image/ab67616d0000b273893489768de0c42b4d217b82',
                                                'popularity': 87,
                                                'preview_link': 'https://p.scdn.co/mp3-preview/011ff5d71b1fad87bc1f4bed5a1abab3e0500426?cid=c572c383999a4c658ee57597e802d157',
                                                'track_name': 'K-POP'}]}

        # Assert equal test if same response as mock data and response
        self.assertEqual(retrieve_Spotify_artist_data, expected_artist_data)

    # Test token refresh access
    @patch('spotifyAPI.requests.post')
    def test_refresh_Spotify_access_token_is_successful(self, mock_data):
        # Mock/dummy response of HTTP response like
        mock_response = Mock()

        # Dummy Status code (from Mock() object for requests post)
        # 200 is successful code
        mock_response.status_code = 200

        # Dummy method to return this object of response ("Json"  data of access_token and expiration ) when a post request is made
        mock_response.json.return_value = {
            'access_token': 'johnSmith1234567',
            'expires_in': 3600
        }

        # Mock data is context of requests.post and set the return values to be "dummy http response" to be called and test.
        mock_data.return_value = mock_response

        # Call
        self.spotify.refresh_Spotify_access_token()

        # Assert equal to each other
        self.assertEqual(self.spotify.access_token, 'johnSmith1234567')


if __name__ == '__main__':
    unittest.main()
