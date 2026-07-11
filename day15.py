with open("notes.txt", "r") as file:
    lines = file.readlines()
counter = 1
for entry in lines:
    print(f"technology {counter}: {entry.strip()}")
    counter += 1 
