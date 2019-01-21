# coding:utf-8
import pymysql
from ConfigurationFolder.ReadConfig import ReadConfig


class DB:
    def __init__(self):
        self.base_config = ReadConfig().get_database_config()
        self.connection = pymysql.connect(host = self.base_config[0], port = int(self.base_config[1]),
                                        user = self.base_config[2], passwd = self.base_config[3],
                                        db = self.base_config[4])
        self.c = self.connection.cursor(cursor = pymysql.cursors.DictCursor)

    def get_verification_code(self):
        self.c.execute("select * from cq_verification_code where uin = 40805092")
        data = self.c.fetchall()
        verify_code = data[-1]['verify_code']
        # print(f'获取到最新的验证码是：{verify_code}')
        self.connection.close()
        return verify_code

    # def get_follow_list(self, uin):
    #     sql = "select count(*) from cq_follow where uin = %s" % uin
    #     self.cursor.execute(sql)
    #     data = self.cursor.fetchone()['count(*)']
    #     self.conn.close()
    #     return data




