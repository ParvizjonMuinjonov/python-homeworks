import dask.dataframe as dd

# Define function to filter flights with departure delay > 30 minutes
def filter_delayed_flights(df):
    return df[df['DepDelay'] > 30]

# Define function to add Delay_Per_Hour column by dividing delay by flight duration
def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['FlightDuration']
    return df

# Load the flights dataset from Parquet files
flights_df = dd.read_parquet('flights/*.parquet', 
                             columns=['DepDelay', 'FlightDuration'])

# Create and apply the pipeline
pipeline_df = (flights_df
               .pipe(filter_delayed_flights)
               .pipe(add_delay_per_hour))

# Compute the result and display it
result_df = pipeline_df.compute()
print(result_df.head())