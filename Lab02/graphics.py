import plotly.graph_objects as go
import random

dashes = {
    "best": None,
    "random": "dash",
    "worst": "dot"
}


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def plot_data(statistics):
    fig = go.Figure()
    for alg_name in statistics:
        color = random_color()
        for arr_type in statistics[alg_name]:
            dash = dashes[arr_type]
            size = list(statistics[alg_name][arr_type].keys())
            compares = list(statistics[alg_name][arr_type].values())
            fig.add_trace(go.Scatter(x=size, y=compares, name=(alg_name + " " + arr_type), line=dict(color=color, dash=dash, width = 4 )))
    fig.show()
