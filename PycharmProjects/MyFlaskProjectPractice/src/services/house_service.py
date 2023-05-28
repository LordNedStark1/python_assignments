from src.models.House import House
from src.repositories.repository import Repository, db_factory


class HouseService:
    def __init__(self):
        self._repo = Repository(db_factory())

    def save_house(self, address, house_number, persons):
        house = House(address, house_number)
        # house.persons.extend(persons)
        house.persons.append(persons)
        house_id = self._repo.save(house)

        return house_id

    def find_house_by_id(self, house_id):
        return self._repo.find_by_id(house_id)
