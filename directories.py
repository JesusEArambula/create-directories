import os, message

# Function to create directories
def create_directory(directory):
    os.makedirs(directory, exist_ok = True)
    print(f"Folder << {directory} >> created successfully.")

# Function to create paths to subfolder
def create_path(directory, subdirectories, files_subdirectories):
    message.break_line()
    print(f"Creating subdirectories for {directory} ...")
    for subdirectory in subdirectories:
        # Create paths for subfolder
        
        #                    Cohort Directory
        #      ______________________|________________________
        #      |         |       |       |          |         |
        #  Documents   Files   Flyer   Report   Schedule   Roster
        
        os.makedirs(os.path.join(directory, subdirectory), exist_ok=True)

        # Check if the current subdirectory we're creating is the Files subdirectory
        # To create the Files subdirectory its own subdirectories

        #                         Files Directory
        #      ___________________________|_________________________
        #      |           |          |       |          |         |
        #  Agreement   Enrollment   Waiver   Certificates   Sign-ins
        if subdirectory == "Files":
            for files_subdirectory in files_subdirectories:
                os.makedirs(os.path.join(directory + "/" + subdirectory, files_subdirectory), exist_ok=True)
                print(f"Folder << {subdirectory}/{files_subdirectory} >> inside Files directory created successfully.")
        print(f"Folder << {directory}/{subdirectory} >> created successfully.")



