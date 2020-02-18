import random
import discord
from .ai import ChatAI

BOT_RESPONSE_CHANCE = 0.25


class ChatBot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)
        self.chat_ai = ChatAI()
        self.chat_ai.load_model()

    async def on_message(self, message):
        if message.author == self.user:
            return

        # The bot should reply to messages starting with !bot or just randomly
        if message.content.startswith("!bot"):
            msg = message.content[len("!bot "):]
        elif random.random() < BOT_RESPONSE_CHANCE:
            msg = message.content
        else:
            return

        async with message.channel.typing():
            response = self.chat_ai.get_bot_response(message.author.nick, msg)

        await message.channel.send(response)
