import pandas as pd
import sqlite3

# Step 1: Read the CSV file into a DataFrame
#df = pd.read_csv('your_file.csv')

url = "https://raw.githubusercontent.com/riteshc6/amazon_scraper/master/downloads/Computers%20%26%20Accessories.csv"
df = pd.read_csv(url) 

# Step 2: Connect to an SQLite database (create if it doesn't exist)
conn = sqlite3.connect('amazon.db')

# Step 3: Write the DataFrame to the SQLite database
# This creates a new table 'your_table_name' in the database
df.to_sql('amazon', conn, if_exists='replace', index=False)

# Step 4: Close the connection
conn.close()