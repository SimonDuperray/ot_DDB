from reportlab.pdfgen import canvas
import datetime
from analysis import clsPdf
from analysis import graphsPdf
import os

def drawMyRuler(pdf):
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
    os.remove('daily_resume.pdf')
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.day)+str(' - ')+str(todayDate.month)+str(' - ')+str(todayDate.year)
    fileName = "daily_resume.pdf"
    documentTitle = "DailyResume"
    title = "ACTIVITE QUOTIDIENNE DU " + currentDate

    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)
    pdf.drawString(190, 770, title)
    pdf.line(60, 750, 540, 750)
    pdf.drawString(100, 720, "Classements")
    channelsCls = clsPdf('CHANNEL', 5)
    pdf.drawString(100, 690, "CHANNELS")
    y=660
    for i in range(len(channelsCls)):
        index_ = str(i+1) + str(". ")
        pdf.drawString(100, y, index_)
        pdf.drawString(110, y, str(str(" ")+list(channelsCls.keys())[i]) + str("=>") + str(list(channelsCls.values())[i]))
        y-=20
    authorsCls = clsPdf('AUTHOR', 5)
    pdf.drawString(370, 690, "AUTHORS")
    y=660
    for k in range(len(authorsCls)):
        index_ = str(k+1) + str(". ")
        pdf.drawString(370, y, index_)
        pdf.drawString(380, y, str(str(" ")+list(authorsCls.keys())[k]) + str("=>") + str(list(authorsCls.values())[k]))
    pdf.line(340, 710, 340, 600)
    pdf.line(60, 580, 540, 580)
    pdf.drawString(100, 550, "Statistiques Globales")
    currentTotalMembers = "Nombre de membres=>"+"None"
    pastTotalMembers = "Nombre de membres en plus qu'hier=>"+"None"
    pdf.drawString(100, 520, currentTotalMembers)
    pdf.drawString(100, 490, pastTotalMembers)
    pdf.line(340, 540, 340, 480)
    currentTextChannel = "Nb salons textuels=>"+"None"
    currentVoiceChannel = "Nb salons vocaux=>"+"None"
    pdf.drawString(370, 520, currentTextChannel)
    pdf.drawString(370, 490, currentVoiceChannel)
    pdf.line(60, 470, 540, 470)
    pdf.drawString(100, 440, "Graphiques")
    graphAuthor = graphsPdf('AUTHOR')
    graphChannel = graphsPdf('CHANNEL')
    graphAuthorPath = "graphs-mail/current_AUTHOR.png"
    graphChannelPath = "graphs-mail/current_CHANNEL.png"
    pdf.drawInlineImage(graphAuthorPath, 10, 280, 300, 150)
    pdf.drawInlineImage(graphChannelPath, 300, 280, 300, 150)
    pdf.save()
    filelist = [f for f in os.listdir("graphs-mail") if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join("graphs-mail", f))