import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os
import re
import csv


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


def track_list(session, playlist_url):
    results = session.playlist_tracks(playlist_url)
    tracks = results["items"]
    while results["next"]:
        results = session.next(results)
        tracks.extend(results["items"])
    return tracks


def extract_to_csv(file, tracks):
    with open(file, "w") as file:
        writer = csv.writer(file)

        writer.writerow(["track", "artist"])

        for track in tracks:
            name = track["track"]["name"]
            artists = ", ".join(
                [artist["name"] for artist in track["track"]["artists"]]
            )
            writer.writerow([name, artists])
