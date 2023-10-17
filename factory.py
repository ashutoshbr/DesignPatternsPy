# Decide during run time what type of instance do you want
# Person class could either be a Teacher or a Student
from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """
        Interface method
        """


class Teacher(IPerson):
    def person_method(self):
        print("Teacher")


class Student(IPerson):
    def person_method(self):
        print("Student")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Teacher":
            return Teacher()
        elif person_type == "Student":
            return Student()
        else:
            print("Invalid Type!")
            return -1


if __name__ == "__main__":
    choice = input("Type: ")
    person = PersonFactory.build_person(choice)
    person.person_method()
