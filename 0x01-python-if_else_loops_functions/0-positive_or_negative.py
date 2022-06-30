#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is Positive")
if number == 0:
    print(f"{number:d} is Zero")
if number < 0:
    print(f"{number:d} is Negative\n")
