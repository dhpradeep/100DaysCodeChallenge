import datetime

while True: 
    date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))

    if input("type y if you want to isert time also : ").lower() == "y": 
        time_entry = input('Enter a time in hh:min:sec format : ')
        hour, minute, sec = map(int, time_entry.split(':'))
    else:
        hour , minute , sec = 0, 0, 0    

    dateandtime = datetime.datetime.now()
    birthdate = datetime.datetime(year, month, day, hour ,minute, sec)
    totalSec = dateandtime - birthdate
    totalsecinint = int(totalSec.total_seconds())
    print(round(totalsecinint,0 ))

    if input("Do you want to try again(y/n): ").lower()== "n":
        exit()
