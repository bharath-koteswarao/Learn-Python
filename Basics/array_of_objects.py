class Student:
    def __init__(self, name, fname, phn):
        self.name = name
        self.father_name = fname
        self.phone = phn

    def show(self):
        print(self.name)
        print(self.father_name)
        print(self.phone)


def main():
    size = int(input("Enter the size of array : "))
    student_array = []
    for i in range(0, size):
        name = input("Enter the name of Student : ")
        father_name = input("Enter name of father : ")
        phone = input("Enter your phone number : ")
        student_array.append(Student(name, father_name, phone))

    print()

    for student in student_array:
        print(student.name + " " + student.phone + " " + student.father_name)


main()
