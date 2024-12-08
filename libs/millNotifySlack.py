import slack_sdk
import syslog
from configparser import ConfigParser

class millNotifySlack:
    def __init__(self, token):
        self.slack_token = token
        try:
            self.client = slack_sdk.WebClient(token=self.slack_token)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"Exception: create slack client => {e}")

    def sendMessageToUser(self, user_id, msg):
        try:
            response = self.client.conversations_open(users=user_id)
            channel = response["channel"]["id"]

            result = self.client.chat_postMessage(
                channel=channel,
                text=msg
            )

            assert result["ok"]
            syslog.syslog(syslog.LOG_INFO, f"Slack sent successfully to: {user_id}")
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"Exception: sending message: {user_id} => {e}")
                  

    def sendMessageToGroupChannel(self, channel_id, msg):
        try:
            result = self.client.chat_postMessage(
                channel=channel_id,
                text=msg
            )
            assert result["ok"]
            syslog.syslog(syslog.LOG_INFO, f"Slack sent successfully to: {channel_id}")
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"Exception: sending group message: {channel_id} => {e}")
