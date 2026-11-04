# what is leaf year
# # A Leap Year is a year that has 366 days instead of 365 days.
# Normally, February has 28 days. But in a leap year, February has 29 days.

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
