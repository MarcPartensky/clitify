#!/usr/bin/env python
"""
Show information about the spotify user.
"""

import os
import spotipy

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
cache_path = os.path.join(os.environ["XDG_RUNTIME_DIR"], "spotipy-cache")


redirect_uri = "http://localhost:8888/callback/"
scope = "user-read-currently-playing"


auth_manager = spotipy.oauth2.SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_path=cache_path,
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# track = sp.current_user_playing_track()

# token = auth_manager.get_cached_token()
# access_token = token["access_token"]

track = sp.currently_playing()["item"]

track_id = track["id"]
image = track["album"]["images"][0]["url"]
name = track["name"]
artists_names = ", ".join(map(lambda a: a["name"], track["artists"]))
message = f"{artists_names} - {name}"
print(message)
