#!/usr/bin/env python3

import os
import sys
import site
from typing import Optional

GREEN   = "\033[92m"
RESET   = "\033[0m"
RED     = "\033[91m"

if __name__ == "__main__":
    status1: str = "You're still plugged in"
    status2: str = "Welcome to the construct"
    in_env: Optional[str] = os.environ.get("VIRTUAL_ENV")
    packages_path: str = site.getsitepackages()[0]
    current_path: str = sys.executable
    if (sys.prefix != sys.base_prefix):
        print(f"MATRIX STATUS: {status2}\n")
        print(f"Current Python: {current_path}")
        print(f"Virtual Environment: {os.path.basename(in_env)}")
        print(f"Environment Path: {in_env}")
        print(f"\n{GREEN}SUCCESS: You're in an isolated environment!{RESET}")
        print("Safe to install packages without affecting the global system.\n")
        print(f"Package installation path: \n{packages_path}")
    else:
        print(f"MATRIX STATUS: {status1}\n")
        print(f"Current Python: {current_path}\n")
        print(f"Virtual Environment: None detected")
        print(f"{RED}WARNING: You're in the global environment!{RESET}")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")
