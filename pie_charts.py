from matplotlib.figure import Figure

def create_pie_chart(data, column, title=None):
    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    pie_data = data[column].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(title if title else f'Pie Chart of {column}')
    ax.axis('equal')  # Equal aspect ratios
    return fig
