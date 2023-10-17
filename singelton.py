from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def display_data():
        """
        Interface method
        """


class PersonSingelton(IPerson):
    __instance = None

    def __init__(self, name, age) -> None:
        if PersonSingelton.__instance is not None:
            raise Exception("Singelton cannot be instantiated!")
        else:
            self.name = name
            self.age = age
            PersonSingelton.__instance = self

    @staticmethod
    def get_instance():
        if PersonSingelton.__instance is None:
            PersonSingelton("Default Name", 0)
        return PersonSingelton.__instance

    @staticmethod
    def display_data():
        print(
            f"Name: {PersonSingelton.__instance.name}\tAge: {PersonSingelton.__instance.age}"
        )


if __name__ == "__main__":
    p1 = PersonSingelton("Foo Bar", 25)
    print(p1)
    p1.display_data()

    # Not Allowed!!
    # p2 = PersonSingelton("Egg Spam", 30)
    # p2.display_data()

    p2 = PersonSingelton.get_instance()
    print(p2)
    p2.display_data()
