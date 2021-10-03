from pyrogram import Client

with Client("my_account") as app:
    photos = app.get_profile_photos("me")

    app.set_profile_photo(photo="our_profit.png")
    app.delete_profile_photos(photos[1].file_id)
