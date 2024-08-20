import json
import os


class Shop:
    list_shop = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name

    @classmethod
    def create_shop(cls) -> None:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file_shop:
            data = json.load(file_shop)

        for shops in data.get("shops", []):
            shop = Shop(
                name=shops.get("name"),
                location=shops.get("location"),
                products=shops.get("products"),
            )
            Shop.list_shop.append(shop)
