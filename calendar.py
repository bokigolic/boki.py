# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))

