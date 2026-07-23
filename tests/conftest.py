import pytest 
import sqlite3
from modules.database import LibraryDatabase

@pytest.fixture(scope="module")
def connect_test_db():
    conn = LibraryDatabase("./database/test.db")
    conn.row_factory = sqlite3.Row
    yield conn


