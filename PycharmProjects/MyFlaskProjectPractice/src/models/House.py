import json


class House:
    def __init__(self, location, house_number):
        self.persons = []
        self.address = location
        self.house_number = house_number

    def to_dict(self):
        return {
                'address': self.address,
                'number': self.house_number,
                'persons': [p.__dict__ for p in self.persons]
                }

    def to_json(self):
        return json.dumps(self.to_dict())
