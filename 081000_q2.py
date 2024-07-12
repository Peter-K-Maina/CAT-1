class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def addGrade(self, subject, grade):
        self.grades[subject] = grade

    def get_avGrade(self):
        if not self.grades:
            return 00
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name} 
                 Grade: {self.grades}"
    
class Classroom:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def displayStudents(self):
        if not self.students:
            print("No Students listed.")
        else:
            for student in self.students:
                print(f"\nName: {student.name} 
                        \nGrade: {student.grades}")

    def get_StdAvGrade(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.get_avGrade()
        return None

    def get_SubjAv(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return None
        return total / count
    
def main():

    classroom = Classroom()
    
    student1 = Student("Peter")
    student1.addGrade("IS 1", 78)
    student1.addGrade("French", 84)
    classroom.addStudent(student1)
    
    student2 = Student("Luke")
    student2.addGrade("IS 1", 75)
    student2.addGrade("French", 80)
    classroom.addStudent(student2)
    
    # Display Students
    print("Students")
    classroom.displayStudents()
    
    # Student Average
    studentName = "Peter"
    averageGrade = classroom.get_StdAvGrade(studentName)
    if averageGrade is not None:
        print(f"\n{studentName} Av Grade: {averageGrade}")
    else:
        print(f"\nStudent '{studentName}' not found.")
    
    # Subject Average per class
    subject = "IS 1"
    classAv = classroom.get_SubjAv(subject)
    if classAv is not None:
        print(f"\nClass {subject} Average Score : {classAv}")
    else:
        print(f"\n '{subject}' has no Grades yet.")
    
if __name__ == "__main__":
    main()