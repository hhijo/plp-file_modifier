# Read contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words
words = content.split()
word_count = len(words)

# Convert text to uppercase
uppercase_content = content.upper()

# Write the processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content + "\n")
    file.write(f"\nWORD COUNT: {word_count}\n")

# Print success message
print("✅ File 'output.txt' created successfully with processed text and word count.")
