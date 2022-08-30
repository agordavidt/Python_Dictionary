"""
Date: 30/08/2022
Program: A nested dictionary from user inputs
Author: David Agor
"""
d = {}
size = int(input("Enter the size of nested dictionary: "))
for i in range(size):
    dict_name = input("Enter the name of child dictionary: ")
    d[dict_name] = {}
    name = input("Enter name: ")
    age = input("Enter age: ")
    d[dict_name]["Name"] = name
    d[dict_name]["Age"] = age
print(d)