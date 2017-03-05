from flask_script import Manager
from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
