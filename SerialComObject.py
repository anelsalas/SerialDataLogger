# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:09:56 2019

@author: ASALAS
"""
import platform
import serial
import sys

class SerialPort:
    def __init__(self):
        self.baud = 9600
        self.usingplatform = ""
        self.GetPlatform()
        self.serialport = self.SerialPortInit()
        
    def GetPlatform (self):
        self.usingplatform = platform.machine()
        if self.usingplatform  == "aarch64":
            print("Platform", self.usingplatform, "Using Jetson Nano\n")
        elif self.usingplatform  == "AMD64":
            print("Platform: " , self.usingplatform, "Running on a Windows System\n")
    
        
    def SerialPortInit(self):
        try:
        # serialport = serial.Serial("/dev/ttyUSB1",9600)
            if self.usingplatform == "AMD64":
               return (serial.Serial("COM4",self.baud))
            elif self.usingplatform == "aarch64":
               return(serial.Serial("/dev/ttyACM0",self.baud))

               
        except serial.SerialException as serialerr:
            error = serialerr
            print (error)
            self.serialport.Serial.close()
            sys.exit()

    def ClosePort(self):
        self.serialport.Serial.close()
            
    
    def Data_gen(self):
        t = 0
        while True:
            t+=0.1
            try:
                line = self.serialport.readline()
                line = line.decode()
                line = line.replace('\r','')
                line = line.replace('\n','')
                dat = line
            except:
                dat = 0
            yield t, dat
            
        self.ClosePort()
    
    
    
    