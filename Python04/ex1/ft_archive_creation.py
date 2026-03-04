#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    
    try:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        with open('new_discovery.txt', 'w') as file:
            entries: list = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
			]
            for entry in entries:
                print(entry)
                file.write(entry + '\n')
        print()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as e:
        print(f"ERROR: {e}")
