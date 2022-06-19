import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

request = {
    'id' : 'a0f25f98-c5c3-4a00-b550-f616ae36b27a',
    'name' : 'Bananos',
    'description' : 'Docena',
    'price' : 1500
}  
print(request)

def dbConnection():
    try:  
        con = psycopg2.connect(
        database="store", 
        user="postgres", 
        password="bthemounim1",
        host="localhost"
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # Autocommit  
        return con
    
    except Exception as e:
        print("error", e)
        
def addProduct(product):
    #Connection to database
    con = dbConnection()
    cursor = con.cursor()
    
    id = product['id']
    name = product['name']
    description = product['description']
    price = str(product['price'])

    #Insert new Product
    ssql = f""" INSERT INTO products (id, name, description, price) 
            VALUES ('{id}', '{name}', '{description}', '{price}');"""
    try:
        cursor.execute(ssql)
        print("Product added successfully")
    except Exception as e:
        print(e)
    finally:
        # Closing database connection.
        if con:
            cursor.close()
            con.close()
            print("PostgreSQL connection is closed")

def listProducts():
    #Connection to database
    con = dbConnection()
    cursor = con.cursor()
    
    #Show all products
    ssql = f"""SELECT * FROM products"""
    try:
        cursor.execute(ssql)
        # Selecting rows from products table using cursor.fetchall
        product_records = cursor.fetchall()
        # Print each row and it's columns values
        for row in product_records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Description: ", row[2])
            print("Price: ", row[3], "\n")
            
    except (Exception, psycopg2.Error) as e:
        print("Error while fetching data from PostgreSQL", e)
        
    finally:
        # Closing database connection.
        if con:
            cursor.close()
            con.close()
            print("PostgreSQL connection is closed")