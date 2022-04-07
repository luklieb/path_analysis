#!/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

df = pd.read_csv('path.csv')

fig = plt.figure()
ax = plt.subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)
ax3d = plt.axes(projection='3d')

start = 1
end = 100
skip = 5

xdata = df[['x_pth']].iloc[start:end:skip]
ydata = df[['y_pth']].iloc[start:end:skip]
zdata = df[['z_pth']].iloc[start:end:skip]
tdata = df[['t_pth']].iloc[start:end:skip]
tBias = df[['t_pth']].iloc[0]
tDiff = tdata.diff().mean() #nanosec 0.25 sec sample rate
tEnd = (df[['t_pth']].iloc[-1] - tBias) * 1e-9
maxSpeedX = df[['x_pth']].diff().max() 

qtdata = (tdata - tdata.iloc[0])/1e9
print(tdata.min())
print(tdata.max())

ax3d.scatter3D(xdata, ydata, zdata, c=tdata, cmap='hsv')

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(axfreq, 'Time', 1., tEnd.values[0], valinit=0, valstep=10)

def update(val):
    ind = int(slider.val)
    xdata = df[['x_pth']].iloc[start:ind:skip]
    ydata = df[['y_pth']].iloc[start:ind:skip]
    zdata = df[['z_pth']].iloc[start:ind:skip]
    tdata = df[['t_pth']].iloc[start:ind:skip]
    ax3d.clear()
    ax3d.scatter3D(xdata, ydata, zdata, c=tdata, cmap='hsv')
    fig.canvas.draw()

slider.on_changed(update)

plt.show()

"""
df2 = pd.read_csv('tracker.csv')
print(df2)
print(df2.head())
print(df2.info())
xdata2 = df2[['x_trk']].iloc[start:end:skip]
ydata2 = df2[['y_trk']].iloc[start:end:skip]
zdata2 = df2[['z_trk']].iloc[start:end:skip]
tdata2 = df2[['t_trk']].iloc[start:end:skip]/1633969004000000000
ax.scatter3D(xdata2, ydata2, zdata2, c=tdata2, cmap='hsv')

"""