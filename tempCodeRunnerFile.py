def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)#!like here we have used factorial for finding factorial
print(factorial(4))
print(factorial(5))