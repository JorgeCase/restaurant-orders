from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient1 = Ingredient("presunto")
    ingredient2 = Ingredient("queijo mussarela")

    dish1 = Dish("lasanha presunto", 25.90)
    dish2 = Dish("lasanha berinjela", 27.00)
    dish3 = Dish("lasanha presunto", 25.90)

    assert dish1.name == "lasanha presunto"
    assert dish1.price == 25.90
    assert dish1.recipe == {}

    assert repr(dish1) == "Dish('lasanha presunto', R$25.90)"
    assert dish1 == dish3
    assert not dish1 == dish2

    assert hash(dish1) == hash(dish3)
    assert hash(dish1) != hash(dish2)

    dish1.add_ingredient_dependency(ingredient1, 50)
    dish1.add_ingredient_dependency(ingredient2, 25)
    assert dish1.recipe == {ingredient1: 50, ingredient2: 25}

    except_ingredients = {ingredient1, ingredient2}
    assert dish1.get_ingredients() == except_ingredients

    except_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }

    assert dish1.get_restrictions() == except_restrictions

    with pytest.raises(ValueError):
        Dish("lasanha presunto", -1)

    with pytest.raises(TypeError):
        Dish("lasanha presunto", "invalid price")
