import os, message

# Function to create directories
def create_directory(directory):
    os.makedirs(directory, exist_ok = True)
    print(f"Folder << {directory} >> created successfully.")

# Function to create paths to subfolder
def create_path(directory, subdirectories):
    message.break_line()
    print(f"Creating subdirectories for {directory} ...")
    for subdirectory in subdirectories:
        # Create paths for subfolder
        
        #                    Cohort Directory
        #      ______________________|________________________
        #      |         |       |       |          |         |
        #  Documents   Files   Flyer   Report   Schedule   Roster
        
        path_to_create = os.path.join(directory, subdirectory)
        os.makedirs(path_to_create, exist_ok=True)
        print(f"Folder << {directory}/{subdirectory} >> created successfully.")



