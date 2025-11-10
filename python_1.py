print("hello world!")
print ("Sarah Bansod.","My age is 18.")
print (27)
print (69+21)

name= "mogu bottle"
age= 2
price= 25.90

print (type(name))
print (type(age))
print (type(price))

age2= 18
old= False
e= None
print(type(old))
print(type(e))

#-----------------------------
print("Hello World")
#single line comment or/

"""
multi-lined comment
"""

#*Arithmetic opertors
a= 5
b=2

#for ex.
sum = a+b
print (sum)

#or even directly
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # %:'modulo' to find out the remainder
print(a**b) #power operator; meaning: a^b
#answer for the div operator will always be a floating no. even if the ans is in whole no. for ex:
c=4
d=2

print(c/d)

#Relational Operators
p=50
q=20

print(p==q) #False
print(p!=q) #True
print(p<=q) #False
print(p>=q) #True
print(p>q) #True
print(p<q) #False

#assignment operators
num= 10
num= num+10     #i.e. 10+10=> 20
"""can also write it as 'num+=10' and similarly '-=' and '*=' and '/=' as well..
and '%=' and '**=' too..last waale se square hoga its like a^b """

print("num:" , num)

num2= 10
num2**= 5

print("num2:", num2)


#logical operators
r=50
s=30
print(not False)
print(not (r>s))
 
#ex:

val1 = True
val2 = True

print("AND operator:" , val1 and val2)
 #the value will come TRUE only when both are true
print("OR operator:" , (a==b) and (a>b))
#remember the logic frm maths..AND: T-T-T and OR:F-F-F

#----------------------------------------------------

#TYPE COVERSION
"""TYPE COVERSION:conversion of the type of the variable into another type,there
are 2 types Type Coversion and Type Casting"""

"""conv: automatically coverts the variable
  cast: has to be commanded manually for the coversion"""

z=2
t=4.25

sum= z + t  #2.0 + 4.25 => 6.25

print(sum)
#float>int it is superior since it gives extra info than int(whole no. val)
#pyhton already does the int to float coversion here (implicit conv) and hence its valid and gives the output

"""if 'a' is taken as a STR then the sum will not occur and it will show it as an error..
becoz only str and str can be concatenated together...not 'float' to str"""
# to covert it tho, u have to write this => int("2") and simlilarly for float, float("2")

z2= float("2")
t2= 4.25

print(type (z2))
print(z2 + t2)

#VARIABLES, DATA TYPES, OPERATORS, PRINTING OUTPUTS



#USER INPUT IN PYHTON 
name2= (input("Enter your name:"))
print("Welcome", name2)

age=(input("Enter your age:"))
print("yay! you're", age)

#result for an input()is always str
val= input("enter the subject:")
print(type(val), val)

#all the values n evrything will get coverted into a string for ex.
# "amon" "18" "99.99" etc

int("5")
val= float(input("enter your marks:"))
print(type(val), val)
print("---------------------------------------")

#PRACTICE QUESTIONS
#1)
first= int(input("enter first no."))
second= int(input("enter second no."))

print("sum=", first + second)
#instead of 'first' and 'second' (a,b) or (x,y) etc can also be used as variable name

#2)WAP to input side of a square &print its area
side= float(input("enter side length of square:"))

print("area of the square is:", side * side) #instd of side*side u can also write it as 'side **2'

#3)
x= float(input("enter 1st no.:"))
y= float(input("enter 2nd no.:"))

print("the avg of the nos. is:", (x+y)/2)

#4)
a1= int(input("1st no:"))
b1= int(input("2nd no:"))

print(a1 >=b1)

