#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        print("{}".format("FizzBuzz" if not (i % 15) else "Buzz" if not i % 5
              else "Fizz" if not i % 3 else i), end=" ")
