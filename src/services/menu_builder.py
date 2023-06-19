import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dish_data = self.menu_data.dishes

        if restriction:
            filtered_data = [
                dish
                for dish in dish_data
                if restriction not in Dish.get_restrictions(dish)
            ]
        else:
            filtered_data = dish_data

        available_dishes = []
        for dish in filtered_data:
            if self.inventory.check_recipe_availability(dish.recipe):
                available_dishes.append(dish)

        if not available_dishes:
            return pd.DataFrame()

        dish_names = [dish.name for dish in filtered_data]
        ingredients = [Dish.get_ingredients(dish) for dish in filtered_data]
        prices = [dish.price for dish in filtered_data]
        restrictions = [Dish.get_restrictions(dish) for dish in filtered_data]

        menu_dict = {
                "dish_name": dish_names,
                "ingredients": ingredients,
                "price": prices,
                "restrictions": restrictions,
        }

        menu_df = pd.DataFrame(menu_dict)

        return menu_df
