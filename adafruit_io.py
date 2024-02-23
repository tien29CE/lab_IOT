import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *
from simple_ai import *

AIO_FEED_IDs = ["ai", "cambien1", "cambien2", "cambien3", "nutnhan1", "nutnhan2"]
AIO_USERNAME = "tien_le"
AIO_KEY = "aio_UWDa29EgPa2H2qrN55qwiIErUL9p"

def connected(client):
    print("Ket noi thanh cong ...")
    for feed in AIO_FEED_IDs:
        client.subscribe(feed)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client, feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

count = 0
ai_result = previous_result = ""
while True:
    if (count >= 2):
        # value = random.randint(0, 60)
        # client.publish("cambien1", value)
        previous_result = ai_result
        ai_result = image_detector()
        if(ai_result != previous_result):
            client.publish("ai", ai_result)
    count += 1
    readSerial(client)
    time.sleep(1)