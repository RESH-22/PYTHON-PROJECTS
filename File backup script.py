import shutil

source = "data.txt"
backup = "backup_data.txt"

shutil.copy(source, backup)

print("Backup created")
