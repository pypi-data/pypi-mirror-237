from notificationmethods.notificacion import Notificacion
import requests

class Email(Notificacion):

    def __init__(self, sender, api_key, host,
                ):
        self.sender = sender
        self.host = host
        self.api_key = api_key

    def send(self, to, subject, reply_to, bcc, attachments=None,
             body='<p>--Emtpy--</p>'):
        try:
            r = requests.post(
                f"https://api.mailgun.net/v3/{self.host}/messages",
                auth=("api", self.api_key),
                data={
                    "from": self.sender,
                    "to": to,
                    "subject": subject,
                    "html": body,
                    'h:Reply_to':reply_to,
                    'bcc':bcc,
                    'files':attachments
                }
            )
        except Exception as error:
            print(error)