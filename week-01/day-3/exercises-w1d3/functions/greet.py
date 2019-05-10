# - Create variable named `al` and assign the value `Greenfox` to it
# - Create a function called `greet` that greets it's input parameter
#     - Greeting is printing e.g. `Greetings, dear Greenfox`
# - Greet `al`

al = "Greenfox"

def greet(value):
    return f"Greetings, dear {value}"

print(greet(al))