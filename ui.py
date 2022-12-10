import numpy as np
import pandas as pd

from datetime import datetime

import random
import geopandas as gpd
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from matplotlib import cm


def store(results):
    file = open("results.csv", "a")
    file.write(','.join(results))
    file.close()


def UI():
    print("Welcome to our experiment for COMP3736")
    print("In this experiment, you will be shown 20 different visualizations")
    print("For each visualization, you will be asked to respond to a question corresponding to the visualization")
    print("Please enter your option between 1 and 4 for each question")
    questions = ["Which country has the highest plastic waste per capita?",
                 "Which country has the highest plastic waste?",
                 "Which British region has the lowest plastic waste per capita?",
                 "Which British region has the highest plastic waste?",
                 "Which continent has the highest plastic waste per capita?",
                 "Which continent has the lowest plastic waste?",
                 "Which nation has the highest plastic waste per capita?",
                 "Which nation has the highest plastic waste?",
                 "Which US state has the highest plastic waste per capita?",
                 "Which US state has the lowest plastic waste?"]
    answers = [["Romania", "Sweden", "Hungary", "Serbia", 4],
               ["Moldova", "North Macedonia", "Latvia", "Switzerland", 2],
               ["Scotland", "East Midlands", "London", "South West", 2],
               ["South West", "London", "North East", "Northern Ireland", 1],
               ["Antarctica", "Europe", "North America", "South America", 1],
               ["Oceania", "South America", "Africa", "Asia", 2],
               ["England", "Scotland", "Wales", "Northern Ireland", 2],
               ["England", "Scotland", "Wales", "Northern Ireland", 3],
               ["California", "New York", "Texas", "Florida", 1],
               ["Wisconsin", "New Jersey", "Hawaii", "Alaska", 3]]
    results = []  # format is [time, correct]

    for pos, q in enumerate(questions):
        display()  # show the graph

        print("Q: " + q)
        for position, option in enumerate(answers[pos][:-1]):
            print(position + 1, ":", option)
        start_time = datetime.now()

        ans = int(input("Option: "))
        while ans < 1 or ans > 4:
            print("Invalid option, please try again")
            ans = int(input("Option: "))

        time_taken = datetime.now() - start_time
        results.append(str(time_taken.microseconds))
        results.append(str(ans == answers[pos][4]))
    store(results)
    print(results)


# to be changed to show image
def display():
    print("IMAGE HERE")


def generate(option, number_of_regions):
    """

    :param option: overall waste or per capita
    :param number_of_regions: number of regions to generate data for
    :return: an array of data
    """
    random.seed(120)

    upper = 3600  # in millions of tonnes
    if option == 2:  # change if per capita
        upper = 320  # in kg per person

    data = []
    for i in range(number_of_regions):
        data.append(random.randint(0, upper) / 100)

    return data


if __name__ == "__main__":
    # ukCountries(generate(1,12))
    UI()
    # print(generate(1, 5))
