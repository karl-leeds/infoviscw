import time

import numpy as np
import pandas as pd

from datetime import datetime

import random
import geopandas as gpd
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from matplotlib import cm

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


def store(results):
    file = open("results.csv", "a")
    file.write(','.join(results))
    file.write(',')
    file.close()


def end():
    file = open("results.csv", "a")
    file.write('\n')
    file.close()


def UI():
    print("Welcome to our experiment for COMP3736")
    print("In this experiment, you will be shown 20 different visualizations")
    print("For each visualization, you will be asked to respond to a question corresponding to the visualization")
    print("Please enter your option between 1 and 4 for each question")
    print("Make sure to read the question and your options thoroughly before answering\n")

    waiting = input("Press enter when you're ready to begin...")

    random.seed(420)  # so reproducible
    # sequence = random.sample(range(0, 20), 20)  # order the questions are selected in
    sequence = [i for i in range(0, 20)]
    questions = ["Which continent has the highest pollution?",
                 "Which continent has the lowest pollution per capita?",
                 "Which country has the highest pollution?",
                 "Which country has the highest pollution per capita?",
                 "Which nation has the lowest pollution?",
                 "Which nation has the highest pollution per capita?",
                 "Which US state has the largest pollution?",
                 "Which US state has the smallest pollution per capita?",
                 "Which British region had the highest pollution?",
                 "Which British region had the lowest pollution per capita?",
                 "Which country has the highest plastic waste per capita?",
                 "Which country has the highest plastic waste?",
                 "Which British region has the lowest plastic waste per capita?",
                 "Which British region has the highest plastic waste?",
                 "Which continent has the highest plastic waste per capita?",
                 "Which continent has the lowest plastic waste?",
                 "Which nation has the highest plastic waste per capita?",
                 "Which nation has the highest plastic waste?",
                 "Which US state has the highest plastic waste per capita?",
                 "Which US state has the lowest plastic waste?"]
    answers = [["Oceania", "South America", "Africa", "Asia", 4],
               ["Oceania", "Europe", "North America", "South America", 1],
               ["Poland", "Norway", "Slovenia", "France", 3],
               ["Romania", "Sweden", "Austria", "Serbia", 3],
               ["England", "Scotland", "Wales", "Northern Ireland", 4],
               ["England", "Scotland", "Wales", "Northern Ireland", 3],
               ["Texas", "Indianapolis", "Nevada", "Florida", 2],
               ["Oregon", "Wisconsin", "North Dakota", "Wyoming", 2],
               ["SW", "SC", "NI", "NW", 4],
               ["SC", "WA", "LN", "NE", 1],
               ["Romania", "Sweden", "Hungary", "Serbia", 4],
               ["Serbia", "North Macedonia", "Latvia", "Switzerland", 1],
               ["Scotland", "East Midlands", "London", "South West", 2],
               ["South West", "London", "North East", "Northern Ireland", 1],
               ["Antarctica", "Europe", "North America", "South America", 1],
               ["Oceania", "South America", "Africa", "Asia", 2],
               ["England", "Scotland", "Wales", "Northern Ireland", 2],
               ["England", "Scotland", "Wales", "Northern Ireland", 3],
               ["California", "New York", "Texas", "Florida", 1],
               ["Wisconsin", "New Jersey", "Hawaii", "Alaska", 3]]
    dimensions = [(1000, 500),
                  (1000, 500),
                  (900, 500),
                  (900, 500),
                  (800, 500),  # 5
                  (800, 500),
                  (1000, 500),
                  (1000, 500),
                  (800, 500),
                  (800, 500),  # 10
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  (1000, 500),
                  ]

    for pos, q in enumerate(questions):
        curr = sequence[pos]
        root = tk.Tk()
        root.title("InfoVis Survey")

        canvas = tk.Canvas(root, width=1000, height=500)
        canvas.pack()

        og = Image.open('q{}.png'.format(str(curr + 1)))
        newI = og.resize(dimensions[curr])
        img = ImageTk.PhotoImage(newI)
        canvas.create_image(0, 0, anchor=NW, image=img)

        question = Label(text='Q{}:{}'.format(str(curr + 1), q))
        question.pack(side=tk.TOP)

        frame = tk.Frame(root)
        frame.pack()

        var = tk.IntVar()

        option1 = tk.Radiobutton(frame, text=answers[curr][0], value=1, variable=var)
        option1.pack(side=tk.LEFT)
        option2 = tk.Radiobutton(frame, text=answers[curr][1], value=2, variable=var)
        option2.pack(side=tk.LEFT)
        option3 = tk.Radiobutton(frame, text=answers[curr][2], value=3, variable=var)
        option3.pack(side=tk.LEFT)
        option4 = tk.Radiobutton(frame, text=answers[curr][3], value=4, variable=var)
        option4.pack(side=tk.LEFT)

        def check_answer(start, answer):
            # check the value of the selected radio button
            selected = var.get()

            store([str((start - datetime.now()).microseconds), str(selected == answer)])
            root.destroy()

        start_time = datetime.now()
        submit_button = tk.Button(root, text="Submit", command=lambda: check_answer(start_time, answers[curr][4]))
        submit_button.pack()

        root.mainloop()

    end()

    time.sleep(1)


if __name__ == "__main__":
    UI()
