from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async
import json
from .models import *


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'channel_room'
        self.room_group_name = 'channel_group'
        print(self.room_group_name)
        print("Arrived Here")
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # order = Order.give_order_details(self.room_name)
        self.accept()
        
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def notif_send(self, event):
        print(event)
        data = json.loads(event['value'])
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'payload': data
        }))


class InstructorNotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'channel_room_instructor'
        self.room_group_name = 'channel_group_instructor'
        print(self.room_group_name)
        print("Arrived Here")
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # order = Order.give_order_details(self.room_name)
        self.accept()
        
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def notif_send(self, event):
        print(event)
        data = json.loads(event['value'])
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'payload': data
        }))