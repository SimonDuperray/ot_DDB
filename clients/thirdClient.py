import discord
import asyncio
import time
from random import randint

def thirdBot():
    client = discord.Client()
    TOKEN = "NzIyMTIzMjY4NTI5NzE3MjQ5.Xuef5w.oqa9q24WjWYXowUqmawufvfMTis"
    receive = ["Je veux commencer le Python", "Regardez mon site", "Voila mon projet", "Je n'y arrive pas", "C'est trop dur", "Bonjoir", "J'arrete la programmation"]
    send = ["coucou", "salut", "ca va ?", "au revoir", "je deco", "++", "vous pouvez m'aider ?"]
    @client.event
    async def on_ready():
        print("===================")
        print("Bot 3 connected")
        print("===================")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        time.sleep(5)

        if message.content == "?close":
            await client.close()

        if message.content in receive:
            await message.channel.send(send[randint(0, len(send)-1)])
            
    client.run(TOKEN)
thirdBot()