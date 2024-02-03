import seaborn as sns
from matplotlib.figure import Figure

def create_dynamic_bar_chart(data, x_var, hue_var=None):
    fig = Figure(figsize=(10, 6))
    ax = fig.subplots()
    sns.countplot(x=x_var, hue=hue_var, data=data, palette='viridis', ax=ax)
    ax.set_title(f'{x_var} Distribution' + (f' by {hue_var}' if hue_var else ''))
    return fig
