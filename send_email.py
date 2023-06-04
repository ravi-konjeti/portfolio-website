import smtplib, ssl

host = "smtp.gmail.com"
port = 465


username = "ravikonjeti1234@gmail.com"
password = "igatyilmxmlmicui"

reciever = "ravikonjeti1234@gmail.com"

context = ssl.create_default_context()


message = """\
Subject :Hi!
How are You?
bi
"""

with smtplib.SMTP_SSL(host, port,context= context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)