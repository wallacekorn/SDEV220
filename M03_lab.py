# -*- coding: utf-8 -*-
"""
Created: Fri Apr  7 20:23:04 2023
Author: David Amon
Class: SDEV220 Spring 2023

Program Name: M03_LAB
Program Description: An app that will accept user input for a car. The app stores "car" into the vehicle type in the Vehicle super class. 
    The app then asks the user for the year, make, model, doors, and type of roof and stores the data in attributes.
    The app then outputs the data in an easy-to-read and understandable format.
"""
#Definitions
class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Asks the user for the year, make, model, doors, and type of roof
print("\nPlease enter the following: ")
vehicleType = input("Vehicle type (Car, Bike, Rowboat, etc.): ")
year = input("Vehicle Year: ")
make = input("Vehicle Make: ")
model = input("Vehicle Model: ")
doors = input("Vehicle Door Count: ")
roof = input("Vehicle Roof Style: ")

# Creates the object - stores user input
automobileObject = Automobile(year, make, model, doors, roof)

# Prints the object data in an easy-to-read and understandable format
print (f"\nVehicle Data Results: \nVehicle Type: {automobileObject.vehicleType}\nVehicle Year: {automobileObject.year}\nVehicle Make: {automobileObject.make}\nVehicle Model: {automobileObject.model}\nVehicle Door Count: {automobileObject.doors}\nVehicle Roof Style: {automobileObject.roof}")































