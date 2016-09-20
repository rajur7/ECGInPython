# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
#
# x = np.arange(0, 2*np.pi, 0.01)
# # x=1
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))  # update the data
#     return line,
#
#
# # Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.ma.array(x, mask=True))
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, init_func=init,
#                               interval=25, blit=False)
# plt.show()







from math import *
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def Plongeon():
    h = float(input("height = "))
    g = 9.81

    #calculate air time, Tc
    Tc = sqrt(2 * h / g)

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, h+1))  #ymax : initial height+1
    line, = ax.plot([], [], ' o', lw=2)

    step = 0.01  # animation step
    xs = [1]  # the vertical position is fixed on x-axis
    ys = [h]


    #    animation function.  This is called sequentially
    def animate(y):
        ys[-1] = y
        line.set_data(xs, ys)
        return line,

    def get_y():
        t = 0
        while t <= Tc:
            y = -0.5 * g * t**2 + h  # the equation of diver's displacement on y axis
            yield y
            t += step

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, frames=get_y, interval=100)

    plt.show()
Plongeon()