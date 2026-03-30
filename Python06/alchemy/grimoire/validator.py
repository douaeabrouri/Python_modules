
def validate_ingredients(ingredients: str) -> str:
    liste: list = ["fire", "water", "earth", "air"]
    for even in liste[:]:
        if even in ingredients:
           return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
