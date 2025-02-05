import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1) #grid system

def animate(i):
    graph_data = open('/home/pdtecholution/Documents/Technolution prerequisites/Transformer Monitoring/Vibration analysis/Vibration/accelCatch.txt','r').read()
    lines = graph_data.split('\n')
    xs = [] #empty list
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear() #clear screen to get rid of previous screen
    ax1.plot(xs, ys)
    

ani = animation.FuncAnimation(fig,animate,interval=1000) #1000ms
plt.show()

'''
def animate(i):
    graph_data = open('samplefile.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if

'''
