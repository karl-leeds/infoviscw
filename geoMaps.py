# Website that helped create this: https://towardsdatascience.com/a-beginners-guide-to-create-a-cloropleth-map-in-python-using-geopandas-and-matplotlib-9cc4175ab630
# import pkg_resources
#
# pkg_resources.require("matplotlib==3.5.0")

import random
import warnings
import matplotlib
matplotlib.use('TkAgg')

import geopandas as gpd
import matplotlib.pyplot as plt

from matplotlib import cm
import numpy as np

# warnings.filterwarnings("ignore",category=plt.cm.warning)


# Generate list of random values of size input
def genRandom(size):
    numbers = []

    for i in range(0, size):
        numbers.append(random.randint(0, 100))

    return numbers


# UK Countries - Requires 4 values
def ukCountries(values):
    # Read the shapefile and store in dataframe
    map_df = gpd.read_file("geo_files/NUTS1_Jan_2018_SGCB_in_the_UK.shp")

    # Add values to the dataframe
    map_df['Value'] = values

    # Create figure and axes
    fig, ax = plt.subplots(1, figsize=(20, 20))
    ax.axis("off")
    plt.title("PLaceholder Title", fontsize=50)

    # Set Colourmap
    colour = plt.colormaps.get_cmap('Greens')

    # Set the colour scheme
    sm = cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
    sm.set_array([])

    # Set the color legend
    cbar = fig.colorbar(sm)
    cbar.set_label("Unit", fontsize=30)

    # Increase the fontsize of the colour legend
    for t in cbar.ax.get_yticklabels():
        t.set_fontsize(20)

    # Label Every State
    map_df['coords'] = map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    map_df['coords'] = [coords[0] for coords in map_df['coords']]

    # for idx, row in map_df.iterrows():
    #     plt.annotate(s=row['NAME_1'], xy=row['coords'], horizontalalignment='center', fontsize=10, text="hello")

    # Plot the map
    map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
    plt.savefig()


# # UK Counties - Requires 192 values
# def ukCounties(values):
#     # Read the shapefile and store in dataframe
#     map_df = gpd.read_file("geo_files/GBR_adm2.shp")
#
#     # Add the values to the dataframe
#     map_df['Value'] = values
#
#     # Filter out unnecessary data
#     map_df = map_df[['ID_2', 'NAME_2', 'Value', 'geometry']]
#
#     # Create figure
#     fig, ax = plt.subplots(1, figsize=(50, 50))
#     ax.axis("off")
#     plt.title("Placeholder Title", fontsize=50)
#
#     # Set Colourmap
#     colour = cm.get_cmap('Greens');
#
#     # Set the colour scheme
#     sm = plt.cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
#     sm.set_array([])
#
#     # Set the color legend
#     cbar = fig.colorbar(sm)
#     cbar.set_label("Unit", fontsize=30)
#
#     # Increase the fontsize of the colour legend
#     for t in cbar.ax.get_yticklabels():
#         t.set_fontsize(20)
#
#     # Label Every State
#     map_df['coords'] = map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
#     map_df['coords'] = [coords[0] for coords in map_df['coords']]
#
#     for idx, row in map_df.iterrows():
#         plt.annotate(s=row['NAME_2'], xy=row['coords'], horizontalalignment='center', fontsize=10)
#
#     # Plot DataFrames
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#
#
# # English Counties - Required 112 values
# def englishCounties(values):
#     # Read the shapefile and store in dataframe
#     map_df = gpd.read_file("geo_files/GBR_adm2.shp")
#
#     # Filter out the English counties, and include the values
#     map_df = map_df[map_df["NAME_1"] == 'England']
#     map_df['Value'] = values
#
#     # Filter out all unnecessary data
#     map_df = map_df[['ID_2', "NAME_2", 'Value', 'geometry']]
#
#     # Create figure and axis
#     fig, ax = plt.subplots(1, figsize=(30, 30))
#
#     # Disable axis
#     ax.axis("off")
#
#     plt.title("Placeholder Title", fontsize=50)
#
#     # Set Colourmap
#     colour = cm.get_cmap('Greens');
#
#     # Set the colour scheme
#     sm = plt.cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
#     sm.set_array([])
#
#     # Set the color legend
#     cbar = fig.colorbar(sm)
#     cbar.set_label("Unit", fontsize=30)
#
#     # Increase the fontsize of the colour legend
#     for t in cbar.ax.get_yticklabels():
#         t.set_fontsize(20)
#
#     # Label Every State
#     map_df['coords'] = map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
#     map_df['coords'] = [coords[0] for coords in map_df['coords']]
#
#     for idx, row in map_df.iterrows():
#         plt.annotate(s=row['NAME_2'], xy=row['coords'], horizontalalignment='center', fontsize=10);
#
#     # Plot DataFrame
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#
#
# # US States - Requires 52 values
# def usStates(values):
#     # Read the shapefile and store in dataframe
#     map_df = gpd.read_file("geo_files/USA_adm1.shp")
#     map_df['Value'] = values
#
#     # Filter out Hawaii and Alaska as they mess up the visualization
#     map_df = map_df[map_df["NAME_1"] != 'Alaska']
#     map_df = map_df[map_df["NAME_1"] != 'Hawaii']
#
#     # Tidy the dataframe
#     map_df = map_df[['ID_1', 'NAME_1', 'Value', 'geometry']]
#
#     # Create the figure and disable axes
#     fig, ax = plt.subplots(1, figsize=[200, 150])
#     ax.axis("off")
#     plt.title("Placeholder Title", fontsize=300)
#
#     # Set Colourmap
#     colour = cm.get_cmap('Blues');
#
#     # Set the colour scheme
#     sm = plt.cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
#     sm.set_array([])
#
#     # Set the color legend
#     cbar = fig.colorbar(sm, orientation="horizontal", fraction=0.05, pad=0)
#     cbar.set_label("Unit", fontsize=200)
#
#     # Increase the fontsize of the colour legend
#     for t in cbar.ax.get_xticklabels():
#         t.set_fontsize(200)
#
#     # Label Every State
#     map_df['coords'] = map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
#     map_df['coords'] = [coords[0] for coords in map_df['coords']]
#
#     for idx, row in map_df.iterrows():
#         plt.annotate(s=row['NAME_1'], xy=row['coords'], horizontalalignment='center', fontsize=100,
#                      arrowprops=dict(visible="True"))
#
#     # Plot DataFrames
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#
#
# # World - Requires 177 values
# def world(values):
#     map_df = gpd.read_file("geo_files/ne_110m_admin_0_countries.shp")
#
#     map_df['index'] = np.arange(177)
#     map_df['Value'] = values
#     map_df = map_df[['index', 'NAME', 'Value', 'geometry']]
#
#     fig, ax = plt.subplots(1, figsize=[100, 100])
#
#     # Set Colourmap
#     colour = cm.get_cmap('Blues');
#
#     # Plot DataFrames
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#
#
# # Continents - Requires 8 values
# def continents(values):
#     # Dataframe of every country in the world
#     map_df = gpd.read_file("geo_files/ne_110m_admin_0_countries.shp")
#
#     # Give every country an index (not already in shp file)
#     map_df['index'] = np.arange(177)
#
#     countryValue = []
#
#     # Give every country a value depending on its continent
#     for i in map_df['CONTINENT']:
#         if (i == "Europe"):
#             countryValue.append(values[0])
#         elif (i == 'North America'):
#             countryValue.append(values[1])
#         elif (i == 'South America'):
#             countryValue.append(values[2])
#         elif (i == 'Asia'):
#             countryValue.append(values[3])
#         elif (i == 'Africa'):
#             countryValue.append(values[4])
#         elif (i == 'Oceania'):
#             countryValue.append(values[5])
#         elif (i == 'Antarctica'):
#             countryValue.append(values[6])
#         elif (i == 'Seven seas (open ocean)'):
#             countryValue.append(values[7])
#
#     map_df['Value'] = countryValue
#
#     # Filter the dataframe for cleaner data
#     map_df = map_df[['index', 'CONTINENT', 'Value', 'geometry']]
#
#     # Create figure
#     fig, ax = plt.subplots(1, figsize=[15, 10])
#     ax.axis("off")
#     plt.title("Placeholder Title", fontsize=30)
#
#     # Set colour scheme
#     colour = cm.get_cmap("Greens")
#
#     # Set the colour legend
#     sm = plt.cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
#     sm.set_array([])
#
#     cbar = fig.colorbar(sm, orientation="horizontal", fraction=0.05, pad=0)
#     cbar.set_label("Unit", fontsize=20)
#
#     # Increase the fontsize of the colour legend
#     for t in cbar.ax.get_xticklabels():
#         t.set_fontsize(20)
#
#     # Plot the world
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#
#
# # Europe - Requires 38 values
# def europe(values):
#     # Get the value of every country, and filter by Europe
#     map_df = gpd.read_file("geo_files/ne_110m_admin_0_countries.shp")
#     map_df = map_df[map_df["CONTINENT"] == 'Europe']
#
#     # Filter out Russia, because is messes up the visualization
#     map_df = map_df[map_df["NAME"] != 'Russia']
#
#     map_df['Value'] = values
#     map_df = map_df[['NAME', 'Value', 'geometry']]
#
#     fig, ax = plt.subplots(1, figsize=[10, 10])
#     ax.axis("off")
#     plt.title("Placeholder Title", fontsize=20)
#
#     colour = cm.get_cmap("Greens")
#
#     # Set the colour scheme
#     sm = plt.cm.ScalarMappable(cmap=colour, norm=plt.Normalize(vmin=0, vmax=100))
#     sm.set_array([])
#
#     # Set the color legend
#     cbar = fig.colorbar(sm, fraction=0.05, pad=0)
#     cbar.set_label("Unit", fontsize=20)
#
#     # Plot Europe
#     map_df.plot(column='Value', cmap=colour, edgecolor='0', linewidth=2, ax=ax)
#

ukCountries(genRandom(12))
# englishCounties(genRandom(112))
# ukCounties(genRandom(192))
# usStates(genRandom(52))
# world(genRandom(177))
# continents(genRandom(8))
# europe(genRandom(38))
