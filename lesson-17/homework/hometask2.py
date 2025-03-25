import pandas as pd

# Step 1: Load the movies.csv file
movies_df = pd.read_csv('movie.csv')

# Step 2: Create two smaller DataFrames
df1 = movies_df[['director_name', 'color']]  # director_name and color
df2 = movies_df[['director_name', 'num_critic_for_reviews']]  # director_name and num_critic_for_reviews

# Step 3: Perform a left join on director_name
left_join_df = pd.merge(df1, df2, on='director_name', how='left')

# Step 4: Perform a full outer join on director_name
outer_join_df = pd.merge(df1, df2, on='director_name', how='outer')

# Step 5: Count rows in each resulting DataFrame
left_join_rows = len(left_join_df)
outer_join_rows = len(outer_join_df)

# Step 6: Display the row counts
print(f"Number of rows in Left Join DataFrame: {left_join_rows}")
print(f"Number of rows in Full Outer Join DataFrame: {outer_join_rows}")