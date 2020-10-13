sec = int(input("Enter sec: "))
hour = sec // 3600
minutes = sec // 60
sec = sec % 60

if minutes >= 60:
    if sec >= 60:
        print("Have {}  hours {} minutes and {} seconds".format(hour, minutes - 60 * hour, sec - 60))
    else:
        print("Have {}  hours {} minutes and {} seconds".format(hour, minutes - 60 * hour, sec))
else: 
    print("Have {}  hours {} minutes and {} seconds".format(hour, minutes, sec))



