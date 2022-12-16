#!/usr/bin/env python
import os
import sys
import spotipy
import termcolor

delta_volume = int(sys.argv[1])

from main import spotipy, auth_manager
auth_manager.scope = (
    "user-read-playback-position user-read-playback-state user-modify-playback-state"
)

sp = spotipy.Spotify(auth_manager=auth_manager)

playback = sp.current_playback()
volume = playback["device"]["volume_percent"] + delta_volume

sp.volume(volume_percent=volume)

track = playback["item"]
track_id = track["id"]
image = track["album"]["images"][0]["url"]
name = track["name"]
artists_names = ", ".join(map(lambda a: a["name"], track["artists"]))
os.system(f"curl -so /tmp/spimage {image}")
message = f"{volume}% {artists_names} - {name}"
cmd = f'notify-send -i /tmp/spimage "{message}" 2> /dev/stdout'
os.system(cmd)

c_message = termcolor.colored(f"{volume}%", "yellow")
c_artists_names = termcolor.colored(artists_names, "blue")
c_name = termcolor.colored(name, "green")

colored_message = f"{c_message} {c_artists_names} - {c_name}"
print(colored_message)
