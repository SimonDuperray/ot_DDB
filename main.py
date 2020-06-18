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
    """
        FONCTIONNEL
        Fonction: Fichier principal du Bot
        Fonctionnalités: -> Détection de message
                         -> Enregistrement des messages dans le fichier csv (except bot and embed)
                         -> Déconnexion du bot
                         -> Formulaire de commandes
                         -> Histogramme (message privé)
                         -> Camembert (message privé)
                         -> Classement (message privé)
                         -> Envoi de résumé quotidien par mail (en pdf)
        Modifications:   -> Prendre en compte les messages envoyés sur le serveur (no messages privés)
                         -> Salons vocaux
                         -> Trouver les id de tous les salons (compter nb) pour fichier pdf
                         -> Utiliser des filtres pour l'heure (ne plus prendre en compte les secondes)
                         -> Newsletter (envoi automatique des mails à minuit)
    """

    # Création d'un nouveau client
    client = discord.Client()
    TOKEN = "NzIxOTg2NjMxNjc4MTY1MDM0.Xuc2kQ.B4m0n98h1yvPhzJ3imJRlSV10jg"

    # Filtres
    botsID = ['DDB#1758', 'DataDiscordBot#3453'] # ne pas prendre en compte les messages envoyés par les bots
    authorizedPseudos = ['Kartodix#2540', 'Tehistir#9627'] # personnes autorisées à utiliser les commandes
    adminClose = "Kartodix#2540" # personne autorisée à fermer le bot
    categories = ['CHANNEL', 'AUTHOR', 'CONTENT', 'DATE', 'TIME'] # labels disponibles pour les statistiques

    # Connexion du Bot au serveur
    @client.event
    async def on_ready():
        print("===================")
        print("Main Bot connected")
        print("===================")
        # Message de statut
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help to see commands"))

    # Détecteur de messages
    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return

        # Si un message est envoyé...
        if message.content:
            
            # Récupération de la date et de l'heure à laquelle le message a été envoyé
            currentDatetime = datetime.datetime.now()
            currentDate = str(currentDatetime.year)+str('/')+str(currentDatetime.month)+str('/')+str(currentDatetime.day)
            currentTime = str(currentDatetime.hour)+str(':')+str(currentDatetime.minute)+str(':')+str(currentDatetime.second)

            author = message.author

            # Initialisation et stockage des données du message dans la liste unique
            currentDataSet = []
            currentDataSet.append(message.channel)
            currentDataSet.append(message.author)
            currentDataSet.append(message.content)
            currentDataSet.append(currentDate)
            currentDataSet.append(currentTime)

            # Si ce n'est pas un bot qui envoie le message et si ce n'est pas un embed alors on l'ajoute dans le csv
            if not str(message.author) in botsID and not message.content.startswith('```'):
                with open("dataset.csv", "a", newline='') as f:
                    writer = csv.writer(f, delimiter=";")
                    writer.writerow(currentDataSet)

            # Deconnexion du bot
            if (str(message.author) == adminClose) and (str(message.content) == "?close"):
                await message.channel.send("Je dois y aller !")
                await client.close()

            # Formulaire de commandes
            if (str(message.author) in authorizedPseudos) and (str(message.content) == "?help"):
                description = ('===============\n'
                               'PARAMETRES:\n'
                               '===============\n'
                               '```'
                               '-> Paramètres disponibles:\n\n'
                               'PARAMETRE: CHANNEL / AUTHOR / DATE\n\n'
                               'nb: précision du classement\n'
                               '```'
                               '===============\n'
                               'HISTOGRAMMES:\n'
                               '===============\n'
                               '```'
                               '-> ?hist PARAMETRE nb\n\n'
                               '```'
                               '===============\n'
                               'CAMEMBERTS:\n'
                               '===============\n'
                               '```'
                               '-> ?cam PARAMETRE nb\n\n'
                               '```'
                               '===============\n'
                               'CLASSEMENTS:\n'
                               '===============\n'
                               '```'
                               '-> ?cls PARAMETRE nb\n\n'
                               '```')
                embed = discord.Embed(title="**Formulaire de commandes**", description=description, color=0xD35400)
                await message.channel.send(embed=embed)

            # Histogramme
            if (str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?hist") and (str(message.content).split()[1] in categories):
                histogrammeBot(str(message.content.split()[1]), int(message.content.split()[2]))
                await author.send(file=discord.File('hist.png'))
                os.remove('hist.png')

            # Camembert
            if(str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?cam") and (str(message.content).split()[1] in categories) and (str(message.content).split()[2]):
                camembertBot(str(message.content).split()[1], int(message.content.split()[2]))
                await author.send(file=discord.File('cam.png'))
                os.remove('cam.png')

            # Classement
            if (str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?cls") and (str(message.content).split()[1] in categories) and (str(message.content).split()[2]):
                title="**Classement "+str(message.content).split()[1]+"**"
                cls_ = classementBot(str(message.content).split()[1], int(str(message.content).split()[2]))
                description = ""
                for i in range(len(cls_)):
                    currentPos = str(i+1)+str(". ")+str(str(" ")+str(list(cls_.keys())[i])) + str("=>") + str(list(cls_.values())[i])
                    description+= str('```css\n')+currentPos+str('```') 
                embed = discord.Embed(title=title, description=str(description), color=0x3498DB)
                await message.author.send(embed=embed)

            # Envoi du résumé par mail
            if(str(message.author) in authorizedPseudos) and (str(message.content).split()[0]=="?mail") and (str(message.content).split()[1]):
                toaddr_ = str(message.content).split()[1]
                createPdfFile()
                send_resume_email(toaddr_)
                await message.channel.send('Email envoyé! :)')
                os.remove(returnFileName())

    client.run(TOKEN)

discordBot()