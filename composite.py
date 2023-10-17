from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees) -> None:
        """
        Interface method
        """

    @abstractstaticmethod
    def display_department():
        """
        Interface method
        """


class Accounting(IDepartment):
    """
    Leaf Node
    """

    def __init__(self, employees) -> None:
        self.employees = employees

    def display_department(self):
        print(f"Accounting department: {self.employees}")


class Development(IDepartment):
    """
    Leaf Node
    """

    def __init__(self, employees) -> None:
        self.employees = employees

    def display_department(self):
        print(f"Development department: {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []

    def add_department(self, department):
        self.sub_departments.append(department)
        self.employees += department.employees

    def display_department(self):
        print("Parent Department")
        print(f"Parent Department base employees: {self.base_employees}")
        for dept in self.sub_departments:
            dept.display_department()
        print(f"Total number of employees: {self.employees}")


if __name__ == "__main__":
    dept1 = Accounting(100)
    dept2 = Development(200)
    parent_dept = ParentDepartment(25)
    parent_dept.add_department(dept1)
    parent_dept.add_department(dept2)
    parent_dept.display_department()
