#Python loops and Control Statements 

#if statement
val=input("Entre the Number:")
value_float=float(val)
if(value_float%2==0):
    print("The number is Even")


#else statement
val=input("Enter the Number:")
value_float=float(val)
if(value_float%2==0):
    print("The number is Even")
else:
    print("The number is Odd")



#More examples of if-else statement 
#Age form 

age=float(input("Enter your age : "))

if(age<18):
    print("Minor age ")
else:
    print("You are not minor ")


#Nested if else condition 

age=float(input("Enter your age : "))

if(age<18):
    print("Minor age ")
elif(age>=18 and age<=45):
    print("Mid Age")
elif(age>=45 and age<=50):
    print("Senior Mid age")
else:
    print("Senior Citizen")


##Loop statements 
#For loop , While loop

#For Loop

lst=[1,2,3,4,5,6,7,8]
for i in lst:
    print(i**3)

#Find the sum of all Elements in list 
lst=[1,2,3,4,5,6,7,8]
sum1=0
for i in lst:
    sum1=sum1+i
print(sum1)

#find the sum of even and odd number 
lst=[1,2,3,4,5,6,7,8]
even_sum=0
odd_sum=0

for i in lst:
    if(i%2==0):
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i

print("Even sum is {}".format(even_sum))
print("Odd sum is {}".format(odd_sum))

i=i+1


#While loop 

i=0
even_sum=0
odd_sum=0
while(i<10):
    if(i%2==0):
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i

i=i+1
print(even_sum , odd_sum)


#Break statement

x=1
while(x<7):
    print(x)
    if x==4:
        break
    print(x)
    x=x+1


#Continue statement or skipping statement

x=0
while(x<7):
    x=x+1
    if x==4:
        continue
    print(x)









