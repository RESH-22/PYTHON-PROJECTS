import os
import shutil

path = "downloads"

for file in os.listdir(path):
    filename, extension = os.path.splitext(file)

    extension = extension[1:]

    if os.path.exists(path + "/" + extension):
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
    else:
        os.makedirs(path + "/" + extension)
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
