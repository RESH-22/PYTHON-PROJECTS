import os

path = "."

size = 0

for root, dirs, files in os.walk(path):
    for file in files:
        size += os.path.getsize(os.path.join(root, file))

print("Folder size:", size, "bytes")
