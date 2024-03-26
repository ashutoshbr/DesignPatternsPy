## SOLID 🪨
1. Single Responsibility Principle\
   A class should have just one reason to change
2. Open/Closed Principle\
   Class should be open for extension but closed for modification
3. Liskov Principle\
   When extending a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the client code.
4. Interface Segregation Principle\
   Clients shouldn't be forced to depend on methods they do not use
5. Dependency Inversion Principle\
   High-level classes shouldn't depend on low-level classes. Both should depend on abstractions. Abstractions shouldn't depend on details. Details should depend on abstractions.

## Factory 🏭
A **creational design pattern** that provides an interface for creating objects in an abstract superclass.
## Singelton 🧑
Singleton is a **creational design pattern** that lets you ensure
that a class has only one instance, while providing a global
access point to this instance.
## Proxy 🥷
A **structural design pattern** that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
## Composite 🌳
Composite is a **structural design pattern** that lets you compose
objects into tree structures and then work with these
structures as if they were individual objects.


## Mixin
A class which has no purpose on its own. It needs to be mixed in with another class to add functionality to that class.
Multiple inheritance is used to achieve mixins in python.