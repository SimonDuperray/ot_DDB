from reportlab.pdfgen import canvas
import datetime
from analysis import clsPdf
from analysis import graphsPdf
import os

def drawMyRuler(pdf):
    """
        FONCTIONNEL
        Paramètre: -> pdf: pdf file
        Fonction: Affichage des valeurs (x, y) sur le fichier pdf pour faciliter la mise en page
    """
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')

def createPdfFile():
    """ 
        FONCTIONNEL
        Fonction: Création du fichier pdf
        STRUCTURE:  -> Titre (date actuelle en dynamique)
                    -> Classements: * channels
                                    * authors
                    -> Statistiques Globales: * nb total membres
                                              * membres en plus que la veille
                                              * nb text chanel
                                              * nb voc chanel
                    -> Graphiques: * Histogramme => channels
                                   * Histogramme => authors
                                   * Camembert => channels
                                   * Camembert authors
        Modifications: -> Ajout des camemberts  
                       -> Compléter les statistiques globales
    """

    # Récupération de la date actuelle pour rafraichir le titre du pdf
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.day)+str(' - ')+str(todayDate.month)+str(' - ')+str(todayDate.year)
    global fileName
    fileName = "daily_resume" + str(todayDate.day) + str(todayDate.month) + str(todayDate.year) + ".pdf"
    documentTitle = "DailyResume"
    title = "ACTIVITE QUOTIDIENNE DU " + currentDate

    # Initialisation du pdf
    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    # Titre et ligne horizontale
    pdf.drawString(190, 770, title)
    pdf.line(60, 750, 540, 750)

    # PARTIE CLASSEMENT
    pdf.drawString(100, 720, "Classements")

    # Partie channels
    channelsCls = clsPdf('CHANNEL', 5)
    pdf.drawString(100, 690, "CHANNELS")
    y_channel=660
    for i in range(len(channelsCls)):
        index_ = str(i+1) + str(". ")
        pdf.drawString(100, y_channel, index_)
        pdf.drawString(110, y_channel, str(str(" ")+list(channelsCls.keys())[i]) + str("=>") + str(list(channelsCls.values())[i]))
        y_channel-=20
    
    # Partie authors
    authorsCls = clsPdf('AUTHOR', 5)
    pdf.drawString(370, 690, "AUTHORS")
    y_author=660
    for k in range(len(authorsCls)):
        index_ = str(k+1) + str(". ")
        pdf.drawString(370, y_author, index_)
        pdf.drawString(380, y_author, str(str(" ")+list(authorsCls.keys())[k]) + str("=>") + str(list(authorsCls.values())[k]))
        y_author-=20

    # Séparateurs horizontaux et verticaux 
    pdf.line(340, 710, 340, 600)
    pdf.line(60, 580, 540, 580)

    # PARTIE STATISTIQUES GLOBALES
    pdf.drawString(100, 550, "Statistiques Globales")

    # Partie gauche
    currentTotalMembers = "Nombre de membres=>"+"None"
    pastTotalMembers = "Nombre de membres en plus qu'hier=>"+"None"
    pdf.drawString(100, 520, currentTotalMembers)
    pdf.drawString(100, 490, pastTotalMembers)

    # Séparateur vertical
    pdf.line(340, 540, 340, 480)

    # Partie droite
    currentTextChannel = "Nb salons textuels=>"+"None"
    currentVoiceChannel = "Nb salons vocaux=>"+"None"
    pdf.drawString(370, 520, currentTextChannel)
    pdf.drawString(370, 490, currentVoiceChannel)

    # Séparateur horizontal
    pdf.line(60, 470, 540, 470)

    # PARTIE GRAPHIQUES
    pdf.drawString(100, 440, "Graphiques")

    # Création et enregistrement des graphiques
    graphAuthor = graphsPdf('AUTHOR', 5)
    graphChannel = graphsPdf('CHANNEL', 5)
    graphAuthorPath = "graphs-mail/current_AUTHOR.png"
    graphChannelPath = "graphs-mail/current_CHANNEL.png"

    # Affichage des graphiques sur le pdf
    pdf.drawInlineImage(graphAuthorPath, 10, 280, 300, 150)
    pdf.drawInlineImage(graphChannelPath, 300, 280, 300, 150)

    # Sauvegarde du fichier
    pdf.save()

    # Suppression de tous les graphes générés
    filelist = [f for f in os.listdir("graphs-mail") if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join("graphs-mail", f))

def returnFileName():
    """
        FONCTIONNEL
        Fonction: On retourne le nom du dossier en global pour l'utiliser dans d'autres fonctions plus facilement
    """
    return fileName