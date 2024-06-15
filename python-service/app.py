from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.drop_all()
    db.create_all()
    logging.info("Database tables created and all items cleared.")

    default_elements = [
        Element(name='McLaren F1'),
        Element(name='BMW M3 GTR'),
        Element(name='Lamborghini Murciélago SV manual'),
        Element(name='Toyota Supra Mk4'),
        Element(name='Koenigsegg Regera'),
        Element(name='Bugatti Bolide'),
        Element(name='Pagani Zonda R'),
        Element(name='Aston Vanquish S'),
        Element(name='Porsche 911 GT3 RS'),
        Element(name='Nissan Skyline R34'),
        Element(name='Dodge Viper SRT10'),
        Element(name='BMW M3 E30'),
        Element(name='BMW M3 E36'),
        Element(name='BMW M3 E46'),
        Element(name='BMW M3 E92'),
        Element(name='BMW M3 F80'),
        Element(name='BMW M3 G80'),
        Element(name='BMW M5 E34'),
        Element(name='BMW M5 E39'),
        Element(name='BMW M5 E60'),
        Element(name='BMW M5 F90'),
        Element(name='BMW M6 E63'),
        Element(name='BMW M6 F13'),
        Element(name='BMW M8 F92'),
        Element(name='BMW E38 750iL V12'),
        Element(name='BMW M760e xDrive V12'),
    ]

    db.session.bulk_save_objects(default_elements)
    db.session.commit()
    logging.info("Default elements added to the database.")

# Routes
@app.route('/elements', methods=['GET'])
def get_elements():
    try:
        elements = Element.query.all()
        return jsonify([{'id': element.id, 'name': element.name} for element in elements])
    except Exception as e:
        logging.error(f"Error fetching elements: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/elements', methods=['POST'])
def add_element():
    try:
        data = request.get_json()
        name = data.get('name')

        print('name of new element:', name)

        new_element = Element(name=name)

        db.session.add(new_element)
        db.session.commit()

        logging.info(f"Added new element: {new_element}")

        return jsonify({'message': 'Element added successfully', 'id': new_element.id, 'name': new_element.name}), 201

    except Exception as e:
        logging.error(f"Error adding element: {e}")
        return jsonify({'error': 'Failed to add element'}), 500

@app.route('/clear-items', methods=['DELETE'])
def clear_items():
    try:
        db.session.query(Element).delete()
        new_element = Element(name='McLaren F1 ( yes i really want this one)')
        db.session.add(new_element)
        db.session.commit()
        return jsonify({'message': 'Items cleared successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to clear items'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
