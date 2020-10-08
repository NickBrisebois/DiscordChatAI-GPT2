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

        has_mentioned = False
        for mention in message.mentions:
            if str(mention) == self.user.name+"#"+self.user.discriminator:
                has_mentioned = True
                break;


        if random.random() < BOT_RESPONSE_CHANCE or has_mentioned == True:
            msg = message.content
        else:
            self.chat_ai.add_to_history(message.author.name, message.content)
            return

        msg = message.content
        msg.replace("@"+self.user.name+"#"+self.user.discriminator, "")
        msg.replace("@"+self.user.name, "")

        async with message.channel.typing():
            response = self.chat_ai.get_bot_response(message.author.name, msg)

        for resp in response:
            # look for mentions
            new_resp = resp
            for word in resp.split():
                if word.startswith("@"):
                    for member in message.channel.members:
                        if word == "@"+member.name:
                            new_resp = new_resp.replace(word, member.mention)
            
            await message.channel.send(new_resp)
