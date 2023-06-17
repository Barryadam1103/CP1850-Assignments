print("Units Of Time")

#Ask user for the Following times
days = int(input("Enter the amount of days:  "))
hours = int(input("Enter the amount of days:  "))
mins = int(input("Enter the amount of minutes:  "))
sec = int(input("Enter the amount of seconds:  "))


#Do multipcation for the different untis of time

days_in_seconds = days * 24 * 60 * 60
hours_in_seconds = hours * 60 * 60
minutes_in_seconds = mins * 60

sec_total = days_in_seconds + hours_in_seconds + minutes_in_seconds + sec


print("The total amount in seconds is:  ", sec_total)