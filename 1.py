####################################################################
#* prime number
#!Task1: Find weather number is prime numbers .
#!Task2: Find all the prime numbers between m and n.
#!Task3: Find the sum of all prime numbers between m and n.
#!Task4: wap to print prime digits of a given numbers
#~ task 1
#^ approach 1 
# num = int(input("enter the number"))
# count = 0
# if(num == 0 or num == 1):
#     print("not prime not composite")
# else:
#     i = 2
#     while(i<num):
#         if(num%i == 0):
#          count+=1  
#         i+=1
# if(count>0):
#    print("composite")
# else:
#    print("prime")         
#^ approach 2 
# import math  
# n = int(input("enter the number"))
# is_prime = True
# i = 2
# while(i*i<=n):
#     if(n%i == 0):
#         is_prime = False
#         break
#     i+=1
# if(is_prime == True):
#     print("prime")
# else:
#     print("composite")    
