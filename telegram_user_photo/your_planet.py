import time

from pyrogram import Client

with Client("my_account") as app:
    while True:
        photos = app.get_profile_photos("me")

        app.set_profile_photo(photo="our_profit.png")
        # app.delete_profile_photos(photos[1].file_id)

        time.sleep(60)

        photos = app.get_profile_photos("me")

        app.set_profile_photo(photo="your_planet.png")
        # app.delete_profile_photos(photos[1].file_id)

        time.sleep(60)