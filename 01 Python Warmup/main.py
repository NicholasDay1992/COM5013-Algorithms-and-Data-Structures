from student import Student
from module import Module

def main():
    nick = Student("nick", "21001234")
    sam = Student("Sam", "12345678")
    lucy = Student("Lucy", "87654321")
    
    students = [nick,sam,lucy]
    
    com5013 = Module("DSA","COM5013", students)
    #com5013.print_register()
    
    module_dictionary = {"com5013" : com5013 }
    module_dictionary["com5013"].print_register()
    
    nick.assign_mark("COM5013", 56)
    nick.assign_mark("COM4008", 67)
    
    nick.print_marks()
    
    
main()