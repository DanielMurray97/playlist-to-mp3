import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import re


def spotify_session():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_SECRET_ID")

    details = SpotifyClientCredentials(client_id, client_secret)
    session = spotipy.Spotify(client_credentials_manager=details)
    return session


def extract_playlist_id(playlist_link):
    if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", playlist_link):
        playlist_url = match.groups()[0]
        return playlist_url
    else:
        raise ValueError(
            "Expected Spotify Playlist URL Format: https://open.spotify.com/playlist/"
        )
