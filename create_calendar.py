import datetime, calendar

# Function to create a calendar
def print_calendar(month, year):
    print(f"{datetime.date(year, month, 1).strftime('%B %Y')}")
    print("Su Mo Tu We Th Fr Sa")
    first_day = datetime.date(year, month, 1).weekday() + 1
    month_days = calendar.monthrange(year, month)[1] + 1
    if first_day != 7:
        print("   " * first_day, end="")
    for day in range(1, month_days):  # Adjust based on month length
        if day > 31:
            break
        print(f"{day:2} ", end="")
        if (day + first_day) % 7 == 0:
            print()
    print()

print_calendar(6, 2026)