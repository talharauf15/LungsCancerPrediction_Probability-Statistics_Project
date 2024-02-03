import seaborn as sns
from matplotlib.figure import Figure

def create_scatter_plot(data, x, y, hue=None, title=None):
    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    sns.scatterplot(x=x, y=y, hue=hue, data=data, ax=ax)
    if title:
        ax.set_title(title)
    return fig
