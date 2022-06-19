import psycopg2
from psycopg2.sql import SQL, Identifier
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:  
    con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="bthemounim1",
        host="localhost"
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # Autocommit  
    cursor = con.cursor()
except Exception as e:
    print(e)

#Create a database
def createDataBase(db_name):
    ssql = """CREATE DATABASE {}
                WITH
                OWNER = postgres
                ENCODING = 'UTF8'
                CONNECTION LIMIT = -1;"""
    try:
        cursor.execute(SQL(ssql).format(Identifier(db_name)))
        print("Database successfully created")
    except Exception as e:
        print(e)
        
def createTables(name):
    sql_command = f""" CREATE TABLE public.{name}
                    (
                        id uuid NOT NULL,
                        name character varying(30) NOT NULL,
                        description character varying(30) NOT NULL,
                        price integer NOT NULL,
                        PRIMARY KEY (id)
                    );
                """
                
    try:
        cursor.execute(sql_command)
        print("Database successfully created")
    except Exception as e:
        print(e)

# Creating store DataBase
#db_name = "store"
#createDataBase(db_name)


        
    

    





