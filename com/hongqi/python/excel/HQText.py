import MySQLdb
conn = MySQLdb.connect(host = "127.0.0.1",user = "root",password = "123456",database = "bot",charset = "utf8")

f0 = open('/Users/yangchiher/Desktop/data_/sql/faqanswers_error.txt','w')
f = open('/Users/yangchiher/Desktop/data_/sql/faqanswers_error_.txt')# 只读数据

#f = open('/Users/yangchiher/Desktop/data_/sql/faqanswers.txt')

lines = f.readlines()
f.close()
i = 0

errorCount = 0
for line in lines:
    text = line
    i+=1
    if i > 10000:
        break

    list = []
    count = 0
    if i > 1:
        space = 0
        start = 0
        tempspace = 0
        line = line + '    ' + 'end'
        for j in range(len(line)):
            if line[j] == ' ':
                space += 1
            else:
                tempspace = space
                space = 0
                if tempspace > 1:
                    end = j
                    count +=1
                    if count == 12 and len(line[start:end]) > 35: #处理时间堆叠问题
                        list.append(line[start:end][0:25])
                        list.append(line[start:end][25:50])
                        count += 1
                    else:
                        list.append(line[start:end])

                    #print(line[start:end])
                    start = j



        if count !=15:
            #print(text)
            index_ = line.rfind('>')
            print('########index_##########', index_)
            print(line[5:index_ + 1])
            for k in range(len(list)):
                print('####', list[k])
            errorCount +=1
            #print('第  ', i, '  行数据')
            #print('####分割错误########')
            if len(list[count-3]) > 50:
                print(list[count-3])
            f0.write(text)

        list.clear()

        #array = line.split('    ')
        #arrayLen = len(array)

        # print('######id#########',array[0])
        # print(array[arrayLen - 15])
        # print(array[arrayLen - 14])
        # print(array[arrayLen - 13])
        # print(array[arrayLen - 12])
        # print(array[arrayLen - 11])
        # print(array[arrayLen - 10])
        # print(array[arrayLen - 9])
        # print(array[arrayLen - 8])
        # print(array[arrayLen - 7])
        # print(array[arrayLen - 6])
        # print(array[arrayLen - 5])
        # print(array[arrayLen - 4])
        # print(array[arrayLen - 3])
        # print(array[arrayLen - 2])
        # print(array[arrayLen - 1])

        # index = 0
        # id = array[index]
        # print('id ',id)
        # index +=1
        # answer = array[index]
        # print('answer ', answer)
        # index += 1
        # labels = array[index]
        # print('labels ', labels)
        # index += 1
        # link = array[index]
        # print('link ', link)
        # index += 1
        # status = array[index]
        # print('status ', status)
        # relatedQuestions = array[arrayLen - 11]
        # print('relatedQuestions ', relatedQuestions)
        # index += 1
        # useType = array[arrayLen - 10]
        # print('useType ', useType)
        # reserve1 = array[arrayLen - 9]
        # print('reserve1 ', reserve1)
        # index += 1
        # reserve2 = array[arrayLen - 8]
        # print('reserve2 ', reserve2)
        # index += 1
        # reserve3 = array[arrayLen - 7]
        # print('reserve3 ', reserve3)
        # index += 1
        # reserve4 = array[arrayLen - 6]
        # print('reserve4 ', reserve4)
        # reserve5 = array[arrayLen - 5]
        # print('reserve5 ', reserve5)
        # createdAt = array[arrayLen - 4]
        # print('createdAt ', createdAt)
        # updatedAt = array[arrayLen - 3]
        # print('updatedAt ', updatedAt)
        # FaqId = array[arrayLen - 2]
        # print('FaqId ', FaqId)
        # tenantId = array[arrayLen - 1]
        # print('tenantId ', tenantId)

        #print('第  ',i,'  行数据')
        # cursor = conn.cursor()
        # sql = "insert into faqanswers values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # val = (id, answer, labels, link, 0, relatedQuestions, 0, reserve1, reserve2, reserve3, reserve4, reserve5, createdAt, updatedAt, FaqId,tenantId)
        # cursor.execute(sql, val)
        # result = cursor.fetchall()
        # cursor.close()

# conn.commit()
# conn.close()

#f0.close()

print('总共 ',errorCount,' 行错误 ', len(lines))