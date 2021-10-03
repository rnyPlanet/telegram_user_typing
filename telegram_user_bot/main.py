from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")

commands = ["coms", "type", "hack", "pidor", "flip", "un", "clown", "rat", "test", "sleep", "thx", "d"]


@app.on_message(filters.command(commands[0], prefixes=".") & filters.me)
def type(_, msg):
    coms = "Commands: "
    for i in commands:
        coms += " \n." + i
        if i in "type":
            coms += " __text__"
        if i in "pidor":
            coms += " __empty__ OR @uname OR @uname1 @unameN"
        if i in "flip":
            coms += " __text__"
        if i in "rat":
            coms += " __empty__ OR @uname OR @uname1 @unameN"
        if i in "sleep":
            coms += " __empty__ OR @uname OR @uname1 @unameN"
        if i in "thx":
            coms += " __empty__ OR @uname"
        if i in "d":
            coms += ""
    msg.edit(coms)


@app.on_message(filters.command(commands[1], prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.2)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.2)

        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command(commands[2], prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while (perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")


@app.on_message(filters.command(commands[3], prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
    single_chat = None

    usernames = msg.text.split(" ")
    if len(usernames) == 1:
        usernames = None
        try:
            single_chat = msg.chat.username
        except:
            print()

    while (perc < 100):
        try:
            text = "📡 Система поиска пидарасов активированна... " + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(5, 10)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    if usernames is not None:
        if len(usernames) == 2:
            msg.edit(f"🟢 Пидарас обнаружен! {usernames[1]}")
        elif len(usernames) > 2:
            pidors = "🟢 Пидарасы обнаружены! "
            for i in usernames:
                if '.pidor' not in i:
                    pidors += " " + i

            msg.edit(pidors)
    else:
        if single_chat == None:
            msg.edit(f"🟢 Ты пидарас!")
        else:
            msg.edit(f"🟢 Пидарас обнаружен! @{single_chat}")

    sleep(3)


REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


@app.on_message(filters.command(commands[4], prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)


@app.on_message(filters.command(commands[5], prefixes=".") & filters.me)
def unread_chat(app, message):
    message.delete()
    app.send(
        functions.messages.MarkDialogUnread(
            peer=app.resolve_peer(message.chat.id), unread=True
        )
    )


@app.on_message(filters.command(commands[6], prefixes=".") & filters.me)
def type(_, msg):
    msg.edit("Дружочек, ты видимо не понял с кем общаешься. Вот эта твоя манера речи 'клоунская' меня не впечатляет, давай встретимся, объясню на понятном тебе языке, языке боли")


@app.on_message(filters.command(commands[7], prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
    single_chat = None

    usernames = msg.text.split(" ")
    if len(usernames) == 1:
        usernames = None
        try:
            single_chat = msg.chat.username
        except:
            print()

    while (perc < 100):
        try:
            text = "📡 Поиск крыс... " + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(5, 10)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    if usernames is not None:
        if len(usernames) == 2:
            msg.edit(f"🐀 Ебать {usernames[1]} крыса!")
        elif len(usernames) > 2:
            rats = "🐀 Ебать"
            for i in usernames:
                if '.rat' not in i:
                    rats += " " + i

            rats += " крысы!"
            msg.edit(rats)
    else:
        if single_chat == None:
            msg.edit(f"🐀 Ты крыса!")
        else:
            msg.edit(f"🐀 Ебать @{single_chat} крыса!")

    sleep(3)


@app.on_message(filters.command(commands[7], prefixes=".") & filters.text)
def del_rat(_, msg):
    me = app.get_me()
    try:
        app.delete_messages(msg.chat.id, msg.message_id)
    except:
        if me.username in msg.message:
            app.send_message(msg.chat.id, "Да сам ты крыса!")

@app.on_message(filters.command(commands[8], prefixes=".") & filters.me)
def hack(_, msg):
    try:
        msg.edit(f"соси ❤")
    except:
        app.send_message(msg.chat.id, "соси ❤")


@app.on_message(filters.command(commands[9], prefixes=".") & filters.me)
def hack(_, msg):
    single_chat = None

    usernames = msg.text.split(" ")
    if len(usernames) == 1:
        usernames = None
        try:
            single_chat = msg.chat.username
        except:
            pass

    try:
        if usernames is not None:
            if len(usernames) == 2:
                msg.edit(f"Бля, {usernames[1]} иди поспи иди приляг!")
            elif len(usernames) > 2:
                rats = "Бля"
                for i in usernames:
                    if '.sleep' not in i:
                        rats += " " + i

                rats += " идите поспите идите прилягте!"
                msg.edit(rats)
        else:
            if single_chat == None:
                msg.edit(f"Бля, иди поспи иди приляг!")
            else:
                msg.edit(f"Бля, @{single_chat} иди поспи иди приляг!")
    except:
        if usernames is not None:
            if len(usernames) == 2:
                app.send_message(msg.chat.id, f"Бля, {usernames[1]} иди поспи иди приляг!")
            elif len(usernames) > 2:
                rats = "Бля"
                for i in usernames:
                    if '.sleep' not in i:
                        rats += " " + i

                rats += " идите поспите идите прилягте!"
                app.send_message(msg.chat.id, rats)
        else:
            if single_chat == None:
                app.send_message(msg.chat.id, f"Бля, иди поспи иди приляг!")
            else:
                app.send_message(msg.chat.id, f"Бля, @{single_chat} иди поспи иди приляг!")

    sleep(3)

@app.on_message(filters.command(commands[10], prefixes=".") & filters.me)
def photo(_, msg):
    msg.delete()
    single_chat = None

    usernames = msg.text.split(" ")
    if len(usernames) == 1:
        usernames = None
        try:
            single_chat = msg.chat.username
        except:
            pass

    if usernames is not None:
        if len(usernames) == 2:
            app.send_photo(msg.chat.id, "photo.jpg", caption=f"{usernames[1]}")
    else:
        if single_chat == None:
            app.send_photo(msg.chat.id, "photo.jpg")
        else:
            app.send_photo(msg.chat.id, "photo.jpg", caption=f"@{single_chat}")

@app.on_message(filters.command(commands[11], prefixes=".") & filters.me)
def d(_, msg):
    try:
        app.delete_messages(msg.chat.id, msg.reply_to_message.message_id)
    except:
        pass
    msg.delete()

app.run()