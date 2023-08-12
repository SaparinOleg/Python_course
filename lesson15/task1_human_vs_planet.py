from datetime import datetime


class LogMixin:
    def __new__(cls, *args):
        print(f'new {cls.__name__} was created')
        return super().__new__(cls)


class Human(LogMixin):

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.name

    def get_age(self):
        return datetime.now().year - self.date_of_birth


class Planet(LogMixin):
    def __init__(self, name):
        self.name = name
        self.humans = []

    def __str__(self):
        return self.name

    def add_human(self, new_humans):
        self.humans.extend(new_humans)

    def get_count(self):
        return len(self.humans)

    def __gt__(self, other):
        return self.get_count() > other.get_count()

    def __lt__(self, other):
        return self.get_count() < other.get_count()

    def __ne__(self, other):
        return self.get_count() != other.get_count()

    def __eq__(self, other):
        return self.get_count() == other.get_count()


planet1 = Planet('Earth')
planet2 = Planet('Mars')
h1 = Human('Ihor', 1989)
h2 = Human('Jack', 2000)
h3 = Human('Olesya', 1997)
h4 = Human('Oleh', 1991)
h5 = Human('Mark Watney', 1994)
planet1.add_human([h1, h2, h3, h4])
planet2.add_human([h5])

print()
print(planet1, ':', sep='', end=' ')
for i in range(len(planet1.humans)):
    print(planet1.humans[i], end=", ") if i < len(planet1.humans)-1 else print(planet1.humans[i])

print()
print(planet2, ':', sep='')
print(planet2.humans[0], ', ', planet2.humans[0].get_age(), ' yo', sep='')

print()
print(planet1.humans[3], planet1.humans[3].get_age())
print(h1.name, end=" ")
print(h1.get_age())

print()
print(planet1.__gt__(planet2))
print(planet1 > planet2)
print(planet1.__lt__(planet2))
print(planet1 < planet2)
print(planet1.__ne__(planet2))
print(planet1 != planet2)
print(planet1.__eq__(planet2))
print(planet1 == planet2)
