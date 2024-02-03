# This was created to test functions only
# Actual implementation is in UI.py file
from data_loader import load_data
from analysis.descriptive_stats import display_basic_info
from visualization.histograms import plot_age_distribution
from visualization.bar_charts import plot_gender_distribution, plot_cancer_level_distribution
from visualization.box_plots import plot_age_distribution_by_level
from visualization.scatter_plots import plot_scatter
from visualization.pie_charts import plot_pie_chart

def main():
    file_path = 'data/cancer patient data sets.csv'
    
    data = load_data(file_path)
    
    display_basic_info(data)
    
    plot_age_distribution(data)
    
    plot_gender_distribution(data)
    plot_cancer_level_distribution(data)
    
    plot_age_distribution_by_level(data)
    
    plot_scatter(data=data, x_column='Age', y_column='Alcohol use', hue='Level', title='Age vs Alcohol Use by Cancer Level')
    
    plot_pie_chart(data=data, column='Level', title='Distribution of Cancer Levels')

if __name__ == '__main__':
    main()
