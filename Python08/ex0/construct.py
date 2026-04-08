#!/usr/bin/env python3
import os
import sys
import site

GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"


def get_env_info() -> dict:
    """Collect all environment information."""
    return {
        "in_env": os.environ.get("VIRTUAL_ENV"),
        "current_path": sys.executable,
        "packages_path": site.getsitepackages()[0],
        "is_venv": sys.prefix != sys.base_prefix
    }


def display_venv_info(info: dict) -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {info['current_path']}")
    print(f"Virtual Environment: {os.path.basename(info['in_env'])}")
    print(f"Environment Path: {info['in_env']}")
    print(f"\n{GREEN}SUCCESS: You're in an isolated environment!{RESET}")
    print("Safe to install packages without affecting the global system.\n")
    print(f"Package installation path:\n{info['packages_path']}")


def display_no_venv_info(info: dict) -> None:
    """Display info when outside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {info['current_path']}")
    print("Virtual Environment: None detected")
    print(f"\n{RED}WARNING: You're in the global environment!{RESET}")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


if __name__ == "__main__":
    info: dict = get_env_info()

    if info["is_venv"]:
        display_venv_info(info)
    else:
        display_no_venv_info(info)
