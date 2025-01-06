# arr=[int (i) for i in input().split()]
#
# cot=0
# for i in arr:
#     if i!=0:
#         print(int(i),end="")
#     else:
#         cot+=1
# for i in range(cot):
#     print(0,end="")
#
#
#
# num = int(input())
# while num>=1:
#     print(num%2,end="")
#     num = num//2
#
#
# day=input()
# n=int(input())
# days=["sun","mon","sun","tue","wen","the","fri","sat"]
# day_num=1
# for i in range(7):
#     if day==days[i]:
#         day_num=i
#
# n+=day_num
# print(n//7)


# n=int(input("enter number"))
# flag=1
# sum=0
# while flag:
#
#     if n==1:
#         print("happy")
#         break
#     sum=0
#     for i in str(n):
#         sum=sum+int(i)**2
#     n=sum
#
#
#
#
#


# r=int(input("rat"))
# f=int(input("unit"))
# arr=[int(i) for i in input().split(" ")]
# sum=0
#
# for i in range(len(arr)):
#     sum+=arr[i]
#
#     if sum>=(r*f):
#         print(i+1)
#         break

# import numpy as np
#
# arr = np.empty((3,3),int)
#
# for i in range(3):
#     for j in range(3):
#         arr[i,j]=int(input(f"{i},{j} "))
#
# print(arr)
#
#
# def sum(li):
#     s=0
#     for i in range(len(li)):
#         s+=li[i]
#     return s
#





# t=int(input("enter number of test cases : "))
# for i in range(t):
#     n=int(input("enter the number of values : "))
#     arr=[int(i) for i in input().split()]
#     goal=int(input("Enther the tagert : "))
#     c=0
#     for i in range(n):
#         li=[]
#         for j in range(n):
#
#
#
#
#             if sum(li)==goal:
#                 print(li)
#                 c += 1



# a = 55/77
# print(f"{a:.3f}")
#

# print("sharon holhm hh",sep="h")



# n=int(input("enter the vale of n : "))
# arr=[None]*n
# for i in range(n):
#     arr[i]=int(input(f"enter the value of n in {i+1}"))
#
# for i in range(0,n):
#     for j in range(1,n):
#         if arr[i]==arr[j]:
#             arr.pop(j)
#
# print(arr)

# n=int(input("enter the vale of n : "))
# arr=[None]*n
# for i in range(n):
#     arr[i]=int(input(f"enter the value of n in {i+1}"))
# i=0
# while i<len(arr):
#     j=i+1
#     while j<len(arr):
#         if arr[i]==arr[j]:
#             print("here")
#             arr.pop(j)
#         else:
#             j+=1
#     i+=1
# print(arr)



# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
#
#
# n=int(input("enter a number"))
# print(f"the factorial of {n} is {fact(n)}")
#
#

def f(*args, **kwargs):
    print((args[1]))


lis=["dfd","fdd","fss"]
# for i,v in enumerate(lis, start=1):
#     print(i)


f(9,76,6)





