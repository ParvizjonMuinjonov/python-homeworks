import dask.dataframe as dd

# Read all valid Parquet files in the directory
flights_df = dd.read_parquet("flights",
                             columns=['Year', 'Month', 'ArrDelay', 'DepDelay'],
                             engine='pyarrow')

# Group by Year and Month
grouped_df = flights_df.groupby(['Year', 'Month']).agg({
    'ArrDelay': ['count', 'mean'],  # 'count' on any column gives total flights
    'DepDelay': ['max']
})

# Compute and reset index
result_df = grouped_df.compute().reset_index()

# Rename columns
result_df.columns = ['Year', 'Month', 'Total_Flights', 'Avg_ArrDelay', 'Max_DepDelay']

# Show result
print(result_df)
