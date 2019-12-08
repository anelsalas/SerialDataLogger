# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 06:34:24 2019

@author: ASALAS
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import csv


#xdata, ydata = [0]*matrixsize, [0]*matrixsize


class Matplot:
    def __init__(self,com):
        self.numberOfElements = 30000
        self.xdata, self.ydata = [0]*self.numberOfElements, [0]*self.numberOfElements
        
        # Creates just a figure and only one subplot
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('10 bit ADC (1024)')
        self.ax.set_title('Preassure vs Time')

        self.line, = self.ax.plot(np.random.rand(10))
        self.ax.set_ylim(0, 1023)
        self.ax.set_xlim(0, 1000)#self.numberOfElements)
        self.com = com
        self.totalcount = 0
        self.file = open("data.csv","a")
        self.writer = csv.writer(self.file)

       
   
    def run(self,data):
        t,y = data
        del self.xdata[0]
        del self.ydata[0]
        self.xdata.append(t)
        self.ydata.append(y)
        self.totalcount += 1
        self.writer.writerow(y)
        

        self.line.set_data(self.xdata, self.ydata)
#        if self.totalcount == 25000:
#            with open("data.csv", "wb") as f:
#                writer = csv.writer(f)
#                writer.writerows(self.ydata)
        return self.line,
    
    def updatePlot(self):
        animation.FuncAnimation(self.fig, self.run, self.com.Data_gen, interval=0, blit=True)
        plt.show()
    
def testplots():
        # First create some toy data:
        x = np.linspace(0, 2*np.pi, 400)
        y = np.sin(x**2)
        
        # Creates just a figure and only one subplot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Simple plot')
        
        # Creates two subplots and unpacks the output array immediately
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.plot(x, y)
        ax1.set_title('Sharing Y axis')
        ax2.scatter(x, y)
        
        # Creates four polar axes, and accesses them through the returned array
        fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
        axes[0, 0].plot(x, y)
        axes[1, 1].scatter(x, y)
        
        # Share a X axis with each column of subplots
        plt.subplots(2, 2, sharex='col')
        
        # Share a Y axis with each row of subplots
        plt.subplots(2, 2, sharey='row')
        
        # Share both X and Y axes with all subplots
        plt.subplots(2, 2, sharex='all', sharey='all')
        
        # Note that this is the same as
        plt.subplots(2, 2, sharex=True, sharey=True)
        
        # Creates figure number 10 with a single subplot
        # and clears it if it already exists.
        fig, ax=plt.subplots(num=10, clear=True)
        
        plt.show()