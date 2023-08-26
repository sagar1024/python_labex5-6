#1MCAB Python Programming
#LAB EXERCISE 5

#Q1. Write a program to handle the exception of ZeroDivisionError.

print("Q1.")

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"

print(division(10, 2))
print(division(10, 0))


#Q2. Write a program to handle the exception of IndexError.

print("Q2.")

def print_list(list1, index):
    try:
        print(list1[index])
    except IndexError:
        print("Index out of range")


list1 = [1, 2, 3, 4, 5]
print_list(list1, 5)
print_list(list1, 2)
