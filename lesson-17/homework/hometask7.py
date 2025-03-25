import pandas as pd

# Load the employee.csv file
employee_df = pd.read_csv('employee.csv')

# Normalize BASE_SALARY within each DEPARTMENT
employee_df['Normalized_Salary'] = employee_df.groupby('DEPARTMENT')['BASE_SALARY'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() != x.min() else 0
)

# Display the result
print(employee_df.head())