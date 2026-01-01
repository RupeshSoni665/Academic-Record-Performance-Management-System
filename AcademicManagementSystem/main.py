from student import Student
from database import *
import sqlite3

def main():
    conn = connect_db()
    create_tables(conn)
    logic = Student()

    while True:
        print("\n1.Add Student")
        print("2.Add Subject marks")
        print("3.Semester Result")
        print("4.Complete Student Report")
        print("5.Reattempt Failed Subject")
        print("6.View Backlogs")
        print("7.Exit")

        ch = input("Choice: ")

        try:
            if ch == "1":
                r = int(input("Roll: "))
                n = input("Name: ")
                if student_exists(conn, r):
                    print("Student exists")
                else:
                    add_student(conn, r, n)
                    print("Student added")

            elif ch == "2":
                r = int(input("Roll: "))
                if not student_exists(conn, r):
                    print("Student not found")
                    continue

                sem = int(input("Semester: "))
                n = int(input("No. of subjects: "))

                for _ in range(n):
                    sub = input("Subject: ")
                    credits = int(input("Credits: "))
                    marks = int(input("Marks: "))

                    existing = subject_exists_latest(conn, r, sem, sub)
                    if existing and existing[0] != "Fail":
                        print("Subject already passed in this semester")
                        continue

                    grade, gp = logic.grade_and_points(marks)
                    res = logic.result_status(marks)

                    add_subject_attempt(conn, r, sem, sub, credits, marks, grade, gp, res)
                    print("Recorded")

            elif ch == "3":
                r = int(input("Roll: "))
                sem = int(input("Semester: "))

                print("\nSemester", sem)
                for s,a,c,m,g,res in get_subjects_for_semester(conn,r,sem):
                    print(f"{s} | Attempt:{a} | Marks:{m} | Grade:{g} | {res}")

                print("GPA:", calculate_gpa(conn,r,sem))

            elif ch == "4":
                r = int(input("Roll: "))
                print("\n==== COMPLETE REPORT ====")

                for sem in get_semesters(conn,r):
                    print("\nSemester", sem)
                    for s,a,c,m,g,res in get_subjects_for_semester(conn,r,sem):
                        print(f"{s} | Attempt:{a} | Marks:{m} | Grade:{g} | {res}")
                    print("Semester GPA:", calculate_gpa(conn,r,sem))

                print("\nOverall CGPA:", calculate_cgpa(conn,r))

            elif ch == "5":
                r = int(input("Roll: "))
                bl = get_backlogs(conn,r)
                if not bl:
                    print("No backlogs")
                    continue

                for i,(s,sem) in enumerate(bl,1):
                    print(f"{i}.{s} (Sem {sem})")

                sel = int(input("Select: "))
                s,sem = bl[sel-1]

                marks = int(input("New Marks: "))
                grade,gp = logic.grade_and_points(marks)
                res = logic.result_status(marks)

                add_subject_attempt(conn,r,sem,s,0,marks,grade,gp,res)
                print("Reattempt updated")

            elif ch == "6":
                for s,sem in get_backlogs(conn,int(input("Roll: "))):
                    print(s,"Semester",sem)

            elif ch == "7":
                break

        except ValueError:
            print("Invalid input")

    conn.close()

if __name__ == "__main__":
    main()
