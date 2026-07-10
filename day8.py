def show_profile(name, years, project, level):
    
    if years >= 10:
        level = "Senior Engineer" 
    elif years >= 5:
        level = "Experienced Engineer"
    else:
        level = "Early Career Engineer"

    print("Profile")
    print("-------")
    print(f"Name: {name}")
    print(f"Experience: {years} years")
    print(f"Level: {level}")
    print(f"Project: {project}")

    
    
name = input("Enter your name: ")
years = int(input("Enter your years of experience: "))  
project = input("Enter your current project: ")
level = ""

show_profile(name, years, project, level)