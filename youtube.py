import yt_dlp as youtube_dl
from urllib import request as rq
import os
import pandas as pd
import re


def initizilze_yt_dlp(directory, vid_link):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": directory + "/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
        "restrictfilenames": True,
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([vid_link])


def create_download_dir(dir_name):
    path = f"{dir_name}"

    if os.path.exists(path):
        return path
    try:
        os.makedirs(path)
        return path

    except OSError:
        print("Creation of the download directory failed")

def download_tracks(playlist_dir):

    songs = pd.read_csv(playlist_dir)
    dir = create_download_dir('MP3')

    i = 0
    while i < len(songs["track"]):
        this_song = songs["track"][i]+" " + songs["artist"][i] + ' ' + 'lyrics'
        this_search = "+".join(this_song.strip().split())
        div = rq.urlopen(
            f"https://www.youtube.com/results?search_query={this_search}")

        video_ids = re.findall(r"watch\?v=(\S{11})", div.read().decode())

        if video_ids:
            url = "https://www.youtube.com/watch?v=" + video_ids[0]

            print (f'Downloading song: {this_song}')

            initizilze_yt_dlp(dir, url)

            i += 1

if __name__ == '__main__':
    pass