"""
File Handling and Exception Handling Program
Reads a file, modifies content, and writes to a new file with error handling
"""

def process_file(input_filename, output_filename):
    """
    Reads input file, modifies content, and writes to output file
    Handles common file operations errors
    """
    try:
        # Read input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write to output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Success! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'")
    except IOError as e:
        print(f"Error: An I/O error occurred - {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def main():
    print("=== File Processing Program ===")
    
    # Get user input with validation
    while True:
        input_file = input("Enter the filename to read: ").strip()
        if input_file:  # Simple non-empty check
            break
        print("Error: Filename cannot be empty")
    
    output_file = "modified_" + input_file
    
    # Process the file
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()