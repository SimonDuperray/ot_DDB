import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from createpdf import returnFileName
import os

def send_resume_email(toaddr_):
    """
        FONCTIONNEL
        Paramètre: toaddr_ => email receveur
        Fonction: Envoi d'un mail avec pièce jointe au mail passé en paramètre
        Modifications: -> stocker le mot de passe du compte dans un fichier externe (avec le token)
    """

    # Déclaration des informations essentielles à l'envoi du mail
    fromaddr = ""
    toaddr = str(toaddr_)
    msg= MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Activité Quotidienne"

    # Contenu du mail
    body = "Voici ce qui s'est passé sur ton serveur aujourd'hui !"
    msg.attach(MIMEText(body, 'plain'))

    # Déclaration de la pièce jointe
    filename = returnFileName()
    attachement = open(filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachement).read())
    encoders.encode_base64(p)

    # Ajout de la pièce jointe
    p.add_header('Content-Disposition', "attachment; filename="+str(filename))
    msg.attach(p)

    # Connexion au serveur pour l'envoi du mail
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "password")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()