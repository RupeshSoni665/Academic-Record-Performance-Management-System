# Academic Record & Performance Management System

## Overview
The **Academic Record & Performance Management System** is a console-based application developed using **Python and SQLite** that models real-world university academic evaluation workflows.  
The system enables structured management of student records, subject-wise grades, credit-based evaluation, semester-wise GPA, overall CGPA, backlog tracking, and subject reattempt handling.

This project focuses on core computer science fundamentals such as **object-oriented programming**, **database design**, and **data integrity**, without using external frameworks or graphical interfaces.

---

## Problem Statement
Manual handling of academic records often leads to inconsistent grade calculations, difficulty tracking semester-wise performance, improper backlog handling, and lack of structured academic history.  
This project aims to design a robust academic management system that closely reflects how universities evaluate student performance while ensuring correctness and data consistency.

---

## Technologies Used
- Python  
- SQLite  
- SQL  
- Object-Oriented Programming (OOPS)  
- DBMS Concepts  

---

## Key Features

### Student Management
- Add and manage student records using unique roll numbers  
- Prevent duplicate student entries  

### Subject & Semester Management
- Add subjects semester-wise with credits and marks  
- Assign grades and pass/fail status  
- Enforce strict rules to prevent duplicate subjects in the same semester  

### Credit-Based Evaluation
- Semester-wise GPA calculation using weighted grade points  
- Overall CGPA calculation across all semesters  
- Only the latest valid (passed) attempt contributes to GPA and CGPA  

### Backlog Tracking
- Automatically mark failed subjects as active backlogs  
- Maintain backlog status until the subject is cleared  

### Subject Reattempt Workflow
- Allow reattempts only for failed (backlog) subjects  
- Preserve complete attempt history for each subject  
- Update academic performance using only the latest attempt  
- Automatically clear backlog upon successful reattempt  

### Complete Student Academic Report
- Displays all semesters  
- Shows subject-wise marks, grades, and attempt history  
- Displays semester-wise GPA and final overall CGPA  
- Mirrors a real university transcript structure  

### Error Handling & Validation
- Prevents invalid inputs (marks, credits, duplicates)  
- Ensures database integrity and consistency  

---

## Project Structure

AcademicManagementSystem/
│
├── main.py # Application entry point and menu handling
├── student.py # Academic grading and result logic
├── database.py # Database operations, GPA/CGPA logic
├── students.db # SQLite database (auto-generated)
├── activity.log # Optional activity logging
└── README.md


---

## Database Design

### students
| Column  | Description |
|--------|-------------|
| roll_no | Unique student identifier |
| name | Student name |

### subjects
| Column | Description |
|--------|------------|
| roll_no | Student reference |
| semester | Semester number |
| subject | Subject name |
| attempt_no | Attempt count |
| credits | Subject credits |
| marks | Marks obtained |
| grade | Assigned grade |
| grade_point | Grade point |
| result | Pass / Fail |
| is_latest | Latest valid attempt flag |

### backlogs
| Column | Description |
|--------|------------|
| roll_no | Student reference |
| semester | Semester of failure |
| subject | Failed subject |
| status | ACTIVE / CLEARED |

---

## GPA & CGPA Calculation Logic

### Grade to Grade Point Mapping
| Grade | Grade Point |
|------|-------------|
| A | 10 |
| B | 8 |
| C | 6 |
| Fail | 0 |

### Semester GPA Formula
