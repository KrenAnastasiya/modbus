#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from tkinter import Tk, Canvas, Frame, BOTH
  
from tkinter import *

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	
import logging


import time
	
color_enter = "red"
color_exit = "red"


def record_enter(i):
	rq = client.write_register(1, i, unit=1)
	rr = client.read_holding_registers(1, 1, unit=1)
	print(rr.registers[0])
	print("Запись на вход")
	return rr.registers[0]

def record_exit(i):
	print("Запись на выход")
	rq = client.write_register(2, i, unit=1)
	rr = client.read_holding_registers(2, 1, unit=1)
	print(rr.registers[0])
	return rr.registers[0]



def ready():
	color_enter = "green"
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)

def ready_exit():
	color_exit = "green"
	canvas.create_rectangle(340,50, 580, 290, outline="gray", fill=color_exit)
	canvas.pack(fill=BOTH, expand=1)

def wait_pass():
	color_enter = "yellow"
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)

def passw():
	color_enter = "blue"
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)

def timeout():
	color_enter = "red"
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)

def switch_demo(argument):
    switcher = {
        1: ready,
        2: wait_pass,
        3: passw,
        4: timeout
    }



def callback():
	color_enter = "red"
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)
	rq = client.write_register(2, 3, unit=1)
	rr = client.read_holding_registers(2, 1, unit=1)
	print(rr.registers[0])
	switch_demo(rr)

def callback_exit():
	color_enter = "red"
	canvas.create_rectangle(340,50, 580, 290, outline="gray", fill=color_exit)
	canvas.pack(fill=BOTH, expand=1)
	rq = client.write_register(2, 3, unit=1)
	rr = client.read_holding_registers(2, 1, unit=1)
	print(rr.registers[0])
	switch_demo(rr)





logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO) 

i = 0
while (i<=10):
	i = i + 1
	client = ModbusClient('localhost', port=5020)

	client.connect()


	#i = 0
	#while True: # Запускаем цикл
	#    i = i+1
	#    record(i)
	#    time.sleep(10)

	first_enter = client.read_holding_registers(1, 1, unit=1)

	second_enter = record_enter(i)


	first_exit = client.read_holding_registers(2, 1, unit=1)

	second_exit = record_exit(i)
		
	master = Tk()
	master.geometry("630x500")
		
	canvas = Canvas()
	canvas.create_text(130, 30, anchor=W, font="Purisa",
	           text="На вход")
	canvas.create_rectangle(50,50, 290, 290, outline="gray", fill=color_enter)
	canvas.pack(fill=BOTH, expand=1)
	canvas.create_text(420, 30, anchor=W, font="Purisa",
	            text="На выход")
	canvas.create_rectangle(340,50, 580, 290, outline="gray", fill=color_exit)
	canvas.pack(fill=BOTH, expand=1)

	b = Button(master, text="Сбросить на вход", command=callback,height=10, width=50)
	b.pack()
	b1 = Button(master, text="Сбросить на выход", command=callback_exit,height=10, width=50)
	b1.pack(padx=5, pady=15)

	

	if(first_enter.registers[0]!=second_enter):
		print(first_enter.registers[0])
		print("----")
		print(second_enter)
		print("регистр изменен1")
		ready()
	if(first_exit.registers[0]!=second_exit):
		print(first_exit.registers[0])
		print("====")
		print(second_exit)
		print("регистр изменен2")
		ready_exit()

	#wait_pass()
	#passw()
	#timeout()
	master.mainloop()  

 
   