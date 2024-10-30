# Write a program to find whether a given username contains less than 10
# characters or not.

username_user = input("Enter a username less than 10 character:\n")

if (len(username_user)>10):
    print ("Username is more than 10 characters")

else:
    print("This username is available")
