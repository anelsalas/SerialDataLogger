# -*- coding: utf-8 -*-

import numpy as np
import PlotObject
import SerialComObject


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# To save the animation, use e.g.
# ani.save("movie.mp4")
# or
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)


#quit()
   
elements = 100
fig, ax = plt.subplots()

x = np.arange(0,elements,1)
y = np.zeros(elements)
ax.set_ylim(0,1024)
ax.set_xlim(0,elements)

line, = ax.plot(x, y)
com = SerialComObject.SerialPort()

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(data):
    l,l2 = data
    y[l2] = l
    line.set_ydata(y)
    return line,



ani = animation.FuncAnimation(
    fig, animate,com.XDat_gen, init_func=init, interval=0, blit=True, save_count=50)
plt.show()
    



if __name__ == "__main__":
   main()       

