"""
#refer to code and debug youtube channel for the video and practice this python.
name='Vishwa'
age= 27
place='Bangalore'
is_student = False

print("Hello",name,"your current age is",age,"and current address is",place,)
print("hello " + name + " your present age is " + str(age) + " your present address is " + place)

#using the f-string 
print(f"You name is {name}, current age is {str(age+20)}, U live in {place}")

#explicit conversion- means we are converting the data from one type to another type
num1="100"
num2="500"
num3= int(num1)+ int(num2)
print(num1,type(num1))
print(num2,type(num2))
print(f'')

num1=100
num2=200
Total= num1+num2 
print(f"The Total is = {Total}")

num1=input()
num2=input( )
num3=input( )
print(f'The entered value is {num1}, and the value of num2 is {num2}, and same like num3 value is {num3}')

#print( 10 ** 3 - 12 * 43 // 23 + 12 - 78)

a = 0
b = 50
print(a == b)
print(a >= b)
print(a <= b)
print( a < b)
print( a > b)
print( a != b)

n = int(input())
if n % 2 != 0:
    print("weird")
elif n % 2 == 0 and 2 <= n <=5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <=20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

a = int(input())
b = int(input())
print(f"Sum = {a+b}")
print(f"Subtract = {a-b}")
print(f"Product = {a*b}")
print(f"Division = {a/b}")

age = int(input("Enter your current age = "))
can_vote = age >= 18
senior_citizen = age >= 60
print(f"User can vote = {can_vote}")
print(f"User is Senior citizen = {senior_citizen}")

sub1 = int(input("The marked score in maths is = "))
sub2 = int(input("The Marked score in the science is = "))
sub3 = int(input("The Marked scored in env = "))
Total = sub1+sub2+sub3
Avg = Total / 3
print(f"The Total Marks scored in all 3 subjects is ={Total}")
print(f"The Average Mark obtained per subject is = {Avg:.2f}")


90 above - > A
81 - 90 - > B
71 - 80 - > C
61 - 70 - > D
60 and below - > Fail  

marks = int(input("Enter marks = "))
if marks >= 91:
    print("A")
elif marks >= 81 and marks <= 90:
    print("B")
elif marks >= 71 and marks <= 80:
    print("C")
elif marks >= 61 and marks <= 70:
    print("D")
elif marks !=60 and marks <=60:
    print("Fail")

age = 28
certificate = True
if age >= 18:
    if certificate == True:
        print("Your Eligible to Vote")
    else:
        print("Cannot vote due to no certificate")
else:
    print("Cannot vote,age is less than 18")

age = int(input("The age is = "))
if age >= 18:
    status = "Adult"
else:
     status  = "Minor"
print(f"Your status is {status}")

age = int(input("Enter age is = "))
Status = "Adult" if age >= 18 else "Minor"
print(f"The status is {Status}")

num = int(input("Enter a number ="))
if num > 0:
    print(f"The number is positive")
elif num < 0:
    print(f"The number is negative")
else:
   print(f"The number is zero ") 


#Take two numbers as input. Print the greater of the two.if they are equal, print "both are equal"
num1 = int(input("The first number is = "))
num2 = int(input("The second number is = "))
if num1 > num2:
    print(f"The num1 is greater than num2")
elif num2 > num1:
    print(f"The num2 is greater than num1")
else: 
    print(f"The both numbers are equal")

#Take a students marks as input. Print their grade based on the scale:
#90 and above -> A

marks= int(input("The student total marks is = "))
if marks >= 90:
    print("The Grade is A")
elif marks >= 75 and marks <= 89:
    print("The Grade is B")
elif marks >= 60 and marks <= 74:
    print("The Grade is C")
elif  marks >= 40 and marks <= 59:
    print("The Grade is D")
else:
    print("The Grade is Failed")

#take a year as input, check if its a leap year. A year is a leap year if its divisible by 4, but not 100,
#unless its also an divisible by 400.

year = int(input("Enter a year ="))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print("Its a Leap year")
else:
    print("Its not Leap year")

#home work quest:-  Q11
age =int(input("Enter the age= "))
valid_id = input("Do you have valid ID(True/False): ")
if age >= 18 and valid_id == "True":
    print("Person is Eligible to enter the venue")
else:
    print("The person is not Eligible to enter the venue")

#Q12:-
num1 = int(input('Enter first num'))
num2 = int(input('Enter second num'))
num3 = int(input('Enter third num'))
if num1 >= num2 and num1 >= num3:
    print("Largest number is =", num1)
elif num2 >= num3 and num2 >= num3:
    print("Largest number is =", num2)
else:
    print("largest number is =", num3) 

#Q13:
num = int(input("Enter a num:"))
print("even" if num % 2 == 0 else "Odd")

price = int(input("The Total price is "))

if price > 5000:
    discount = 20

elif price > 2000:
    discount = 10

elif price > 1000:
    discount = 5

else:
    discount = 0

print("Discount =", discount, "%")

#print Hello 10 times
i = 1
while i <= 5:
    print("Hello")
    print("Done")
    i += 1

# print 1 to 10 numbers by using the while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# 1 to n print, n is the number input by the user.
n = int(input("Enter a num ="))
i = 1
while i <= n:
    print(i)
    i += 1

#start and end by user
#start to end print using while loop.

start = int(input("Enter start number ="))
end = int(input("Enter end number = "))
i = start 
while i <= end:
    print(i, end=" ")
    i += 1
print(f'After while loop, start the value is{start}')

#start to end print even numbers
start = int(input("Enter start number ="))
end = int(input("Enter end number = "))
i = start
while  i<=end:
    if i % 2 == 0:
      print(i, end=" ")
    i += 1

#print start to end, numbers which are divisible by 3 & 4.

start = int(input("Enter a start num = "))
end = int(input("Enter a end number = "))
i = start
while i <= end:
    if i % 3==0 and i % 4==0:
        print(i, end=" ")
    i += 1

#print the numbers from 10 to 1.
i = 10
while i >= 1: (when we are going from descending to ascending order use ">=" symbol)
    print(i, end =" ")
    i -= 1   (here its should -=1 since we are printing from last to first order)

#Q15:- Print all the numbers which are divisible by 3 & 5 from 1 to 100.
start = 1
end = 100
i = start
while i <= 100:
    if i % 3==0 and i % 5 ==0:
        print(i, end = " ")
    i += 1

#Q16 Sum of all the numbers from 1 to 100.
start = 1
end = 100
i = start
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(f'sum = {sum}')

start = 1
end = 100
i = start
sum = 0
while i <= end:
    sum = sum + i
    i += 1
print("Sum =", sum)  

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
total = 0
while i <= end:
    total = total + i
    i += 1

print(f"Total = {total}")

#Q17:- Sum of all the numbers from 1 to 100 which are divisible by 2 & 7.
start = 1
end = 100

sum = 0
i = start

while i <= end:

    if i % 2 == 0 and i % 7 == 0:
        print(i, end=" ")
        sum = sum + i

    i += 1

print("\nSum =", sum)

#Q18:- Ask a number from the user, print the multiplication table upto 10.
num= int(input("Enter a number = "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1

#Q19:- Ask a number from the user, and print all the factors.
num = int(input("Enter a number = "))
i = 1
while i <= num:
   if num % i == 0:
       print(i, end=" ")
   i += 1

#For loop:- This loop we will be using when we know the range when its going to end.

#Q20:- 
#print the number from 13 to 36
for i in range(13,36):
    print(i, end=" ")

##print the number from 1 to 56 with difference of 8.
for i in range(1,56,8):
    print(i, end = " ")

#print the number from 30 to 1 with difference of 3.
for i in range(30, 1, -3):  
    print(i, end = " ")
#In the For loop when we are going to print the numbers from descending to the ascending order 
we should consider adding "-" in the third place in the range bracket
otherwise the code doesn't run because here in the For Loop it always 
checks the numbers from right(+) side to left(-) side hence in the right side,
it should always start with small numbers first and then the big number second)

#print the numbers from the 200 to 100
for i in range(200,100, -10):
    if i % 2 ==0 and i % 4 ==0:
       print(i, end = " ")
 
#Dynamic For loop:-
#start and end, print start to end.
start = int(input("Enter a start number = "))
end = int(input("Enter a end number = "))

for i in range(start, end + 1):
    print(i, end= " ")

#print the start to end by total by using the dynamic for loop.
start = int(input("enter a start number = "))
end = int(input("enter a end number"))
total = 0
for i in range (start, end +1):
    total += i
    print(total)

#print the numbers from 1 to 20 where stop the loop for 10.
i = 1
while i <= 20:
    print(i, end = " ")
    i += 1
    if i == 11:
        break
        
#print the numbers from 20 to 45 where apply loop at 35.
i = 20
while i <= 45:
    i += 1
    if i == 36:
        break
    print(i, end = " ")

#print the numbers from 0 to 10 while using the continue statement which are divisible by 2.
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end = " ")

Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)

total = 0
while True: #here True is writeen means it will 'n- no of times' or many times)
    num = int(input("Enter a number = "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)

#Nested Loop example
for i in range(1,6):
    print(f"i={i}")
    for j in range(10,15):
        print(f"j={j}")

#Nested loop some more examples:-
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
print this above number by using nested loop.

for i in range(1,6):
    for j in range(1, 6):
        print(j, end = " ")

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

for i in range(1,6):
    for k in range(1, 6 - i):
        print("", end= " ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#space pattern loop
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1

for i in range(5,0, -1):
    for j in range(1, i -1+1):
        print(" ", end=" ")
    for k in range(5, i-1, -1):
        print(k, end = " ")
    print()
#Next question number 29 in the below
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

for i in range(1,6):
    for j in range(1,5-i +1):
        print(" ", end = " ")
    for k in range(1,(i*2)-1 +1):
        print(k, end = " ")
    print()
for i in range(4, 0, -1):
    for j in range(1,5-i +1):
        print(" ", end = " ")
    for k in range(1,(i*2)-1 +1):
        print(k, end = " ")
    print()

#Q30:- 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

for i in range(1,6):
    for j in range(1, 5-i +1):
        print(" ", end=" ")
    for k in range(1,(i*2) -1 +1):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, 5 -i +1):
        print(" ", end = " ")
    for k in range(1,(i*2) - 1 +1):
        print("*", end =" ")
    print()

#great function example code
def greet():
    print("Good Morning!")
    print("This is afternoon!")
    print("This is evening!")
greet()


#Q35:- Write a function that ask a number from user and prints if that number is odd or even.
def odd_num():
    num = int(input("Enter a number = "))
    if num % 2 == 0:
        print("its a even number")
    else:
        print("its odd number")
odd_num()      


#Q37:- Write a function that prints all the factors of a number entered by a user.
def factor():
    num = int(input("Enter a number = "))
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end= " ")
factor()

# print 3 int's as a parameter and its total.
def addition(a,b,c):
    ans = a + b + c
    print(f"Total = {ans}")

addition(23,34,56)

#Ask a name,age,gender, print
def greet(name,age,gender):
    print(f"Hey {name}! Your age is {age} and gender is {gender}")
greet("Vishwa", 27, "Male")

#Q37:- Write an function called add that takes two numvers as paramteres and print their sum.
def add(num1, num2):
    sum= num1 + num2
    print(f"The Total sum of two numbers is = {sum}")
add(13, 56)

#Q38:- write an function called rectangle_area that takes length and breadth as parameters and print the area.
def rectangle_area(length, breadth):
    area = length * breadth
    print(f"The area of the rectangle is = {area}")
rectangle_area(0.13,5)

#Q39:- Write an function called find_max that takes three numbers as parameters and prints the largest one.
def find_max(num1, num2, num3):
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num3 and num2> num1:
        print(num2)
    else:
       print(f'{num3} is largest number')
find_max(12,34,26)

#Q40:- Write a function called discount_price that takes original_price and discount_percent as parameters and print the final price after discount.
def discount_price(original_price, discount_percent):
    discount_amount= (discount_percent / 100)* original_price
    final_price= original_price - discount_amount
    print(f"{final_price} is the final price")
discount_price(34000,19)

#return statement example 
def addition(n1,n2,n3):
    return n1 + n2 + n3
ans = addition(10,23,40)
print(ans)

#True or false return, if the user can vote or not.
def can_vote(age):
    if age >=18:
        return True
    else:
        return False
ans=can_vote(14)
print(ans)
================

def greet(name,age):
    return f"Your name is {name} and age is {age} years"
    print("Good")
    print("Bye")
    print("Done")
print(greet("Vishnu", 27))
==============================

#Return True if the number is prime number otherwise return false.
def is_prime(num):
    count = 0

    for i in range(1, num +1):
        if num % i == 0:
            count += 1
    if count == 2:
            return True
    else:
            return False
print(is_prime(2))
print(is_prime(32))
print(is_prime(9))

#Q41:- Write an function called "square" that takes a number and returns its square.Store the result and print it.
def square(num):
    return num * num
print(square(19))
=========================
#Q42:- Write a function called min_of_three that takes three numbers and returns the smallest without using any built-in function.
def min_of_three(n1,n2,n3):
    if n1<n2 and n1<n3:
        return(n1)
    elif n2<n1 and n2<n3:
        return(n2)
    else:
        return(n3)
print(min_of_three(13,1,-32))
===============================

#Q43:- Write a function called absolute_value that takes a number and returns its absolute value without using the built-in-abs() function.(absolute value - any number place from "0")
def absolute_value(n1):
    return abs(n1)       #here "return" is abs function whereas in the question its mentioned that we shouldn't use.
print(absolute_value(23))
print(absolute_value(-5))
print(absolute_value(-19))
print(absolute_value(33))

#hence the above code is wrong because we have used function

def absolute_value(num):
    if num >=0:   #(these prints only for positive num)
        return num
    return num * -1
print(absolute_value(-5))
print(absolute_value(-19))
print(absolute_value(33))
==============================

#local variable example:-
def addition(n1,n2,n3):
    total=(n1+n2+n3)
    print(f"The Total is {total}")
addition(10,20,30)
#here in the above code "total" is local variable it means i will not able to use total outside the written function.

#global variable example
def xyz(n1,n2):
    n1=12      #here n1 & n2 are both local variables and this will be always ignore when we have written global variable in code.
    n2=34      
    print(f"Inside function n1={n1} and n2={n2}")
n1=20
n2=40    #n1 &n2 values are global variables and it always takes this values as first numbers.
xyz(n1,n2)
print(n1)
print(n2)
=============

name = "Vishwanath"   #here "name" is global variable

def greet():
    name = "vishal"    #here this "name" is a local variable so it won't consider.
    print(f"hey {name}!, Good Morning")

greet()
print(name)
==================

#Q44:- Write an lambda function that takes a number and returns its cube, store it in a variable and call it.
cube = lambda x: x ** 3
print(cube(35))

#Q45:- Write an lambda function that takes a number and returns "Positive" or "Negative".
Check_number = lambda x: "Positive" if  > 0 else "Negative"
print(check_number(14))
print(check_number(-5))

#Q46:- Write an function fizzbuzz(n) that takes a single number and pronts "Fizz" if its divisible by 3, "Buzz" if its divisible by 5. "Fizzbuzz" if its divisible by both, otherwise print the number itself.
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
num = int(input("Enter a number: "))
fizzbuzz(num)

===============
#Q47:- Write a function power(base,exp) that returns base raised to exp using a loop - no ** operator or poe() allowed.
def power(base,exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result
base= int(input("Enter base: "))
exp=int(input("Enter exponent: "))
print(power(base,exp))
============================================
#Q48:- Write a function tax_calculator(income) that takes annual income & returns the tax amount based on these slabs:
#upto 250000 -> no tax,  2,50,000 to 5,00,000 -> 5%, 5,00,000 to 10,00,000 -> 20% & above 10,00,000 -> 30%
def tax_calculator(income):
    if income <= 250000:
        print("No tax")
    elif income <=500000:
        tax = income * 0.05
    elif income <= 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.30
    return tax
income = int(input("Enter annual income"))
print("Tax Amount =", tax_calculator(income))

(or)

def tax_calculator(income):

    if income <= 250000:
        tax = 0

    elif 250000 < income <= 500000:
        tax = income * 0.05

    elif 500000 < income <= 1000000:
        tax = income * 0.20

    else:
        tax = income * 0.30

    return tax

income = int(input("Enter annual income: "))
print("Tax Amount =", tax_calculator(income))

=========================================

marks = [45,34,54,65,23,65,76,91]
#to get the length of the list.
n = len(marks)
print(f"Length of list={n}")

#max
maxi = max(marks)
print(f"Maximum marks = {maxi}")
mini = min(marks)
print(f"Minimum marks = {mini}")

#To sort using the sorted(), it will always return you a new list.
new_list = sorted(marks, reverse=True)
print(f"new_list = {new_list}")

=============

lst=["Anirudh","yash","rishab",45,54.68,"rakshith"]
#R H ->    0          1      2    3    4      5        
#L R ->  # -6         -5     -4   -3  -2      -1 
#print(lst[0])
#print(lst[-3])
#print(lst[5])
n= len(lst)
print(f"the second element is ={lst[n-1]}")
===============

lst=["Aniketh","raj",23,89,"vishwa"]
print(f"lst={lst}")
lst[1]='abcde'
lst[-1]='abcde'
print(f"lst={lst}")

=========================

#Create a list of 5 of ur fav movies.Print the first,last and middle movie from your list using both positive and negative indexing where appropriate.
#Create a list of 5 no's and replace second & 4th elements of this list with the number 0 using indexing.Print the updated list.
lst=[10,20,30,40,50]
lst[1]=0
lst[3]=0
print(lst)

==========

#slicing example:-
#     0  1   2   3   4   5    6  7   8   9   10 
#   -11 -10 -9  -8  -7  -6   -5 -4  -3   -2   -1
lst=[34, 45, 56, 77,108, 29,-23, 39, 89, 21, 30]
lst1=lst[0:4]
lst1=lst[1:99]
lst1=lst[6:8]
lst1=lst[:4]
lst1=lst[0:9:2]
lst1=lst[::3]
print(lst1)
=============
fruits=["appale","mango","banana"]
for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")
==========

fruits=["appale","mango","banana"]
for fruit in fruits:
    print(fruit)
#IN the above example we have used for loop.
===================

#using a while loop
fruits = ["apple","orange","banana","mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i +=  1
=============

#Given a list of no's, write a python code using a loop to find and print largest element.Do not use the built-in max() function.
nums=[6, -5, 4, 2, 10, 95, -54, 9 , 25]
maxi = float("-inf")     #maxi is a just variable name and float("-inf")- is negative infinity.
for num in nums:
    if num > maxi:
        maxi = num
print(f"Maximum number={maxi}")
=============

#Write a prgm that a list and target number.Use a loop to determine if the target number exists in the list. Do not use the in operator.
def target_exists(lst,target):
    for num in lst:
        if num == target:
            return True
    return False

nums=[6, -5, 4, 2, 10, 34, -45, 78]
print(target_exists(nums,17))
print(target_exists(nums,10))
print(target_exists(nums,-5))
=============

#Given a list of no's, use a loop to calculate & print their average.We can use len() to get the count of elements, but avoid using sum() for the total.
def calculate_average(nums):
    n= len(nums)
    total=0
    for num in nums:
        total += num
    return total/n

nums = [6, -5, 4, 23, 36, -75, 40, 0, 9]
print(calculate_average(nums))
======================================

#List methods exmaples:-

lst=['Arya',54,'banana',98]
#lst.append(100)
#lst.insert(3,'Delhi')
x=lst.pop()
print(x)
print(lst)
===========

#examples for pop with index and without index

#create a sample list
fruits=['apple','banana', 'cherry','date', 'mango','orange'] 
last_fruit=fruits.pop()
print(last_fruit)
print(fruits)

#Pop with specific index values(removes index 1)
specific_fruit=fruits.pop(1)
fruits.remove('mango')
print(specific_fruit)
print(fruits)      #It did not include 'date' when output is printed because that item was already permanently removed in the previous step of the code.Python executes code sequentially, line by line. Here is exactly what happened to the list.
=====================
#other list examples in the python:-
nums=[3,6,7,-10,93,28,-2,0,193]
new_list=sorted(nums)
print(f"new_list = {new_list}", id(new_list))
print(f"nums={nums}",id(nums))
print(nums.index(-2))
print(nums.count(93))
print(nums.clear())

===========
#Membership "in" & "not in" examples :-
nums=[2,5,7,0,34,77,-83,91,-82,10,0]
print(93 not in nums)
print(77 in nums)
=================
#Q59. Reverse a list without using the .reverse() method or list slicing ([::-1]).
numbers=[23,45,78,39,10,91]
reversed_list=[]
for i in range(len(numbers) -1, -1, -1):
    reversed_list.append(numbers[i])
print("Original list:", numbers)
print("Reversed list:",reversed_list)

===========

#Q60. Given two lists, merge them into a single new list without modifying the originals.
list1=[12,34,56,54]
list2=[1,-3,89,34]
merged_list=[]
for item in list1:
    merged_list.append(item)
for item in list2:
    merged_list.append(item)
print("Merged List:", merged_list)
print("List1:", list1)
print("List2:",list2)
================================

#Q61. Given a list, remove all duplicate elements while preserving the original order of the unique items.
numbers=[12,43,78,90,21,65,5,10,12,90]
unique_list=[]
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
#print("Original List:", numbers)
print("List after removing duplicates:", unique_list)
=========================================
#(or) try this another method.

def remove_duplicates(lst):
    result=[]
    for num in lst:
        if num not in result:
            result.append(num)
    return result
nums=[1,5,3,4,6,4,5,7,9,3,6]
print(remove_duplicates(nums)) 

==========================

#Q62. Separate a list of integers into two distinct lists: one containing all the even numbers and the other containing all the odd numbers.

lst=[12,45,90,56,11,13,18]
odd_list=[]
even_list=[]
for item in lst:
    if item % 2 ==0:
        even_list.append(item)
    else:
        odd_list.append(item)
print("Even List:", even_list)
print("Odd List:", odd_list)
==============================

#other ways to write the solution is:-
def even_odd_lists(lst):
    even_list=[]
    odd_list=[]
    for num in lst:
        if num %2 ==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    print(f"Even list={even_list}")
    print(f"Odd list={odd_list}")
nums=[1,2,4,6,4,8,0,5,10,3]
even_odd_lists(nums)

=====================

#Q63. Create a list containing the squares of numbers from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
lst=[1,2,3,4,5,6,7,8,9,10]
squares=[]
for num in lst:
    squares.append(num*num)
print(squares)
==========================
#any method/ solution

result = []
for i in range(1, 11):
    result.append(i * i)
print(result)

=========

#Q64. Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurrences of that integer from the list.
def remove_duplicates(lst,target):
    result=[]
    for num in lst:
        if num !=target:
            result.append(num)
    return result
nums=[1,2,3,1,4,5,6,7,2,4]
print(remove_duplicates(nums, 2))
====================================

#Q65:-Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.
def replace_negative(lst):
    n=len(lst)
    for i in range(0,n):
        if lst[i] < 0:
            lst[i]=0
    return lst
nums=[1,4,-1,34,67,80,-19,0,-63,45,-4]
print(replace_negative(nums))

================================

#Examples of list comprehension:-
#Q66:- Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
new_list=[i * i for i in range(1,21) if i%2==1]
print(new_list)

=====================
#Make a new list from 1 to 10 by using the comprehension list:-
new_list=[i for i in range(1,11)]
#new_list=[i for i in range(10,-1,-1)]
print(new_list)

=============

#Make a list to print only the even numbers from 1 to 20.
new_list=[ i for i in range(1,21) if i % 2==0 ]
print(new_list)
================
#Make a list to print only the divisible numbers from 1 to 20 divisible by 3 & 7.
new_list=[ i for i in range(1,21) if i % 3==0 or i % 7==0]
print(new_list)
================================
#Print the list from 1 to 100, to make list of all prime numbers.
def is_prime(num):
    factors=0
    for i in range(1, num+1):
        if num % i == 0:
            factors +=1
    if factors==2:
        return True
    return False
new_list=[i for i in range(2,101)if is_prime(i)== True]
print(new_list)
========================

#Q67:- Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75. 
marks=[45,87,12,94,23,88,91,11]
new_list=[num for num in marks if num >= 75]
print(marks)
print(new_list)

===========

matrix=[
    [4,8,1],
    [9,7,2],
    [5,6,9],
]                   #3*3 matrix 
#print(matrix[0][2])
#print(type(matrix))
for i in range(0,3):
    for j in range(0,3):
        print(matrix[i][j],end=" ")
    print()

=============

matrix=[
    [4,8,1],
    [9,7,2],
    [5,6,9],
]                   #3*3 matrix 
#print(matrix[0][2])
#print(type(matrix))
total = 0
for i in range(0,3):
    for j in range(0,3):
        total= total + matrix[i][j]
print(total)

===================================
#Dynamic iteration example:- #write the matrix for (4*5)

matrix=[
    [3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12],
    [1, 2,  3, 4, 5],
    [6, 7,  8, 9, 10],
]
rows= len(matrix)
columns=len(matrix[0])
for i in range(0, rows):
    for j in range(0,columns):
        print(matrix[i][j],end=" ")
    print()
=====================================
#Q69. Given a 3x3 matrix as input, print its lower triangle. Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).
#here in the above questn, they have given "Upper Triangle"= Square matrix[Rows==columns] i.e.  3*3, 4*4 etc
1  2  3
4  5  6
7  8  9

1  *  *
4  5  *
7  8  9
---------------------- #answer:-
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],        
]
rows=len(matrix)
columns=len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i >=j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

==========================

#Q70:- (lower traingle)
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],        
]
rows=len(matrix)
columns=len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i <=j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
===============================
#Q71:-(main diagonal element(centre elements should be *))
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],        
]
rows=len(matrix)
columns=len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i ==j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
========================
#Q72. Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left) elements and replace everything else with an asterisk (*).

1  2 3
4  5 6
7  8 9

Expected Output:
*  * 3
*  5 *
7  * *

Above is question & below is answer
-------------

matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 1],
    [7, 8, 9, 7],
    [9, 7, 3, 1],
]

rows=len(matrix)
columns=len(matrix)
for i in range(0,rows):
    for j in range(0,columns):
        if i + j == rows - 1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end= " ")
    print()
====================

#Q73. Given a 4x4 matrix, print only the border elements and replace the inner elements with an asterisk (*).
matrix = [              # j=0 j=1 j=2 j=3
    [1, 2, 3, 4],       #  i=0
    [5, 6, 7, 8],       #  i=1
    [9, 10, 11, 12],    #  i=2
    [13, 14, 15, 16]    #  i=3
]

#Ans:-
rows=len(matrix)
columns=len(matrix)
for i in range(0,rows):
    for j in range(0,columns):
        if i == 0 or i==rows-1 or j==0 or j==columns-1:
            print(matrix[i][j],end=" ")
        else:
            print("*", end=" ")
    print()
=======================

#Q74:- Create a tuple of 5 of your favourite songs. Print the first, last, and middle one using indexing.
songs = ("song1", "song2", "song3", "song4", "song5")
print(f"First song: {songs[0]}")
print(f"last song: {songs[4]}")
print(f"Middle song: {songs[2]}")
=================================

#Q75: Create a tuple of 8 numbers. Using slicing, print the first 3, last 3, and every alternate element.
numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print(f"First 3 numbers: {numbers[0:3]}")
print(f"last 3 numbers: {numbers[-3:]}")
print(f"Every alternate number: {numbers[::2]}")
================================================

#76:- Create a tuple of marks of 6 students. Print the highest, lowest, total, and average.
marks=[50,64,88,96,100,42]
highest=max(marks)
lowest=min(marks)
Total=sum(marks)
average=Total/len(marks)
print(f"The highest student marks is= {highest}")
print(f"The lowest student marks is= {lowest}")
print(f"The total student marks is= {Total}")
print(f"The average student marks is= {average:.2f}")

=================================

#Q77: Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.
nums=[]
for i in range(0,5):
    num=int(input(f"Enter a number{i+1}: "))
    nums.append(num)
numbers_tuple=tuple(nums)
print("Tuple :",numbers_tuple)
print("Tuple :",min(numbers_tuple))
print("Tuple :",max(numbers_tuple))
====================================

#Q78:Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum, and maximum. Unpack the returned tuple and print each value.
def get_stats(nums):
    total=sum(nums)
    average=total/len(nums)
    minimum=min(nums)
    maximum=max(nums)
    return(total,average,minimum,maximum)
nums=(20,40,30,60,80)
total,average,minimum,maximum=get_stats(nums)
print("The Sum :", total)
print("The Average :", average)
print("The Minimum :", minimum)
print("The Maximum :", maximum)

=================================
#Dictonaries examples:-

#example 1:-

student={"name":"vijay", "age":"27"}
print(student, id(student))
#update
student["age"]=30
print(student,id(student))
#add
student["gender"]="male"
print(student, id(student))
============
 
#EXA2:-

student={
    "name":"Rahul",
    "age":"36",
    "gender":"Male",
    "city":"Hyderbad",
} 

k=input("Enter key= ")
if k in student:
    print(student[k])
else:
    print("key doesn't exists")
===============================
"""

marks={
    "science": 99,
    "maths":100,
    "cs":88,
    "Hindi":43,
    "History":77,
}
print(marks.items())
