import plotly.graph_objects as go
import random


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def plot_data(statistics):
    fig = go.Figure()
    for alg_name in statistics:
        color = random_color()
        size = list(statistics[alg_name].keys())
        time = list(statistics[alg_name].values())
        fig.add_trace(go.Scatter(x=size, y=time, name=alg_name, line=dict(color=color, width=4)))
    fig.show()


def plot_ratio(statistics):
    fig = go.Figure()
    color = random_color()
    size = list(statistics.keys())
    ratio = list(statistics.values())
    fig.add_trace(go.Scatter(x=ratio, y=size, name='ratio', line=dict(color=color, width=4)))
    fig.show()
