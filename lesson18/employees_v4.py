import csv
import traceback
import urllib.request
from calendar import weekday
from datetime import date, datetime
from exceptions import EmailAlreadyExistsException
from exceptions import EmailValidationException
import ssl

TODAY = date.today()


class Employee:
    email: str

    def __init__(self, name, salary, email: str):
        self.name = name
        self.salary = salary
        self.set_email(email)

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
            raise EmailValidationException
        with open('emails.csv', 'r') as file:
            if email in file.read():
                raise EmailAlreadyExistsException
        return True

    def set_email(self, email):
        try:
            self.validate_email(email)
            self.email = email
            self.save_email(email)
        except EmailValidationException:
            Logger.log_stack_trace('Invalid address.')
        except EmailAlreadyExistsException:
            Logger.log_stack_trace('Email already exists.')


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


class Logger:

    @classmethod
    def log(cls, msg: str):
        with open('logs.txt', 'a') as logs:
            logs.write(f'{datetime.now()} \n {msg} \n')
        print(msg)

    @classmethod
    def log_stack_trace(cls, msg: str = ''):
        msg = f'{msg} \n {traceback.format_exc()} \n'
        cls.log(msg)


class Candidate:
    def __init__(self, first_name: str, last_name: str,
                 email: str,
                 tech_stack: list, main_skill: str, main_skill_grade: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f'{self.full_name}, {self.email}, {self.tech_stack}, {self.main_skill}: {self.main_skill_grade}'

    def __repr__(self):
        return str(self)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, path: str):
        if path.startswith('http'):
            # context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(path, context=context) as url_file:
                file = url_file.read().decode('utf-8').split('\n')
                return cls.__parse_candidates(line for line in file if line)
        with open(path, 'r') as file:
            return cls.__parse_candidates(file)

    @classmethod
    def __parse_candidates(cls, file):
        candidates = csv.reader(file)
        next(candidates)
        result = []
        for line in candidates:
            full_name, email, technologies, main_skill, main_skill_grade = line
            first_name, last_name = full_name.split()
            technologies = technologies.split('|')
            result.append(Candidate(first_name, last_name, email, technologies, main_skill, main_skill_grade))
        return result


employee1 = Developer('Polygraph Poligraphovych', 0, 'Sharikov@gmailcom', tech_stack=['Turbo Pascal'])
employee2 = Developer('Philip Philipovich', 115, 'PP@gmail.com', tech_stack=['C', 'C++', 'C#', 'Java', 'Python'])
employee3 = Developer('Ivan Arnoldovich', 65, 'VanyaA@i.ua', tech_stack=['C', 'C++'])
employee4 = Developer('Daria Petrovna', 65, 'kukolkaoutlook.com', tech_stack=['C', 'C++'])
employee5 = Recruiter('Zinaida Prokofievna', 75, 'Zina Pro@gmail.com')


url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'

print('Candidates from url:')
for candidate in Candidate.generate_candidates(url):
    print(candidate)

print('\nCandidates from local file:')
for candidate in Candidate.generate_candidates('candidates.csv'):
    print(candidate)
