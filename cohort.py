# Cohort class to organize cohort information
# Initialize cohort class intance
class Cohort:
    def __init__ (self, 
                  cohort_id, 
                  cohort_num, 
                  cohort_month, 
                  cohort_year, 
                  cohort_days, 
                  cohort_start, 
                  cohort_end, 
                  cohort_directory, 
                  cohort_files):
        self.cohort_id = cohort_id
        self.cohort_num = cohort_num
        self.cohort_month = cohort_month
        self.cohort_year = cohort_year
        self.cohort_days = cohort_days
        self.cohort_start = cohort_start
        self.cohort_end = cohort_end
        self.cohort_directory = cohort_directory
        self.cohort_files = cohort_files
    
    # Return cohort number
    def get_num(self):
        return self.cohort_num
    
    # Return cohort month
    def get_month(self):
        return self.cohort_month
    
    # Return cohort year
    def get_year(self):
        return self.cohort_year
    
    # Return cohort days option
    def get_days(self):
        return self.cohort_days
    
    # Return cohort start date
    def get_start_date(self):
        return self.cohort_start
    
    # Return cohort end date
    def get_end_date(self):
        return self.cohort_end
    
    # Return cohort directory name
    def get_directory(self):
        return self.cohort_directory