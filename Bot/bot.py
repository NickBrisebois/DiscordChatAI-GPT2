import discord
from .ai import ChatAI

class ChatBot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)
        self.chat_ai = ChatAI()

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("!bot"):
            await message.channel.send(self.chat_ai.get_bot_response(message.content))

        