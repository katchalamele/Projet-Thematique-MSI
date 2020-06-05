import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

# this is the call to matplotlib that allows dynamic plotting
plt.ion()
fig = plt.figure(figsize=(13,6))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

def live_plotter(x_vec,y1_data,y2_data,y3_data,y4_data,line1,line2,line3,line4,pause_time=0.1):
    if line1==[]:
        # create a variable for the line so we can later update it
        line1, = ax1.plot(x_vec,y1_data, linewidth=5)
        line2, = ax2.plot(x_vec,y2_data, linewidth=5, color='blue', label='Envoyés')
        line3, = ax2.plot(x_vec,y3_data, linewidth=5, color='green', label='Reçus')
        line4, = ax3.plot(x_vec,y4_data, linewidth=5)
        #update plot label/title
        ax1.title.set_text('Nombre de croisements')
        ax2.title.set_text('Messages envoyés et reçus')
        ax3.title.set_text('Croisements par minutes')
        
        fig.text(0.5, 0.04, '<-- 25 dernières secondes -->', ha='center', va='center')
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    line2.set_ydata(y2_data)
    line3.set_ydata(y3_data)
    line4.set_ydata(y4_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        ax1.set_ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    if np.min(y2_data)<=line2.axes.get_ylim()[0] or np.max(y2_data)>=line2.axes.get_ylim()[1]:
        ax2.set_ylim([np.min(y3_data)-np.std(y3_data),np.max(y2_data)+np.std(y2_data)])
    if np.min(y4_data)<=line4.axes.get_ylim()[0] or np.max(y4_data)>=line4.axes.get_ylim()[1]:
        ax3.set_ylim([np.min(y4_data)-np.std(y4_data),np.max(y4_data)+np.std(y4_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    #plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1,line2,line3,line4