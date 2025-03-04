import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--save", help="Save File", action="store_true")
parser.add_argument('input_file', help="TSV File to read from", type=argparse.FileType('r', encoding='latin-1'))
args = parser.parse_args()

# print(args.save)

import matplotlib.animation as animation

def nanify(vals):
    if vals == -1:
        return np.nan
    return vals

history = pd.read_csv(args.input_file, sep="\t", header=None)
history = history.map(nanify)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

line = ax.plot([],[],[], '-o')[0]

def init():
    line.set_data_3d([],[],[])
    line.set_markersize(10)
    line.set_linewidth(2.5)
    return line,


def update_lines(num):

    line.set_data_3d(history.values[:num, :].T)
    line.set_color((0.5,0.5,0.5,0.2))
    
    line.set_markevery((num-1, 1))
    if not np.isnan(history.values[num, 0]):
        line.set_markeredgecolor((history.values[num, 0]/255,history.values[num, 1]/255,history.values[num, 2]/255))
        line.set_markerfacecolor((history.values[num, 0]/255,history.values[num, 1]/255,history.values[num, 2]/255))
        ax.set_title('Fruit: %i \nCurrent Colour: #%0.2X%0.2X%0.2X' % (num, *history.values[num, :].T.astype(np.int64)))

    if args.save:
        angle_norm = -(num/3 + 180) % 360 - 180
        ax.view_init(20, angle_norm-45, 0)

    return line,

# Setting the Axes properties
ax.set(xlim3d=(0, 255), xlabel='R')
ax.set(ylim3d=(0, 255), ylabel='G')
ax.set(zlim3d=(0, 255), zlabel='B')

ax.xaxis.line.set_color('r')
ax.yaxis.line.set_color('g')
ax.zaxis.line.set_color('b')

ax.xaxis.line.set_linewidth(2.5)
ax.yaxis.line.set_linewidth(2.5)
ax.zaxis.line.set_linewidth(2.5)


ax.set_xticks(np.arange(0, 255+1, 255))
ax.set_yticks(np.arange(0, 255+1, 255))
ax.set_zticks(np.arange(0, 255+1, 255))


ani = animation.FuncAnimation(
    fig, update_lines, history.shape[0], init_func=init, interval=100)

ax.view_init(20, -45, 0)

if args.save:
    print("Saving to file")
    ani.save("history.mp4")
    print("File Saved")
else:
    plt.show()


# for angle in range(0, 360*3 + 1):
#     # Normalize the angle to the range [-180, 180] for display
#     angle_norm = -(angle/3 + 180) % 360 - 180

#     # Cycle through a full rotation of elevation, then azimuth, roll, and all
#     elev = 20
#     azim = 0
#     roll = 0
#     azim = angle_norm-45

#     # Update the axis view and title
#     ax.view_init(elev, azim, roll)
#     # plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

#     plt.draw()
#     plt.pause(.001)