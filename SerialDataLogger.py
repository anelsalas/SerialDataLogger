# -*- coding: utf-8 -*-

import numpy as np
import PlotObject

#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#import numpy as np
#import sys

import SerialComObject



def main():  
    com = SerialComObject.SerialPort()
    myplot = PlotObject.Matplot(com)
    
    #ani = animation.FuncAnimation(fig, run, com.Data_gen, interval=0, blit=True)
    myplot.updatePlot()
    #plt.show()
    com.ClosePort() 

if __name__ == "__main__":
   main()       
        