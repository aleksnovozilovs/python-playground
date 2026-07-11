def display_stack():
    technologies = ["Python", "PowerShell", "Git"]
    print("My tech stack")
    print("-------------")
    for technology in technologies:
        print(technology)

def greet(name):
    print(f"Hello {name}!")
    print("Welcome back to Python.")
    print()

def add(a, b):
    return a + b

greet("Aleks")
display_stack()
print()
result = add(25, 17)
print(result)