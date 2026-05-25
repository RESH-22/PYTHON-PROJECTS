word = input("Search word: ")

with open("text.txt") as f:
    for line in f:
        if word in line:
            print(line)
