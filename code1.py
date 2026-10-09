import pandas as pd
import numpy as np

# Creating a messy dummy dataset to demonstrate cleaning capabilities
messy_data = {
    'Join_Date': ['2023-01-15', '2023/02/20', 'invalid_date', '2023-01-15', '2023-05-12'],
    'Emp_ID': ['101', '102', '103', '101', '105'],
    'Salary_String': ['$50,000', '$70,000', None, '$50,000', '$62,000'],
    'Performance_Score': [4.5, np.nan, 3.8, 4.5, 4.0]
}
df_messy = pd.DataFrame(messy_data)

print("--- Original Messy Dataset ---")
print(df_messy)

cleaning_log = []

# 1. Detect and handle missing values (drop / fill / impute)
missing_count = df_messy.isnull().sum().sum()
cleaning_log.append(f"Detected {missing_count} total missing values.")

# Impute missing numeric values with the column mean
mean_score = df_messy['Performance_Score'].mean()
df_messy['Performance_Score'] = df_messy['Performance_Score'].fillna(mean_score)
cleaning_log.append(f"Imputed missing Performance_Score values with mean score: {mean_score:.2f}")

# Fill missing text/categorical values with a placeholder
df_messy['Salary_String'] = df_messy['Salary_String'].fillna('$0')
cleaning_log.append("Filled missing Salary_String fields with a default placeholder ('$0').")


# 2. Fix incorrect dtypes (dates, numbers) and parse dates
# Clean string characters to convert to numeric types
df_messy['Salary_Cleaned'] = df_messy['Salary_String'].str.replace('$', '').str.replace(',', '')
df_messy['Salary_Cleaned'] = pd.to_numeric(df_messy['Salary_Cleaned'])
cleaning_log.append("Cleaned text punctuation and cast 'Salary_String' to numeric integer.")

# Parse date errors, setting unparseable text to NaT (Not a Time)
df_messy['Parsed_Date'] = pd.to_datetime(df_messy['Join_Date'], errors='coerce')
cleaning_log.append("Parsed 'Join_Date' column into standard datetime format (errors set to NaT).")


# 3. Remove duplicates and standardize column names
# Drop identical row values based on a primary identifier key
duplicate_count = df_messy.duplicated(subset=['Emp_ID']).sum()
df_clean = df_messy.drop_duplicates(subset=['Emp_ID'], keep='first').copy()
cleaning_log.append(f"Identified and removed {duplicate_count} duplicate row(s) based on 'Emp_ID'.")

# Standardize columns to snake_case / lowercase layout
df_clean.columns = df_clean.columns.str.strip().str.lower()
cleaning_log.append("Standardized all dataset header column names to lowercase layout.")


# 4. Output a cleaned dataset and a brief cleaning log
print("\n--- Final Cleaned Dataset ---")
print(df_clean)

print("\n--- Brief Cleaning Log Summary ---")
for line in cleaning_log:
    print(f"- {line}")

# Export final assets
df_clean.to_csv('cleaned_dataset_utility.csv', index=False)
with open('cleaning_process_log.txt', 'w') as log_file:
    for line in cleaning_log:
        log_file.write(f"{line}\n")
print("\nGenerated final output files: 'cleaned_dataset_utility.csv' and 'cleaning_process_log.txt'")