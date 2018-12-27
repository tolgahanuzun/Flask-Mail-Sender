import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from flask import Flask, request, abort

app = Flask(__name__)

# Email
SENDER = 'mail@mail.com'
SENDERNAME = 'Sender'
USERNAME_SMTP = "mail@mail.com"
PASSWORD_SMTP = "123456789"
HOST = "Host adress"
PORT = 587


def send_email(reply_to, recipient, subject, body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = formataddr((SENDERNAME, SENDER))
    msg['To'] = recipient
    msg.add_header('Reply-To', reply_to)

    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(body, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, recipient, msg.as_string())
        server.close()
    except Exception as e:
        return False
    else:
        return True


@app.route('/', methods=['POST'])
def index():
    if not request.json:
        abort(400)
    data = request.json
    send = send_email(SENDER, data['recipient'], data['subject'], data['body'])
    return f'Message send: {send}', 201

if __name__ == '__main__':
    app.run(debug=False)
