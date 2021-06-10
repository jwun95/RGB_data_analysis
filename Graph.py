from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import Database

def run():
    fig = plt.figure()     #figure(도표) 생성

    ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 300)) #x축과 y축값 설정

    max_points = 50

    line, = ax.plot(np.arange(max_points), 
                    np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)

    def init():
        return line

    def animate(i):
        y = Database.total_run()
        old_y = line.get_ydata()
        new_y = np.r_[old_y[1:], y]
        line.set_ydata(new_y)
        print(new_y)
        return line

    anim = animation.FuncAnimation(fig, animate  , init_func= init ,frames=200, interval=1000, blit=False)
    plt.show()

if __name__ == "__main__":
    run()
