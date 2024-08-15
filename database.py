import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="bhavani1021",
    port=3306,
    database="employee_data"
)
mycursor = mydb.cursor()

def insert(id, name, phone, role, gender, salary):
    mycursor.execute('INSERT INTO empdata VALUES (%s, %s, %s, %s, %s, %s)', (id, name, phone, role, gender, salary))
    mydb.commit()

def id_exists(id):
    mycursor.execute("SELECT COUNT(*) FROM empdata WHERE id=%s", (id,))
    result = mycursor.fetchone()
    return result[0] > 0

def fetch_employees():
    mycursor.execute("SELECT * FROM empdata")
    result = mycursor.fetchall()
    return result
def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute("UPDATE empdata SET name=%s, phone=%s, role=%s, gender=%s, salary=%s WHERE id=%s",( new_name, new_phone, new_role, new_gender, new_salary,id))
    mydb.commit()
def delete(id):
    mycursor.execute("DELETE FROM empdata WHERE id=%s", (id,))
    mydb.commit()

def search(option, value):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM empdata WHERE `{option}`=%s", (value,))
    results = mycursor.fetchall()
    mycursor.close()
    return results
def deleteall_records():
    mycursor.execute("DELETE FROM empdata")
    mydb.commit()

