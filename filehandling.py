def modify_content(content):
  
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n✅ Original content read successfully.")

        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
            print(f"✅ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write to file.")

if __name__ == "__main__":
    main()
