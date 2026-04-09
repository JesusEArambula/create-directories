
files_dict = {}


files_list = []
files_types = []
index = 0

user_input = str(input(">> Enter name for root folder: "))

while user_input == "":
    print(">> ERROR: Root folder cannot be blank!")
    user_input = str(input(">> Enter name for root folder: "))

files_dict[user_input] = []

while True:
    print("=== Create a file ===\n1) Folder\n2) Document")
    # Take user input for the file name
    user_input = str(input(">> What would you like to create? (1/2)"))
    # Exit loop when user enteres "exit"
    if user_input == "exit":
        break
    # Check if the user is being a goofball
    if user_input == "":
        print(">> ERROR: That is not an option!")
        continue
    # Create a folder and ask for name
    if user_input == "1":
        user_input = input(">> Enter folder name: ")
        files_dict[user_input] = []
        print(files_dict)
    if user_input == "2":
        print("=== File Types Available ===\n1) Microsoft Word (docx)\n2) Excel Sheet (xlsx)\n3) Powerpoint (pptx)")
        user_input = str(input(">> Enter document option (1, 2, 3): "))
    
    
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
