import asyncio
import datetime
import time

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest

api_id = 
api_hash = ''

async def main():
    client = TelegramClient("anon", api_id, api_hash)

    await client.start()
    me = await client.get_me()

    async def change(srt):
        await client(UpdateProfileRequest(
            srt
        ))

    async def show(text, maximum):
        symbol = '✡'
        count_symbols = int((maximum / 2))

        text = (symbol * count_symbols) + text
        while True:
            for i in range(len(text)):
                if len(text[i:i + maximum]) < maximum:
                    await change(text[i:i + maximum] + text[:maximum - len(text[i:i + maximum])])
                    continue
                await change(text[i:i + maximum])

            await asyncio.sleep(2)

    text = 'Кушатель Мацы'
    await show(text, 12)

    # await client(UpdateProfileRequest(
    #     '{:%H:%M}'.format(datetime.datetime.now() + datetime.timedelta(hours=3)),
    #     me.last_name
    # ))

asyncio.get_event_loop().run_until_complete(main())

# def show(text, maximum):
#     symbol = '✡'
#     count_symbols = int((maximum / 2))
#
#     text = (symbol * count_symbols) + text
#     for _ in range(2):
#         for i in range(len(text)):
#             if len(text[i:i + maximum]) < maximum:
#                 t = text[i:i + maximum] + text[:maximum - len(text[i:i + maximum])]
#                 print(t)
#                 continue
#             print(f"{text[i:i + maximum]}")
#
# text = 'Кушатель Мацы'
# show(text, 15)


