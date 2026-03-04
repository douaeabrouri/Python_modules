#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        with open("ancient_fragment.txt", "r") as file:
            print(file.read())
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(" ERROR: Storage vault not found. Run data generator first.")
