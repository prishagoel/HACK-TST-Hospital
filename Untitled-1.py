import mysql.connector
f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()
mycur.execute("create database Hacktst;")
print("database created")
mycur.execute("use Hacktst;")
que = "create table trial(sno tinyint NOT NULL primary key, name varchar(30), section varchar(5));"
mycur.execute(que)
print("table created")
sn = int(input("enter sno"))
nam = input("enter name")
sec = ("enter section")
mycur.execute("insert into trial(sn, nam, sec)values({},'{}','{}').format(sno, name, section);")
print("values inserted")
mycur.execute("select * from Hacktst;")
f.commit()
mycur.close()
f.close()