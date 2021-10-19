from pymsteams import connectorcard

class Teams:
    def __init__(self, url_connect):
        self.url_connect = url_connect
        
    def send_message(self, text):
        channel = connectorcard(self.url_connect)
        channel.text(text)
        channel.send()