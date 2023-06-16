from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("ovo")
    ingredient3 = Ingredient("farinha")

    # Test __eq__
    assert ingredient1 == ingredient3
    assert not ingredient1 == ingredient2

    # Test __hash__
    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient1) != hash(ingredient2)

    # Test __repr__
    assert str(ingredient1) == "Ingredient('farinha')"
    assert ingredient1.name == "farinha"

    # Test restrictions
    assert ingredient1.restrictions == {
        Restriction.GLUTEN
    }
