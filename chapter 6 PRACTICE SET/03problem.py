# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.



spam_1= ("make a lot of money")
spam_2= ("buy now")
spam_3= ("subscribe this")
spam_4= ("click this")

message = input("write a comment : \n ")
message = message.lower()

if ((spam_1.upper() in message) or (spam_1.lower() in message)or (spam_2.lower() in message)or(spam_3.lower() in message)or(spam_4.lower() in message)or(spam_2.upper() in message) or (spam_3.upper() in message) or (spam_4.upper() in message)) :
    print("This is a spam comment")

else:
    print("This is not a spam comment")