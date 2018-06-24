#1.下载并导入代码库:pymysql
import pymysql

class DBConnection:
    def execute_sql_command(self):
        #2.获取数据库连接
        conn= pymysql.connect(host="127.0.0.1", user="root", password="root",
                 database="pirate", port=3306,charset='utf8')
        try:
        #3.获取数据库游标
            cursor=conn.cursor()
            #4.编写sql语句
            sql='select * from hd_user order by id desc;'
            #5.通过游标执行sql语句
            cursor.execute(sql)
            #6.获取执行结果
            row = cursor.fetchone()
            # print(row)
            # all_result=cursor.fetchall()
            # for row in all_result:
            #     print(row)
            conn.commit()
            return row
        finally:
            conn.close()

if __name__=='__main__':
    DBConnection().execute_sql_command()