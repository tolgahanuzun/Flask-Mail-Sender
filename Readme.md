# Flask Mail Sender

Sends mail with data from the post method.

- You can send with your own mail server information.
- You can send mail with Amazon SES.

## Install 

No need for 3rd party libraries for sending mail. This project is just Flask. Web server listen to post requests. So it's just a tool in sending mail.

```python3
pip install -i requirements.py
```

And open run.py. Edit the information by yourself.

```
# Email
SENDER = 'mail@mail.com'
SENDERNAME = 'Sender'
USERNAME_SMTP = "mail@mail.com"
PASSWORD_SMTP = "123456789"
HOST = "Host adress"
PORT = 587
```

`python run.py` run. 

## How it works?

```bash
curl -X POST \
  http://127.0.0.1:5000/ \
  -H 'content-type: application/json' \
  -d '{
	"recipient": "tolgahanuzun2@gmail.com",
	"subject": "Flask Mail Sender",
	"body": "<br><br> <b>Mail test</b>"
    }'
```
