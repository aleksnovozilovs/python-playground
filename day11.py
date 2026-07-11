tech_stack = {"Python": "Programming language", "PowerShell": "Automation", "Git": "Version control"}

print("My technologies")
print("---------------")

for technology, description in tech_stack.items():
    print(technology, " -> ", description)

search_item = input("Which technology do you want information about? ").casefold()

for technology, description in tech_stack.items():
    if technology.casefold() == search_item:
        print(description)
        break

else:
    print("Technology not found!")