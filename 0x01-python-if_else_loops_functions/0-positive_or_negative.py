#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number:d} is positive" if number > 0 else f"{number:d} is zero" if
      number == 0 else f"{number:d} is negative")
