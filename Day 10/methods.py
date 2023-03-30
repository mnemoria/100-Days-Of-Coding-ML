class Student:
    program = "BS Computer Science"
    section = "3-1N"

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def attendance_status(self, attendance: str):
        self.attendance = attendance

    @classmethod
    def new_section(cls, section: str):
        cls.section = section

    @staticmethod
    def check_age(age):
        if age > 18:
            return 'Adult'
        else:
            return 'Not an adult'

if __name__ == "__main__":
    student1 = Student("Walker", "Matthew")

    # Modifying the object by adding attendance
    Student.attendance_status(student1, "Present")
    print(f"Name: {student1.last_name}, {student1.first_name}")
    print(f"Status: {student1.attendance}")

    # Changing the value of section using the class method 
    Student.new_section("4-1N")
    print(f"{student1.last_name}, {student1.first_name} from {student1.section}")

    # Calling a static method using the class and class instance 
    print(Student.check_age(5))
    print(student1.check_age(20))