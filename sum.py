
# print("hello world")
# print(5)
# todo MODULES AND PIPS
# print("hello world",7)
# print(17*34)
# print("hey python i am a good boy \n and you are  also good boy/girl")
# # this is a single libne comment
'''hey i am
aftab a very
good boy,this is a multi line comment which will not run ,single or double cort'''
# print("hey python i am a\"good boy\"\n and you are  also good boy/girl")
# print("this will\"execute")
# print("this will not"execute") 
# print("hey",4,7,sep="~")
# print("hey",4,7,sep="~",end="009")
# print("harryt")
# print("hey",4,7,sep="~",end="009\n")
# print("harryt")

# todo# VARIABLES AND DATA TYOES
# a=1
# b=True
# c="harry"
# d=None
# # we cant add ,subtract two different data types like adding a and b
# print(type(a))
# print("the type of a is",type(a))
# print("the type of b is",type(b))
# print("the type of c is",type(c))
# print("the type of d is",type(d))
# CALCULATOR
# a=1
# b=2
# print("the value of a+b is:",a+b)
# print("the value of a-b is:",a-b)
# print("the value of a*b is:",a*b)
# print("the value of a/b is:",a/b)
# print("the value of a//b is:",a//b)
# a=1
# b=2
# c="4"
# d="5"
# e="harry"
# f="bhai"
# print(a+b)
# print(c+d)
# print(e+f)
# explicit datatype
# print(int(c)+int(d))
# Todo -->IMPLICIT DATATYPE(comp will chnge z to float itself andadd it)
# x=1.2
# z=4
# print(x+z)
# todo --TAKING USER input day-10 
# a=input()
# print("my name is",a)
# a=input("enter your name:")
# print("my name is",a)
# b=input("first number is:")
# c=input("second number is:")
# print(c+b)
# print(int(c)+int(b))
# print(float(c)+float(b))
# todo -lecture 11,strings in python, strings can be in 1 or 2 quotation marks
# name="harry"
# print("hello,"+name)
# apple='''i want to
# eat an ice"of
# white color'''
# print(apple)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print("lets use a for loop\n")
# for characters in apple:
    # print(characters)
# todo -lecture 12,strings slicing and operation on strings
# names=("mango")
# print(names[0:5]),including 0 but not 5
# print(len(names))
# pine=len(names)
# print(pine)
# print(names[:5])
# print(names[:])# use to copy string
# print(names[0:-3])
#!both this and above nd below are same, print(names[0:len(names)-3]) 
# print(names[:len(names)-3]) 
# print(names[-3:-1]) #includes the -3 term but not -1 term include n but not include o,,,,[2:4]
# print(names[2:])
# print(names[-len(names):len(names)])
# todo-->string methods in python day--13
# v="harry"
# print(len(v))
# ?strings are immutablwe
a="!!!Harry !!!!!!!! !!!!!! harry !!!!!"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!")) #strip means ! ko gyb krdega but jo baad main honge sirf unhe
# print(a.replace("harry","john"))
# print(a.split(" "))#split ,ye lgakr tukdo main baat deta ay
# c="welcome to the console\n"
# b="welcometomyworld"
# print(b.capitalize())# first letter ko capital kr dega or baaki sbko small mai krdega
# print(b.center(55))#ye shuruaat main 55 space de dega
# print(len(b.center(50)))
# print(len(b))
# print(a.count("harry"))
# print(a.endswith("harry"))
# print(a.endswith("harr",3,7))
# print(b.find("my"))
# print(b.find("is"))
# print(b.index("is")) , index will give you error
# isalnum means  numeric term made up of a-z or 0-9,A-Z
# isalpha it contains alphabet not numbers
# print(b.isalnum())*
# print(b.isalpha())*
# print(b.islower())
# d="you        Go down"

# print(d.isspace()) ,#agr space hai to truemilega
# print(c.isprintable()),#agr caracter printable hai mtlb alpjabet or no. hai to true dega but agr\nlgadia to \n printable ni ay vo new line caracter deta ay
# print(b.isprintable())
# # 
# print(d.istitle()),#hmara jp vo hai uske saare first letter bde ay y nhi true or falsebtata ay
# print(d.startswith("you"))
# print(d.swapcase()),#small alfabet ko chota kr deta or bde ko chota
# print,(d.title()),#saare first letter ko bda kr dega


# todo day-14,if else statement
# a=int(input("enter your age:"))
# print("your age is:",a)
# if(a>18):
#     print("you can vote")
#     print("yes")
# else:
#     print("you can not vote")
#     print("no") 
#?space before print is intandation ,any print statement after intandation will be counted in if else statement    
# if(a>18):
#     print("you can vote")
#     print("yes")
# else:
#     print("you can not vote")
# print("yay")
# ?in this code no will be run becz yay is a code like others
# num=int(input("enter the number:"))
# if(num<0):
#     print("number is negative")
# elif(num>0):
#     if(num<=10):
#         print("number is between 1-10")
#     elif(num>10 and num<=20):
#         print("number is between 11-20")
#     else:
#         print("number is greater than 20")
# else:
#     print("number is zero")   
# todo day-16 match case statement
# x=int(input("enter the value of x:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case _ if x!=90:
#         print(x,"is not 90")
#     case _ if x!=80:
#         print(x,"is not 80")
#     case _:
#         print(x)    
#!in this code if we put x=67 , case!=90 wala case match hoga to usjke niche wale case alreaduy match mhi honge
#!ek baar koi case match ho gya to baaki apne aap hi match ni hogio

# todo day-17 for loops
# name="aftab"
# for i in name:
#  print(i)  
#  if(i=="f     "):
#   print("there is something special")
# colors=("red","blue","green")
# for color in colors:
#     print(color)
# colors=["red","blue","green"]
# for color in colors:
#     print(color)
#     for x in color:
#      print(x)    
# for k in range(5):
#     print(k)
# for k in range(6):
#     print(k+1)
# for p in range(1,2001):
    # print(p)    
# todo day-18 while loops
# i=int(input("enter the number:"))
# while(i<=38):
#     i=int(input("enter the number:"))
#     print(i)

# print("done with the loop")

# count=5
# while(count>0):
#     print(count)
#     count=count-1
# else:
#     print("done with the loop")  
     
# n=1
# while (n<=10):
#     print(3,"X",n,"=",3*n)
#     n=n+1









# print("3-10")
# num = 2
# while num < 10:#10
#     num = num + 1#10
#     print(num)#3,4,5,6,7,8,9,10
# print("2 to 9")
# num1 = 2
# while num1 < 10:#10
#     print(num1)    
#     num1 = num1 + 1
# print("only 10")
# num2 = 2
# while num2 < 10:
#     num2 = num2 + 1
# print(num2)
#?calc
# while a!=-1 or b!=-1 :
#    a = int(input("enter first value"))
#    b= int(input("enter second value"))
#    print(a + b)
# else :
#     print("calculation end")
#?table printer
# while True :
#     num = int(input("Enter a table number"))
#     i = 1
#     while i<11:
#         print( num,"X",i,"=",num*i)
#         i=i+1

# i = 6
# while i<11 and i>5:
#     i=i+1
#     print(i)

# for j in range(5,11,1):
#     print(j)


# # todo day-19 break nd continue
# for i in range(12):
#     print("5 x",i,"=",5*(i))
#     if(i==10):
#        break
    

# print("loop ko chhor kr nikl jao")
# ?isme phle 10 tk print krdega fir jab i=10 hoga uske bad brerak krega 
# for i in range(12):
#     if(i==10):
#        break
#     print("5 x",i,"=",5*(i))
# print("loop ko chhor kr nikl jao")
# # ?isme jaise hi i=10 hoga vo break kr gega
# for i in range(12):
#     if (i==10):
#         print("skip the iteration")
#         continue
#     print("5 x",i,"=",5*i)    
# todo day-20  funtion
# def calculateGmean(a,b):
#     mean=(a+b)/(a*b)
#     print(mean)
    

# a=23
# b=12
# calculateGmean(a,b)
# c=34
# d=90
# calculateGmean(c,d)

# def isgreater(x,y):
#     if(x>y):
#         print("x is greater than y")
#     else:
#         print("y is greater than x")
# x=634
# y=24
# isgreater(x,y)       
# todo day-21 functions arguement
# def average(m=3,n=1):
#     print("the average is",(m+n)/2)
# average()     
# average(1,5)
# # ?isme m=1,n=5 ko maan kr avg nikalegas
# average(7)
# # ?isme m=7 and n=1 le lega
# average(b=10)
# def name(fname,mname="johm",lname="king"):
#     print("hello,",fname,mname,lname)
# name("aaloo","laloo","paloo")    
# todo day-22 ,lists
# marks=[7,8,9,"harruy",True]
# marks[0]=
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(len(marks))
# # ?len-5 hai but index hai 0,1,2,3,4 

# print(marks[-3])#negative index
# print(marks[len(marks)-3])#positive index
# print(marks[5-3])#positive index
# print(marks[2])#positive index 
# !above 4 codes are same
# if "harruy" in marks:
#     print("yes")
# else:
#     print("no")
# if 8 in marks:
#     print("yes")
# else:
#     print("no")
# if "8" in marks:
#     print("yes")
# else:
#     print("no")         
# if "ha" in "harry":
#     print("yes")    
# print(marks)
# print(marks[:])
# print(marks[1:])
# # print(marks[1:-1])  conveert it into positive index
# print(marks[1:4])    
# lulu=[1,2,3,4,5,"aaloo",True,"laloo",54,59,"gugu"]
# print(lulu)
# print(lulu[1:9])
# print(lulu[1:9:2])
# # !isme phle 1:9 tk jaiga fir 1st print krke  2-2 ke gap main 2nd print kr dega
# print(lulu[1:9:3])
# # !isme phle 1:9 tk jaiga fir 1st print krke  3-3 ke gap main 3rd   print kr dega
# lst=[i for i in range(4)]
# print(lst)
# lst=[i*i for i in range(4)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)


# todo day-23 list methid in python
# l=[0,3,2,5,1,5,6,9,4,5]
# # print(l)
# m=l
# m[0]=9#!thiswill replace 0 by 9 from 0th index
# print(l)

# m=l.copy()
# m[0]=9#!thiswill replace 0 by 9 from 0th index
# print(l)
# l.append(9)
# print(l)
# ?list ki end main new character jod dega
# l.sort()
# print(l)
# # ?ascendeing ordr mai kr dega
# l.sort(reverse=True)
# print(l)
# # ?descendeing ordr mai kr dega

# l.reverse()
# print(l)
# ?original list ko  ulta kr dega
# print(l.index(5))
# print(l.count(5))
# l.insert(1,899)
# print(l)
# # ?iska mtlb haio ki 1 index pr 899 insert krdo
# m=[900,90,9000]
# l.extend(m)
# print(l)
#?iska mtlb hai l ko kholo or or m ko uske end mai rkhdo
# print(l)
# k=m+l
# print(k)
#todo--> tuples day-24
# tup=(1)#this is not a tuple
# tup=(1,)#thi is a tuple
# tup=(1,2,3,"green" ,"red")
# tup[0]=90#tuples are immutable so tghis is AN error
# print(type(tup),tup)
# print(len(tup))
# print(tup[0])
# print(tup[2])
# print(tup[-1])
# print(tup[3])
# if "green" in tup:
    # print("yes green is present")
# if 4 in tup:
    # print("yes it is present")
# tup2=tup[1:3]
# print(tup2)
#todo-->day 25 operations on tuples
# countries=("spain","italy","india")
# temp=list(countries)
# temp.append("russia")  #add item 
# temp.pop(3)  #remove item
# temp[2]="finland"  #chnge item
# countries=tuple(temp)
# print(countries)
# !tuples are immutablr
#!strings nd list are mutable
# countries2=("pak","afghan","china")
# sovietunion=countries+countries2
# print(sovietunion)
tuple0=(1,2,3,4,3,4,6,3,1,2)
# res=tuple0.count(3)
# print("count of 3 in tuple0:",res)
# res=tuple0.index(3)
# print(res)
# res=tuple0.index(3,1,8)#isme phle 4 se 8 tk slicing main jo 1st 3 hoga uski index btaiga
# print(res)
# res=len(tuple0)
# print(res)
#todo -->f-strings day - 28
# letter="my name is {} and i am from {}"
# country="india"
# name="harry"
# print(letter.format(name,country))
# print(letter.format(country,name))

# etter="my name is {1} and i am from {0}"
# country="india"
# name="harry"
# print(etter.format(country,name)
#?fromn 396 to405 is string formatting 
country="india"
name="harry"
# print(f"hey my name is {name} and i am from {country}")
# print(f"hey my name is {{name}} and i am from {{country}}")#!agr aapko same yhi print knna hai to name and country ki value nhi

# price=49.0987
# txt=f"for only {price:.2f} dollars!"#!.2f se 2 decimal tak value dega 3f se 3 decimal tk
# print(txt)

# print(2*30)
# print(f"{2*30}")
# print(type(2*30))#!this is an int
# print(type(f"{2*30}"))#!this is an string
#todo-->doc string ,day-29
# def square (n):
#     '''takes in a number n,returns the #!doc string hmesha def wali line ke baad ata ay
#     square of n'''#!this is doc tring
#     print(n**2)
# square(5)
# print(square.__doc__)#!comments have no effect on code but doc string have
#todo-->Recursion ,day-30
def sum(n):
    
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
    
print(sum(4))
#!recursion is the process of defining something in terms of itself
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)#!like here we have used factorial for finding factorial
# print(factorial(4))
# print(factorial(5))
# todo-->sets dauy--31 #?order doesnt matter
# s={2,1,3,2}
# print(s)
#?set main item repeat ni hota or zaroori ni ay ki order main hi ho
# info={"harry",5,77,"false",5.9}
# print(info)
# pom={}
# print(type(pom))#!this is a dictionary
# pon=set()#!empty set
# print(type(pon))
# for value in info:
    # print(value)#!loop is using hwere output wii not be in order
# s1={1,2,1}
# s2={4,5,7}
# print(s1.union(s2))
# print(s1,s2)
# (s1.update(s2))
# print(s1,s2)
# countries2={"pak","afghan","china","india"}
# countries={"spain","italy","india","pak"}
# countries3=countries.intersection(countries2)#!isme new set bnaya gya ki dono ka intersection
# print(countries3)
# countries.intersection_update(countries2)#!ime set ko update kr dia gya
# print(countries)
# countries3=countries.symmetric_difference(countries2)#!jo common ni ay vo print ni hioga
# print(countries3)
# countries3=countries.difference(countries2)#!isme vo ainge jo countries main to hai pr dono mai common nib ay
# print(countries3)
# print(countries.isdisjoint(countries2))
# #!disjoint mtlb dono main kuch bhui common na ho
# countries4=("arab","amrika")
# print(countries.issuperset(countries4))
# print(countries.issuperset(countries2))
#!superset or subset ka mtlb hai ki countries ke saare element countries2 nd countries4 main hai
# countries.add("afgan")
# print(countries)
# countries.remove("pak")
# print(countries)
# item=countries.pop() #!kisi bhi ek item ko set mai se pop krdegA
# print(countries)
# print(item)
# del countries#!this will delete the set
# print(countries)
#todo-->dictionary day-33 
# dic={
#     344:"harry",
#     56:"aaloo",
#     658:"xxx"
# }
# print(dic[56])
info={"name":"karan","age":19,"eligible":True}
# print(info)
# print(info.get("name"))
# print(info["name"])
# print(info.get("name2"))#!this will give none not error
# print(info["name2"])#!this will ive error
# print(info.keys())
# print(info.values())
# print(info.items())
# for key in info.keys():
    # print(info[key])
# for key in info.keys():
#     print(f"the value corresponding to the key {key} is{info[key]}")

# print(info.items())
# for key,values in info.items():
#     print(f"the value corresponding to the key {key} is{info.items()}")
    








#todo-->dictionary methods ,day-34
# ep1={122:1,123:2,124:3}
# ep2={221:4,222:5,223:6}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)#!pop mtlb remove
# ep1.popitem()#!this will remove last pair
# del ep1[122]#!delete122 pair
# del ep1["122"]#!this will give error becz 122 is an integer not string
# print(ep1)    
# empt={}
# print(empt)
#todo-->for loop with else in python ,day--35
# for i in range(5):
#     print(i)
# else:
#     print("sorry no i")    

# for i in []:#!here else will be printed becz there nothing in i
#     print(i)
# else:
#     print("sorry no i")

# for i in range(6):
#     print(i)
#     if(i==4):
#         break

# else:
#     print("sorry no i") #! here else will not be print becz break hone ke baad loop break nhi blki khtm hua ay             

#todo-->exception handling, day-36
# a=input("enter the number:"")
# print(f"multiplication table of {a}is:")

# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a) * i}")
# #!if we type a name not a int in this it will give aan error and the below two will also not run  due to erroer in this    
# print("some imp lines of codes")
# print("end of program")    
  

# a=input("enter the number:")
# print(f"multiplication table of {a}is:")
# try:
#    for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a) * i}")
# except:
#   print("invalid input:")    
# #!in this if we didnt use int except will be run and the below 2 codes are alse run
# print("some imp lines of codes")
# print("end of program")    

# try:
#     num=int(input("enter an integer:"))#3
#     a=[6,3]# 0->6, 1->3
#     print(a[num])#!index-exception
#     #?below code will not excecute because of above exception
#     b = a[num] + 6
#     print(b)
# except ValueError:
#     print("number entered is not an integer")
# except IndexError:
#     print("value of num should be less than 2")

#todo-->finally keyword in pythonm,day--373
#! chahe try mai jaaye ya except mai jai  finally will always be executed
# try:
#     l=[1,4,6,8]
#     i=int(input("enter the index:"))
#     print(l[i])
# except:
#     print("some error occured")
# finally:
#     print("i will always executed")   

#todo--> raising custom errors,day-38
# a=int(input("enter any number:"))
# if(a<5 or a>9):
    # raise ValueError("value should be between 5 and 9")
# !errors are raised by raise variable

#todo-->short hand if else statements, day -41
# a=330000
# b=3300
# print("A")if a>b else print("=") if a==b else print("B")

# c=9 if a>b else 0
# print(c)

#todo-->enumerate function,day-42
#

# marks=[12,54,87,98,66,56,1]
# for index,mark in enumerate(marks):
#     print(mark)
#     if(index==3):
#         print("harry,awesome")
# # ! isme index mai marks de dega

# marks=[12,54,87,98,66,56,1]
# for mark,index in enumerate(marks):
#     print(mark)
#     if(index==3):
#         print("harry,awesome")
# !isme marks mai index de dega


# for index,mark in enumerate(marks,start=1):
    # print(mark)
    # if(index==3):
        # print("harry,awesome")
#!isme index 1 se cgalu hui hai 
       
#todo-->how import works,day--44
# import math
# result=math.sqrt(9)#?output is 3.000
# print(result)

#!maan lo ki main sirf ek function import krna chahta hu, we use from
# from math import sqrt,pi
# result=sqrt(9)*pi
# print(result)

#!us*ing as keyword 
# from math import sqrt as s,pi
# result=s(9)*pi
# print(result)

# import math as m
# result=m.sqrt(9) * m.pi
# print(result)

# import math
# print(dir(math))#!thisd shows all the function of maths 
# import math
# print(math.sqrt,type(math.sqrt)) 
 
# from harry import welcome,harry 
# welcome()
# print(harry)
# #todo-->if_name_=="_ main__"in python ,day 45
# import harry
# harry.welcome()
#!hey you are welcome 2 baar print hoga kyunki ek baar harry.py(wlcm()) mai or ek baar sum.py main(harry.welcome) main likha ay                                                                            ]












#todo-->local vs global variables , day-48
#?global var are declared outside any function or class ,
#?while local variables are declraed within a function or block of code  




# x=10 #global varible

# def my_function():
#     x=5
#     y=4 #local variable
    
# my_function()   
# print(x)
# print(y)#!this will ccause an error becz y is an local var and is not accesible outside of the function 


x=10 #global varible

# def my_function():
#     global x
#     x=5 #thuis will chnge the value of the global variable x
#     y=4 #local variable
    
# my_function()   
# print(x)
# print(y)#!this will ccause an error becz y is an local var and is not accesible outside of the function 

#todo-->file IO in python , day-49
# ?READING A FILE
# f=open('myfile.txt','rt       qs')#!is file ko 2 trike se open kr skte3 at rb or rt ,
# #!rt default hota uski jgh bss r lga do ya r bhi na lgao to bhi chlega becz r mode default hota ay
# !but rb krnese binary ki form mai open krefga
# text=f.read()
# print(text)
# f.close()
#!r mode is default jb r,w,a nhi lga hoga to r mode chlega

# ?WRITING A FILEE
#!agar write mode mairea krke aapne aisi file ko open kr dia jo exist ni krti to vo bn jaigi as below
# f=open('myfile2.txt','w')
# text=f.read()
# print(text)
# f.close()

#!keep in mind that writing to na file will overwrite its content
#!if u want to append a file instead of overwriting it,u can open it in append mode 
# f=open('myfile.txt','w')
# f.write("hello,world!")
# f.close()

#!append method my file main append krta chla jaiga
# f=open('myfile.txt','a')
# f.write("hello,world!")
# f.close()

#!another method of file handling
# with open("myfile.txt","a")as f:
#     f.write("hey i am inside with")

#todo-->read(),readlines() nd othr mthds,day-->50

#todo-->object oriented programing day-->56
#todo-->class and objects  day-->57
# class person:#?this is a classs
#     name="harry"
#     occupation="software developer"
#     networth=10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# #!ye name wagera ki hmne default values leli hai upr
#!jb hm class define kr rhe hain to self arguement lena hi lena ay
# a=person()#?these are objects
# b=person()
# c=person()

# a.name="shivi"
# a.occupation="HR"
# print(a.name)
# b.name="khushi"
# b.occupation="chor"

# a.info()
# b.info()
# c.info()
# #!c.info default value le lega

#todo-->constructors in python day-->58
# class person:
#     def __init__(self,n,o):  #?ye ek constructor bnata hai
#      print("hey i am a person")
#      self.name=n
#      self.occ=o
     
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# #  #!here we are giving 3 arguesments self ,n and o self apne aap pass ho rh hai or baaki ke 2 hmne diye hain n and o       
# a=person("harry","HR")#!this is a object and whenever we r calling a object it will call the constructor(hey i m a person)
# b=person("divya","CR")#!this is a object and whenever we r calling a object it will call the constructor(hey i m a person)
# # # c=person()#!ye 2positional arguement ko miss kr rha ay n and o
# # # d=person(1,2,3) #!it takes 3 positional argyuements but 4 are given,self apne aap pass ho rha hai automatically 


# a.info()
# b.info()     
     
#todo-->decorators ,day-->59
#?function-> to do reusable work
#1) without return
# def table_Of_Five():
#     for i  in range(1,11):
#         print(i*5)

#2) with return(most imp)
#!calculator
#operand(value)
# def inputValue():
#     first  = int(input("Enter first value"))
#     second  = int(input("Enter second value"))
#     arr = [first,second]
#     return arr  

# def inputOperator():
#     op = input("Enter the operator")
#     return op

# def operation(valList,operator):
#     if(operator == "+"):
#         ans = valList[0] + valList[1]
#         return ans
#     elif(operator == "-"):
#         ans = valList[0] - valList[1]
#         return ans
#     elif(operator == "*"):
#         ans = valList[0] * valList[1]
#         return ans
#     elif(operator == "/"):
#         ans = valList[0] / valList[1]
#         return ans

# def display(answer):
#     print(answer)
    
# inValList =  inputValue()#[first,second]
# inOperator = inputOperator()#op
# ans = operation(inValList,inOperator)
# display(ans)
# Passing the function as an argument

# def inputName():
#     name = input("Enter the name")
#     return name

# def greting(nameFunction):
#     print(nameFunction())
#     print("hello!")
    
# greting(inputName)
# #? class






#todo-->getters and setters,day-->59

# 9










                                                                                                                  