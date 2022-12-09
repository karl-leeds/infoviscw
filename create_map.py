import numpy as np
import pandas as pd

from datetime import datetime

import random
import geopandas as gpd
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from matplotlib import cm

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


# create a map
def create_map(map_path, values, title, unit, filename):
    # Read the shapefile and store in dataframe
    map_df = gpd.read_file(map_path)

    # Add values to the dataframe
    map_df['Value'] = values
    print(max(values))
    print(map_df.values)

    # # Filter out Hawaii and Alaska as they mess up the visualization
    # map_df = map_df[map_df["NAME_1"] != 'Alaska']
    # map_df = map_df[map_df["NAME_1"] != 'Hawaii']
    #
    # # Tidy the dataframe
    # map_df = map_df[['ID_1', 'NAME_1', 'Value', 'geometry']]



    # # Give every country an index (not already in shp file)
    # map_df['index'] = np.arange(177)
    #
    # countryValue = []
    #
    # # Give every country a value depending on its continent
    # for i in map_df['CONTINENT']:
    #     if i == "Europe":
    #         countryValue.append(values[0])
    #     elif i == 'North America':
    #         countryValue.append(values[1])
    #     elif (i == 'South America'):
    #         countryValue.append(values[2])
    #     elif (i == 'Asia'):
    #         countryValue.append(values[3])
    #     elif (i == 'Africa'):
    #         countryValue.append(values[4])
    #     elif (i == 'Oceania'):
    #         countryValue.append(values[5])
    #     elif (i == 'Antarctica'):
    #         countryValue.append(values[6])
    #     elif (i == 'Seven seas (open ocean)'):
    #         countryValue.append(values[7])
    #
    # map_df['Value'] = countryValue
    #
    # # Filter the dataframe for cleaner data
    # map_df = map_df[['index', 'CONTINENT', 'Value', 'geometry']]

    # Create figure and axes
    fig, ax = plt.subplots(1, figsize=(20, 20))
    ax.axis("off")
    plt.title(title, fontsize=50)

    # Set Colourmap
    colour = plt.colormaps.get_cmap('Blues')

    # Set the colour scheme
    sm = cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=max(values)))
    sm.set_array([])

    # Set the color legend
    cbar = fig.colorbar(sm, fraction=0.03)
    cbar.set_label(unit, fontsize=30)

    # Increase the fontsize of the colour legend
    for t in cbar.ax.get_yticklabels():
        t.set_fontsize(20)

    # Label Every State
    map_df['coords'] = map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    map_df['coords'] = [coords[0] for coords in map_df['coords']]

    # Plot the map
    map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
    # plt.show()
    plt.tight_layout()
    # plt.savefig(filename, bbox_inches='tight', transparent=True)


if __name__ == "__main__":
    blah = ["Plastic pollution per capita (kg)", "Overall plastic pollution (million kg)"]
    q_number = 9
    unit = blah[(q_number % 2)]
    regions = 12
    title = "Plastic pollution per capita " + "for each US state"
    map_path = "geo_files/NUTS1_Jan_2018_SGCB_in_the_UK.shp"
    file_name = "q" + str(q_number) + ".png"
    create_map(map_path, generate(q_number, unit, regions), title, unit, file_name)
