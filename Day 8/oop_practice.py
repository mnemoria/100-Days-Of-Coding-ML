import csv, os

class Student:
    
    student_list = []

    def __init__(self, first_name: str, last_name: str, age: int):
        # Run validations to the received arguments
        assert age > 0

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        Student.student_list.append(self)
    
    def __repr__(self):
        return f"Student('{self.last_name}, {self.first_name}': {self.age})"

    @classmethod # Unique to the class, usually used to manipulate different structures of data to instantiate object, like in this case with a csv file
    def instantiate_from_csv(cls):
        csv_path = os.path.abspath("Day 8\\oop_practice.csv")
        
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            student_list = list(reader)

        for student in student_list:
            Student(
                first_name=student.get('first_name'),
                last_name=student.get('last_name'),
                age=int(student.get('age'))
            )

    @staticmethod #Not inherently unique to the class but still related
    def is_integer(num):
        if isinstance(num, float):
            return num.is_intger()
        elif isinstance(num, int):
            return True
        else:
            return False

if __name__ == "__main__":
    #student1 = Student("Athena", "White", 20)
    #student2 = Student("Sara", "Mendez", 20)
    #student3 = Student("Alex", "Doe", 20)
    #student4 = Student("Sean", "Walker", 20)
    #student5 = Student("Tony", "Montana", 20)

    #for student in Student.student_list:
    #    print(f"{student.first_name} {student.last_name}")

    Student.instantiate_from_csv()
    print(Student.student_list)