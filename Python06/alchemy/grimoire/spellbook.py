from alchemy.grimoire.validator import validate_ingredients

def record_spell(spell_name: str, ingredients: str) -> str:
    string: str = validate_ingredients(ingredients)
    if "INVALID" in string:
        return f"Spell recorded: {spell_name} ({ingredients} -INVALID)"
    else:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"

