# File creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Line 1: This is a sample text.\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Python is fun!\n")
        print("File created successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File creation process completed.")

# File reading and display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File reading process completed.")

# File appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appended text 1\n")
            file.write("Line 5: 98765\n")
            file.write("Line 6: More content added!\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File appending process completed.")

create_file()
read_file()
append_to_file()