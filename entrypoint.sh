#!/bin/bash

if [ "$1" == "--genmodel" ]; then
    python3 -u /chat/main.py --genmodel
else 
    python3 -u /chat/main.py --token=$DISCORD_TOKEN
fi
