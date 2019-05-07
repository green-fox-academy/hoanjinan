# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
day_hour = 6
semester = 17
workdays = 5
avg_week = 52

result = day_hour * workdays * semester
print(result)

result /= (avg_week * semester)
#result = result / (avg_week * semester)
print ("{0:.1%}".format(result))