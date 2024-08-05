import psycopg2
from psycopg2 import sql

DATABASE_URL = "postgres://postgres:jaya@localhost:5432/ice_cream"

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def add_seasonal_flavor(name, season):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('INSERT INTO seasonal_flavors (name, season) VALUES (%s, %s)'),
                [name, season]
            )
            cursor.close()
        except Exception as e:
            print(f"Error adding seasonal flavor: {e}")
        finally:
            conn.close()

def add_ingredient(name, stock):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('INSERT INTO ingredient_inventory (name, stock) VALUES (%s, %s)'),
                [name, stock]
            )
            cursor.close()
        except Exception as e:
            print(f"Error adding ingredient: {e}")
        finally:
            conn.close()

def add_customer_suggestion(flavor, allergens):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('INSERT INTO customer_suggestions (flavor, allergens) VALUES (%s, %s)'),
                [flavor, allergens]
            )
            cursor.close()
        except Exception as e:
            print(f"Error adding customer suggestion: {e}")
        finally:
            conn.close()

def add_allergen(name):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('INSERT INTO allergens (name) VALUES (%s)'),
                [name]
            )
            cursor.close()
        except Exception as e:
            print(f"Error adding allergen: {e}")
        finally:
            conn.close()

def add_to_cart(flavor_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('INSERT INTO user_cart (flavor_id) VALUES (%s)'),
                [flavor_id]
            )
            cursor.close()
        except Exception as e:
            print(f"Error adding to cart: {e}")
        finally:
            conn.close()

def get_seasonal_flavors():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM seasonal_flavors')
            flavors = cursor.fetchall()
            cursor.close()
            return flavors
        except Exception as e:
            print(f"Error retrieving seasonal flavors: {e}")
        finally:
            conn.close()
    return []

def get_ingredients():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ingredient_inventory')
            ingredients = cursor.fetchall()
            cursor.close()
            return ingredients
        except Exception as e:
            print(f"Error retrieving ingredients: {e}")
        finally:
            conn.close()
    return []

def get_customer_suggestions():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customer_suggestions')
            suggestions = cursor.fetchall()
            cursor.close()
            return suggestions
        except Exception as e:
            print(f"Error retrieving customer suggestions: {e}")
        finally:
            conn.close()
    return []

def get_allergens():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM allergens')
            allergens = cursor.fetchall()
            cursor.close()
            return allergens
        except Exception as e:
            print(f"Error retrieving allergens: {e}")
        finally:
            conn.close()
    return []

def get_user_cart():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL('SELECT sf.name FROM user_cart AS uc INNER JOIN seasonal_flavors AS sf ON uc.flavor_id = sf.id')
            )
            cart = cursor.fetchall()
            cursor.close()
            return cart
        except Exception as e:
            print(f"Error retrieving user cart: {e}")
        finally:
            conn.close()
    return []