#Practice Questions
#1)
num=(int(input("enter a number:"))) 
a= num%2
if(a==0):
    print("the number is EVEN")
else:
    print("the number is ODD")

#2)
N1=(int(input("enter 1st no.:")))
N2=(int(input("enter 2nd no.:")))
N3=(int(input("enter 3rd no.:")))

if(N1>N2 and N1>N3):
    print("the greatest no. is:", N1)
if(N2>N1 and N2>N3):
    print("the greatest no. is:", N2)
if(N3>N1 and N3>N2):
    print("the greatest no. is:", N3)
else:
    print("there is no greatest no.")

#3)
abc=(int(input("enter a no.:")))
N= abc%7
if(N==0):
    print("it is a multiple of 7")
else:
    print("it is NOT a multiple of 7")

print("end of code")
print("-----------------------------")





