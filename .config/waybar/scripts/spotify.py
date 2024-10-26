#!/usr/bin/python

import subprocess
import json

artist = subprocess.check_output("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/artist/{n;n;p}' | cut -d '\"' -f 2", shell=True, stderr=subprocess.DEVNULL).decode("utf-8").strip()
song = subprocess.check_output("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/title/{n;p}' | cut -d '\"' -f 2", shell=True, stderr=subprocess.DEVNULL).decode("utf-8").strip()

if song == "" or artist == "":
	print("Spotify is offline...")
else:
	song_info = artist + " - " + song

	max_len = 30
	if len(song_info) >= max_len:
		song_info = song_info[:max_len - 3] + "..."
	print(song_info)