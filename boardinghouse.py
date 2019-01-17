import pymysql
import sys
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='boardinghouse',
)
def add():
    room_number = input("Enter room number: ")
    first_name= input("enter first name: ")
    last_name = input("Enter last name: ")
    monthly = input("Enter monthly: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO boarders (`room_number`,`first_name`, `last_name` , `monthly`) VALUES (%s, %s, %s, %s)"
            try:
                cursor.execute(sql, (room_number, first_name, last_name, monthly))
                print("Task added successfully")
            except:
                print("Oops! Something wrong")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("DATA\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from boarders"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("Room#\tfirst_name\t\tlast_name\t\t\t monthly")
            print("-----------------------------------------------------------------------------------------")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t\t\t" + (row[2]) + "\t\t\t" , row[3])

        connection.commit()
    finally:
        print ("")
        return
def update():
    read()
    print("")
    room_number = input("Enter room_number you want to update: ")
    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    monthly = input("Enter monthly: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE boarders SET `first_name`=%s, `last_name`=%s , `monthly`=%s WHERE `room_number` = %s"
            try:
                cursor.execute(sql, (first_name, last_name, monthly, room_number))
                print("Successfully Updated...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def delete():
    read()
    print("")
    room_number = input("Enter room number of the boarders to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM boarders WHERE room_number = %s"
            try:
                cursor.execute(sql, (room_number))
                print("Successfully Deleted...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def search():
    print("\n")
    room_number = input("Enter boarders number that you want to search: ")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from boarders WHERE room_number = %s"
            try:
                cursor.execute(sql, (room_number))
                result = cursor.fetchall()
                print("Room #\tfirst_name\t\t\tlast_name\t\t\tmonthly")
                print("---------------------------------------------------------------------------")
                for row in result:
                   print(str(row[0]) + "\t" + row[1] + "\t\t\t" + (row[2]) + "\t\t\t" , row[3])
            except:
                print("Oops! Something wrong")

        connection.commit()
    finally:
        print("")
        return
def logoff():
    sys.exit(0)

choice = 1
while choice:
    print ("\t\t\tBoarding House")
    print ("[1] Create a new data\t[2] Read data\t[3] = Update data\t[4] = Delete data\t[5] = Search data\t[6] = Log off")
    print("---------------------------------------------------------------------------")

    choice = input("Choices: ")

    if choice == "1":
        add()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    elif choice == "6":
        logoff()
        
    else:
        print ("Invalid Input!\n")
        choice = 1
