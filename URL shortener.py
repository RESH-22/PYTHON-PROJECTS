import hashlib

url = input("Enter URL: ")

short = hashlib.md5(url.encode()).hexdigest()[:6]

print("Short URL: https://short.ly/" + short)
