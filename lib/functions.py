#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f'Hello, {name}!')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')

def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def halve(number):
    result = number / 2
    print(result)
    return result

# greet_programmer()
# greet()
# greet_with_default()
