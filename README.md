## discord gpt2 chatbot
uses Python 3

Bot responds to mentions and also has a 25% chance of responding to random messages. Bot can also briefly remember previous messages and use their context. 

#### To train (non docker):
Run `python3 main.py --genmodel` to train.
Requires a .txt file of the text channel history to be placed in the same directory as name called "chat.txt". An example of the chat.txt format is provided. It's defaulted to the 355M dataset, but you can change its value in main.py and in Bot/ai.py.

### To train (docker):
Requires an nvidia GPU unfortunately (unless you use the non-gpu version). Make sure you have docker-nvidia installed ([guide](https://josehoras.github.io/tensorflow-with-gpu-using-docker-and-pycharm/))

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
