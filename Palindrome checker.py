def check_palindrome(text):
    text = text.lower()  # convert to lowercase
    if text == text[::-1]:
        return "It is a Palindrome"
    else:
        return "Not a Palindrome"

word = input("Enter a string: ")
print(check_palindrome(word))
