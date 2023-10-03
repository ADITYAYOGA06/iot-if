from tkinter import *
import tkinter as tk
import random
import json
from paho.mqtt import client as mqtt_client
import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite')

# Execute the SELECT statement
cursor = conn.cursor()
cursor.execute('SELECT * FROM data_iotif ORDER BY timestamp DESC LIMIT 2')
col1=[]
col2=[]
col3=[]

for item in cursor:
    col1.append(item[0])
    col2.append(item[1])
    col3.append(item[2])

window = Tk()
window.title("MQTT Dashboard")
window.geometry('1366x768') # Width, Height 
window.resizable(False,False) # Width, Height
window.configure(bg="white")

# Header image
canvas = Canvas(window, width=1366,height=192)
canvas.place(x=0,y=0)
img = PhotoImage(file="headerIOTIF2.png")
canvas.create_image(0,0,anchor=NW,image=img)

canvas2 = Canvas(window, width=1366, height=288)
canvas2.place(x=0,y=193)
img2 = PhotoImage(file="dt_tbrtkr.png")
canvas2.create_image(0,0,anchor=NW,image=img2)

canvas3 = Canvas(window, width=1366, height=288)
canvas3.place(x=0,y=481)
img3 = PhotoImage(file="dt_tbr.png")
canvas3.create_image(0,0,anchor=NW,image=img3)

# Create a label for each column
label1a = tk.Label(window, text=col1[0], bg="white", fg="black", font=("Helvetica", 40))
label1a.place(x=50,y=300)
label2a = tk.Label(window, text=col2[0], bg="white", fg="black", font=("Helvetica", 40))
label2a.place(x=250,y=300)
label3a = tk.Label(window, text=col3[0], bg="white", fg="black", font=("Helvetica", 40))
label3a.place(x=650,y=300)
    
# Create a label for each column
label1b = tk.Label(window, text=col1[1], bg="white", fg="black", font=("Helvetica", 40))
label1b.place(x=50,y=560)
label2b = tk.Label(window, text=col2[1], bg="white", fg="black", font=("Helvetica", 40))
label2b.place(x=250,y=560)
label3b = tk.Label(window, text=col3[1], bg="white", fg="black", font=("Helvetica", 40))
label3b.place(x=650,y=560)
    
# client = connect_mqtt()
# subscribe(client)
# client.loop_start()
window.mainloop()
# client.loop_stop()
