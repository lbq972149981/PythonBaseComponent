import pymysql

class DBmethod:
    def __init__(self,name,psd,id,sex,grade,classid):
        self.name = name
        self.psd = psd
        self.id = id
        self.sex = sex
        self.grade = grade
        self.classid = classid
    def add(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root',
                               port=3306, db='school_db', charset='utf8')
        cursor = conn.cursor()
        conn.autocommit(1)
        try:
            value = (self.name,self.id)
            cursor.execute('select * from student where name = %s and id=%s',value)
            data = cursor.fetchone()
            if data != None :
                print('用户已注册！')
                return False
            else:
                return True
        except:
            conn.rollback()
            print("出错")
            pass
        finally:
            cursor.close()
            conn.close()

    def delete(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root',
                               port=3306, db='test', charset='utf8')
        cursor = conn.cursor()
        conn.autocommit(1)
        try:
            value = (self.name, self.id)
            cursor.execute('delete * from student where name = %s and id=%s', value)
            data = cursor.fetchone()
            if data != None:
                print('操作成功！')
                return False
            else:
                return True
        except:
            conn.rollback()
            print("出错")
            pass
        finally:
            cursor.close()
            conn.close()
