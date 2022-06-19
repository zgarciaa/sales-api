import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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

def createRoles():
        con = dbConnection()
        cursor = con.cursor()
        
        #Create basic roles
        ssql = """INSERT INTO sales_api_role (id, name) 
                     VALUES ('2c13e2e0-ef83-11ec-8ea0-0242ac120002', 'admin'),
                            ('5831f790-ef83-11ec-8ea0-0242ac120002','employee'),
                            ('607ed0c6-ef83-11ec-8ea0-0242ac120002','everyone');"""
        try:
            cursor.execute(ssql)
            print("Roles added successfully")
        except Exception as e:
            print(e)
        finally:
            # Closing database connection.
            if con:
                cursor.close()
                con.close()
                print("PostgreSQL connection is closed")
                
