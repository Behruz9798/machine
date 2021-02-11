# #binary search
# from random import randint
# import random
# def search(lst,item):
#     mid = len(lst)//2
#     low = 0
#     high = len(lst)-1
#     while lst[mid]!=item and low<=high:
#         if item > lst[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if low > high:
#         return None
#     else:
#         return mid
    
# a = []
# for i in range(10):
#     a.append(randint(1,20))
# #a.sort()
# print(a)

# value = int(input("a = "))
# print(search(a,value))

#list ni sonlar bilan to'ldirish funksiyasi
from random import randint
def fill_list(lst,qty,low,high):
    for i in range(qty):
        lst.append(randint(low,high))

minimum = int(input('minimum:'))
maximum = int(input('maximum:'))
n = int(input('Quantity:'))
a = []
fill_list(a,n,minimum,maximum)
print(a)