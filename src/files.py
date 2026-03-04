

files_list = []
files_types = []
index = 0

while True:
    # Take user input for the file name
    user_input = str(input(">> Enter file name: "))
    # Exit loop when user enteres "exit"
    if user_input == "exit":
        break
    # Check if the user is being a goofball
    if user_input == "":
        print(">> You have to enter a name! >:c")
        continue
    else:
        # Add the user input to the list of files
        files_list.append(user_input)
        # Take user input for file type
        print("File types available: ")
        print("1) Folder\n2) Word Document (.docx)\n3) Excel Sheet (.xlsx)\n4) Powerpoint (.pptx)")
        try:
            user_input = int(input(">> Enter file type (1, 2, 3, 4): "))
            print(f"Successfully converted to integer: {user_input}")
        except ValueError:
            print("Input is not a valid integer")
            files_list.pop()
            continue
        
        # if user_input < 1 or user_input > 4 or not user_input:
        #     print(user_input)
        #     print("That is not an option for a file type >:c")
        #     continue
        else:
            # Save file type to list of file types
            files_types.append(user_input)

            # Add file extension to end of file name
            if user_input == 1:
                files_list[index] = files_list[index] + " [Folder]"
            if user_input == 2:
                files_list[index] = files_list[index] + ".docx"
            if user_input == 3:
                files_list[index] = files_list[index] + ".xlsx"
            if user_input == 4:
                files_list[index] = files_list[index] + ".pptx"
            

            index += 1
            # Debugging print statemnt
            print(">> File names created so far: ")
            # Loop for each file in the files list
            for i in range(len(files_list)):
                # Print out file name and file type
                print(f"File {i + 1}: {files_list[i]}")
