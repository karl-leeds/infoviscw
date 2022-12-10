import numpy as np
import pandas as pd

from datetime import datetime

import random
import matplotlib
import geopandas as gpd

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def generate(q_number, option, number_of_regions):
    """
    :param option: overall waste or per capita
    :param number_of_regions: number of regions to generate data for
    :return: an array of data
    """
    random.seed(120 + q_number)

    upper = 3600  # in millions of tonnes
    if option == "Plastic pollution per capita":  # change if per capita
        upper = 320  # in kg per person

    data = []
    for i in range(number_of_regions):
        data.append(random.randint(0, upper) / 100)

    return data


# create a bar graph
def create_bar_graph(map_path, values, title, xaxis, yaxis, filename):
    # Read the shapefile to get the region names and store in dataframe
    map_df = gpd.read_file(map_path)
    print(map_df.columns)
    print(map_df.values[0])

    # Parameters
    # map_path: the place where the map shape input file is located
    # Values: the values for each bar (array of values - use from generate)
    # Title: the title of the bar graph (string)
    # xaxis the label for the x axis (string)
    # yaxis: the label for the y axis (string)
    # filename: the filename we wish to save the bar graph as

    map_df['Value'] = values

    # Create figure and axes
    fig, ax = plt.subplots(1, figsize=(10, 7))
    plt.title(title, fontsize=20)

    # Horizontal Bar Plot
    ax.barh(map_df['NAME_1'], values)

    # Add x, y gridlines
    ax.grid(b=True, color='black', linestyle='-.', linewidth=0.5, alpha=0.2)

    # X+Y Axis Label
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)

    for c in ax.containers:
        # Filter the labels
        labels = [v if v > 0 else "" for v in c.datavalues]
        ax.bar_label(c, labels=labels)

    # plt.show()
    plt.tight_layout()

    plt.savefig(filename, bbox_inches='tight', transparent=False)


if __name__ == "__main__":
    blah = ["Plastic pollution per capita (kg)", "Overall plastic pollution (million kg)"]
    q_number = 20
    unit = blah[((q_number + 1) % 2)]  # only plus one for karl questions
    regions = 52  # number of regions in the bar graph
    file_name = "q" + str(q_number) + ".png"
    title = "Plastic pollution for each state"
    v = generate(q_number, unit, regions)
    map_file = "geo_files/USA_adm1.shp"  # location of map file
    yaxis = "State"
    create_bar_graph(map_file, v, title, unit, yaxis, file_name)
