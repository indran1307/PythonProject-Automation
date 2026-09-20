# str =[1,2,3]
# second_list=[]
# #print(str[::-1])
# for i in str:
#     second_list.insert(0,i)
#
# print(second_list)

###########################################################

# str ='indra'
# result =''
# for char in str:
#     result =char + result
# print(result)
###########################################################

# str = input('Enter a string:')
#
# if str == str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


##################################

def duplicates():
    list1 = [1,2,3,11,1,2,4]
    list2 = []
    for i in list1:
        if list1.count(i) == 1:
            list2.append(i)
    print(list2)

duplicates()