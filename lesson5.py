"""
Created on Thu Jun  2 12:37:35 2022

@author: PERSONAL
"""

list1=[1,2,3,4,5]

list2=[]


for x in list1:
    list2.append(x*x)
    
    
print(list2)

print([x*x for x in list1])
print([x**3 for x in list1])

list1=['amar',"akbar","anthony"]

print([len(x) for x in list1])

list1=[2,5,7,9]
      
def cubevalue(x):
    return (x**3)

print(list(map(cubevalue,list1)))


list1=[1,2,3,4,5,6,7]

def isodd (x):
    if(x % 2==1):
        return True
    else:
        return False


print(list(map(isodd,list1)))

print(list(filter(isodd,list1)))

list1=[1,2,3,4,5,6,7]
def isodd (x):
    return(x%2==1)

print(list(filter(lambda x:x%2==1,list1)))


list1=[1,2,3,4,5]

def fadd(x,y):
    return(x+y)

import functools
print(functools.reduce(fadd,list1))#or
print(functools.reduce(lambda x,y:x+y,list1))