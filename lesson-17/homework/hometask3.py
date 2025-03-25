import pandas as pd

# Load the Titanic dataset from an Excel file
titanic_df = pd.read_excel('titanic.xlsx')

# Group the dataset by passenger class (Pclass) and calculate:
# - Average age of passengers in each class
# - Total fare collected from passengers in each class
# - Count of passengers in each class
groupped_df = titanic_df.groupby("Pclass").agg(
    Average_Age=("Age", "mean"),  # Calculate the mean age
    Total_Fare=("Fare", "sum"),  # Calculate the total fare
    Count_of_Passengers=("PassengerId", "count")  # Count the number of passengers
)

# Round the results to 2 decimal places
groupped_df = groupped_df.round(2)

# Reset the index to convert the grouped data into a flat DataFrame
groupped_df.reset_index(inplace=True)

# Save the grouped data to a CSV file
groupped_df.to_csv("titanic.csv", index=False)