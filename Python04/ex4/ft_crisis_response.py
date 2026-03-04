#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        with open("lost_archive.txt", "r") as file:
            print(file.read())
    except FileExistsError as e:
        print(f"ERROR: {e}")

	except PermissionError as e:
