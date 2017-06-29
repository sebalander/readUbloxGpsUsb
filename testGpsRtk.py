#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 00:03:42 2017

@author: sebalander
"""
# %%
import numpy as np
import RTCM3 as rt

# %%
msg = 'B5 62 01 3B 28 00 00 00 00 00 E0 1E 61 13 A8 06 00 00 47 35 73 10 99 F9 62 E5 4E CF 79 EA 09 EF ED 00 C5 76 02 00 58 06 00 00 00 01 00 00 5D 2A'

msg1 = msg.replace(' ', '')

msg2 = [int(msg1[i:i+8], 32) for i in range(0, 96, 8)]



# %% leer pto serie
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()

# %% 
def procesaMensaje(mensaje):
    
    print(mensaje)
    aa = mensaje[-2].split(',')
    lat = aa[1]
    lon = aa[3]
    
    print(lat, lon)
    

# %%
import string as st
mensaje = list()


while len(mensaje) < 8:
    data_raw = str(ser.readline())
    
    if data_raw.find('GNVTG') is not -1:
        # mandar a procesar esta lista porque ya esta completa
        print(mensaje)

        # empezar lista nueva
        mensaje = list()
        mensaje.append(data_raw)
    else:
        mensaje.append(data_raw)


while True:
    data_raw = str(ser.readline())
    
    if data_raw.find('GNVTG') is not -1:
        # mandar a procesar esta lista porque ya esta completa
        # print(mensaje)
        procesaMensaje(mensaje)

        # empezar lista nueva
        mensaje = list()
        mensaje.append(data_raw)
    else:
        mensaje.append(data_raw)

