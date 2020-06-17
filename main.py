import discord
import datetime
import csv
import os
from analysis import histogrammeBot
from analysis import classementBot
from analysis import camembertBot
from sendmail import send_resume_email
from createpdf import createPdfFile
from createpdf import returnFileName

def discordBot():
    client = discord.Client()
    TOKEN = "NzIxOTg2NjMxNjc4MTY1MDM0.Xuc2kQ.B4m0n98h1yvPhzJ3imJRlSV10jg"
    botsID = ['DDB#1758', 'DataDiscordBot#3453']
    authorizedPseudos = ['Kartodix#2540', 'Tehistir#9627']
    adminClose = "Kartodix#2540"
    categories = ['CHANNEL', 'AUTHOR', 'CONTENT', 'DATE', 'TIME']

    @client.event
    async def on_ready():
        print("===================")
        print("Main Bot connected")
        print("===================")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help to see commands"))

    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return

        # si n'importe quel mesage est envoyé dans n'importe quel channel du serveur...
        if message.content:
            currentDatetime = datetime.datetime.now()
            currentDate = str(currentDatetime.year)+str('/')+str(currentDatetime.month)+str('/')+str(currentDatetime.day)
            currentTime = str(currentDatetime.hour)+str(':')+str(currentDatetime.minute)+str(':')+str(currentDatetime.second)
            author = message.author
            currentDataSet = []
            currentDataSet.append(message.channel)
            currentDataSet.append(message.author)
            currentDataSet.append(message.content)
            currentDataSet.append(currentDate)
            currentDataSet.append(currentTime)
            # si ce n'est pas un bot qui envoie le message et si ce n'est pas un embed alors on l'ajoute dans le csv
            if not str(message.author) in botsID and not message.content.startswith('```'):
                with open("dataset.csv", "a", newline='') as f:
                    writer = csv.writer(f, delimiter=";")
                    writer.writerow(currentDataSet)

            # deconnexion du bot
            if (str(message.author) == adminClose) and (str(message.content) == "?close"):
                await message.channel.send("Je dois y aller !")
                await client.close()

            # formulaire de commandes
            if (str(message.author) in authorizedPseudos) and (str(message.content) == "?help"):
                description = ('===============\n'
                               'Graphiques:\n'
                               '===============\n'
                               '```'
                               '-> ?graph PARAMETRE\n\n'
                               '-> Liste des paramètres: AUTHOR CHANNEL DATE (TIME)'
                               '```'
                               '===============\n'
                               'Classements:\n'
                               '===============\n'
                               '```'
                               '-> ?cls PARAMETRE\n\n'
                               '-> Liste des paramètres: AUTHOR CHANNEL DATE (TIME)'
                               '```')
                embed = discord.Embed(title="**Formulaire de commandes**", description=description, color=0xD35400)
                await message.channel.send(embed=embed)

            # histogramme
            if (str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?hist") and (str(message.content).split()[1] in categories):
                histogrammeBot(str(message.content.split()[1]), int(message.content.split()[2]))
                await author.send(file=discord.File('hist.png'))
                os.remove('hist.png')

            # camembert
            if(str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?cam") and (str(message.content).split()[1] in categories) and (str(message.content).split()[2]):
                camembertBot(str(message.content).split()[1], int(message.content.split()[2]))
                await author.send(file=discord.File('cam.png'))
                os.remove('cam.png')

            # classement
            if (str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?cls") and (str(message.content).split()[1] in categories) and (str(message.content).split()[2]):
                title="**Classement "+str(message.content).split()[1]+"**"
                description=str(classementBot(str(message.content).split()[1], int(str(message.content).split()[2])))
                embed = discord.Embed(title=title, description=description, color=0x3498DB)
                await message.author.send(embed=embed)

            # send daily resume per mail
            if(str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?mail") and (str(message.content).split()[1]):
                toaddr_ = str(message.content).split()[1]
                createPdfFile()
                send_resume_email(toaddr_)
                await message.channel.send('Email envoyé! :)')
                os.remove(returnFileName())

    client.run(TOKEN)

discordBot()