import os

def create_file(filename):
    with open(filename, "w") as file:
        print("File created successfully.")

def write_file(filename):
    with open(filename, "w") as file:
        data = input("Enter text to write: ")
        file.write(data)
    print("Data written successfully.")

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    else:
        print("File does not exist.")

def append_file(filename):
    if os.path.exists(filename):
        with open(filename, "a") as file:
            data = input("Enter text to append: ")
            file.write("\n" + data)
        print("Data appended successfully.")
    else:
        print("File does not exist.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File does not exist.")


# Main Program
filename = input("Enter file name (example: sample.txt): ")

while True:
    print("\nFile Manipulation Menu")
    print("1. Create File")
    print("2. Write to File")
    print("3. Read File")
    print("4. Append to File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_file(filename)
    elif choice == "2":
        write_file(filename)
    elif choice == "3":
        read_file(filename)
    elif choice == "4":
        append_file(filename)
    elif choice == "5":
        delete_file(filename)
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
