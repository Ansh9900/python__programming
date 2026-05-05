# import random
# a = [1,2,3,4]
# b = random.shuffle(a)
# print(a)
# str = "anshbansal".       
# print(str[3])

#!recursion 
#*1 to n
# def numbers(n):
#     if(n>0):
#         numbers(n-1)
#         print(n)  
# numbers(100)
#* factorial
# def fact(n):
#     if(n>1):
#         return n*fact(n-1)
#     else:
#         return 1
# a = fact(5) 
# print(a)   
#* harmonic sum
# def harmonic(n):
#     if n==1:
#         return 1
#     else:
#         return(1/n) + harmonic(n-1)
# a = harmonic(5)    
# print(a)
#*fibonacci series
# def fib(n):
#     if(n<=1):
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# n = 5
# for i in range(n):
#     print(fib(i),end="")

#!regular expression
# import re 
# txt  = "ansh bansal op"
# x = re.sub("\s+","9",txt)
# print(x)
#!numpy
# import numpy as np
# a = np.zeros(5)
# print(a)
# n  = int(input("enter a number"))
# i = 1
# count = 0
# while(i<=n):
#     if(n%i==0):
#         count+=1   
#     i+=1
# if(count>2):
#     print("not prime")   
# import re 
# string = input("enter the string")
# a = re.findall(r"[aeiou]",string)
# print(a)
