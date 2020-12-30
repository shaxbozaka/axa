import pytz
api_id = '1239727'
api_hash = 'a12d841c6ddd543b2010b8fad15ef1d7'
from telethon import TelegramClient, sync
client = TelegramClient('Sabitov_3', api_id, api_hash)
client.start()
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
def juma(rept):
    return rept
import cv2
import numpy as np
from datetime import datetime, timedelta
# def get_black_background():
#     path = r'tashkent_n.jpeg'
#     image = cv2.imread(path)
#     # return np.zeros((800, 700))
#     return image

start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")  # Можете выбрать любую дату
rept = 0
end_time = start_time + timedelta(days=1)
# time = datetime.now()
def time():
    dtobj1 = datetime.utcnow()  # utcnow class method
    # print(dtobj1)

    dtobj3 = dtobj1.replace(tzinfo=pytz.UTC)  # replace method

    dtobj1 = datetime.utcnow()  # utcnow class method
    # print(dtobj1)
    time = dtobj3.astimezone(pytz.timezone("Asia/tashkent"))  # astimezone method
    return time

def generate_image_with_text(text, rept):

    # print(text)

    if time().weekday() != 4:
        h, m = text.split(":")
        if m == "0":
            m+="0"
        if h == "0":
            h +="0"
        text = f"{h}:{m}"
        if time().hour >= 18 or (time().hour > 0 or time().hour < 9):
            path = r'tashkent_n.jpeg'
        elif time().hour >= 9 and time().hour <= 12:
            path = r'tashkent_m.jpeg'
        elif time().hour >= 12 and time().hour <= 18:
            path = r'tashkent_d.jpeg'
        image = cv2.imread(path)
        # print(text)
        color = (255, 0, 0)
        org = (500, 500)
        # print(image.shape)
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(image, text, (int(image.shape[1] // 2 + image.shape[1] // 6), int(image.shape[0] // 6)), font, 1.5,
                    color, 2, cv2.LINE_AA)

    else:
        path = r'masjid_m.jpg'
        image = cv2.imread(path)

        color = (255, 0, 0)
        org = (500, 500)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if time().hour > 10 and time().hour < 13:
            text = "Juma namoziga " + str(rept) + " minut qoldi"
        else:
            text = "Juma Muborak!"
        cv2.putText(image, text, (int(image.shape[1] // 2), int(image.shape[0] // 6)), font, 1.5,
                    color, 2, cv2.LINE_AA)
    return image

while start_time < end_time and rept <= 500:
    text = convert_time_to_string(start_time)
    # print(text, rept)
    rept = juma(rept)
    print(rept)
    image = generate_image_with_text(text, rept)
    if time().weekday() == 4:
        cv2.imwrite(f"time/juma-{rept}.jpg", image)
    else:
        cv2.imwrite(f"time/{text}.jpg", image)
    start_time += timedelta(minutes=1)
    rept += 1

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
def time_has_changed(prev_time):
    a = datetime.now()
    if a.second == 55:
        return True


prev_update_time = ""
# import time
while True:

    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(time())
        print(prev_update_time)
        x, y = prev_update_time.split(":")
        x, y = int(x), int(y)
        y += 1
        x += 5
        if x > 24:
            x -= 24
        if y == 60:
            y = "00"
        if y < 10 and y != "00":
            y = "0" + str(y)
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time/{x}:{y}.jpg")
        print(time().weekday())
        if time().weekday() == 4:
            print("passed")
            if time().hour < 13 and time().hour > 10:
                file = client.upload_file(f"time/juma-{(13 - time().hour) * 60 - time().minute - 1}.jpg")
                print("juma2")
            else:
                file = client.upload_file(f"time/juma-1.jpg")
                print("juma1")
        client(UploadProfilePhotoRequest(file))
