import sys
from Adafruit_IO import MQTTClient
import time
import random

AIO_FEED_ID = ["ai", "cambien1", "cambien2", "cambien3", "nutnhan1", "nutnhan2"]
AIO_USERNAME = "tien_le"
AIO_KEY = "aio_QaCo76rDX1Zjoyx3oVry5OEmV7zv"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

count = 0
while True:
    if (count >= 2):
        value = random.randint(0, 60)
        client.publish("cambien1", value)
        count = 0
    count += 1
    time.sleep(1)