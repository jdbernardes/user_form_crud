import streamlit as st
import psycopg2
from dotenv import load_dotenv
import os

def connect_db():
    try:
        conn = psycopg2.connect(dbname=os.environ['DB_NAME'], 
                                user= os.environ['DB_USER'], 
                                host=os.environ['DB_HOST'], 
                                password=os.environ['DB_PASS'], 
                                port = os.environ['DB_PORT'])
        return conn
    except Exception as e:
        print(e)
        print("I am unable to connect to the database")

def create_table():
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                    id SERIAL NOT NULL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    age INT)
        """)
    conn.commit()
    conn.close()

def add_user(sql: str):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()

def query_user() -> list:
    conn = connect_db()
    users: list
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
    conn.close()
    return users

def main():
    st.title("User Form")
    create_table()

    name =st.text_input("Add your name")
    last_name = st.text_input("Add your last name")
    age = st.text_input("Add your age")
    if st.button("Submit"):
        sql = f"INSERT INTO users (name, last_name, age) VALUES ('{name}', '{last_name}', {age})"
        add_user(sql=sql)
        st.success("User Created")

    st.subheader("Users")
    users = query_user()
    for user in users:
        st.write(f"Name: {user[1]}, Last name: {user[2]}, Age: {user[-1]}")

if __name__ == "__main__":
    load_dotenv()
    main()