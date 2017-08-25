class First:
    a = 10
    b = 20


class Second(First):  # Single inheritance
    def __init__(self):
        print(self.a, self.b)


second = Second()


class Third:
    x = "Third class"


class Fourth(First, Third):  # Multiple inheritance. This is not supported in java
    def __init__(self):
        print(self.x, self.a)


fourth = Fourth()
