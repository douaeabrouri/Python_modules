#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist_id: str = input("Input Stream active. Enter archivist ID: ")
        status_report: str = input("Input Stream active. Enter status report: ")
        print()
        sys.stdout.write(
            f"[STANDARD] Archive status from {archivist_id}: {status_report}\n"
        )
        sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print()
        print("Three-channel communication test successful.")
    except Exception as e:
        print(f"ERROR: {e}")
