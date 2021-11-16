class Department:
    MAX_STUDENTS = 20

    def __init__(self,letter_identifier, year):
        self.year = year
        self.letter_identifier = letter_identifier
        self.students = []

    def assign_student(self,student):
        if len(self.students) < Department.MAX_STUDENTS:
            self.students.append(student)
            return True
        else:
            print("Nie miejsca ziomuś")
            return False

    def __str__(self):
        return f"Klasa {self.year}{self.letter_identifier}, {len(self.students)}"

class BiochemDepartment(Department):
    MIN_BIO_GRADE = 3
    MIN_CHEM_GRADE = 3

    def assign_student(self,student):
        bio_grade = student.final_grade_from_subject("Biologia")
        chem_grade = student.final_grade_from_subject("Chemia")
        if bio_grade.value >= self.MIN_BIO_GRADE and chem_grade.value >= self.MIN_CHEM_GRADE:
           return super().assign_student(student)
        else:
            print("za słabe oceny ")
            return False



class MathPhysicDepartment(Department):
    MIN_MATH_GRADE = 3
    MIN_PHYS_GRADE = 3

    def assign_student(self,student):

        math_grade = student.final_grade_from_subject("Matematyka")
        phys_grade = student.final_grade_from_subject("Fizyka")
        if math_grade.value >= self.MIN_MATH_GRADE and phys_grade.value >= self.MIN_PHYS_GRADE:
            return super().assign_student(student)
        else:
            print("za slabe oceny")
            return False
