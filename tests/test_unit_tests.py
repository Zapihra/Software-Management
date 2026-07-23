import pytest
from modules.database import LibraryDatabase as Libdb


def test_authenticate_user(connect_test_db):
    
    user = Libdb.authenticate_user(connect_test_db, "admin", "admin123")
    assert user is not None
    assert user['username'] == "admin"
    assert user['password_hash'] == "pbkdf2_sha256$120000$f04b43f4cfd6f11eae7dff629a13ed7a$ae51eb988c0db7c7c9d77e7a37c56e366451e1a62ee921f1eb26ee91c2534c63"

def test_add_member(connect_test_db):
    #in
    new_member = {"member_code": "MB0002", "name": "abc", "email": "abc@abc", "phone":"123456", "address":"Lappeenranta"}
    Libdb.add_member(connect_test_db, new_member)

    user = Libdb.get_member_by_code(connect_test_db,"MB0002")

    assert user['name'] == 'abc'
    assert user['email'] == 'abc@abc'
    assert user['phone'] == '123456'
    assert user['address'] == 'Lappeenranta'

@pytest.mark.skip()
def test_build_heading():
    
    return

