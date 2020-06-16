import discord
import asyncio
import time
from random import randint

def firstBot():
    client = discord.Client()
    TOKEN = "NzIyMTIyNDY5Nzc5MTc3NTgw.XuefzA.Nx_H-4l9ME9OR0LNkyNXX2DG0Y0"
    receive = ["?start", "coucou", "salut", "ca va ?", "au revoir", "je deco", "++", "vous pouvez m'aider ?"]
    send = ["j'ai un soucis avec mon bot", "Mon code fonctionne, merci", "help", "a l'aide", "c'est tout pour moi", "merci", "allez, salut"]
    @client.event
    async def on_ready():
        print("===================")
        print("Bot 1 connected")
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
firstBot()