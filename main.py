import prompt, names, directories, cohort, message
from cohort import Cohort
from operator import methodcaller

# List of subdifectories to create for each cohort folder
subdirectories = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]

# List to store cohorts' information
cohort_list = []

# Get user input for month and year
# Both will be used to create any cohorts created
month = prompt.enter_cohort_month()
year = prompt.enter_cohort_year()
count = prompt.enter_cohort_count()

# Loop to create cohort objects
for i in range(count):
    message.info_banner(i)
    num = prompt.enter_cohort_number()
    days = prompt.enter_cohort_days()
    start = prompt.enter_cohort_start_date()
    end = prompt.enter_cohort_end_date()
    # Root of cohort folder
    # Change for every cohort number
    directory = names.cohort_directory_name(num, month, year)
    # Create the parent cohort folder if it doesn't already exist
    directories.create_directory(directory)
    # Create enrollment, agreement, syllabus, and roster files
    # based on user cohort number, month, and year input
    files = names.create_file_names(num, month, year)
    # Debuggin for loop
    # Display all files created for cohort
    for file in files:
        print("File Created: " + file)
    # Create paths to sub directories
    directories.create_path(directory, subdirectories)
    
    cohort = Cohort(i, num, month, year, days, start, end, directory, files)
    cohort_list.append(cohort)

results = list(map(methodcaller('get_directory'), cohort_list))
print(results)
