import random
import discord
from .ai import ChatAI

class ChatBot(discord.Client):
    """ChatBot handles discord communication. This class runs its own thread that
    persistently watches for new messages, then acts on them when the bots username
    is mentioned. It will use the ChatAI class to generate messages then send them
    back to the configured server channel.

    ChatBot inherits the discord.Client class from discord.py
    """

    def __init__(self) -> None:
        self.model_name = "355M" # Overwrite with set_model_name()
        super().__init__()


    async def on_ready(self) -> None:
        """ Initializes the GPT2 AI on bot startup """
        print("Logged on as", self.user)
        self.chat_ai = ChatAI() # Ready the GPT2 AI generator
        self.chat_ai.load_model() # Load the GPT2 model


    async def on_message(self, message: discord.Message) -> None:
        """ Handle new messages sent to the server channels this bot is watching """

        if message.author == self.user:
            # Skip any messages sent by ourselves so that we don't get stuck in any loops
            return

        # Check to see if bot has been mentioned
        has_mentioned = False
        for mention in message.mentions:
            if str(mention) == self.user.name+"#"+self.user.discriminator:
                has_mentioned = True
                break

        # Only respond randomly (or when mentioned), not to every message
        if random.random() > float(self.response_chance) and has_mentioned == False:
            return

        processed_input = self.process_input(message.content)

        response = ""
        with message.channel.typing():
            response = self.chat_ai.get_bot_response(self.model_name, message.author.nick, processed_input)

        await message.channel.send(response)


    def process_input(self, message: str) -> str:
        """ Process the input message """
        processed_input = message
        # Convert user ids to just nick names
        processed_input.replace("@"+self.user.name+"#"+self.user.discriminator, "")
        processed_input.replace("@"+self.user.name, "")
        return processed_input


    def check_if_should_respond(self, has_been_mentioned) -> bool:
        """ Check if the bot should respond to a message """
        should_respond = random.random() < self.response_chance

        return should_respond


    def set_response_chance(self, response_chance: float = 0.25) -> None:
        """ Set the response rate """
        self.response_chance = response_chance


    def set_model_name(self, model_name: str = "355M") -> None:
        """ Set the GPT2 model name """
        self.model_name = model_name
