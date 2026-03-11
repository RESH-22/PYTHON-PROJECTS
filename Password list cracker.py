password = "secret"

with open("wordlist.txt") as file:
    for word in file:
        if word.strip() == password:
            print("Password found:", word)
            break
