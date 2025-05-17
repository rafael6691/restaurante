import os
from db import init_db
from auth import crear_usuario, autenticar

def test_functional():
    init_db()
    assert crear_usuario('admin','1234')
    assert autenticar('admin','1234')
    print("All tests passed!")

if __name__ == '__main__':
    test_functional()
