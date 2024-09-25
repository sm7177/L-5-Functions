# Activity-1
# def intro(user,age):
#     print("Hello",user,"your age is",age)
    
# name=input("Enter your name")
# num=int(input("Enter your age"))

# intro(name,num)



#Activity-2
# def recur_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*recur_factorial(n-1)

# num=int(input("Enter a number"))

# if num<0:
#     print("Factorial doesn't exist for negative numbers")
# elif num==0:
#     print("The factorial of 0 is 1")
# else:
#     print("The factorial of",num,"is",recur_factorial(num))
    


# num=5
# sum=1
# while (num>0):
#     sum=sum*num
#     num=num-1
# print("The sum is",sum)




#Avtivity-3
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y

# num1=int(input("Enter number 1"))
# num2=int(input("Enter number 2"))

# print("Sum:",add(num1,num2))
# print("Difference:",sub(num1,num2))
# print("Product:",mul(num1,num2))
# print("Quotient:",div(num1,num2))

# def even_odd(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")
# num=int(input("Enter a number:"))
# even_odd(num)

# def positive_negative(a):
#     if a>0:
#         print("positive")
#     elif a==0:
#         print("the number is zero")
#     else:
#         print("negative")
        
# num=int(input("Enter a number"))
# positive_negative(num)


marks=int(input("Enter your marks:"))
total_marks=500

percentage=float((marks/total_marks)*100)

name=input("Enter your name:")

if percentage>=80:
    print("Your garde is A",name)
elif percentage>=60:
    print("Your grade is B",name)
elif percentage>=40:
    print("Your grade is C",name)
else:
    print("You have failed your exam",name)

