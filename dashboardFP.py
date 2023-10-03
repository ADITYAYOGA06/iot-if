from tkinter import *
import random
import json
from paho.mqtt import client as mqtt_client
from tkinter import Tk, Canvas, ttk
import sqlite3
from paho.mqtt import client as mqtt_client
import random
from datetime import datetime
import tkinter as tk

broker = '0.tcp.ap.ngrok.io'
port = 12107
topic = "tes/ngrok"
client_id =  f'python-mqtt-{random.randint(0, 100)}'

# connect to the database
conn = sqlite3.connect('db.sqlite')

# create a cursor
cursor = conn.cursor()

buat_tabel = '''CREATE TABLE IF NOT EXISTS data_iotif (
                        tds INTEGER NOT NULL,
                        warning TEXT NOT NULL,
                        saran TEXT NOT NULL,
                        timestamp NOT NULL
                        );'''

cursor.execute(buat_tabel) 
conn.commit()

def connect_mqtt() -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data_sensor_val = int(msg.payload.decode())
        warning=''
        saran=''
        timestamp=datetime.now()
        if data_sensor_val > 650:
            warning='bahaya'
            saran='periksa sumber air anda'
        elif data_sensor_val > 500:
            warning='kurang baik'
            saran='mungkin ada kontaminasi'
        else:
            warning='aman'
            saran='air aman'
        
        cursor.execute("INSERT INTO data_iotif (tds, warning, saran, timestamp) VALUES(?, ? , ?, ?);", (data_sensor_val, warning, saran, timestamp))
        conn.commit()

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
 run()