import pandas as pd  # Import the pandas library for data manipulation and analysis

# Define a function to categorize age into groups
def age_group(age):
    if age < 18:  # If age is less than 18, classify as 'Child'
        return 'Child'
    elif pd.isna(age):  # If age is NaN (missing), classify as 'Unknown'
        return 'Unknown'
    else:  # Otherwise, classify as 'Adult'
        return 'Adult'

# Read the 'Age' column from the Titanic dataset Excel file
titanic_df = pd.read_excel("titanic.xlsx", usecols=['Age'])

# Apply the age_group function to the 'Age' column and create a new column 'Age_Group'
titanic_df['Age_Group'] = titanic_df['Age'].apply(age_group)

