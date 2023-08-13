import mysql.connector
def create_table():
    f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
    mycur = f.cursor()
    que = "create table discharged(ID varchar(20), BED_NUMBER integer, NAME varchar(30), AGE integer, GENDER varchar(20), DOCTOR_ID varchar(20), DATE_DISCHARGE date, DATE_ADMISSION date);"
    mycur.execute(que)
    print("table created")
    f.commit()
    f.close()
    mycur.close()
    
    
    