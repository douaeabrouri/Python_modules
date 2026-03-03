#!/usr/bin/env python3


def get_score(player: tuple) -> int:
    return player[1]


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    players: list = [
        ("alice", 3000),
        ("bob", 3008),
        ("charlie", 5000),
        ("diana", 700)
    ]
    achivements: dict = {
        "alice": ["first_kill", "level_10", "boss_slayer"],
        "bob": ["first_kill", "treasure_hunter"],
        "charlie": ["level_10", "boss_slayer", "speed_demon"],
        "diana": ["first_kill", "level_10"],
    }
    active_players: list = ["alice", "bob", "charlie"]
    regions: list = ["north", "east", "central", "north", "east"]
    print()
    print("=== List Comprehension Examples ===")
    high_score: list = [x[0] for x in players if x[1] > 2000]
    print(f"High scorers (>2000): {high_score}")
    score_doubled: list = [score * 2 for name, score in players]
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {name: score for name, score in players}
    score_categories = {
        name: "high" if score > 2000 else "medium" if score > 1500 else "low"
        for name, score in players
    }
    achivement_count: dict = {
            name: len(achs)
            for name, achs in achivements.items()
    }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achivement_count}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_player: set = {name for name, score in players}
    print(f"Unique players: {unique_player}")
    unique_achievements: set = {
           ach
           for achs in achivements.values()
           for ach in achs
    }
    print(f"Unique achievements: {unique_achievements}")
    active_regions: set = {name for name in regions}
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    total_players: int = len(players)
    tua: int = len(unique_achievements)
    average_score: float = sum(score for name, score in players) / len(players)
    top: tuple = max(players, key=get_score)
    top_achievements: int = len(achivements[top[0]])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {tua}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top[0]} ({top[1]} points,"
        f" {top_achievements} achievements)"
    )
