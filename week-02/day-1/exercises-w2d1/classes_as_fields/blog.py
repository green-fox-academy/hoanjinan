class BlogPost():
    def __init__(self, author_name, title, text, publication_date):
        self.author_name = author_name
        self.title = title
        self.text = text
        self.publication_date = publication_date

blog1 = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04.")
blog2 = BlogPost("Tim Urban", "Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")
blog3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", "2017.03.28.")

print("\"" + blog1.title + "\" " + "titled by " + blog1.author_name + " posted at " + "\"" + blog1.publication_date + "\"\n\t" + blog1.text)
print("\"" + blog2.title + "\" " + "titled by " + blog2.author_name + " posted at " + "\"" + blog2.publication_date + "\"\n\t" + blog2.text)
print("\"" + blog3.title + "\" " + "titled by " + blog3.author_name + " posted at " + "\"" + blog3.publication_date + "\"\n\t" + blog3.text)

class Blog():
    def __init__(self):
        self.blog_list = []

    def add_post(self, post):
        self.blog_list.append(post)
        for i in range(len(self.blog_list)):
            print(self.blog_list[i].title)

    def delete_post(self, post_index):
        self.blog_list.pop(post_index)
        for i in range(len(self.blog_list)):
            print(self.blog_list[i].title)

    def update_post(self, post_index, post):
        self.blog_list[post_index] = post
        for i in range(len(self.blog_list)):
            print(self.blog_list[i].title)

blog = Blog()
blog.add_post(blog1)
blog.add_post(blog2)
blog.add_post(blog3)
blog.delete_post(0)
blog.update_post(1, blog1)
print()