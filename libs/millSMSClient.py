from twilio.rest import Client
import syslog

class millSMSClient:
    def __init__(self, account_sid, auth_token, from_phone_number):
        self.client = Client(account_sid, auth_token)
        self.from_phone_number = from_phone_number

    def send_message(self, to_phone_number, message_body):
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=self.from_phone_number,
                to=to_phone_number
            )
            syslog.syslog(syslog.LOG_ERR, f"SMS Message sent successfully to: {to_phone_number}")
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"Exception: sending SMS Message to {to_phone_number} => {e}")


