print("Please enter your birthday ")
bd_y=int(input("Year:"))
bd_m=int(input("Month (1-12):"))
bd_d=int(input("Date:"))

from datetime import datetime
now = datetime.now()
SECONDS_PER_DAY     = 86400
age = datetime(int(bd_y), int(bd_m), int(bd_d))
inseconds = (now-age) * SECONDS_PER_DAY

print(("Your age in days: " + str(now - age)))
print("Your age in seconds: ",str(inseconds))
