import discord
from .ai import ChatAI

class ChatBot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)
        self.chat_ai = ChatAI()
        self.chat_ai.load_model()

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("!bot"):
            stripped_msg = message.content[len("!bot "):]
            await message.channel.send(self.chat_ai.get_bot_response(stripped_msg))

        