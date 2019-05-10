unique_set = (["Ava", "Oliver", "Ethan", "Amelia", "Oliver", "Mia", "Lucas", "Ava", "Ethan", "Enzo"])

def unique(value):
    new_set = set()
    for i in unique_set:
        if i not in new_set:
            new_set.add(i)
    return new_set

print(unique(unique_set))