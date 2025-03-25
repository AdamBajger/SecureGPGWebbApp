import sqlite3

def create_table_users(database: sqlite3.Connection):
    database.execute(sql: "CREATE DATABASE main; USE DATABASE main; CREATE TABLE users ")
    

