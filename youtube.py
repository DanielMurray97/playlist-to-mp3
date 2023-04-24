import yt_dlp as youtube_dl
from urllib import request as rq
import os


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
