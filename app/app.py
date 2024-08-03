import streamlit as st
import psycopg2
import os

def connect_db():
    return psycopg2.connect(
        host = os.getenv('DB_HOST'),
        database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASS')
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
                id SERIAL NOT NULL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT)
    """)
    conn.commit()
    cur.close()
    conn.close()


def add_user(first_name:str, last_name:str, age:int):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO users (first_name, last_name, age)
        VALUES ((%s), (%s), (%d))
    """, (first_name), (last_name), (age)
    )
    conn.commit()
    cur.close()
    conn.close()

def query_user():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall
    cur.close()
    conn.close()
    return users

def main():
    st.title("User Form")
    create_table()

    name =st.text_input("Add your name")
    last_name = st.text_input("Add your last name")
    age = st.time_input("Add your Age")
    if st.button("Submit"):
        add_user(name, last_name, age)
        st.success("User Created")
    
    st.subheader("Users")
    users = query_user()
    for user in user:
        st.write(f"Name: {user[0]}, Last name: {user[1]}, Age: {user[-1]}")

if __name__ == "__main__":
    main()