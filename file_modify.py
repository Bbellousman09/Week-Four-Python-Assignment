def read_and_modify_file(input_filename, output_filename):  
    try:  
        # Open the input file for reading  
        with open(input_filename, 'r') as infile:  
            # Read the content of the file  
            content = infile.read()  
        
        # Modify the content (for example, convert it to uppercase)  
        modified_content = content.upper()  

        # Write the modified content to the output file  
        with open(output_filename, 'w') as outfile:  
            outfile.write(modified_content)  

        print(f"Modified content has been written to '{output_filename}'.")  

    except FileNotFoundError:  
        print(f"Error: The file '{input_filename}' does not exist.")  
    except IOError:  
        print(f"Error: The file '{input_filename}' could not be read.")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  


def main():  
    # Ask the user for the input file name  
    input_filename = input("Please enter the input filename: ")  
    # Specify the output file name  
    output_filename = "modified_" + input_filename  
    
    # Call the function to read and modify the file  
    read_and_modify_file(input_filename, output_filename)  


if __name__ == "__main__":  
    main()