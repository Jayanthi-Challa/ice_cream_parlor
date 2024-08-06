import psycopg2
from psycopg2 import sql, OperationalError

DATABASE_URL = "postgres://postgres:jaya@localhost:5432/ice_cream"

def create_tables():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Create tables with constraints
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seasonal_flavors (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                season TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredient_inventory (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                stock INTEGER NOT NULL CHECK (stock >= 0)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer_suggestions (
                id SERIAL PRIMARY KEY,
                flavor TEXT NOT NULL,
                allergens TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_cart (
                id SERIAL PRIMARY KEY,
                flavor_id INTEGER NOT NULL REFERENCES seasonal_flavors(id) ON DELETE CASCADE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS allergens (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Tables created successfully")

    except OperationalError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_tables()