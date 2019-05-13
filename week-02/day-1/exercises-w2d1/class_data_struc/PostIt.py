class PostIt():
    def __init__(self, bg_colour, text, text_colour):
        self.bg_colour = bg_colour
        self.text = text
        self.text_colour = text_colour

post1 = PostIt("orange", "Idea_1", "blue")
post2 = PostIt("pink", "Awesome", "Black")
post3 = PostIt("yellow", "Superb!", "green")
print("an " + post1.bg_colour + " with " + post1.text_colour + ": \"" + post1.text + "\"")
print("an " + post2.bg_colour + " with " + post2.text_colour + ": \"" + post2.text + "\"")
print("an " + post3.bg_colour + " with " + post3.text_colour + ": \"" + post3.text + "\"")