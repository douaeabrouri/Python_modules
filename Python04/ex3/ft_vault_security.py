#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        with open("secure_vault.txt", "r") as file:
            for line in file:
                print(f"[CLASSIFIED] {line.strip()}")
        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as file1:
            file1.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except Exception as e:
        print(f"ERROR: {e}")
