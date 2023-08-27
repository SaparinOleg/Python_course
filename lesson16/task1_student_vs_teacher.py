class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return self.first_name, self.last_name


class Student(Person):
    def __init__(self, *args, student_id):
        super().__init__(*args)
        self.student_id = student_id

    def get_full_name(self):
        return self.student_id, f'{self.first_name} {self.last_name}'


class Teacher(Person):
    def __init__(self, *args, employee_id):
        super().__init__(*args)
        self.employee_id = employee_id

    def get_full_name(self):
        return self.employee_id, f'{self.first_name} {self.last_name}'

    def teach(self):
        print(f'The teacher {self.first_name} {self.last_name} is in class now')


teacher1 = Teacher('Roman', 'Smyk', 24, employee_id=1)
student1 = Student('Dmitro', 'Kishinsky', 25, student_id=1)
student2 = Student('Oleh', 'Saparin', 32, student_id=2)


print(teacher1.get_full_name())
print(student1.get_full_name())
print(student2.get_full_name())
teacher1.teach()
