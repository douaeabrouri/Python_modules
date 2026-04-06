#!/usr/bin/env python3

import os
import sys
import site

# in_env = os.environ.get("VIRTUAL_ENV")
# packages_path = site.getsitepackages()[0]
# print(f"==========>{in_env}")
# # print(f"==========>{os.path.basename(in_env)}")
# print(f"==========>{packages_path}")
# print(type(packages_path))
# # print(f"==========>{sys.base_prefix}")

if __name__ == "__main__":
    status1: str = "You're still plugged in"
    status2: str = "Welcome to the construct"
    in_env: str = os.environ.get("VIRTUAL_ENV")
    packages_path: str = site.getsitepackages()[0]
    current_path: str = sys.executable
    if (sys.prefix != sys.base_prefix):
        print(f"MATRIX STATUS: {status2}\n")
        print(f"Current Python: {current_path}")
        print(f"Virtual Environment: {os.path.basename(in_env)}")
        print(f"Environment Path: {in_env}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.\n")
        print(f"Package installation path: \n{packages_path}")
    elif (sys.prefix == sys.base_prefix):
        print(f"MATRIX STATUS: {status1}\n")
        print(f"Current Python: {in_env} detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")
        
        