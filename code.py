
import pandas as pd

# 1. Read CSV and inspect the dataset
try:
    df = pd.read_csv('sample_data.csv')
    print("--- Dataset Loaded Successfully ---")

except FileNotFoundError:
    data = {
        'Employee_ID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
        'Salary': [45000, 65000, 60000, 50000, 75000],
        'Experience_Years': [2, 5, 4, 3, 6]
    }

    df = pd.DataFrame(data)
    print("--- Generated Dummy Dataset ---")

print("\n--- First 3 Rows ---")
print(df.head(3))

print("\n--- Last 2 Rows ---")
print(df.tail(2))

print("\n--- Data Types and Info ---")
df.info()

# 2. Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Specific Statistics ---")
print(f"Mean Salary: {df['Salary'].mean()}")
print(f"Median Experience: {df['Experience_Years'].median()}")
print(f"Minimum Salary: {df['Salary'].min()}")
print(f"Maximum Salary: {df['Salary'].max()}")
print(f"Total Records: {df['Employee_ID'].count()}")

# 3. Filter rows and select columns
print("\n--- Filtering and Slicing ---")
high_earners = df[df['Salary'] > 55000]

selected_columns = high_earners[
    ['Name', 'Department', 'Salary']
]

print(selected_columns)

# 4. Save filtered results to CSV
output_file = 'filtered_employee_analysis.csv'
selected_columns.to_csv(output_file, index=False)

print(f"\nResults saved to '{output_file}'")