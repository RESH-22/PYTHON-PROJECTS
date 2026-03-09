import os

path = "files"

for i, file in enumerate(os.listdir(path)):
    os.rename(os.path.join(path, file),
              os.path.join(path, f"file_{i}.txt"))
