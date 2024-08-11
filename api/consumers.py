import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SolicitudConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'solicitudes_pendientes'

        # Únete al grupo de solicitudes pendientes
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Deja el grupo de solicitudes pendientes
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        tipo = text_data_json.get('type')

        if tipo == 'nuevo_solicitud':
            # Aquí puedes enviar la nueva solicitud a todos los clientes conectados
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_solicitud',
                    'data': text_data_json
                }
            )

    async def send_solicitud(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))
