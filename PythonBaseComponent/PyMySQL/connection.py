import pymysql
db = pymysql.connect("localhost","root","root","school_db","3306","utf8")
cursor = db.cursor()
cursor.execute("select 姓名 from xs limit 5")
results = cursor.fetchall()
for row in results:
    id = row[0]
    kc = row[1]
    cj = row[3]
    print("id=%s,kc=%s,cj=%s"% (id,kc,cj))
db.close()