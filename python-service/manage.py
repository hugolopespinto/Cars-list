from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import sys

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import Element

class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


##
##  To execute the following commands, run the following
##  commands in the terminal:
##
##  docker exec -it hyperspace-python python manage.py {command} {args}
##
##  ex1: docker exec -it hyperspace-python python manage.py clear_db
##  ex2: docker exec -it hyperspace-python python manage.py create_db
##  ex3: docker exec -it hyperspace-python python manage.py create_item "McLaren F1 LM"
##

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'clear_db':
        with app.app_context():
            db.drop_all()
            db.create_all()
            print("Database tables cleared successfully.")
    if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
        with app.app_context():
            db.create_all()
            print("Database tables created successfully.")
    if len(sys.argv) > 2 and sys.argv[1] == 'create_item':
        with app.app_context():
            name = sys.argv[2]
            new_element = Element(name=name)
            db.session.add(new_element)
            db.session.commit()
            print("Database tables created successfully.")
