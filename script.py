"""Module providing a function printing python version."""
import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """method"""
    greeting = f'hello, {who_to_greet}'
    return greeting


name = input("Your Name? ")
print(greet(name))
print(greet('jhony'))
