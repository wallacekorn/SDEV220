# -*- coding: utf-8 -*-
"""
Created: Thu Mar 30 14:39:52 2023
Author: David Amon
Class: SDEV220 Spring 2023

File Name: M02_LAB_CaseStudy.py
Program Name: Student Award Calculator
Program Description: Program asks for student first name, last name, and GPA. 
    It then echoes the student's name and indicates whether their GPA qualifies 
    for the Honor Roll or Dean's List.
"""
QUIT_SENTINEL = "ZZZ"   # Sentinel value for exiting the loop/program
HONOR_ROLL = 3.25       # Const storing mininmum GPA for Honor Roll
DEANS_LIST = 3.5        # Const storing minimum GPA for Dean's List
studentFirstName = ""   # Stores the student's FIRST name
studentLastName = ""    # Stores the student's LAST name
studentGPAstring = ""   # Stores the input GPA
studentGPA = 0.0        # Stores the input GPA once converted to a float

# ask for and accept a student's last name.
studentLastName = input('Please enter student\'s Last name or "' + QUIT_SENTINEL + '" to quit. ')

# quit processing student records if the last name entered is 'ZZZ'.
while studentLastName != QUIT_SENTINEL:
    # ask for and accept a student's first name.
    studentFirstName = input("What is the student's First name? ")
    
    # ask for and accept the student's GPA as a float.
    studentGPAstring = input("What is the student's GPA? ")
    
    # This loop validates the GPA entry to assure correct entry and prevent errors
    isItValidGPA = False
    while isItValidGPA == False:
        isFloat = False
        while isFloat == False:
            try:
                studentGPA = float(studentGPAstring)
                isFloat = True
            except ValueError:
                print ("Entry was not a floating point number")
                studentGPAstring = input("What is the student's GPA? ")
        # Checks to make sure the GPA is in a valid range
        if studentGPA > 4.0 or studentGPA < 0:
            print("GPA cannot exceed 4.0 or be negative")
            studentGPAstring = input("What is the student's GPA? ")
        else:
            isItValidGPA = True
            
    # test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
    if studentGPA >= DEANS_LIST:
        print(studentFirstName + " " + studentLastName + " made the Dean's List! ")
    
    # test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
    elif studentGPA >= HONOR_ROLL:
        print(studentFirstName + " " + studentLastName + " made the Honor Roll! ")
    
    # output if the student doesn't make either award list
    else:
        print("\n" + studentFirstName + " " + studentLastName + " did not make Honor Roll or Dean's List. :( ")
    
    # re-prompts for more students and offers a way to end the program
    studentLastName = input('\nPlease enter student\'s last name or "' + QUIT_SENTINEL + '" to quit. ')
