import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv 

df = pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
def random_set_off_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([data],["average"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range (0,1000):
        set_off_mean=random_set_off_mean(100)
        mean_list.append(set_off_mean)
    show_fig(mean_list)

setup()