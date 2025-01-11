# i=int(input("enter a number:"))
# for a in range(1,11):
#     print(i , "X",a,"=",i*a)

# i=int(input("enter a number:"))
# def m2cm(i):
#     print("cm in", i ,"m is",i*100)    
# m2cm(i)    
# j=int(input("enter second number:"))
# def cm2m(j):
#     print("m in", j ,"cm is",j/100)    
# cm2m(j)

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))   




# num=int(input("enter a number:"))
# def fiborec(n):
#     if n==0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fiborec(n-1)+ fiborec(n-2)
    
# print(fiborec(num))

# num=int(input("enter a number:"))
# def fiboiter(n):
#     prevNum=0
#     currentNum=1
#     for i in range(1,n):
#         prevprevNum=prevNum
#         prevNum=currentNum
#         currentNum=prevprevNum+prevNum
#     return currentNum

# print(fiboiter(num))

i=1
while i<5:
    j=1
    while j<5:
        j=j+1
    i=i+1
    print("*")f
    