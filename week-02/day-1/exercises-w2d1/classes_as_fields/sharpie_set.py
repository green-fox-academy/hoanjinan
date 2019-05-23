class SharpieSet():
    def __init__(self):
        self.sharpie_list = {"Red": 70, "Blue": 0, "Yellow": 50}

    def count_usable(self):
        for key, value in self.sharpie_list.items():
            print(f"The link level of {key} sharpie is: {value}")

    def remove_trash(self, sharpie):
        if sharpie in self.sharpie_list:
            if self.sharpie_list[sharpie] <= 0:
                self.sharpie_list.pop(f"{sharpie}")
                for key, value in self.sharpie_list.items():
                    print(f"The link level of {key} sharpie is: {value}")
            else:
                print(f"The link level of {sharpie} sharpie is: {self.sharpie_list[sharpie]}")
        else:
            print(f"The {sharpie} sharpie is not in the list!")

sharpie = SharpieSet()
sharpie.count_usable()
sharpie.remove_trash("Blue")
sharpie.remove_trash("Red")
sharpie.remove_trash("blue")
sharpie.remove_trash("Yellow")
sharpie.count_usable()