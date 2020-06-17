import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from createpdf import returnFileName
import os

def send_resume_email(toaddr_):
    """
        send email with the daily resume in pdf format
    """
    fromaddr = "datadiscordbot@gmail.com"
    toaddr = str(toaddr_)
    msg= MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Activité Quotidienne"
    body = "Voici ce qui s'est passé sur ton serveur aujourd'hui !"
    msg.attach(MIMEText(body, 'plain'))
    filename = returnFileName()
    attachement = open(filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachement).read())
    encoders.encode_base64(p)
    # p.add_header('Content-Disposition', "attachement; filename= daily_resume.pdf")
    p.add_header('Content-Disposition', "attachment; filename="+str(filename))
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "CaVaFaireDesMillions!!")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

# send_resume_email("simon.duperray4949@gmail.com")