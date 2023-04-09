# -*- coding: utf-8 -*-
"""
Created: Sun Apr  9 16:57:24 2023
Author: David Amon
Class: SDEV220 Spring 2023

Program Name: M03_Tutorial
Program Description: Small program showing basic math operations in both Functional and Object Oriented paradigms
"""

#Functional
print("\nFunctional Example: ")
def subtract(x,y):
    return x - y
print(subtract(200,100))
def add(x,y):
    return x + y
print(add(200,100))
def multiply(x,y):
    return x * y
print(multiply(200,100))
def divide(x,y):
    return x / y
print(divide(200,100))

#Object Oriented
print("\nObject Oriented Example: ")
class do_math():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def add(self):
        return self.val1 + self.val2
    def multiply(self):
        return self.val1 * self.val2
    def subtract(self):
        return self.val1 - self.val2
    def divide(self):
        return self.val1 / self.val2
    
    def double_input(self):
        self.val1 *= 2
        self.val2 *= 2

math_instance = do_math(3,4)
print(math_instance.add())
print(math_instance.multiply())
print(math_instance.subtract())
print(math_instance.divide())

print(math_instance.double_input())
print(math_instance.add())
print(math_instance.multiply())
print(math_instance.subtract())
print(math_instance.divide())