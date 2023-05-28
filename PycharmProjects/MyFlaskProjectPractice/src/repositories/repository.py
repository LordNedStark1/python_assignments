

from flask import jsonify
from pymongo import MongoClient

from src.models.House import House


def db_factory():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['practice_files']
    return db


class Repository:

    def __init__(self, db):
        self.db: MongoClient = db
        self.collection = self.db['houses']

    def save(self, house: House):
        person_dicts = []
        for person in house.persons:
            person_dict = {
                'name': person._name,
                'age': person._age,
                'height': person._height
            }
            person_dicts.append(person_dict)
        house_dict = {
            'address': house.address,
            'house_number': house.house_number,
            'persons': person_dicts
        }
        result = self.collection.insert_one(house_dict)

        return result.inserted_id

    def find_by_id(self, house_id):
        data = self.collection.find_one({'_id': house_id})
        if data is not None:
            return data
        # if data:
        #     return jsonify(data), 200
        # else:
        #     return 'Data not found', 404


    # except errors.ConnectionError:
    #     return 'Error connecting to database', 500