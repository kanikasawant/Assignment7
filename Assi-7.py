def update_file(file="NewFile.txt"):
    try:
        # Open the file in append mode
        f = open(file, "a")
        
        # Write data to the file
        roll_number = "26"
        name = "Kanika Sawant"
        class_name = "SYCO"
        f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])
                
        # Reopen the file in read mode
        f = open(file, "r")
        
        # Read and print the data from the file
        print(f.readlines())

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

# Call the function
# update_file()
update_file()


