#!/bin/bash

if [ $1 == "--genmodel" ]; then
    /chat/main.py --genmodel
else 
    /chat/main.py --token=$DISCORD_TOKEN
fi
