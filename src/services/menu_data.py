import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def load(self, path):
        with open(path, mode="r") as file:
            data = csv.DictReader(file)
            dishes = {}

            for row in data:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                if dish_name in dishes:
                    dishes[dish_name].add_ingredient_dependency(
                        Ingredient(ingredient_name),
                        recipe_amount
                    )
                else:
                    new_dish = Dish(dish_name, price)
                    new_dish.add_ingredient_dependency(
                        Ingredient(ingredient_name),
                        recipe_amount
                    )
                    dishes[dish_name] = new_dish

            self.dishes = set(dishes.values())
