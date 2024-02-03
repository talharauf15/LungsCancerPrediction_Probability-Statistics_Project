import seaborn as sns
from matplotlib.figure import Figure

def create_age_histogram(data):
    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    sns.histplot(data['Age'], bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_title('Age Distribution')
    return fig
