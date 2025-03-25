import pandas as pd

# Define pipeline functions
def filter_survivors(df):
    return df[df['Survived'] == 1]

def fill_age_mean(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

# Load the Titanic dataset from Excel
titanic_df = pd.read_excel('titanic.xlsx')

# To Create and apply the pipeline:
pipeline_df = (titanic_df
               .pipe(filter_survivors)
               .pipe(fill_age_mean)
               .pipe(add_fare_per_age))

# Display the result
print(pipeline_df.head())