import asyncio
import random

from telethon.sync import TelegramClient, events

api_id =
api_hash = ""

with TelegramClient("anon", api_id, api_hash) as client:
    @client.on(events.UserUpdate)
    async def handler(event):
        if event.typing:
            async with client.action(event.chat_id, 'typing'):
                await asyncio.sleep(3)
            # await client.action(event.chat_id, 'cancel')
            #
            # if random.choice([True, False]):
            #     async with client.action(event.chat_id, 'record-voice'):
            #         await asyncio.sleep(3)
            #     await client.action(event.chat_id, 'cancel')

    client.run_until_disconnected()
