#!/usr/bin/python

import subprocess
from subprocess import PIPE, STDOUT

command = subprocess.run(["playerctl", "metadata", "-f", "{{xesam:artist}} - {{xesam:title}}"], stdout=PIPE, text=True, stderr=STDOUT)
playing = command.stdout.strip()

max_len = 30

if len(playing) >= max_len:
    playing = playing[:max_len - 3] + "..."

print(playing) 