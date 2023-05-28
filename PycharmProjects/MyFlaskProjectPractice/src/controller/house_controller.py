from bson import ObjectId

from src.services.house_service import HouseService
from flask import Flask
# from flask_restful import Api, Resource

app = Flask(__name__)
# api = Api(app)


class HouseController:
    house_service = HouseService()


    def create_house(self, location, street_number, person):
        house_id = self.house_service.save_house(location, street_number, person)
        return house_id

    @app.route('/')
    def find_house_by_id(self):
        return "yes"
        # variable = ObjectId("64728f2a3fd7bfd5ab91c229")
        # return self.house_service.find_house_by_id(variable)

        # if house:
        #     return house, 200
        # else:
        #     return {'error': 'House not found'}, 404


# Define routes
# api.add_resource(HouseController, '/house', '/house/<string:house_id>')

if __name__ == '__main__':
    app.run(debug=True)
