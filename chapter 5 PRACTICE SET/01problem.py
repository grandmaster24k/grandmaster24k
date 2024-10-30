#   Write a program to create a dictionary of Hindi words with values as their English
#  translation. Provide user with an option to look it up!

words = {
    "kursi" : "chair" ,
    "billi" : "cat" , 
    "madad" : "help" , 
     "dawakhana" :  "hospital" ,
}
word = input("Enter word you want meaning of: ")

if word in words :
 print(words[word])

else: 
 print("Word not found :( ")

 # using loops early