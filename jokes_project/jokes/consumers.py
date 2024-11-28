from channels.generic.websocket import AsyncJsonWebsocketConsumer

class JokesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Received connection req")
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()
        print("Connection Accepted")

    async def disconnect(self):
        await self.channel_layer.group_discard('jokes', self.channel_name)

    async def send_jokes(self, event):
        text_message=event['text']

        await self.send(text_message)
