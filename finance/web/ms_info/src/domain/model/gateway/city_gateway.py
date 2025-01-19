from abc import ABCMeta, abstractmethod


class CityGateway(metaclass=ABCMeta):
    @abstractmethod
    def get_city_coordinates(self, city_name, country_code) -> str:
        "run get_city_coordinates"