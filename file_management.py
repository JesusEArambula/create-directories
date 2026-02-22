import os, shutil, cohort
from cohort import Cohort

print(os.getcwd())
os.chdir(os.getcwd() + '/class documents')
print(os.getcwd())
print(os.listdir())

# Copy a file using shutil
# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

# shutil.copyfile('agreement form.docx', '../(#20 SPANISH) Mon Wed March 2026 Workshop 360 Valencia/Cohort #20 Agreement Form.docx')
# print(os.listdir())


number = int(input("Enter number: "))
cohort_list = []

for i in range(number):
    print(f"<<<<<<<<<<<<<< Enter information for cohort {i + 1} >>>>>>>>>>>>>>")
    num = input(f"Enter cohort number: ")
    month = input(f"Enter cohort month: ")
    year = input(f"Enter cohort year: ")
    print("Select cohort's days.")
    print("1) Monday/Wednesday")
    print("2) Tuesday/Thursaday")
    days = input(f"Enter cohort's days option (1/2): ")
    start = input(f"Enter cohort start date: ")
    end = input(f"Enter cohort end date: ")
    
    cohort = Cohort(i, num, month, year, days, start, end)
    cohort_list.append(cohort)

    

print(cohort_list)
