import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ravikonjeti1234@gmail.com"
    password = "xauohlrxayeoeper"
    reciever = "ravikonjeti1234@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

if "__name__" == "__main__":
    send_email()
