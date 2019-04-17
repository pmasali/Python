import pymysql

db = pymysql.connect("localhost","root","password","sakila")

cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# sql = """CREATE TABLE EMPLOYEE (
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)"""

# cursor.execute(sql)

# sql = """INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES
# ('Mac','Mohan',20,'M',2000)"""

# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     print("exception")
#     db.rollback()

sql = """SELECT * FROM EMPLOYEE"""

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("name: %s lname: %s age: %d sex: %s income: %d" % (fname, lname, age, sex, income))
except:
    print("Unable to fetch db")

db.close()


    