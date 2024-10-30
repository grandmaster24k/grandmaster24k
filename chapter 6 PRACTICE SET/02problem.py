# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

a = int(input("Enter marks : "))
b = int(input("Enter marks : "))
c = int(input("Enter marks : "))

if (a >= 33 and b >= 33 and c >= 33) and  (a + b + c /100) >= 40 :
          print("you are passed \n Congrats!")
          print (f"you passed with a percentage of {(a + b + c /100)}")
else:
        print("you are failed \n Sorry!\n try next year")
        print (f"you failed with a percentage of {(a + b + c /100)}")
          

      

