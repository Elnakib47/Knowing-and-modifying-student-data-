import sqlite3

def connect():
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id INTEGER PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")
    conn.commit()
    conn.close()





def insert(fn,ln,term,gpa):
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data1 VALUES (NULL,?,?,?,?)",(fn,ln,term,gpa))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert("sherif","said",10,3.7)
print(view())

