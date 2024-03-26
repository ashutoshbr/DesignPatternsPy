class LivingBeings:
    def eat(self):
        print("Eating")


class FlyMixin:
    def fly(self):
        print("Flying")


class Horse(LivingBeings):
    pass


class Eagle(LivingBeings, FlyMixin):
    pass


e = Eagle()
e.fly()
