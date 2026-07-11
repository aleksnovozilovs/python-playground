tech_stack = []

for i in range (3):
    language = input("Enter your favorite programming language: ")
    tech_stack.append(language)

print("Your tech stack:")
print(tech_stack)
remove_language = input("Which technology do you want to remove? ")

if remove_language in tech_stack:
    tech_stack.remove(remove_language)
    print(f"{remove_language} has been removed from your tech stack.")
    print("------------------------")
    print("Updated tech stack:")
    print(tech_stack)
else:
    print("Tehcnology not found.")