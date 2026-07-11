file = open("notes.txt", "r")

lines = file.readlines()
print(lines)

file.close()

print(type(lines))

for line in lines:
    print(line.strip())