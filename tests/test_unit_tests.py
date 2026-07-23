import pytest
from modules.database import LibraryDatabase


def test_authenticate_user(connect_test_db):
    
    user = LibraryDatabase.authenticate_user(connect_test_db, "admin", "admin123")
    assert user is not None
    assert user['username'] == "admin"
    assert user['password_hash'] == "pbkdf2_sha256$120000$f04b43f4cfd6f11eae7dff629a13ed7a$ae51eb988c0db7c7c9d77e7a37c56e366451e1a62ee921f1eb26ee91c2534c63"
    

@pytest.mark.skip()
def test_build_heading():
    
    return

@pytest.mark.skip()
def test_add_user(connect_test_db):


    return