from tkinter import *
from paho.mqtt import client as mqtt_client
from tkinter import Tk, Canvas, ttk
import sqlite3
from paho.mqtt import client as mqtt_client
from datetime import datetime
import tkinter as tk

window = Tk()
window.title("MQTT Dashboard")
window.geometry('1366x768') 
window.resizable(False,False) 
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

def refresh_data():
    # Connect to the database
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    data1=[]
    data2=[]
    # Retrieve the two latest data from the database
    cursor.execute("SELECT * FROM data_iotif ORDER BY timestamp DESC LIMIT 2")
    # connection.commit()

    data = cursor.fetchall()

    # Update the display with the latest data
    data2=data[0]
    data1=data[1]

    # Close the connection to the database
    connection.close()

    # update the ui
    label1a.config(text=data1[0])
    label2a.config(text=data1[1])
    label3a.config(text=data1[2])
    label4a.config(text=data1[3])

    label1b.config(text=data2[0])
    label2b.config(text=data2[1])
    label3b.config(text=data2[2])
    label4b.config(text=data2[3])

    # Call the refresh function again after 10000 milliseconds (10 second)
    window.after(10000, refresh_data)

# Create a label for each column
label1a = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label1a.place(x=50,y=280)
label2a = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label2a.place(x=280,y=280)
label3a = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label3a.place(x=680,y=280)
label4a = tk.Label(window, bg="white", fg="black", font=("Helvetica", 30))
label4a.place(x=410,y=360)

# Create a label for each column
label1b = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label1b.place(x=50,y=540)
label2b = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label2b.place(x=280,y=540)
label3b = tk.Label(window, bg="white", fg="black", font=("Helvetica", 35))
label3b.place(x=680,y=540)
label4b = tk.Label(window, bg="white", fg="black", font=("Helvetica", 30))
label4b.place(x=410,y=620)

refresh_data()
window.mainloop()