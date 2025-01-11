a=0
result=0
userinput=""

while userinput!="q":
    a=int(input("enter a number:"))
    result=a+result
    userinput=input("check q has entered or not:")
    
print(result)