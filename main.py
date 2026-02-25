import prompt, names, directories, cohort, message, shutil, os
from cohort import Cohort
from operator import methodcaller

# List of subdifectories to create for each cohort folder
subdirectories = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]
# The Files subdirectory contains its own list of subdirectories
files_subdirectories = ["Attendance Agreement", "Enrollment Form", "Laptop Waiver", "Sign-in Sheets"]

# Dictionary to choose day options
# 1) Monday/Wednesday
# 2) Tuesday/Thursday
day_options = {1: "Mon Wed", 2: "Tue Thu"}

# List to store cohorts' information
cohort_list = []

# Get user input for month and year
# Both will be used to create any cohorts created
month = prompt.enter_cohort_month()
year = prompt.enter_cohort_year()
count = prompt.enter_cohort_count()

# Loop to create cohort objects
for i in range(count):
    # Print out Cohort Number Banner divider
    message.info_banner(i)

    # Get user cohort information
    num = prompt.enter_cohort_number()
    option = prompt.enter_cohort_days()
    start = prompt.enter_cohort_start_date()
    end = prompt.enter_cohort_end_date()
    
    # Add cohort certificates name for Files' subdirectory
    files_subdirectories.append(names.certificates(num))
    
    # Root of cohort folder
    # Change for every cohort number
    directory = names.cohort_directory_name(num, month, year, day_options[option])
    
    # Create the parent cohort folder if it doesn't already exist
    directories.create_directory(directory)
    
    # Create enrollment, agreement, syllabus, and roster files
    # based on user cohort number, month, and year input
    files = names.create_file_names(num, month, year, day_options[option])
    
    # Debuggin for loop
    # Display all files created for cohort
    for file in files:
        print("File Created: " + file)
    # Create paths to sub directories
    directories.create_path(directory, subdirectories, files_subdirectories)
    # Remove the previous cohort Files subdirectory
    files_subdirectories.pop()

    # Copy files from class documents to cohort's class documents directory
    documents_list = os.listdir()
    for document in documents_list:
        if document == 'roster.xlsx':
            shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Roster/Cohort #20 {document.title()}")
        if document == 'schedule.xlsx':
            shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Schedule/Cohort #20 {document.title()}")
        if document == 'certificate.docx':
            shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Files/Cohort #20 Certificates/Cohort #20 {document.title()}")
        else:
            shutil.copyfile(document, f"../(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Class Documents/Cohort #20 {document.title()}")

    
    # TODO: Go to Files directory in current cohort parents directory

    # Create cohort class instances (objects)
    cohort = Cohort(i, num, month, year, option, start, end, directory, files)
    cohort_list.append(cohort)

results = list(map(methodcaller('get_directory'), cohort_list))
print(results)
