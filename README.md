# Academic Record & Performance Management System

## Overview
The **Academic Record & Performance Management System** is a **console-based application** developed using **Python and SQLite** that models real-world university academic evaluation workflows.  
It manages student records, subject-wise grades, credit-based evaluation, semester-wise GPA, overall CGPA, backlog tracking, and controlled subject reattempts.

The project focuses on **core computer science fundamentals**—object-oriented programming, database design, and data integrity—without using external frameworks or a GUI.

---

## Problem Statement
Manual academic record management often leads to:
- inconsistent grade calculations
- difficulty tracking semester-wise performance
- improper handling of backlogs and reattempts
- loss of academic history

This project addresses these issues by providing a **structured, normalized, and rule-driven system** that mirrors how universities evaluate student performance.

---

## Technologies Used
- **Python**
- **SQLite**
- **SQL**
- **Object-Oriented Programming (OOPS)**
- **DBMS Concepts**

---

## Key Features

### Student Management
- Add and manage students using unique roll numbers
- Prevent duplicate student entries

### Subject & Semester Management
- Add subjects semester-wise with credits and marks
- Assign grades and pass/fail status
- Prevent duplicate subject entries in the same semester unless clearing a backlog

### Credit-Based Evaluation
- **Semester-wise GPA** calculation using weighted grade points
- **Overall CGPA** calculation across all semesters
- Only the **latest valid (passed) attempt** contributes to GPA/CGPA

### Backlog Tracking
- Automatically mark failed subjects as **ACTIVE backlogs**
- Maintain backlog status until successfully cleared

### Subject Reattempt Workflow
- Allow reattempts **only for failed (backlog) subjects**
- Preserve **complete attempt history** for each subject
- Update academic performance using **only the latest attempt**
- Automatically clear backlog upon passing

### Complete Student Academic Report
- Displays all semesters
- Shows subject-wise marks, grades, and attempt history
- Displays semester-wise GPA and final overall CGPA
- Closely mirrors a real university transcript

### Error Handling & Validation
- Prevents invalid inputs (marks, credits, duplicates)
- Ensures database integrity and consistency

---

## Project Structure
```bash
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

### Grade → Grade Point Mapping
| Grade | Grade Point |
|------|-------------|
| A | 10 |
| B | 8 |
| C | 6 |
| Fail | 0 |

### Semester GPA Formula
GPA = Σ(grade_point × credits) / Σ(credits)


### Overall CGPA Formula
CGPA = Σ(all semesters grade_point × credits) / Σ(all semesters credits)


**Notes**
- Only **latest passed attempts** are considered
- Failed attempts do **not** affect GPA or CGPA

---

## How to Run the Project

### Prerequisites
- Python 3.x installed
- No external libraries required

### Steps
1. Clone the repository
2. Navigate to the project directory
3. (Optional) Delete `students.db` if re-running after schema changes
4. Run the application:
python main.py
---

## Sample Workflow
1. Add a student
2. Add subjects with credits and marks
3. View semester-wise results and GPA
4. Check backlogs for failed subjects
5. Reattempt failed subjects
6. View complete academic report with CGPA

---

## Design Principles Followed
- Separation of concerns (logic, database, interface)
- Normalized relational database schema
- Data integrity through constraints and validation
- Realistic academic workflow modeling
- Maintainable and extensible architecture

---

## Future Enhancements
- GUI integration (Tkinter)
- Transcript export (CSV/PDF)
- Semester credit limits
- Ranking and topper analysis

---

