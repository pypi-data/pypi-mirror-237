import os
from dotenv import load_dotenv
import mysql.connector


load_dotenv()

def fetch_all_from_database(db: str, table: str):
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=db

        )

        cursor = conn.cursor()

        query = "SELECT * FROM {}".format(table)
        cursor.execute(query)    
        result = cursor.fetchall()
        return result
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()


def delete_all_from_database(db: str, table: str):
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=db

        )

        cursor = conn.cursor()
        
        query = "TRUNCATE {}".format(table)
        cursor.execute(query)
        return "All records deleted"
            
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()
        
        
        
