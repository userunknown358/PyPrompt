#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s4yem
#
# Created:     13/03/2025
# Copyright:   s4yem
# Licence:     licence
#-------------------------------------------------------------------------------

import os
import sys
import time
import random
import math
import tkinter
from tkinter import *
from tkinter import messagebox

while True:
    program = input("\nThis is pyprompt 0.1.1. Type 'Help' for help or 'Exit' to quit.\n"
                    "Program names are case-sensitive.\nPrograms: Help, Calculator, About, Notepad, SQL\n").strip()

    # Exit condition
    if program.lower() == "exit":
        print("Exiting PyPrompt. Goodbye!")
        break  # Ends the loop and exits the program

    # Help
    elif program.lower() == "help":
        print("\nAvailable Programs: Notepad (EXPERIMENTAL), About, Calculator, Help, SQL")
        print("Type 'Exit' to quit.")

    # About
    elif program.lower() == "about":
        input("\nPyprompt 0.1.1: \nBy userunknown358.\nI am not good at Python at the moment, so expect lots of bugs.\n"
              "Press 'Enter' to return to the menu.")

    # Calculator
    elif program.lower() == "calculator":
        while True:
            print("\nEnter number 1 (or type 'back' to return):")
            number1 = input().strip()
            if number1.lower() == "back":
                break  # Returns to the main menu

            print("Enter number 2:")
            number2 = input().strip()
            print("Select an operation (+, -, *, /) or type 'Help' for options:")
            operation = input().strip()

            if operation.lower() == "help":
                print("\n+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division")
            elif operation == "+":
                print("Result:", float(number1) + float(number2))
            elif operation == "-":
                print("Result:", float(number1) - float(number2))
            elif operation == "*":
                print("Result:", float(number1) * float(number2))
            elif operation == "/":
                if float(number2) != 0:
                    print("Result:", float(number1) / float(number2))
                else:
                    print("Error: Division by zero")
            else:
                print("Invalid operation")

            input("Press 'Enter' to return to the menu.")  # Pause before returning

    # **FIXED NOTEPAD**
    elif program.lower() == "notepad":
        print("\nNotepad - Start typing your text. Type 'EXIT' on a new line to save and exit.")
        lines = []

        while True:
            line = input()
            if line.strip().lower() == "exit":  # User explicitly exits
                break
            lines.append(line)

        filename = input("Enter filename to save (e.g., note.txt): ").strip()
        if filename:
            with open(filename, "w") as f:
                f.write("\n".join(lines))
            print(f"File saved as {filename}")
        else:
            print("No filename provided. Note was not saved.")

        input("Press 'Enter' to return to the menu.")  # Pause before returning

    # SQL
    elif program.lower() == "sql":
        print("\nSQL is not supported at the moment.")
        input("Press 'Enter' to return to the menu.")  # Pause before returning

    # Invalid input
    else:
        print("Invalid program name. Please try again.")
