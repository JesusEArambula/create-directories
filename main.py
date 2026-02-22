import prompt, names, directories, cohort
from cohort import Cohort

# List of subdifectories to create for each cohort folder
subdirectories = ["Class Documents", "Files", "Flyer", "Report", "Schedule", "Roster"]

# List to store cohorts' information
cohort_list = []

# Get user input for month and year
# Both will be used to create any cohorts created
cohort_month = prompt.enter_cohort_month()
cohort_year = prompt.enter_cohort_year()
cohort_count = prompt.enter_cohort_count()

# Loop to create cohort objects
for i in range(cohort_count):
    pass

# Get user input for the cohort numbers, month, and year
cohort_number_1 = prompt.enter_cohort_1()
cohort_number_2 = prompt.enter_cohort_2()

# Create enrollment, agreement, syllabus, and roster files
# based on user cohort number, month, and year input
cohort_1_files = names.create_file_names(cohort_number_1, cohort_month, cohort_year)
cohort_2_files = names.create_file_names(cohort_number_2, cohort_month, cohort_year)

# Root of cohort folder
# Change for every cohort number
cohort_1_directory = names.cohort_directory_name(cohort_number_1, cohort_month, cohort_year)
cohort_2_directory = names.cohort_directory_name(cohort_number_2, cohort_month, cohort_year)

# Create the parent folder if it doesn't already xist
directories.create_directory(cohort_1_directory)
directories.create_directory(cohort_2_directory)

# Create paths to sub directories
directories.create_path(cohort_1_directory, subdirectories)
directories.create_path(cohort_2_directory, subdirectories)
