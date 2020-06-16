import discord
import asyncio
import time
from random import randint

def secondBot():
    client = discord.Client()
    TOKEN = "NzIyMTIzMTE5NzMyNTg4NjE0.Xuef2g.AmKleKiu1EPwf-TDN_mKgm6VUMo"
    receive = ["j'ai un soucis avec mon bot", "Mon code fonctionne, merci", "help", "a l'aide", "c'est tout pour moi", "merci", "allez, salut"]
    send = ["Je veux commencer le Python", "Regardez mon site", "Voila mon projet", "Je n'y arrive pas", "C'est trop dur", "Bonjoir", "J'arrete la programmation"]
    @client.event
    async def on_ready():
        print("===================")
        print("Bot 2 connected")
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
secondBot()