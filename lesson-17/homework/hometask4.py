import pandas as pd  # Import the pandas library for data manipulation and analysis

# Read the CSV file 'movie.csv' into a DataFrame
movie_df = pd.read_csv('movie.csv')

# Group the DataFrame by 'color' and 'director_name' columns
# Then aggregate the data to calculate:
# - Total_reviews: Sum of 'num_critic_for_reviews'
# - Average_duration: Mean of 'duration'
groupped_df = movie_df.groupby(["color", "director_name"]).agg(
    Total_reviews = ("num_critic_for_reviews", "sum"),
    Average_duration = ("duration", "mean"),

)

# Print the resulting grouped and aggregated DataFrame
print(groupped_df)