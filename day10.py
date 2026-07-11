tech_stuck = ["Python", "Java", "PowerShell", "Git", "Linux"]

print("My tech stack")
print("--------------")

for language in tech_stuck:
    print("- " + language)

print()
print("Total technologies: ", len(tech_stuck))

search_item = input("What technology are you looking for?").casefold()

if search_item in [language.casefold() for language in tech_stuck]:
    print("Found!")
else:
    print("Not found.")
