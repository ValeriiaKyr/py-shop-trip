import json
import math
import os
from datetime import datetime
from decimal import Decimal

from app.car import Car
from app.shop import Shop


class Customer:

    list_customer = []

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def create_customer(cls) -> None:
        Car.create_car()
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file_customer:
            data = json.load(file_customer)

        for custom in data.get("customers", []):
            customer = Customer(
                name=custom.get("name"),
                product_cart=custom.get("product_cart"),
                location=custom.get("location"),
                money=custom.get("money"),
                car=Car.cars_dict[custom.get("name")],
            )
            Customer.list_customer.append(customer)

    def distance_to_shop(self, some_shop: Shop) -> float:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file_cost_fuel:
            data = json.load(file_cost_fuel)

        fuel_cost = data.get("FUEL_PRICE")

        distance_c = self.location
        distance_sh = some_shop.location
        distance = round(
            (math.sqrt(
                (
                    (distance_sh[0] - distance_c[0]) ** 2
                ) + (
                    (distance_sh[1] - distance_c[1]) ** 2
                )
            ) * 2
            ),
            2
        )
        cost_trip = round(
            ((distance * self.car.fuel_consumption) / 100) * fuel_cost,
            2
        )

        return cost_trip

    def will_cost(self, one_shop: Shop) -> float:

        cost_milk = (self.product_cart.get("milk")
                     * one_shop.products.get("milk"))
        cost_breads = (self.product_cart.get("bread")
                       * one_shop.products.get("bread"))
        cost_butter = (self.product_cart.get("butter")
                       * one_shop.products.get("butter"))
        total_cost = cost_milk + cost_breads + cost_butter

        return total_cost

    def create_check(self, one_shop: Shop) -> None:
        cost_milk = (self.product_cart.get("milk")
                     * one_shop.products.get("milk"))
        cost_breads = (self.product_cart.get("bread")
                       * one_shop.products.get("bread"))
        if cost_breads == int(cost_breads):
            cost_breads = int(cost_breads)

        cost_butter = (self.product_cart.get("butter")
                       * one_shop.products.get("butter"))
        total_cost = cost_milk + cost_breads + cost_butter

        current_datatime = datetime(2021, 1, 4, 12, 33, 41)
        current_datatime = current_datatime.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_datatime}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        print(f"{self.product_cart.get("milk")} milks for {cost_milk} dollars")
        print(
            f"{self.product_cart.get("bread")} "
            f"breads for {cost_breads} dollars"
        )
        print(
            f"{self.product_cart.get("butter")} "
            f"butters for {cost_butter} dollars"
        )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def custom_at_home(self, money_spent: float) -> None:
        cost_now = round(Decimal(self.money) - Decimal(money_spent), 2)

        print(f"{self.name} rides home")
        print(f"{self.name} now has {cost_now} dollars\n")
