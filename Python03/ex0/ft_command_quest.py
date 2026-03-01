#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args: list[str] = sys.argv
    lenght: int = len(sys.argv)
    count: int = 0
    program_name = sys.argv[0].split("/")[-1]

    if lenght == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print("Total arguments: 1")
    else:
        print(f"Program name: {program_name}")
        if lenght > 1:
            for i in args:
                count += 1
            print(f"Arguments received: {count - 1}")
        for j, arg in enumerate(args[1:], 1):
            print(f"Argument {j}: {arg}")
        print(f"Total arguments: {count}")
