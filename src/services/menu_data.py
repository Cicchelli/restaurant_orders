import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_dishes(source_path)

    def _load_dishes(self, source_path: str):
        all_dishes = {}
        with open(source_path, encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                dish = all_dishes.setdefault(dish_name, Dish(dish_name, price))
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), recipe_amount
                )

        return set(all_dishes.values())
