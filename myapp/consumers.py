import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Начать процесс загрузки сообщений на этом этапе, если нужно

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Логика для обработки полученного сообщения от клиента (если это необходимо)
        
        # Например, начать процесс получения сообщений:
        await self.load_messages()

    async def load_messages(self):
        # Имитация загрузки сообщений и отправка прогресса в WebSocket
        total_messages = 100  # Общее количество сообщений (например)
        
        for i in range(total_messages):
            # Имитация получения сообщения
            await sync_to_async(self.get_message)(i)
            
            # Вычисление прогресса
            progress = (i + 1) * 100 // total_messages
            await self.send(text_data=json.dumps({
                'progress': progress,
                'id': i,  # ID сообщения (можно изменить)
                'subject': f'Тема {i}',  # Пример темы сообщения
                'sent_at': '2024-11-05T15:54:00Z',  # Пример даты отправки
                'received_at': '2024-11-05T15:54:30Z',  # Пример даты получения
                'body': f'Текст сообщения номер {i}',  # Пример текста сообщения
                'attachments': None  # Пример отсутствия прикрепленного файла
            }))

    def get_message(self, message_id):
        # Логика для получения сообщения из БД или другого источника
        pass
