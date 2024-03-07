from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Setup
    ingred_1 = Ingredient("carne")
    ingred_2 = Ingredient("ovo")
    ingred_3 = Ingredient("carne")

    # Assertion
    assert (
        ingred_1 == ingred_3
    ), "Ingredientes com o mesmo nome devem ser iguais"
    assert (
        ingred_1 != ingred_2
    ), "Ingredientes com nomes diferentes não devem ser iguais"

    # Hash check
    assert hash(ingred_1) != hash(
        ingred_2
    ), "Hashes de ingredientes diferentes devem ser diferentes"
    assert hash(ingred_1) == hash(
        ingred_3
    ), "Hashes de ingredientes iguais devem ser iguais"

    # Property check
    assert ingred_1.name == "carne", "O nome do ingrediente deve ser 'carne'"
    assert (
        repr(ingred_1) == "Ingredient('carne')"
    ), "A representação deve corresponder ao formato esperado"

    # Restriction check
    expected_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert (
        ingred_1.restrictions == expected_restrictions
    ), "O ingrediente deve ter restrições corretas"
    assert ingred_2.restrictions == {
        Restriction.ANIMAL_DERIVED
    }, "O ingrediente deve ter restrições corretas"
    assert (
        ingred_3.restrictions == expected_restrictions
    ), "O ingrediente deve ter restrições corretas"
