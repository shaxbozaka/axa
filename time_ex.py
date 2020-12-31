import pytz
from datetime import datetime
from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
api_id = '1239727'
api_hash = 'a12d841c6ddd543b2010b8fad15ef1d7'
from pyrogram import Client
client = TelegramClient('Sabitov_3', api_id, api_hash)
client.start()

def time():
    x = pytz.timezone("Asia/tashkent")
    time = datetime.now(x)
    # astimezone method
    return time


def time_has_changed(prev_time):
    a = datetime.now()
    if a.second == 55:
        return True



with Client("salom pyrogram", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")


    prev_update_time = ""
    while True:

        if time_has_changed(prev_update_time):
            prev_update_time = time()
            # print(prev_update_time)
            x, y = time().hour, time().minute
            x, y = int(x), int(y)
            y += 1

            if x == 24:
                x = 0
            if y < 10 and y != "00":
                y = "0" + str(y)
            if y == 60:
                y = "00"
            #
            # client(DeletePhotosRequest(client.get_profile_photos('me')))
            # file = client.upload_file(f"time/{time().hour}:{time().minute}.jpg")


            if time().weekday() == 4:
                if time().hour < 13 and time().hour > 10:
                    print("passed")
                    file = f"time/{x}:{y}.jpg"
                else:
                    file = f"time/juma_muborak.jpg"
            else:
                file= f"time/{x}:{y}.jpg"
                
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            app.set_profile_photo(photo=file)
