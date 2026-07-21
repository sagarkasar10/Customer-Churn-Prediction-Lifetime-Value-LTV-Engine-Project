"""Handles database connection for the Customer Churn project."""

import sqlite3
from backend.config import DATABASE_PATH


def get_database_connection():
    #Create and return a connection to the SQLite database.


    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def close_database_connection(connection):
    #Close an active database connection.

    if connection:
        connection.close()