from person import Person

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.marks = {}
    
    def print_student(self):
        print(" " + super().get_name() + " " + super().get_id())
    
    def assign_mark(self, module, mark):
        self.marks[module] = mark
    
    def print_marks(self):
        print(self.marks)
        