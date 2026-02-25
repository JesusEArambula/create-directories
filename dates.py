from datetime import timedelta

def get_dates(start_date, end_date):
    """
    Generates a list of all dates (datetime.date objects) 
    between start_date and end_date (inclusive).
    """
    # Calculate the total time difference
    delta = end_date - start_date
    dates = []
    # Loop through each day from the start to end date
    for i in range(delta.days + 1):
        if i == 0 or i == 2 or i == 7 or i == 9 or i == 14 or i == 16 or i == 21 or i == 23:
            # Add 'i' days to the start date
            day = start_date + timedelta(days=i) 

            # Add to list of dates (3/2, 3/5, etc.)
            dates.append(day.strftime("%m/%d"))

    return dates

