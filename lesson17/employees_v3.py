import csv
import traceback
from calendar import weekday
from datetime import date, datetime
from exceptions import EmailAlreadyExistsException
from exceptions import EmailValidationError

TODAY = date.today()


class Employee:

    def __init__(self, name, salary, email: str):
        self.name = name
        self.salary = salary
        try:
            self.validate_email(email)
            self.email = email
            self.save_email(email)
        except EmailValidationError:
            print('Invalid address.')
            with open('logs.txt', 'a') as logs:
                logs.write(f'{datetime.now()} \n {traceback.format_exc()} \n\n')
        except EmailAlreadyExistsException:
            print('Email already exists.')
            with open('logs.txt', 'a') as logs:
                logs.write(f'{datetime.now()} \n {traceback.format_exc()} \n\n')

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

    def check_salary(self, days=0):
        if not days:
            return sum(self.salary for day in range(1, TODAY.day + 1) if weekday(TODAY.year, TODAY.month, day) < 5)
        return self.salary * days

    @staticmethod
    def work():
        return 'I come to the office'

    @staticmethod
    def save_email(email):
        with open('emails.csv', 'a', newline='\n') as file:
            csv.writer(file).writerow([email])

    @staticmethod
    def validate_email(email):
        if '@' not in email or '.' not in email or ' ' in email:
            raise EmailValidationError
        with open('emails.csv', 'r') as file:
            if email in file.read():
                raise EmailAlreadyExistsException
        return True


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
    def work(self, *args):
        return super().work() + ' and start to hiring'


employee1 = Developer('Polygraph Poligraphovych', 0, 'Sharikov@gmailcom', tech_stack=['Turbo Pascal'])
employee2 = Developer('Philip Philipovich', 115, 'PP@gmail.com', tech_stack=['C', 'C++', 'C#', 'Java', 'Python'])
employee3 = Developer('Ivan Arnoldovich', 65, 'VanyaA@i.ua', tech_stack=['C', 'C++'])
employee4 = Developer('Daria Petrovna', 65, 'kukolkaoutlook.com', tech_stack=['C', 'C++'])
employee5 = Recruiter('Zinaida Prokofievna', 75, 'Zina Pro@gmail.com')
