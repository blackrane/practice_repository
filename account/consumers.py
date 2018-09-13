from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NoticeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        await self.channel_layer.group_add(self.user_name, self.channel_name)
        print(f"added {self.channel_name} channel to {self.user_name}")

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel from gossip {close_code}")

    async def user_event(self, event):
        await self.send(text_data=json.dumps(event,ensure_ascii=False))
        print(f"Got message{event} at {self.channel_name}")
