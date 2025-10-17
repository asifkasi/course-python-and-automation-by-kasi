# Solutions for Array.txt Questions

# Question 1: Month Name Program
"""
1. Write a python program that reads an integer between 1 and 12 and prints the month of the year in English.
Test Data :
Input a number between 1 to 12 to get the month name: 8
Expected Output:
August
"""
print("=" * 50)
print("QUESTION 1: Month Name Program")
print("=" * 50)

def get_month_name():
    """
    Solution: Write a python program that reads an integer between 1 and 12 
    and prints the month of the year in English.
    """
    # List of month names
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    try:
        # Get month number from user
        month_number = int(input("Input a number between 1 to 12 to get the month name: "))
        
        # Validate the input and print corresponding month
        if 1 <= month_number <= 12:
            print(months[month_number - 1])
        else:
            print("Invalid month number! Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run Question 1
get_month_name()

print("\n" + "=" * 50)
print("QUESTION 2: Array Processing Program")
print("=" * 50)

"""
2. Write a C program that reads and prints the elements of an array of length 7. 
Before printing, replace every negative number, zero, with 100.
Test Data:
Input the 5 members of the array:
25
45
35
65
15

Expected Output:
Array values are:
n[0] = 25
n[1] = 45
n[2] = 35
n[3] = 65
n[4] = 15
"""

def process_array():
    """
    Solution: Reads and prints the elements of an array. 
    Before printing, replace every negative number and zero with 100.
    (Adapted from C program to Python)
    """
    try:
        # Get the number of elements
        n = int(input("Enter the number of array elements: "))
        
        # Initialize array
        arr = []
        
        # Input array elements
        print(f"Input the {n} members of the array:")
        for i in range(n):
            value = int(input())
            arr.append(value)
        
        # Process array: replace negative numbers and zeros with 100
        processed_arr = []
        for value in arr:
            if value <= 0:
                processed_arr.append(100)
            else:
                processed_arr.append(value)
        
        # Print the processed array
        print("\nArray values are:")
        for i in range(len(processed_arr)):
            print(f"n[{i}] = {processed_arr[i]}")
            
    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Run Question 2
process_array()

print("\n" + "=" * 50)
print("BONUS: Alternative Solutions")
print("=" * 50)

# Alternative solution for Question 1 using calendar module
def get_month_name_calendar():
    """Alternative solution using calendar module"""
    import calendar
    
    try:
        n = int(input("Input a number between 1 to 12 to get the month name: "))
        
        if 1 <= n <= 12:
            print(calendar.month_name[n])
        else:
            print("Invalid input! Please enter a number from 1 to 12.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Alternative solution for Question 2 using list comprehension
def process_array_advanced():
    """Alternative solution using list comprehension"""
    try:
        n = int(input("Enter the number of array elements: "))
        arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
        
        # Process using list comprehension
        processed_arr = [100 if x <= 0 else x for x in arr]
        
        print("\nArray values are:")
        for i, value in enumerate(processed_arr):
            print(f"n[{i}] = {value}")
            
    except ValueError:
        print("Invalid input! Please enter valid integers.")

print("\nAlternative Month Name Solution:")
get_month_name_calendar()

print("\nAlternative Array Processing Solution:")
process_array_advanced()