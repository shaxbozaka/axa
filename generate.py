from datetime import datetime, timedelta
import cv2
import numpy as np
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")  # Можете выбрать любую дату
rept = 0
end_time = start_time + timedelta(days=1)


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


def juma(rept):
    return rept

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
    cv2.imwrite(f"time/juma-muborak.jpg", image)
    print("passed juma")

juma_muborak()
# #
while start_time < end_time:

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
print("passed time")

while rept <= 500:
    path = r"masjid_m.jpg"
    image = generate_image_with_text(f"Juma namoziga {rept} minut qoldi", path)
    rept = juma(rept)
    cv2.imwrite(f"time/juma-{rept}.jpg", image)
    rept += 1

print("passed All")
