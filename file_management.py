import os, shutil

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

class Cohort:
    def __init__ (self, cohort_num, cohort_month, cohort_day1, cohort_day2, cohort_year):
        self.cohort_num = cohort_num
        self.cohort_month = cohort_month
        self.cohort_day1 = cohort_day1
        self.cohort_day2 = cohort_day2
        self.cohort_year = cohort_year

number = int(input("Enter number: "))

cohort_list = []


for i in range(number):
    value = input(f"Enter item {i + 1} value: ")
    my_dict[i] = "Cohort #" + value

print(my_dict)
