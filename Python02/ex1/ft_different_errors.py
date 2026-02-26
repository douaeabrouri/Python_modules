#!/usr/bin/env python3

def	garden_operations() -> None:

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
           print("Caught ValueError: invalid literal for int()")
           
    print("Testing ZeroDivisionError...")
    try:
        divisor = 0
        print(f"{10/divisor}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    
    print("Testing FileNotFoundError...")
    try:
        open("missing.file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    
    print("Testing KeyError...")          
    try:
       dict = {"x" :"abc", "x2" :  1, "x3" : 5}
       data = dict["notfoundvalue"]
       print(f"{data}")
    except KeyError:
        print("Caught an error, but program continues!")

def  test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    try:
       number = int("abc")
       div = 10 / 0
    except (ValueError, ZeroDivisionError):
    	print("All error types tested successfully!")

test_error_types()