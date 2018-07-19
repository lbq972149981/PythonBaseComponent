import pymysql
class DBConnect:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def isUser(self):
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',
                               port=3306,db='school_db',charset='utf8')
        cursor = conn.cursor()
        conn.autocommit(1)
        try:
            value = (self.username,self.password)
            cursor.execute('select * from student where name=%s and psd = %s',value)
            data = cursor.fetchone()
            if data != None:
                return True
            else:
                return False
            pass
        except:
            conn.rollback()
            print("出错")
            pass
        finally:
            cursor.close()
            conn.close()
