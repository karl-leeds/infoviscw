import numpy as np
import pandas as pd

from datetime import datetime

import random
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


# create a bar graph
def create_bar_graph(values, regions, title, xaxis, yaxis, filename):

    #Parameters
    #Values: the values for each bar (array of values)
    #Regions: the names of the regions that we are including in the bar graph - ie the labels of each bar (array of strings)
    #Title: the title of the bar graph (string)
    #xaxis the label for the x axis (string) 
    #yaxis: the label for the y axis (string)
    #filename: the filename we wish to save the bar graph as 
    
    # Create figure and axes
    fig, ax = plt.subplots(1, figsize=(30, 30))
    plt.title(title, fontsize=50)
    
    # Horizontal Bar Plot
    ax.barh(regions, values)

    # Add x, y gridlines
    ax.grid(b=True, color='black', linestyle='-.', linewidth=0.5, alpha=0.2)

    # X+Y Axis Label
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)

    for c in ax.containers:
        # Filter the labels
        labels = [v if v > 0 else "" for v in c.datavalues]
        ax.bar_label(c, labels=labels)

    
    plt.show()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', transparent=True)


if __name__ == "__main__":
    file_name = "q" + str(q_number) + ".png"
    
    #add other parameters
    create_bar_graph(file_name)
