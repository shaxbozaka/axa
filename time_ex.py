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
import cv2import pytz
api_id = '1239727'
api_hash = 'a12d841c6ddd543b2010b8fad15ef1d7'
from telethon import TelegramClient, sync
client = TelegramClient('Sabitov_2352', api_id, api_hash)
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

def generate_image_with_text(text, path):
    x = pytz.timezone("Asia/tashkent")
    time = datetime.now(x)

    return image


def juma_muborak():
    path = r"masjid_m.jpg"
    text = "Juma muborak"
    image = generate_image_with_text(text, path)
    cv2.imwrite(f"time/juma-muborak", image)
    print("passed")

while start_time < end_time :

    if start_time.hour >= 7 and start_time.hour < 11:
        path = r"tashkent_m.jpeg"
    elif start_time.hour >= 11 and start_time.hour < 18:
        path = r"tashkent_d.jpeg"
    elif start_time.hour >= 18 or start_time.hour < 7:
        path = r"tashkent_n.jpeg"

    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text, path)
    cv2.imwrite(f"time/{text}.jpg", image)
    start_time += timedelta(minutes=1)

while rept <= 500:
    path = r"masjid_m.jpg"
    image = generate_image_with_text(f"Juma namoziga {rept} minut qoldi", path)
    rept = juma(rept)
    cv2.imwrite(f"time/juma-{rept}.jpg", image)
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
        # print(prev_update_time)
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
        # client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time/{x - 5}:{y}.jpg")

        if time().weekday() == 4:
            if time().hour < 13 and time().hour > 10:
                file = client.upload_file(f"time/juma-{(13 - time().hour) * 60 - time().minute - 1}.jpg")
            else:
                juma_muborak()
                file = client.upload_file(f"time/juma-muborak.jpg")
        client(UploadProfilePhotoRequest(file))
import pytz
from datetime import datetime, timezone
b = timezone.utc
print(b)

print(a)
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
    x = pytz.timezone("Asia/tashkent")
    time = datetime.now(x)
  # astimezone method
    return time

def generate_image_with_text(text, path):

    image = cv2.imread(path)
    color = (255, 0, 0)
    org = (500, 500)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(image, text, (int(image.shape[1] // 2 + image.shape[1] // 6), int(image.shape[0] // 6)), font, 1.5,
                color, 2, cv2.LINE_AA)



    return image


def juma_muborak():
    path = r"masjid_m.jpg"
    text = "Juma muborak"
    image = generate_image_with_text(text, path)
    cv2.imwrite(f"time/juma-muborak", image)
    print("passed")

while start_time < end_time :

    if start_time.hour >= 7 and start_time.hour < 11:
        path = r"tashkent_m.jpeg"
    elif start_time.hour >= 11 and start_time.hour < 18:
        path = r"tashkent_d.jpeg"
    elif start_time.hour >= 18 or start_time.hour < 7:
        path = r"tashkent_n.jpeg"

    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text, path)
    cv2.imwrite(f"time/{text}.jpg", image)
    start_time += timedelta(minutes=1)

while rept <= 500:
    path = r"masjid_m.jpg"
    image = generate_image_with_text(f"Juma namoziga {rept} minut qoldi", path)
    rept = juma(rept)
    cv2.imwrite(f"time/juma-{rept}.jpg", image)
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
#         prev_update_time = convert_time_to_string(time())
#         # print(prev_update_time)
#         x, y = prev_update_time.split(":")
#         x, y = int(x), int(y)
#         y += 1
#         x += 5
#         if x > 24:
#             x -= 24
        
#         if y < 10 and y != "00":
#             y = "0" + str(y)
#         if y == 60:
#             y = "00"
            
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time/{time().hour}:{time().minute}.jpg")

        if time().weekday() == 4:
            if time().hour < 13 and time().hour > 10:
                file = client.upload_file(f"time/juma-{(13 - time().hour) * 60 - time().minute - 1}.jpg")
            else:
                juma_muborak()
                file = client.upload_file(f"time/juma-muborak.jpg")
        client(UploadProfilePhotoRequest(file))
