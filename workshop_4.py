# Solution to Workshop 4 by Hilmi Abdul Hanif
# finds the day of the week on any particular date using the disparate variation equation
def day():
    # days indexed in a list with Sunday = 0 and Saturday = 6
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    d    = int(input("Day  : "))
    m    = int(input("Month: "))    
    year = int(input("Year : "))

    # if the month is January or February, minus 1 from the year
    if m == 1 or m == 2:
        year -= 1

    # phase shift the months, March = 1 ... February = 12
    if m < 3:
        m += 10
    else:
        m -= 2

    # get the last 2 and first 2 digits of the year
    y = year % 100
    c = year // 100

    w = (d + int(2.6*m - 0.2) + y + int(y/4) + int(c/4) - 2*c) % 7

    print("This date falls on a", days_of_week[w])

day()
