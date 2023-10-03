from tkinter import *
from paho.mqtt import client as mqtt_client
from tkinter import Tk, Canvas, ttk
import sqlite3
from paho.mqtt import client as mqtt_client
from datetime import datetime
import tkinter as tk


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

def refresh_data():
    # Connect to the database
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    data1=[]
    data2=[]
    # Retrieve the two latest data from the database
    cursor.execute("SELECT tds, warning, saran FROM data_iotif ORDER BY timestamp DESC LIMIT 2")
    data1.clear()
    connection.commit()

    # latest_data = cursor.fetchall()

    # Update the display with the latest data
    # data_label_1.config(text=latest_data[0])
    # data_label_2.config(text=latest_data[1])
    for item in cursor:
        data1.append(item[0])
        data1.append(item[1])
        data1.append(item[2])
    
    data2=data1.copy()

    # Close the connection to the database
    connection.close()

    label1a = tk.Label(window, text=data1[0], bg="white", fg="black", font=("Helvetica", 40))
    label1a.place(x=50,y=300)
    label2a = tk.Label(window, text=data1[1], bg="white", fg="black", font=("Helvetica", 40))
    label2a.place(x=250,y=300)
    label3a = tk.Label(window, text=data1[2], bg="white", fg="black", font=("Helvetica", 40))
    label3a.place(x=650,y=300)
        
    # Create a label for each column
    label1b = tk.Label(window, text=data2[0], bg="white", fg="black", font=("Helvetica", 40))
    label1b.place(x=50,y=560)
    label2b = tk.Label(window, text=data2[1], bg="white", fg="black", font=("Helvetica", 40))
    label2b.place(x=250,y=560)
    label3b = tk.Label(window, text=data2[2], bg="white", fg="black", font=("Helvetica", 40))
    label3b.place(x=650,y=560)


    # Call the refresh function again after 1000 milliseconds (1 second)
    window.after(1000, refresh_data)


# data_label_1 = tk.Label(window)
# dt_baru1 = data_label_1.pack()
# data_label_2 = tk.Label(window)
# dt_baru2 = data_label_2.pack()



# cursor = conn.cursor()
# cursor.execute('SELECT * FROM data_iotif ORDER BY timestamp DESC LIMIT 2')
# data1.clear()
# conn.commit()

# for item in cursor:
#     data1.append(item[0])
#     data1.append(item[1])
#     data1.append(item[2])

# data2=data1.copy()



# Create a label for each column
# label1a = tk.Label(window, text=data1[0], bg="white", fg="black", font=("Helvetica", 40))
# label1a.place(x=50,y=300)
# label2a = tk.Label(window, text=data1[1], bg="white", fg="black", font=("Helvetica", 40))
# label2a.place(x=250,y=300)
# label3a = tk.Label(window, text=data1[2], bg="white", fg="black", font=("Helvetica", 40))
# label3a.place(x=650,y=300)
    
# # Create a label for each column
# label1b = tk.Label(window, text=data2[0], bg="white", fg="black", font=("Helvetica", 40))
# label1b.place(x=50,y=560)
# label2b = tk.Label(window, text=data2[1], bg="white", fg="black", font=("Helvetica", 40))
# label2b.place(x=250,y=560)
# label3b = tk.Label(window, text=data2[2], bg="white", fg="black", font=("Helvetica", 40))
# label3b.place(x=650,y=560)


refresh_data()
window.mainloop()