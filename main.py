class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(Student(name, grade))
        print(f"Student {name} added successfully")

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} removed successfully")
                return
        print(f"Student {name} not found")

    def calculate_average_grade(self):
        total_grade = sum(student.grade for student in self.students)
        average_grade = total_grade / len(self.students)
        return average_grade

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Grade: {student.grade}")

    def update_grade(self, name, new_grade):
        for student in self.students:
            if student.name == name:
                student.grade = new_grade
                print(f"Grade of student {name} updated successfully")
                return
        print(f"Student {name} not found")

def main():
    system = StudentManagementSystem()
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Calculate average grade")
        print("4. Display students")
        print("5. Update grade")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            system.add_student(name, grade)
        elif choice == "2":
            name = input("Enter student name: ")
            system.remove_student(name)
        elif choice == "3":
            average_grade = system.calculate_average_grade()
            print(f"Average grade: {average_grade}")
        elif choice == "4":
            system.display_students()
        elif choice == "5":
            name = input("Enter student name: ")
            new_grade = float(input("Enter new grade: "))
            system.update_grade(name, new_grade)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()