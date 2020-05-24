import MySQLdb
conn = MySQLdb.connect(host = "127.0.0.1",user = "root",password = "123456",database = "i_bot_sync",charset = "utf8")
cursor = conn.cursor()
sql = "select * from i_faq_id limit 10"
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
conn.close()
for i in range(len(result)):
    obj = result[i]
    print(obj)