def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the input file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Generate output file name
        output_filename = "modified_" + filename

        # Write modified content to new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Successfully read '{filename}' and wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Cannot read or write to the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
