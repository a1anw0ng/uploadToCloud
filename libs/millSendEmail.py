import smtplib
import syslog
from email.message import EmailMessage


class millSendEmail:
    def __init__(self, gmail_user, gmail_password, to_email, email_subject, email_body):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.to_email = to_email
        self.email_subject = email_subject
        self.email_body = email_body

    def send_email(self, receiver, subject, body):
        self.to_email = receiver
        self.email_subject = subject
        self.email_body = body
        msg = EmailMessage()
        msg.set_content(self.email_body)
        msg['Subject'] = self.email_subject
        msg['From'] = self.gmail_user
        msg['To'] = self.to_email

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.gmail_user, self.gmail_password)
            server.send_message(msg)
            server.quit()
            syslog.syslog(syslog.LOG_ERR, f"Email sent successfully to: {receiver}")
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"Exception: sending email to {receiver} => {e}")

