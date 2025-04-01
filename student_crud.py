import psycopg2
DB_NAME="postgres"
DB_USER="postgres.zpxwnpqhwmwmmgdizqyb"
DB_PASSWORD="Codeblocks@123"
DB_HOST="aws-0-ap-south-1.pooler.supabase.com"
DB_PORT="6543"

def db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD,
            host=DB_HOST, 
            port=DB_PORT
        )
        return conn
    except:
        print("Connection Failed!!")
        return None
    
def create_teacher_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""\
        CREATE TABLE IF NOT EXISTS teacher (
            id SERIAL PRIMARY KEY NOT NULL, 
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def create_students_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""\
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY NOT NULL, 
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL, 
            course_id INT REFERENCES courses(course_id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def create_courses_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""\
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY NOT NULL,
            course_name VARCHAR(100), 
            course_description TEXT
                   
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def create_enrollments_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""\
        CREATE TABLE IF NOT EXISTS enrollements (
            studetent_id SERIAL REFERENCES students(student_id),
            course_id SERIAL REFERENCES courses(course_id)   
        )
    """)


    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")


def insert_teacher():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age) VALUES ('Mrigendra Pradhan', 20) RETURNING id")
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted!!")

def update_teacher(id, name, age):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE teacher SET name = %s, age = %s WHERE id= %s", (name, age, id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data Updated!!")

def alter_student():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE students ADD COLUMN gender VARCHAR(100)")
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Updated!!")



def insert_teacher():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age, course_id) VALUES ('Mrigendra Pradhan', 20, 1)")
    conn.commit()
    cursor.close()
    conn.close()
    print("Teacher Data Inserted!!")

def insert_course():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_name, course_description) VALUES ('Python Programming', 'Learn the basics of Python.') RETURNING course_id")
    conn.commit()
    cursor.close()
    conn.close()
    print("Course Data Inserted!!")

def insert_student():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course_id, gender) VALUES ('Bikash Shrestha', 18, 1, 'Male') RETURNING student_id")
    conn.commit()
    cursor.close()
    conn.close()
    print("Student Data Inserted!!")

def insert_enrollment():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollements (student_id, course_id) VALUES (1, 1)")
    conn.commit()
    cursor.close()
    conn.close()
    print("Enrollment Data Inserted!!")


def rename_student_column():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE enrollements RENAME TO enrollments")
    conn.commit()
    cursor.close()
    conn.close()
    print("Enrollment Data Inserted!!")


if __name__ == "__main__":
    #create_students_table()
    #create_courses_table()
    #create_enrollments_table()
    #alter_student()
    #insert_teacher()
    #insert_course()
    #insert_student()
    #insert_enrollment()
    rename_student_column()

    
    

