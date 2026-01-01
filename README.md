📘 Academic Record & Performance Management System
📌 Overview

The Academic Record & Performance Management System is a console-based application developed using Python and SQLite that models real-world university academic evaluation workflows.
The system enables structured management of student records, subject-wise grades, credit-based evaluation, semester-wise GPA, overall CGPA, backlog tracking, and subject reattempt handling.

This project focuses on core computer science fundamentals such as object-oriented programming, database design, and data integrity, without relying on external frameworks or GUIs.

🎯 Problem Statement

Manual handling of academic records often leads to:

inconsistent grade calculations

difficulty tracking semester-wise performance

improper handling of backlogs and subject reattempts

lack of structured academic history

The objective of this project is to design a robust, structured academic management system that closely reflects how universities evaluate student performance while ensuring data consistency and correctness.

🛠️ Technologies Used

Python – core programming language

SQLite – lightweight relational database

SQL – data storage and retrieval

Object-Oriented Programming (OOPS) – separation of logic and responsibilities

DBMS Concepts – normalization, constraints, and relational design

✨ Key Features
👨‍🎓 Student Management

Add and manage student records using unique roll numbers

Prevent duplicate student entries

📚 Subject & Semester Management

Add subjects semester-wise

Assign credits, marks, grades, and pass/fail status

Enforce strict validation to prevent duplicate subjects in the same semester

📊 Credit-Based Evaluation

Semester-wise GPA calculation using weighted grade points

Overall CGPA calculation across all semesters

Only valid (latest passed) attempts contribute to GPA/CGPA

🚨 Backlog Tracking

Automatically mark failed subjects as ACTIVE backlogs

Maintain backlog status until successfully cleared

🔁 Subject Reattempt Workflow

Allow reattempts only for failed (backlog) subjects

Preserve complete attempt history for each subject

Update performance using only the latest valid attempt

Automatically clear backlog upon passing

📄 Complete Student Academic Report

Displays:

all semesters

subject-wise marks, grades, and attempts

semester-wise GPA

final overall CGPA

Mirrors a real university transcript structure

🧠 Error Handling & Validation

Prevents invalid inputs (marks, credits, duplicates)

Ensures database integrity and consistent academic records

🗂️ Project Structure
AcademicManagementSystem/
│
├── main.py        # Application entry point and menu handling
├── student.py     # Academic grading and result logic
├── database.py    # Database operations, GPA/CGPA logic
├── students.db    # SQLite database (auto-generated)
├── activity.log   # Optional activity logging
└── README.md

🧩 Database Design
students
Column	Description
roll_no	Unique student identifier
name	Student name
subjects
Column	Description
roll_no	Student reference
semester	Semester number
subject	Subject name
attempt_no	Attempt count
credits	Subject credits
marks	Marks obtained
grade	Assigned grade
grade_point	Grade point
result	Pass / Fail
is_latest	Latest valid attempt flag
backlogs
Column	Description
roll_no	Student reference
semester	Semester of failure
subject	Failed subject
status	ACTIVE / CLEARED
📐 GPA & CGPA Calculation Logic
🎓 Grade → Grade Point Mapping
Grade	Grade Point
A	10
B	8
C	6
Fail	0
📊 Semester GPA Formula
GPA = Σ(grade_point × credits) / Σ(credits)

📘 Overall CGPA Formula
CGPA = Σ(all semesters grade_point × credits) / Σ(all semesters credits)


✔ Only latest passed attempts are considered
✔ Failed attempts do not affect GPA/CGPA

▶️ How to Run the Project
Step 1: Prerequisites

Python 3.x installed

No external libraries required

Step 2: Setup

Clone the repository

Navigate to the project directory

(Optional) Delete students.db if re-running after schema changes

Step 3: Run
python main.py

🧪 Sample Workflow

Add a student

Add subjects with credits and marks

View semester-wise results and GPA

Check backlogs for failed subjects

Reattempt failed subjects

View complete academic report with CGPA

🧠 Design Principles Followed

Separation of concerns (logic, database, interface)

Normalized relational schema

Data integrity through constraints and validation

Realistic academic workflow modeling

Maintainable and extensible architecture

🚀 Future Enhancements

GUI integration (Tkinter)

Transcript export (CSV/PDF)

Semester credit limits

Ranking and topper analysis

📌 Conclusion

This project demonstrates a strong understanding of Python programming, DBMS fundamentals, and real-world academic evaluation logic.
It is designed to be simple, accurate, and extensible, making it suitable for learning, interviews, and further enhancements.
