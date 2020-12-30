
api_id = '1239727'
api_hash = 'a12d841c6ddd543b2010b8fad15ef1d7'
from telethon import TelegramClient, sync
client = TelegramClient('Sabitov_3', api_id, api_hash)
client.start()
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
import cv2
import numpy as np
from datetime import datetime
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")  # Можете выбрать любую дату
end_time = start_time + timedelta(days=1)
time = datetime.now()
def generate_image_with_text(text):
    text = convert_time_to_string(start_time)
    # print(text)
    h, m = text.split(":")
    if m == "0":
        m+="0"
    if h == "0":
        h +="0"
    text = f"{h}:{m}"
    if time.hour + 5 >= 18 or (time.hour > 0 or time.hour + 5 < 9):
        path = r'tashkent_n.jpeg'
    elif time.hour + 5 >= 9 and time.hour + 5 <= 12:
        path = r'tashkent_m.jpeg'
    elif time.hour+ 5 >= 12 and time.hour + 5 <= 18:
        path = r'tashkent_d.jpeg'

    image = cv2.imread(path)
    # print(text)
    color = (255, 0, 0)
    org = (500, 500)
    # print(image.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(image, f"You will see", (int(image.shape[1] // 2), int(image.shape[0] // 4)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    # cv2.putText(image, "this image at", (int(image.shape[1] // 2), int(image.shape[0] // 6)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(image, text, (int(image.shape[1] // 2 + image.shape[1] // 6), int(image.shape[0] // 6)), font, 1.5, color, 2, cv2.LINE_AA)

    return image

while start_time < end_time:
    text = convert_time_to_string(start_time)
    # print(text)

    image = generate_image_with_text(text)
    cv2.imwrite(f"time/{text}.jpg", image)
    start_time += timedelta(minutes=1)
    from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
def time_has_changed(prev_time):
    a = datetime.now()
    if a.second == 55:
        return True

prev_update_time = ""
import time
while True:

    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        # print(prev_update_time)
        x, y = prev_update_time.split(":")
        x, y = int(x), int(y)
        y += 1
        x += 5
        if x > 24:
            x -= 24
        if y == 60:
            y = "00"
        if y < 10 :
            y = "0" + y
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time/{x}:{y}.jpg")
        client(UploadProfilePhotoRequest(file))
