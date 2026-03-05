#!/usr/bin/env python3


def handle_crisis(file_name: str) -> None:
    if file_name == "standard_archive.txt":
        print(f'ROUTINE ACCESS: Attempting access to "{file_name}"')
    else:
        print(f'CRISIS ALERT: Attempting access to "{file_name}"')
    try:
        with open(file_name, "r") as file:
            print(f"SUCCESS: Archive recovered - {file.read().strip()}")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unknown anomaly - {e}\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    handle_crisis("lost_archive.txt")
    handle_crisis("classified_vault.txt")
    handle_crisis("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
