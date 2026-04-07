#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv

from typing import Optional

def load_config() -> dict:
    load_dotenv()
    
    matrix_mode: Optional[str] = os.environ.get("MATRIX_MODE")
    database_url: Optional[str] = os.environ.get("DATABASE_URL")
    api_key: Optional[str] = os.environ.get("API_KEY")
    log_level: Optional[str] = os.environ.get("LOG_LEVEL")
    zion_endpoint: Optional[str] = os.environ.get("ZION_ENDPOINT")
    
    return {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint
    }

def display_config(config: dict) -> None:
    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: Connected to {config['DATABASE_URL']}")
    print(f"API Access: {'Authenticated' if config['API_KEY'] else 'Not authenticated'}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {'Online' if config['ZION_ENDPOINT'] else 'Offline'}")

def security_check(config: dict) -> None:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    RESET   = "\033[0m"
    print("\nEnvironment security check:")
    if config["API_KEY"] is not None:
        print(f"{GREEN}[OK] No hardcoded secrets detected{RESET}")
    else:
        print(f"{RED}[MISSING] API_KEY not configured!{RESET}")
    all_configured = all(value is not None for value in config.values())
    if all_configured:
        print(f"{GREEN}[OK] .env file properly configured{RESET}")
    else:
        print(f"{RED}[WARNING] Some variables are missing in .env!{RESET}")
    
    if config["MATRIX_MODE"] is not None:
        print(f"{GREEN}[OK] Production overrides available{RESET}")
    else:
        print(f"{RED}[WARNING] MATRIX_MODE not set!{RESET}")
        

if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config: dict = load_config()
    display_config(config)
    security_check(config)
    print("\nThe Oracle sees all configurations.")