import pandas as pd

def get_descriptive_stats(data):
    numeric_data = data.select_dtypes(include=['number'])
    descriptive_stats = numeric_data.describe()
    return descriptive_stats

if __name__ == "__main__":
    # Loading the dataset 
    file_path = 'data/cancer patient data sets.csv' 
    data = pd.read_csv(file_path)
    
    # Printing descriptive statistics
    stats = get_descriptive_stats(data)
    print(stats)
    