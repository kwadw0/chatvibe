import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    #this accepts the websockets connection
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    #this recieves the text data converts it to dictionaries and the value for message is extracted
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))