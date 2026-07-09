name = input("What is your name? ")
years = int(input("How many years have you worked in IT: "))
project = input("What project are you building? ")

if years >= 5:
    if project == "Aviozen":
        print (f"{name}, you have expirience and an exciting AI project!")
    else:
        print (f"{name} is an experienced engineer with an interesting project")
else:
    print (f"{name} keep learning, you are building your future")
    
