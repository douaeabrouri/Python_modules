#!/usr/bin/env python3
import importlib
import sys

GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"

packages: dict = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": " Network access ready",
    "matplotlib": " Visualization ready",
}


def check_dependencies(package: dict) -> bool:
    print("Checking dependencies:")
    done: bool = True
    for package, description in package.items():
        try:
            mod = importlib.import_module(package)
            version: str = mod.__version__
            print(f"{GREEN}[OK] {package} ({version}) - {description}{RESET}")
        except ImportError:
            print(f"{RED}Missing {package} -> {description}{RESET}")
            print(f"  → Install with pip:    pip install {package}")
            print(f"  → Install with Poetry: poetry add {package}")
            done = False
    return done


def analyze_data() -> None:
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")
    data = np.random.randn(1000)
    dataf = pd.DataFrame(data, columns=["example"])
    total: int = len(dataf)
    print(f"Processing {total} data points...")


def generate_visualation() -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    print("Generating visualization...")
    data = np.random.randn(1000)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color="green")
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    done: bool = check_dependencies(packages)
    if done:
        analyze_data()
        generate_visualation()
    else:
        print(f"\n{RED}Some dependencies are missing!{RESET}")
        print("Install all with pip:    pip install -r requirements.txt")
        print("Install all with Poetry: poetry install")
        sys.exit(1)
