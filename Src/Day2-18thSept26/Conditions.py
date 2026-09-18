# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("You are not old enough to vote!")
##########################################################
# list1=[1,2,3,4,5,6]
# list2=[]
# list3=[]
# for i in range(len(list1)):
#     if i%2==0 or i==0:
#         list2.append(list1[i])
#     else:
#         list3.append(list1[i])
# print(list2)
# print(list3)
# print(sum(list3)/len(list3))


###################################################################
# num1,num2,num3 =10,20,30
#
# if num1 > num2 and num1 > num3:
#     print(num1, "is greater")
# elif num2> num1 and num2> num3:
#     print(num2, "is greater")
# else:
#     print(num3, "is greater")
#
# result = max(num1,num2,num3)
# print(result)

###################################################################
#
# list1 =[10,20,30]
# print(max(list1))

##############################################################
#
# subject_marks = int(input("Enter subject marks: "))
# if subject_marks >=90:
#     print("Congratulations! You are congratful!")
# elif subject_marks >=60 and subject_marks <=90:
#     print("Nice and pass")
# elif subject_marks <60:
#     print("fail")
# elif subject_marks >100:
#     print("invalid")

######################################################################

# year = int(input("Enter year: "))
# if year %4 ==0 and year % 100 !=0:
#     print("year is a leap year")
# elif year % 400 ==0:
#     print("year is a leap year")
# else:
#     print("year is not a leap year")

########################################################################

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 ==0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("number is not divisible by 3 or 5")