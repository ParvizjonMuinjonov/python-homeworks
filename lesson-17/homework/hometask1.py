import sqlite3
import pandas as pd

# Step 1: Connect to the chinook.db database
conn = sqlite3.connect('chinook.db')

# Step 2: Load the customers and invoices tables into DataFrames
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

# Step 3: Perform the inner join on CustomerId
merged_df = pd.merge(customers_df, invoices_df, 
                     on='CustomerId', 
                     how='inner')

# Step 4: Group by customer and count invoices
invoice_counts = (merged_df.groupby(['CustomerId', 'FirstName', 'LastName'])
                  .size()
                  .reset_index(name='InvoiceCount'))

# Step 5: Sort by CustomerId for readability
invoice_counts = invoice_counts.sort_values('CustomerId')

# Step 6: Display the results
print(invoice_counts)



# Step 7: Close the connection
conn.close()