from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    Customer.create_customer()
    Shop.create_shop()

    for custom in Customer.list_customer:
        print(f"{custom.name} has {custom.money} dollars")
        all_cost_list = []
        for shop in Shop.list_shop:
            shopping = custom.will_cost(shop)
            cost_to_shop = custom.distance_to_shop(shop)

            total_cost_trip = shopping + cost_to_shop
            print(
                f"{custom.name}'s trip to the "
                f"{shop.name} costs {total_cost_trip}"
            )
            all_cost_list.append(total_cost_trip)

        min_value = min(all_cost_list)
        if custom.money < min_value:
            print(
                f"{custom.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        else:
            min_cost_shop = all_cost_list.index(min_value)
            select_shop = Shop.list_shop[min_cost_shop]
            print(f"{custom.name} rides to {str(select_shop)}\n")
            custom.create_check(select_shop)

            custom.custom_at_home(min_value)
