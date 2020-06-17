import MySQLdb
conn = MySQLdb.connect(host = "127.0.0.1",user = "root",password = "123456",database = "bot",charset = "utf8")

cursor = conn.cursor()
categorySql = "select * from categories limit 100"
cursor.execute(categorySql)
result = cursor.fetchall()
cursor.close()

for i in range(len(result)):
    category = result[i]
    faqSql = "select * from onlinefaqs where category = " + "'"+category[1]+"'"

    cursor_ = conn.cursor()
    cursor_.execute(faqSql)
    result_ = cursor_.fetchall()
    cursor_.close()

    print(category[0], category[1], category[4])

    # for i in range(len(result_)):
    #     faq = result_[i]
    #     print(category[0],category[1],category[4],':',faq[1])

conn.close()