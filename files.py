import mysql.connector

try:
    db = mysql.connector.connect(
        user='root',  
        password='root',  
        host='localhost',
        database='hck'  
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM parents")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
except mysql.connector.Error as err:
    print("Error while connecting to MySQL database: {}".format(err))

finally:
    try:
        db.close()
    except NameError:
        pass