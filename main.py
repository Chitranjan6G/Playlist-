import os
import json

from pyrogram import Client, filters

from youtubesearchpython import *

DOWNLOAD_PATH = "/app/DOWNLOADS/"

async def playlist_dl(c, m):
    playlists = Playlist.get(
        "https://youtube.com/playlist?list=PL_2V_PK19pH-SafYE05XZ2KeiR2w61teJ",
         mode=ResultMode.json
    )
    if "\n" in playlists:
        playlists = playlists.replace("\n", "")
    playlist_json = json.loads(playlists)

    data_json = f"{DOWNLOAD_PATH}/{m.from_user.id}.json"
    if not os.path.exists(f"{DOWNLOAD_PATH}/{m.from_user.id}/"):
        os.makedirs(f"{DOWNLOAD_PATH}/{m.from_user.id}/")

    with open(data_json, "w", encoding="utf8") as write_file:
        json.dump(playlist_json, write_file, indent=4)

    play_length = len(playlist_json['videos'])
    print(f"Playlist length: {play_length}")

    if "videos" in playlist_json:
        for index in range(0, len(playlist_json['videos'])):
            if (int(index) > 2) and (int(index) < 4): # You can add Range
                video_id = playlist_json['videos'][index]['id']
                print(f"Video URL {int(index) + 1} : https://youtu.be/{video_id}")
