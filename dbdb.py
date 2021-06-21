import pymysql

def insert_data(email, pw):
    db = pymysql.connect(host='20171062.mysql.pythonanywhere-services.com',
                    user='20171062', password='1q2w3e4r!@',
                    db='20171062$mydb', charset='utf8')
    c = db.cursor()
    setdata = (email, pw)
    c.execute("INSERT INTO user_tb VALUES (%s, %s)", setdata)
    db.commit()

def get_emailpw(email, pw):
    print(email, pw)
    db = pymysql.connect(host='backseunghun.mysql.pythonanywhere-services.com',
                    user='backseunghun', password='asdf',
                    db='backseunghun$mydb', charset='utf8')
    c = db.cursor()
    setdata = (email, pw)
    c.execute("SELECT * FROM user_tb WHERE email = %s AND pw = %s", setdata)
    ret = c.fetchone()
    print(ret)
