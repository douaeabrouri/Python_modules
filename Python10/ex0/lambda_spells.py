#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result: list[dict] = sorted(
                            artifacts,
                            key=lambda a: a["power"],
                            reverse=True
                        )
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result: list[dict] = list(filter(lambda a: a["power"] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result: list[str] = list(map(lambda a: f"* {a} *", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    max_nb: int = max(mages, key=lambda a: a["power"])["power"]
    min_nb: int = min(mages, key=lambda a: a["power"])["power"]
    powers_list = list(map(lambda a: a["power"], mages))
    avg_nb: float = round(sum(powers_list) / len(mages), 2)
    return {"max_power": max_nb, "min_power": min_nb, "avg_power": avg_nb}


if __name__ == "__main__":
    PURPLE: str = "\033[38;2;229;208;255m"
    RESET: str = "\033[0m"
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
    ]
    print(f"{PURPLE}Testing artifact sorter...{RESET}")
    sorted_artifact: list[dict] = artifact_sorter(artifacts)
    print(
        f"{sorted_artifact[0]['name']} "
        f"({sorted_artifact[0]['power']} power) comes before "
        f"{sorted_artifact[1]['name']} ({sorted_artifact[1]['power']} power)\n"
    )
    print(f"{PURPLE}Testing spell transformer...{RESET}")
    spells: list = ["fireball", "heal", "shield"]
    print(*spell_transformer(spells))
    print(f"\n{PURPLE}Testing mage stats...{RESET}")
    list_test: list = [
        {'power': 60, 'name': "dragon"},
        {'power': 76, 'name': "darwin"},
        {'power': 17, 'name': "hanbol"},
    ]
    dict_test: dict = mage_stats(list_test)
    print(dict_test)
