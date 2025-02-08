# Program Name: main.py (use the name the program is saved as)
# Course: IT3883/Section XXX
# Student Name: Brandon Thweatt
# Assignment Number: Lab2
# Due Date: 02/07/ 2025
# Purpose: What does the program do (in a few sentences)?
# This program takes input from multiple grades received by different students.
# It will take each grade for each student and calculate an average grade point for each student.
# List Specific resources used to complete the assignment.
# PyCharm Enterprise edition

# Initial function
def calculate_averages(filename):

    # create students array
    students = []

    # Condition that opens the input file and takes each line of student grades through a loop to calculate the average
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            name = parts[0]
            scores = list(map(int, parts[1:]))
            average = sum(scores) / len(scores)
            students.append((name, average))

    # Sorts them by highest grade average to lowest
    students.sort(key=lambda x: x[1], reverse=True)

    # Loop that prints out each student and their grade average
    for name, avg in students:
        print(f"{name} {avg:.2f}")


# Assign the input file, then call the initial function passing the filename in
filename = "Assignment2input.txt"
calculate_averages(filename)
