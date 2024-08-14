import json
import os


class Car:

    cars_dict = {}

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def create_car() -> None:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file_cars:
            data = json.load(file_cars)

        for customer in data.get("customers", []):
            cars = customer.get("car", {})
            car = Car(
                brand=cars.get("brand"),
                fuel_consumption=cars.get("fuel_consumption")
            )
            Car.cars_dict[customer["name"]] = car
