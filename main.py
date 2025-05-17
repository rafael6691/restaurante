from db import init_db
from gui.login import iniciar_login

def main():
    init_db()
    iniciar_login()

if __name__ == '__main__':
    main()
