class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def work(self):
        return 'I come to the office'


class Developer(Employee):
    def work(self):
        return super().work() + ' and start to coding'


class Recruiter(Employee):
    def work(self):
        return super().work() + ' and start to hiring'


employee1 = Developer('Polygraph Poligraphovych', 0)
employee2 = Developer('Philip Philipovich', 115)
employee3 = Developer('Ivan Arnoldovich', 65)
employee4 = Developer('Daria Petrovna', 65)
employee5 = Recruiter('Zinaida Prokofievna', 75)

employees = [employee1, employee2, employee3, employee4, employee5]
for employee in employees:
    print(f' {employee} makes ${employee.salary} a day')

print()
print(employee1.work())
print(employee5.work())

print()
print(employee2 > employee5)
print(employee2 < employee5)
print(employee1 != employee2)
print(employee1 == employee2)
print(employee3 == employee4)
