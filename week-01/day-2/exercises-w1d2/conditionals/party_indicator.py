# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people
girls = int(input("Please enter the girls' number: "))
boys = int(input("Please enter the boys' number: "))
total = girls + boys
if total >= 20 and girls == boys and girls > 0:
    print("The party is exellent!")
elif total >= 20 and girls != boys and girls > 0:
    print("Quite cool party!")
elif total < 20 and girls > 0:
    print("Average party...")
else:
    print("Sausage party")