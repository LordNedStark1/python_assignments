

from bson import json_util, ObjectId


import app
# from app import db
from src.models.House import House
from src.models.Person import Person
from src.services.house_service import HouseService

persons = [Person("ade", 29, 5.5), Person("shola", 19, 5.6), Person("ola", 23, 9.9)]
house_service = HouseService()


def main():
    house_id = house_service.save_house("Yaba", 321, persons)
    return house_id


def main2(house_id):
    return house_service.find_house_by_id(house_id)


variable = ObjectId('64728f2a3fd7bfd5ab91c229')
objDict = main2(variable)

print(objDict)
# id, address, house_number, *other = objDict.values()
# print(id, address, house_number)
# print(other[0])
# print(persons)









# print(objDict)
# print(type(variable) == type(""))
# values = list(objDict.values())
# keys = list(objDict.keys())
# print(keys)
# mydict = dict(objDict)


# print(main2())

# @app.route('/add', methods=['POST'])
# def add_document():
#     # data = {'name': 'John', 'age': 25}
#     # house_dict = {"first_house": house}
#     house_dict = json_util.loads(house.to_json())
#     db.my_houses.insert_one(house_dict)
#     # db.your_collection_name.insert_one(data)
#     return 'Document added'
#
#
# print(add_document())
