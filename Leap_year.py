# checking if the year is leap or not
# if the year is divisible by 4 ,then it is leap year else not

year = int(input("Enter the year: "))

if year % 4 == 0:
    #print("{} is leap year!" .format(year))
    print(year,"is a leap year!")
else:
    print("{} is not leap year!".format(year))

