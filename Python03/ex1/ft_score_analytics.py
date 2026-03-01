#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args: list = sys.argv
    scores: list = []
    if len(args) == 1:
        print(
            "No scores provided. Usage: python3"
            " ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        for i in args[1:]:
            try:
                scores.append(int(i))
            except ValueError:
                print(f"oops invalid score: {i}")

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(args)  - 1}")
        print(f"Total players: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
