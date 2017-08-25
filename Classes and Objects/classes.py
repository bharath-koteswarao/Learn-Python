# Example of a class with a simple constructor


class Sample:
    a = 10
    b = 20

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a ** b)

    def show_elements(self):
        print("a is {} and b is {}".format(self.a, self.b))


sample = Sample(10, 2)
sample.show_elements()
