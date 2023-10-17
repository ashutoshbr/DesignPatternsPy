# can be used to pre/post pend something
from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """
        Interface method
        """


class Person(IPerson):
    def person_method(self):
        print("Person")


class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()

    def person_method(self):
        print("Proxy Person")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
