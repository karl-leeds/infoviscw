import matplotlib as matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import squarify
from datetime import datetime
import random

def store(results):
    file = open("results.csv","a")
    file.write(','.join(results))
    file.close()


def UI():
    print("Welcome to our experiment, please enter your option between 1 and 4 for each question")
    questions = ["Which country has the highest plastic waste per capita?"]
    answers = [["China", "Japan", "USA", "Korea", 1], ["a", "b", "c", "d"]]
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
    random.seed(datetime.now().microsecond)

    upper = 3600  # in millions of tonnes
    if option == 2:  # change if per capita
        upper = 320  # in kg per person

    data = []
    for i in range(number_of_regions):
        data.append(random.randint(0, upper) / 100)

    return data


if __name__ == "__main__":
    UI()
    # print(generate(1, 5))
