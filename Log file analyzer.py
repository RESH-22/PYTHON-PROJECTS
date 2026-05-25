file = open("log.txt")

errors = 0

for line in file:
    if "ERROR" in line:
        errors += 1

print("Total Errors:", errors)
