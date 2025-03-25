import pandas as pd

# Function to categorize movie duration into 'Short', 'Medium', or 'Long'
def duration(time):
    if time < 60:
        return 'Short'  # Movies less than 60 minutes are categorized as 'Short'
    elif time > 60 and time < 120:
        return 'Medium'  # Movies between 60 and 120 minutes are categorized as 'Medium'
    elif time > 120:
        return 'Long'  # Movies longer than 120 minutes are categorized as 'Long'
    else:
        return 'Unknown'  # Fallback for unexpected cases

# Read the movie data from a CSV file into a DataFrame
movie_df = pd.read_csv('movie.csv')

# Apply the duration function to the 'duration' column and create a new column 'Duration_term'
movie_df['Duration_term'] = movie_df['duration'].apply(duration)
