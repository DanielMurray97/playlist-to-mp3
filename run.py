from spotify import extract_main
from youtube import download_tracks

if __name__ == "__main__":
    # test playlist link = https://open.spotify.com/playlist/2qCchlQbSqupOCZGIIZqtu?si=438f44e8368f4aa8

    # 100+ song playlist link: https://open.spotify.com/playlist/2ngKkDHzMmsX6dpX5o92Fk?si=1f22f2d968d2497b

    playlist_link = input("Please enter your playlist link:")

    file_name = "test.csv"

    extract_main(file_name, playlist_link)

    download_tracks(file_name)
