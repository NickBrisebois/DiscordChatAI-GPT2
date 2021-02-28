## Python Discord GPT2 ChatBot

Bot responds to mentions and also has a variable chance of responding to random messages.

#### To train (non docker):
Run `python3 main.py --genmodel` to train.
Requires a .txt file of the text channel history to be placed in the same directory as name called "chat.txt". An example of the chat.txt format is provided. It's defaulted to the 355M dataset, but you can change its value in main.py and in Bot/ai.py.

### To train (docker):
Requires an nvidia GPU unfortunately (unless you use the non-gpu version which is much slower). Make sure you have docker-nvidia installed ([guide](https://josehoras.github.io/tensorflow-with-gpu-using-docker-and-pycharm/))

Build docker container: 

```
docker build -t chatai .
```

Run container: 

```
docker run --runtime=nvidia --rm chatai '--genmodel'
```

#### To test:
You can test this bot locally by running `python3 main.py -t`. It will let you input some text and it will print the AI's response.

#### To run on Discord:
 `python3 main.py --token [discord bot token]`

#### Docker environment variables:
Set TOKEN to pass in your discord token
Set RESPONSE_CHANCE to set how likely the bot is to respond (0 for no random responses, 0.25 for 25% chance, etc)
