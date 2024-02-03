import seaborn as sns
from matplotlib.figure import Figure

def create_age_distribution_by_level_chart(data):
    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    sns.boxplot(x='Level', y='Age', data=data, palette='cool', ax=ax)
    ax.set_title('Age Distribution by Cancer Level')
    return fig
