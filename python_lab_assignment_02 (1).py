"""
Python Lab Assignment No. 2
Problem Statement: To find the largest of three numbers.

Name: Samarth Patil
Topic: Decision-Making Statements in Python
"""


def find_largest_of_three():
    print("=" * 60)
    print("PYTHON LAB ASSIGNMENT NO. 2")
    print("FIND THE LARGEST OF THREE NUMBERS")
    print("=" * 60)

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print("\nThe largest number is:", largest)


def demonstrate_operators():
    print("\n" + "=" * 60)
    print("LOGICAL AND RELATIONAL OPERATORS")
    print("=" * 60)

    a = 10
    b = 5

    print("a =", a)
    print("b =", b)

    print("\nRelational Operators:")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

    print("\nLogical Operators:")
    print("(a > 5) and (b < 10):", (a > 5) and (b < 10))
    print("(a > 15) or (b < 10):", (a > 15) or (b < 10))
    print("not(a > b):", not (a > b))


if __name__ == "__main__":
    find_largest_of_three()
    demonstrate_operators()
