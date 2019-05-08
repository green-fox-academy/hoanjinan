tel_book = {"William A. Lathan": "405-709-1865",
            "John K. Miller": "402-247-8568",
            "Hortensia E. Foster": "606-481-6467",
            "Amanda D. Newland": "319-243-5613",
            "Brooke P. Askew": "307-687-2982"}

#print(tel_book["John K. Miller"])

def findNumber(name):
    if "name" in tel_book:
        return tel_book[f"{name}"]

def findPerson(num):
    for key, value in tel_book.items():
        if value == num:
            return key

def if_in_book(name):
    return "name" in tel_book
    

print(findNumber("John K. Miller"))
print(findPerson("307-687-2982"))
print(if_in_book("Chris E. Myers"))