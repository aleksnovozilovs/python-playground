def print_technologies():
    print("My Technologies")
    print("---------------")
    for technology in technologies:
        print(technology)
    print()

def enter_technology():
    new_technology = input("Enter new technology: ")
    print()
    if new_technology in technologies:
        print(f"{new_technology} already exists.")
        print()
    else:
        technologies.add (new_technology)
        print(f"{new_technology} added succsesfully.")
        print()


technologies = {"Python", "Java", "Git"}
print_technologies()

enter_technology()
print_technologies()


