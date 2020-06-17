import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

fromaddr = "datadiscordbot@gmail.com"
toaddr = "simon.duperray4949@gmail.com"
msg= MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Activité Quotidienne"
body = "Voici ce qui s'est passé sur ton serveur aujourd'hui !"
msg.attach(MIMEText(body, 'plain'))
filename = "ARTICLE_RECO.pdf"
attachement = open("ARTICLE_RECO.pdf", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachement).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachement; filename= ARTICLE_RECO.pdf")
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "CaVaFaireDesMillions!!")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()