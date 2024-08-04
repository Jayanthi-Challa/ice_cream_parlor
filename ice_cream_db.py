import sqlite3

conn = sqlite3.connect('ice_cream.db')
cursor = conn.cursor()

# Create a table for seasonal flavors
cursor.execute('''CREATE TABLE seasonal_flavors (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    season TEXT
                )''')

# Create a table for ingredient inventory
cursor.execute('''CREATE TABLE ingredient_inventory (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    stock INTEGER
                )''')

# Create a table for customer suggestions
cursor.execute('''CREATE TABLE customer_suggestions (
                    id INTEGER PRIMARY KEY,
                    flavor TEXT,
                    allergens TEXT
                )''')

# Create a table for user's cart
cursor.execute('''CREATE TABLE user_cart (
                    id INTEGER PRIMARY KEY,
                    flavor_id INTEGER,
                    FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors(id)
                )''')

# Create a table for allergens
cursor.execute('''CREATE TABLE allergens (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

conn.commit()
conn.close()