# Write a program to find out whether a given post is talking about “Harry” or not


name = "harry"

post = input("Write a post : ")
post=post.lower()

if  (name in post):
    print("The post is talking about Harry")
else:
    print("The post is not talking about Harry")