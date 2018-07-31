#!/bin/bash

# Set Display


# Set working directory
cd "$(dirname "$0")"

# PulseAudio restart
echo "Kill pulseaudio"
killall pulseaudio
echo "Restart pulseaudio"
/usr/bin/pulseaudio --start -D --log-target=syslog

export GOOGLE_APPLICATION_CREDENTIALS=./keys/account.json

source ./venv/bin/activate
echo "Run"
export DISPLAY=":0.0"
python speech.py
killall -9 vala-terminal
