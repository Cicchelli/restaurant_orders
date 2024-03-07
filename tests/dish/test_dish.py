from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    # Configuração
    dish = Dish("Comida", 17.0)
    ingredient = Ingredient("ovo")
    dish.add_ingredient_dependency(ingredient, 2)
    dish_2 = Dish("Comida2", 17.0)

    # Verificações de representação
    assert str(dish) == "Dish('Comida', R$17.00)"
    assert dish.name == "Comida"

    # Verificação de hash
    assert hash(dish) != hash(dish_2)
    assert hash(dish) == hash(dish)

    # Verificação de igualdade
    assert dish != dish_2
    assert dish == dish

    # Testes de exceção
    with pytest.raises(TypeError):
        Dish("Comida", "17.0")

    with pytest.raises(ValueError):
        Dish("Comida", -17.0)

    # Verificações finais
    assert dish.get_restrictions() == ingredient.restrictions
    assert dish.get_ingredients() == {ingredient}
