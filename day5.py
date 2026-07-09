name = input("What is your name? ")

if name == "Aleks":
    print (f"Welcome back, {name}!")
else:
    print (f"Hello, {name}!")
    years = int(input("How many years have you worked in IT? "))
    project = input("What project are you building? ")
    if project == "Aviozen" or years >= 10:
        print (f"{name}, you are working on something exciting! ")
    else:
        print (f"{name}, keep learning every day!")
