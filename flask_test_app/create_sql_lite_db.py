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











#import sqlite3

# 1. Connect to the SQLite database (or create it)
#conn = sqlite3.connect('my_database.db')

# 2. Create a cursor object
#cursor = conn.cursor()

# 3. Create a table
#cursor.execute(
'''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
'''
#)

# 4. Insert data into the table
#cursor.execute(
'''
    INSERT INTO users (name, age, email)
    VALUES ('John Doe', 30, 'john@example.com')
'''
#)

# Commit the transaction
#conn.commit()

# 5. Query the database
#cursor.execute('SELECT * FROM users')
#rows = cursor.fetchall()

# Print out each row
#for row in rows:
#    print(row)

# 6. Close the connection
#conn.close()

