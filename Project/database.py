import sqlite3

def create_table():
    conn = sqlite3.connect('products.db')
    cursor=conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS products(
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   in_stock INTEGER)''')
    conn.commit()
    conn.close()

def fetch_products():
    conn=sqlite3.connect('products.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def insert_product(id,name,in_stock):
    conn=sqlite3.connect('products.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO products(id, name, in_stock)VALUES(?, ?, ?)',(id, name,in_stock))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        cursor.close()
        conn.close()


def update_products(new_name,new_stock,id):
    conn=sqlite3.connect('products.db')
    cursor=conn.cursor()
    cursor.execute("UPDATE products SET name = ?, in_stock = ? WHERE id = ?",(new_name,new_stock,id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn=sqlite3.connect('products.db')
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM products WHERE id = ?',(id,))
    result=cursor.fetchone()
    conn.close()
    return result[0]>0

create_table()

