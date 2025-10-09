from student import Student 

class Module:
    def __init__(self, name, code, register):
        self.name = name
        self.code = code
        self.register = register
        
    def print_register(self):
        for student in self.register:
            student.print_student()