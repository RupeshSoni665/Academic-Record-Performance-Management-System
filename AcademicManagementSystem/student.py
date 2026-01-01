# student.py
# Academic grading logic

class Student:

    def grade_and_points(self, marks):
        if marks >= 85:
            return "A", 10
        elif marks >= 70:
            return "B", 8
        elif marks >= 40:
            return "C", 6
        else:
            return "Fail", 0

    def result_status(self, marks):
        return "Pass" if marks >= 40 else "Fail"
