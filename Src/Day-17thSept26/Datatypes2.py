print(max(10,20,4))

import keyword
print(keyword.kwlist)

list1 =['a',1,'b',2]
list2=[]
for i in list1:
    if type(i)==int:
        list2.append(i)
print(list2)