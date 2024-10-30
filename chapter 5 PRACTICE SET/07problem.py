# If the names of 2 friends are same ; what will happen to the program in problem
# 6?

d =  {}
 
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update ({ name : language })
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update ({ name : language })
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update ({ name : language })
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update ({ name : language })



print (d)

#  if there are identical keys it will replace the previous one
