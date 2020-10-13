# Write a Python program to display the current date and time.

import datetime

now_is = datetime.datetime.now()
print("At this point, the exact date and time is: ")
print(now_is.strftime("%Y-%m-%d %H:%M:%S"))

