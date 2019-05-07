current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

remain_hour = 23 - current_hours
remain_minutes = 59 - current_minutes
remain_seconds = 60 - current_seconds
remain_seconds = remain_hour * 60 ** 2 + remain_minutes * 60 + remain_seconds
print (f"{remain_seconds}")