import prompt, names, directories, cohort, message, shutil, os, dates, string
from cohort import Cohort
from datetime import date
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

    # Create a start and end date format 
    start_date = date(int(year), int(start.split('/')[0]), int(start.split('/')[1]))
    end_date = date(int(year), int(end.split('/')[0]), int(end.split('/')[1]))

    # Create a list of the cohorts dates
    date_list = dates.get_dates(start_date, end_date)
    
    # Add cohort certificates name for Files' subdirectory
    files_subdirectories.append(names.certificates_directory(num))
    
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
    os.chdir('class documents')
    print(os.getcwd())
    print(os.listdir())
    # Copy files from class documents to cohort's class documents directory
    documents_list = os.listdir()
    for document in documents_list:
        if document == 'roster.xlsx':
            shutil.copyfile(document, f"../{directory}/Roster/{names.roster(num, month, year)}")
        elif document == 'schedule.xlsx':
            shutil.copyfile(document, f"../{directory}/Schedule/{names.schedule(num, month, year, day_options[option])}")
        elif document == 'flyer.jpg':
            shutil.copyfile(document, f"../{directory}/Flyer/{string.capwords(document)}")
        elif document == 'report.docx':
            shutil.copyfile(document, f"../{directory}/Report/{names.report(num, month, year)}")  
        elif document == 'certificate.docx':
            shutil.copyfile(document, f"../{directory}/Files/Cohort #{num} Certificates/{document}")
        else:
            shutil.copyfile(document, f"../{directory}/Class Documents/Cohort #{num} {string.capwords(document)}")

    
    # TODO: Go to Files directory in current cohort parents directory

    # Create cohort class instances (objects)
    cohort = Cohort(i, num, month, year, option, start, end, directory, files)
    cohort_list.append(cohort)

    # Return to "create-directories" folder
    os.chdir("../")

results = list(map(methodcaller('get_directory'), cohort_list))
print(results)
