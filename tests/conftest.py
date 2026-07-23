import pytest 
import sqlite3
from modules.database import LibraryDatabase

@pytest.fixture(scope="session")
def connect_test_db():
    conn = LibraryDatabase("./database/test.db")
    conn.row_factory = sqlite3.Row
    
    #c = conn.cursor(":memory:")
    
    #c.execute(
    #    '''CREATE TABLE users (
    #        username TEXT,
    #        password_hash TEXT
    #    );''')
    #conn.commit()

    #c.execute("INSERT INTO users VALUES (?,?)", ("admin", "admin123"))
    #conn.commit()

    yield conn

    #conn.close()

