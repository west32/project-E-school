import csv
import dataclasses
import json

from estudent import conversion
from estudent.student import Student


# def load_students_from_csv(file_name="students.csv"):
#     with open(file_name,newline="") as student_file:
#         csv_reader = csv.reader(student_file)
#         students = []
#         for row_index,row in enumerate(csv_reader):
#             if row_index == 0:
#                 continue
#             grades_values = [int(value) for value in row[3].split(",")]
#             # student = Student(first_name=row[0], last_name=row[1])
#             # students.append(student)
#             # for grades_value in grades_values:
#             #     student.add_final_grade(grades_value)
#             # student.promoted = str_to_bool(row[2])
#
#             students.append(
#                 Student.from_csv(
#                     first_name=row[0],
#                     last_name=row[1],
#                     promoted=str_to_bool(row[2]),
#                     grades_values=grades_values
#                 )
#             )
#     return students


class StudentCsvSerializer:

    def __init__(self, file_name="students.csv"):
        self.file_name = file_name
        self.cached_students = None
        self.cached_headers = None

    def save_students(self, students):
        with open(self.file_name, mode="w", newline="", encoding="utf=8") as student_file:
            csv_writer = csv.writer(student_file)
            csv_writer.writerow(["first_name", "last_name", "promoted", "final_grades"])
            for student in students:
                serialized_final_grades = ",".join([str(grade.value) for grade in student._final_grades])
                csv_writer.writerow([student.first_name, student.last_name, student.promoted, serialized_final_grades])

    def load_students(self, use_cache=True):
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, newline="", encoding="utf=8") as students_file:
                csv_reader = csv.reader(students_file)
                self.cached_headers = next(csv_reader)
                self.cached_students = [
                    Student.from_csv(
                        first_name=row[0],
                        last_name=row[1],
                        promoted=conversion.str_to_bool(row[2]),
                        grades_values=[int(value) for value in row[3].split(",")]
                    )
                    for row in csv_reader
                ]
                return self.cached_students

    def load_headers(self, use_cache=True):
        if use_cache and self.cached_headers:
            return self.cached_headers
        else:
            with open(self.file_name, newline="", encoding="utf=8") as students_file:
                csv_reader = csv.reader(students_file)
                self.cached_headers = next(csv_reader)
            return self.cached_headers

    class StudentCsvDictSerializer:
        def __init__(self, file_name="students.csv"):
            self.file_name = file_name
            self.cached_students = None
            self.cached_headers = None


class StudentCVSDictSerializer:
    def __init__(self, file_name="students.csv"):
        self.file_name = file_name
        self.cached_students = None
        self.cahced_headers = None

    def save_students(self, students):
        with open(self.file_name, mode="w", newline="", encoding="utf=8") as students_file:
            headers = ["first_name", "last_name", "promoted", "final_grades"]
            writer = csv.DictWriter(students_file, fieldnames=headers)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "promoted": student.promoted,
                    "final_grades": ",".join([str(grade.value) for grade in student._final_grades]),
                })

    def load_students(self, use_cache=True):
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, newline="", encoding="utf=8") as students_file:
                csv_reader = csv.DictReader(students_file)
                self.cached_headers = csv_reader.fieldnames
                self.cached_students = [
                    Student.from_csv(
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        promoted=conversion.str_to_bool(row["promoted"]),
                        grades_values=[int(value) for value in row["final_grades"].split(",")]
                    )
                    for row in csv_reader
                ]
                return self.cached_students

    def load_headers(self, use_cache=True):
        if use_cache and self.cahced_headers:
            return self.cahced_headers
        else:
            with open(self.file_name, newline="") as students_file:
                csv_reader = csv.DictReader(students_file)
                self.cahced_headers = csv_reader.fieldnames
            return self.cahced_headers


class StudentsJSONSerializer:
    def __init__(self, file_name="students.json"):
        self.file_name = file_name
        self.cached_students = None

    def save_students(self, students):
        students_data = {
            "students": [
                {
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "promoted": student.promoted,
                    "final_grades": [dataclasses.asdict(grade) for grade in student.final_grades]
                }
                for student in students
            ]
        }
        with open(self.file_name, mode="w", encoding="utf-8") as students_file:
            json.dump(students_data, students_file, indent=4)

    def load_students(self, use_cache=True):
        if use_cache and self.cached_students:
            return self.cached_students
        else:
            with open(self.file_name, mode="r") as students_file:
                students_data = json.load(students_file).get("students", [])

            self.cached_students = [
                Student.from_json(**student_data, ) for student_data in students_data
            ]
            return self.cached_students
