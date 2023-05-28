from bson import ObjectId
from flask import Flask
from pymongo import MongoClient

from src.services.house_service import HouseService

app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['your_database_name']


@app.route('/')
def find_house_by_id():
    house_service = HouseService()
    variable = ObjectId("64728f2a3fd7bfd5ab91c229")
    return house_service.find_house_by_id(variable)

def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
