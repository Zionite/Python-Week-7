import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1
def load_and_explore_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset successfully loaded!")
        
        print("\nFirst 5 rows of the dataset:")
        print(data.head())
        
        print("\nDataset Info:")
        print(data.info())
      
        print("\nMissing Values:")
        print(data.isnull().sum())
        
        if data.isnull().sum().any():
            print("\nHandling missing values by filling with column means...")
            data = data.fillna(data.mean())
        else:
            print("\nNo missing values detected!")
            
        return data
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 2
def basic_data_analysis(data):
    print("\nBasic Statistics of Numerical Columns:")
    print(data.describe())
    
    if 'species' in data.columns:
        group_column = 'species'  
    else:
        group_column = data.select_dtypes('object').columns[0]
    
    print(f"\nGrouping by '{group_column}' and computing mean of numerical columns:")
    grouped_data = data.groupby(group_column).mean()
    print(grouped_data)
    
    print("\nInsights:")
    print("Patterns or interesting findings can be inferred based on grouped means and statistical summaries.")

# Task 3
def data_visualization(data):
    sns.set(style="whitegrid")
    
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        data = data.sort_values('date')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x='date', y=data.select_dtypes('number').columns[0])
        plt.title("Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.show()
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=group_column, y=data.select_dtypes('number').columns[0], data=data)
    plt.title("Average Value per Category")
    plt.xlabel(group_column.capitalize())
    plt.ylabel("Average Value")
    plt.show()
    
    plt.figure(figsize=(8, 6))
    sns.histplot(data=data.select_dtypes('number').iloc[:, 0], bins=20, kde=True, color="purple")
    plt.title("Distribution of Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data.select_dtypes('number').columns[0], y=data.select_dtypes('number').columns[1], data=data, hue=group_column)
    plt.title("Scatter Plot of Two Numerical Columns")
    plt.xlabel(data.select_dtypes('number').columns[0])
    plt.ylabel(data.select_dtypes('number').columns[1])
    plt.legend(title=group_column.capitalize())
    plt.show()

if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ")
    dataset = load_and_explore_dataset(file_path)
    if dataset is not None:
        basic_data_analysis(dataset)
        data_visualization(dataset)
