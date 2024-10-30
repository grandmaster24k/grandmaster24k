# . Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

if  (a > b) and (a > c) and (a > d):
    print ("The greatest number is ", a)

elif (b>a) and (b>c)  and (b>d):
    print ("The greatest number is ", b)

elif (c>a) and (c>d)  and (a>b):
    print ("The greatest number is ", c)

elif (d>a) and (d>b)  and (d>c):
    print ("The greatest number is ", d)

print("thanks for participating ")





