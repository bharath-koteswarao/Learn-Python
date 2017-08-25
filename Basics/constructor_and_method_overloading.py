class Book:
    """
    Python doesn't support multiple constructors
    like java. We have to give a default value to a parameter
    If this parameter is not passed then that value would be taken

    However method overloading can be done as usual. It is supported
    """

    def __init__(self, name="default", author="default", date="default"):
        if name is "default" and author is "default" and date is "default":
            print("Default constructor is called")
            del name
            del author
            del date
        else:
            print("Overloaded constructor is called")

    def edit_book(self, name, author):
        self.name = name
        self.author = author

    def edit_book(self, name):
        self.name = name
        print("This is method overloading.")
        """Above two methods have same name but have different arguments"""


def main():
    book1 = Book()
    book2 = Book("bk's book", "bk")
    book3 = Book("bharath's book", "bharath", "some date")
    book1.edit_book("bk book")


main()
