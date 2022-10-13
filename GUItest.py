import tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO21 = 21
GPIO20 = 20
GPIO16 = 16
GPIO26 = 26
GPIO19 = 19
GPIO13 = 13
GPIO12 = 12
GPIO25 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
GPIO.setup(GPIO16, GPIO.OUT)
GPIO.setup(GPIO26, GPIO.OUT)
GPIO.setup(GPIO19, GPIO.OUT)
GPIO.setup(GPIO13, GPIO.OUT)
GPIO.setup(GPIO12, GPIO.OUT)
GPIO.setup(GPIO25, GPIO.OUT)

master = tk.Tk()
master.title("Relay Control")
master.geometry("800x150")

GPIO21_state = True
GPIO20_State = True
GPIO16_State = True
GPIO26_State = True
GPIO19_State = True
GPIO13_State = True
GPIO12_State = True
GPIO25_State = True


def GPIO21button():
	global GPIO21_state
	if GPIO21_state == False:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="ON", fg="green")
		ONlabel.place(x=25, y=50)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="       ", fg="red")
		ONlabel.place(x=25, y=50)


def GPIO20button():
	global GPIO20_State
	if GPIO20_State == False:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=150, y=50)
	else:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=150, y=50)

def GPIO16button():
	global GPIO16_State
	if GPIO16_State == False:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=190, y=50)
	else:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=190, y=50)

def GPIO26button():
	global GPIO26_State
	if GPIO26_State == False:
		GPIO.output(GPIO26, GPIO26_State)
		GPIO26_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=260, y=50)
	else:
		GPIO.output(GPIO26, GPIO26_State)
		GPIO26_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=260, y=50)

def GPIO19button():
	global GPIO19_State
	if GPIO19_State == False:
		GPIO.output(GPIO19, GPIO19_State)
		GPIO19_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=320, y=50)
	else:
		GPIO.output(GPIO19, GPIO19_State)
		GPIO19_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=320, y=50)

def GPIO13button():
	global GPIO13_State
	if GPIO13_State == False:
		GPIO.output(GPIO13, GPIO13_State)
		GPIO13_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=390, y=50)
	else:
		GPIO.output(GPIO13, GPIO13_State)
		GPIO13_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=390, y=50)

def GPIO12button():
	global GPIO12_State
	if GPIO12_State == False:
		GPIO.output(GPIO12, GPIO12_State)
		GPIO12_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=460, y=50)
	else:
		GPIO.output(GPIO12, GPIO12_State)
		GPIO12_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=460, y=50)

def GPIO25button():
	global GPIO25_State
	if GPIO25_State == False:
		GPIO.output(GPIO25, GPIO25_State)
		GPIO25_State = True
		OFFlabel = tk.Label(master, text="ON", fg="green")
		OFFlabel.place(x=520, y=50)
	else:
		GPIO.output(GPIO25, GPIO25_State)
		GPIO25_State = False
		OFFlabel = tk.Label(master, text="      ", fg="red")
		OFFlabel.place(x=520, y=50)

ONbutton = tk.Button(master, text="Fan 1", bg="blue", command=GPIO21button)
ONbutton.place(x=50, y=20)

OFFbutton = tk.Button(master, text="Fan 2",bg="blue" , command=GPIO20button)
OFFbutton.place(x=120, y=20)

ONbutton = tk.Button(master, text="Spare", bg="blue", command=GPIO16button)
ONbutton.place(x=190, y=20)

OFFbutton = tk.Button(master, text="Spare",bg="blue" , command=GPIO26button)
OFFbutton.place(x=260, y=20)

ONbutton = tk.Button(master, text="Spare", bg="blue", command=GPIO19button)
ONbutton.place(x=330, y=20)

OFFbutton = tk.Button(master, text="Spare",bg="blue" , command=GPIO13button)
OFFbutton.place(x=400, y=20)

ONbutton = tk.Button(master, text="Spare", bg="blue", command=GPIO12button)
ONbutton.place(x=470, y=20)

OFFbutton = tk.Button(master, text="Spare",bg="blue" , command=GPIO25button)
OFFbutton.place(x=540, y=20)


Exitbutton = tk.Button(master, text="Close",bg="red", command=master.destroy)
Exitbutton.place(x=540, y=100)
master.mainloop()
