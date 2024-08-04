import sqlite3

def get_db_connection():
    conn = sqlite3.connect('ice_cream.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_seasonal_flavor(name, season):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (name, season) VALUES (?, ?)', (name, season))
    conn.commit()
    conn.close()

def add_ingredient(name, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ingredient_inventory (name, stock) VALUES (?, ?)', (name, stock))
    conn.commit()
    conn.close()

def add_customer_suggestion(flavor, allergens):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customer_suggestions (flavor, allergens) VALUES (?, ?)', (flavor, allergens))
    conn.commit()
    conn.close()

def add_allergen(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def add_to_cart(flavor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_cart (flavor_id) VALUES (?)', (flavor_id,))
    conn.commit()
    conn.close()

def get_seasonal_flavors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def get_ingredients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ingredient_inventory')
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

def get_customer_suggestions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer_suggestions')
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

def get_allergens():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM allergens')
    allergens = cursor.fetchall()
    conn.close()
    return allergens

def get_user_cart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT sf.name FROM user_cart AS uc INNER JOIN seasonal_flavors AS sf ON uc.flavor_id = sf.id')
    cart = cursor.fetchall()
    conn.close()
    return cart