#!/bin/bash

# Make sure response chance has a default value if it's not set
if [ -v "$RESPONSE_CHANCE" ];
then
    RESPONSE_CHANCE = 0.25;
fi


if [ "$1" == "--genmodel" ]; then
    python3 -u /chat/main.py --genmodel
else 
    if [ -v "$DISCORD_TOKEN" ];
    then
        echo "Missing discord token. Please set it as DISCORD_TOKEN environment variable and try again";
        exit -1
    fi
    python3 -u /chat/main.py --token=$DISCORD_TOKEN --response_chance=$RESPONSE_CHANCE
fi
