#!/usr/bin/env python3

import typing
import time


def create_game_events(count: int) -> typing.Generator:
    players: list = ["alice", "bob", "charlie"]
    events: list = ["killed monster", "found treasure", "leveled up"]
    for i in range(count):
        player: str = players[i % len(players)]
        event: str = events[i % len(events)]
        level: int = (i % 20) + 1
        yield (i + 1, player, level, event)


def fibono(n: int) -> typing.Generator:
    a: int = 0
    b: int = 1
    counter: int = 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1


def is_prime(nb: int) -> bool:
    if nb < 2:
        return False
    for i in range(2, nb):
        if nb % i == 0:
            return False
    return True


def prime_generator(n: int) -> typing.Generator:
    two: int = 2
    zero: int = 0
    while zero < n:
        if is_prime(two):
            yield (two)
            zero += 1
        two += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")
    print()
    high_level: int = 0
    treasure: int = 0
    level_up: int = 0
    total_event: int = 0
    start: float = time.time()

    for event in create_game_events(1000):
        number, player, level, event_type = event
        if number <= 3:
            print(f"Event {number}: Player {player}"
                  f" (level {level}) {event_type}")
        if number == 4:
            print("...")
        total_event += 1
        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure += 1
        if event_type == "leveled up":
            level_up += 1
    print()
    end: float = time.time()
    processing_time: float = end - start
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_event}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")
    print()
    print("=== Generator Demonstration ===")
    # fibonacci without brackets
    fibo_str: str = ""
    for num in fibono(10):
        if fibo_str == "":
            fibo_str += str(num)
        else:
            fibo_str += ", " + str(num)

    # prime without brackets
    prime_str: str = ""
    for num in prime_generator(5):
        if prime_str == "":
            prime_str += str(num)
        else:
            prime_str += ", " + str(num)

    print(f"Fibonacci sequence (first 10): {fibo_str}")
    print(f"Prime numbers (first 5): {prime_str}")
