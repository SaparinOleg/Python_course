from calendar import monthrange, weekday
from datetime import date

TODAY = date.today()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary

    def __ne__(self, other):
        if isinstance(other, Employee):
            return self.salary != other.salary

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary

    def __ge__(self, other):
        if isinstance(other, Employee):
            return self.salary >= other.salary

    def __le__(self, other):
        if isinstance(other, Employee):
            return self.salary <= other.salary

    @staticmethod
    def work():
        return 'I come to the office'

    def check_salary(self, days=0):
        if not days:
            return sum(self.salary for day in range(1, TODAY.day + 1) if weekday(TODAY.year, TODAY.month, day) < 5)
        return self.salary * days


class Developer(Employee):
    def __init__(self, *args, tech_stack: list):
        super().__init__(*args)
        self.tech_stack = tech_stack

    def __add__(self, other):
        if isinstance(other, Developer):
            name = f'{self.name} {other.name}'
            salary = max(self.salary, other.salary)
            tech_stack = set(self.tech_stack + other.tech_stack)
            return Developer(name, salary, tech_stack=list(tech_stack))

    def __eq__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) != len(other.tech_stack)

    def __gt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) > len(other.tech_stack)

    def __le__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) < len(other.tech_stack)

    def work(self):
        return super().work() + ' and start to coding'


class Recruiter(Employee):
    def work(self):
        return super().work() + ' and start to hiring'


employee1 = Developer('Polygraph Poligraphovych', 0, tech_stack=['Turbo Pascal'])
employee2 = Developer('Philip Philipovich', 115, tech_stack=['C', 'C++', 'C#', 'Java', 'Python'])
employee3 = Developer('Ivan Arnoldovich', 65, tech_stack=['C', 'C++'])
employee4 = Developer('Daria Petrovna', 65, tech_stack=['C', 'C++'])
employee5 = Recruiter('Zinaida Prokofievna', 75)

employees = [employee1, employee2, employee3, employee4, employee5]
for employee in employees:
    print(f' {employee} makes ${employee.salary} a day')

print()
print(employee2.check_salary(55))
print(employee2.check_salary())

print()
print(employee2.tech_stack)

print()
multi_employee = employee3 + employee4
print(multi_employee.name)
print(multi_employee.salary)
print(multi_employee.tech_stack)

print()
print(employee1 >= employee2)
print(employee1 < employee2)
print(employee1 == employee2)
print(employee1 != employee2)