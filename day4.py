name = input("What is your name? ")
years = int(input("How many years have you worked in IT: "))  
project = input("What project are you building? ")

if project == "Aviozen" and years >= 5:
    print (f"Welcome back {name}! {project} is becoming a serious AI project.")
else:
    print ("Keep learning and keep building!")
