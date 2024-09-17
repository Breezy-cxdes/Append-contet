# Function to append the content of two files
def append_file_content(file1, file2):
    # Read and display the content of the first file
    with open(file1, 'r') as f1:
        content1 = f1.read()
        print(f"Content of first file before appending:\n{content1}")
    
    # Read and display the content of the second file
    with open(file2, 'r') as f2:
        content2 = f2.read()
        print(f"\nContent of second file before appending:\n{content2}")
    
    # Append the content of the second file to the first file
    with open(file1, 'a') as f1:
        f1.write(content2)
    
    # Read and display the content of the first file after appending
    with open(file1, 'r') as f1:
        appended_content1 = f1.read()
        print(f"\nContent of first file after appending:\n{appended_content1}")
    
    # Display the content of the second file, which remains unchanged
    with open(file2, 'r') as f2:
        content2_after = f2.read()
        print(f"\nContent of second file after appending:\n{content2_after}")

# Example usage
file1 = 'Codingal.txt'  # First file to which content will be appended
file2 = 'sample_doc.txt'  # Second file whose content will be appended

append_file_content(file1, file2)
