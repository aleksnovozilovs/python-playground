name = input("Enter your name: ")
password = ""

for i in range(3):
    password = input(f"Please enter your password to continue (Attempt {i + 1} of 3): ")
    if password == "Aviozen":
       print (f"Welcome {name}! Access granted!")
       exit()
    else:
       print ("Incorrect password. Please try again.")

print ("Account Locked, please contact support!")

   