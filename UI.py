# This file sets up a GUI application for visualizing cancer patient data.

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import read_csv

# Importing functions from other modules for plotting and analysis
from visualization.histograms import create_age_histogram
from visualization.bar_charts import create_dynamic_bar_chart
from visualization.box_plots import create_age_distribution_by_level_chart
from visualization.scatter_plots import create_scatter_plot
from visualization.pie_charts import create_pie_chart
from analysis.probability_distributions import fit_binomial_distribution
from analysis.regression_models import perform_logistic_regression
from analysis.descriptive_stats import get_descriptive_stats

# Defining colors for the UI
bg_color = "#4f4f4e"  
button_color = "#bd8dd6"  
text_color = "#ebdcf2"  

# Function to display plots in a new window
def display_plot(create_plot_func, data):
    plot_window = tk.Toplevel()
    plot_window.title("Visualization")
    fig = create_plot_func(data)
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Function to create input form for bar chart
def create_bar_chart_form(data):
    form_window = tk.Toplevel()
    form_window.title("Create Bar Chart")
    tk.Label(form_window, text="X-axis variable:").pack()
    x_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    x_var_entry.pack()
    tk.Label(form_window, text="Hue variable (optional):").pack()
    hue_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    hue_var_entry.pack()
    submit_button = tk.Button(form_window, text="Create Bar Chart",
                              command=lambda: display_plot(
                                  lambda data: create_dynamic_bar_chart(data, x_var_entry.get(), hue_var_entry.get() if hue_var_entry.get() else None),
                                  data))
    submit_button.pack()

# Function to create input form for pie chart
def create_pie_chart_form(data):
    form_window = tk.Toplevel()
    form_window.title("Create Pie Chart")
    tk.Label(form_window, text="Categorical variable:").pack()
    cat_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    cat_var_entry.pack()
    submit1_button = tk.Button(form_window, text="Create Pie Chart",
                               command=lambda: display_plot(
                                   lambda data: create_pie_chart(data, cat_var_entry.get()),
                                   data))
    submit1_button.pack()

# Function to create input form for scatter plot
def create_scatter_plot_form(data):
    form_window = tk.Toplevel()
    form_window.title("Create Scatter Plot")
    tk.Label(form_window, text="X-axis variable:").pack()
    x_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    x_var_entry.pack()
    tk.Label(form_window, text="Y-axis variable:").pack()
    y_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    y_var_entry.pack()
    tk.Label(form_window, text="Hue variable (optional):").pack()
    hue_var_entry = ttk.Combobox(form_window, values=list(data.columns))
    hue_var_entry.pack()
    submit_button = tk.Button(form_window, text="Create Scatter Plot",
                              command=lambda: display_plot(
                                  lambda data: create_scatter_plot(data, x_var_entry.get(), y_var_entry.get(), hue_var_entry.get() if hue_var_entry.get() else None),
                                  data))
    submit_button.pack()

# Function to apply binomial distribution and display results
def on_apply_binomial():
    try:
        binomial_params = fit_binomial_distribution(data['Air Pollution'], trials=10, success_prob=0.5)
        result_text = f"Binomial Parameters: n={binomial_params['n']}, p={binomial_params['p']:.3f}"
        tkinter.messagebox.showinfo("Binomial Distribution Results", result_text)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

# Applying logistic regression
def on_perform_regression():
    try:
        # Applying predictors and target for logistic regression
        predictors = ['Age', 'Air Pollution', 'Alcohol use', 'Dust Allergy','OccuPational Hazards','Genetic Risk',
                      'chronic Lung Disease','Balanced Diet','Obesity','Smoking','Passive Smoker','Chest Pain',
                      'Coughing of Blood','Fatigue','Weight Loss','Shortness of Breath','Wheezing','Swallowing Difficulty',
                      'Clubbing of Finger Nails','Frequent Cold','Dry Cough','Snoring'] 
        target = 'Level'  

        # Perform logistic regression
        regression_result = perform_logistic_regression(data, predictors, target)

        # Displaying the regression result
        tkinter.messagebox.showinfo("Regression Analysis Results", regression_result)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

# Applying descriptive statistics
def display_descriptive_stats(data):
    stats_window = tk.Toplevel()
    stats_window.title("Descriptive Statistics")
    stats_text = get_descriptive_stats(data)
    stats_label = tk.Label(stats_window, text=stats_text, justify="left")
    stats_label.pack()

# Loading the dataset
file_path = 'data/cancer patient data sets.csv' 
data = read_csv(file_path)

# Setting up the main application window
root = tk.Tk()
root.title("Visualizations of Cancer Data")
root.configure(bg=bg_color) # for colors in UI

# Function to create styled buttons
def create_styled_button(parent, text, command):
    return tk.Button(parent, text=text, command=command, bg=button_color, fg=text_color)

# Creating and placing buttons for each visualization and analysis
button_age_distribution = create_styled_button(root, "Age Distribution (Histogram)", lambda: display_plot(create_age_histogram, data))
button_age_distribution_by_level = create_styled_button(root, "Age Distribution by Level (Box Plot)", lambda: display_plot(create_age_distribution_by_level_chart, data))
button_bar_chart = create_styled_button(root, "Create (Bar Charts)", lambda: create_bar_chart_form(data))
button_gender_distribution = create_styled_button(root, "Create (Pie Charts)", lambda: create_pie_chart_form(data))
button_scatter_plot = create_styled_button(root, "Create (Scatter Plots)", lambda: create_scatter_plot_form(data))
binomial_button = create_styled_button(root, "Air Pollution (Binomial Distribution)", on_apply_binomial)
regression_button = create_styled_button(root, "Perform Risk Factor Analysis (Logistic Regression)", on_perform_regression)
button_descriptive_stats = create_styled_button(root, "Descriptive Statistics", lambda: display_descriptive_stats(data))

# Calling button packs
button_age_distribution.pack(pady=5)
button_age_distribution_by_level.pack(pady=5)
button_bar_chart.pack(pady=5)
button_gender_distribution.pack(pady=5)
button_scatter_plot.pack(pady=5)
binomial_button.pack(pady=5)
regression_button.pack(pady=5)
button_descriptive_stats.pack(pady=5)

# Starting the main application loop
root.mainloop()
