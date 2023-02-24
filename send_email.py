import smtplib, ssl, os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'Ivan.Donati71@gmail.com'
    password = os.getenv('PASSWORD')

    receiver = 'Ivan.Donati71@gmail.com'
    context = ssl.create_default_context()

    # la \ serve per dire che il messaggio non inizia con una nuova riga ma con Subject
    # per separare il subject dal resto serve una riga vuota dopo
    # message = '''\
    # Subject: test email
    #
    # text
    # hi
    # hello
    # '''

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)