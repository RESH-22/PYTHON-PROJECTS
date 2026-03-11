text = input("Enter markdown: ")

html = text.replace("**", "<b>").replace("__", "<i>")

print(html)
