# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

# quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
# quote = quote.replace("It you", "It always takes longer than you")
# print(quote)

# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
quote = quote[:quote.find("It")+2] + " always takes longer than " + quote[quote.find("you"):]
print(quote)