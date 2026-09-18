# def leap_year(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
# print(leap_year(2020))
import math


# def practice(num):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")
#
#
# practice(5)

# def factorial(n):
#     fact = math.factorial(n)
#     return fact
#
# print(factorial(5))


def practice(num):
    fact =1
    for i in range(1,num+1):
        fact = fact * i
    return fact
print(practice(4))