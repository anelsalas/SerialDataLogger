# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:09:56 2019

@author: ASALAS
"""
import platform
import serial
import sys

class SerialPort:

    usingplatform = ""
    serialport = None
    def __init__(self):
        self.baud = 9600
        usingplatform = self.GetPlatform()
        serialport = self.SerialPortInit()
        

        
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
               self.serialport = serial.Serial("COM4",self.baud)
            elif self.usingplatform == "aarch64":
               self.serialport = serial.Serial("/dev/ttyACM0",self.baud)
               
        except serial.SerialException as serialerr:
            error = serialerr
            print("Error opening serial port")
            print (error)
            #self.serialport.Serial.close()
            sys.exit()

    def ClosePort(self):
        self.serialport.Serial.close()

    def ReadLine(self):
        line = self.serialport.readline()
        line = line.decode()
        line = line.replace('\r','')
        line = line.replace('\n','')
        yield line

    def printoutData(self):
        while True:
            for l,l2 in self.XDat_gen():
                print(l)

    def XDat_gen(self):
        myiter = 0
        while True:
           myiter += 1
           if myiter == 100:
               myiter = 0

           try:
              dat = int(self.serialport.readline())
           except:
               dat = 0
           yield dat,myiter

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
    
    
    
    
