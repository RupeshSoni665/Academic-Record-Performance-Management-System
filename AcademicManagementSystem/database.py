import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_tables(conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no INTEGER,
            semester INTEGER,
            subject TEXT,
            attempt_no INTEGER,
            credits INTEGER,
            marks INTEGER,
            grade TEXT,
            grade_point INTEGER,
            result TEXT,
            is_latest INTEGER,
            UNIQUE (roll_no, semester, subject, attempt_no)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS backlogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no INTEGER,
            semester INTEGER,
            subject TEXT,
            status TEXT
        )
    """)

    conn.commit()

# ---------- STUDENT ----------
def student_exists(conn, roll):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM students WHERE roll_no=?", (roll,))
    return cur.fetchone() is not None

def add_student(conn, roll, name):
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (?,?)", (roll, name))
    conn.commit()

# ---------- SUBJECT ----------
def subject_exists_latest(conn, roll, sem, subject):
    cur = conn.cursor()
    cur.execute("""
        SELECT result FROM subjects
        WHERE roll_no=? AND semester=? AND subject=? AND is_latest=1
    """, (roll, sem, subject))
    return cur.fetchone()

def get_next_attempt(conn, roll, sem, subject):
    cur = conn.cursor()
    cur.execute("""
        SELECT MAX(attempt_no) FROM subjects
        WHERE roll_no=? AND semester=? AND subject=?
    """, (roll, sem, subject))
    val = cur.fetchone()[0]
    return 1 if val is None else val + 1

def mark_old_attempt_not_latest(conn, roll, sem, subject):
    cur = conn.cursor()
    cur.execute("""
        UPDATE subjects SET is_latest=0
        WHERE roll_no=? AND semester=? AND subject=? AND is_latest=1
    """, (roll, sem, subject))
    conn.commit()

def add_subject_attempt(conn, roll, sem, subject, credits, marks, grade, gp, result):
    attempt = get_next_attempt(conn, roll, sem, subject)
    mark_old_attempt_not_latest(conn, roll, sem, subject)

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO subjects
        (roll_no, semester, subject, attempt_no, credits, marks, grade, grade_point, result, is_latest)
        VALUES (?,?,?,?,?,?,?,?,?,1)
    """, (roll, sem, subject, attempt, credits, marks, grade, gp, result))

    if result == "Fail":
        cur.execute("""
            INSERT INTO backlogs (roll_no, semester, subject, status)
            VALUES (?,?,?,'ACTIVE')
        """, (roll, sem, subject))
    else:
        cur.execute("""
            UPDATE backlogs SET status='CLEARED'
            WHERE roll_no=? AND semester=? AND subject=?
        """, (roll, sem, subject))

    conn.commit()

# ---------- REPORTS ----------
def get_semesters(conn, roll):
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT semester FROM subjects
        WHERE roll_no=? ORDER BY semester
    """, (roll,))
    return [x[0] for x in cur.fetchall()]

def get_subjects_for_semester(conn, roll, sem):
    cur = conn.cursor()
    cur.execute("""
        SELECT subject, attempt_no, credits, marks, grade, result
        FROM subjects
        WHERE roll_no=? AND semester=?
        ORDER BY subject, attempt_no
    """, (roll, sem))
    return cur.fetchall()

def get_latest_subjects(conn, roll, sem):
    cur = conn.cursor()
    cur.execute("""
        SELECT credits, grade_point FROM subjects
        WHERE roll_no=? AND semester=? AND is_latest=1 AND result='Pass'
    """, (roll, sem))
    return cur.fetchall()

def calculate_gpa(conn, roll, sem):
    rows = get_latest_subjects(conn, roll, sem)
    if not rows:
        return 0.0
    pts = sum(c*gp for c,gp in rows)
    creds = sum(c for c,_ in rows)
    return round(pts/creds, 2)

def calculate_cgpa(conn, roll):
    cur = conn.cursor()
    cur.execute("""
        SELECT credits, grade_point FROM subjects
        WHERE roll_no=? AND is_latest=1 AND result='Pass'
    """, (roll,))
    rows = cur.fetchall()
    if not rows:
        return 0.0
    pts = sum(c*gp for c,gp in rows)
    creds = sum(c for c,_ in rows)
    return round(pts/creds, 2)

def get_backlogs(conn, roll):
    cur = conn.cursor()
    cur.execute("""
        SELECT subject, semester FROM backlogs
        WHERE roll_no=? AND status='ACTIVE'
    """, (roll,))
    return cur.fetchall()
