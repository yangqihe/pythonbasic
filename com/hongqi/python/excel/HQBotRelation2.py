
import ast
import MySQLdb
import xlwt

# import os, sys
# codePath = os.path.abspath(os.path.join(__file__, "../..", "json"))
# if os.path.exists(codePath):
#     sys.path.append(codePath)
#sys.path.insert(0, '..')
#sys.path.append("../")

from com.hongqi.python.json import HQJsonUtils


# 关于样式
style_head = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 初始化字体相关
font.name = "微软雅黑"
font.bold = True
font.colour_index = 1 # TODO 必须是数字索引
bg = xlwt.Pattern() # 初始背景图案
bg.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
bg.pattern_fore_colour = 23 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
# 设置字体
style_head.font = font
# 设置背景
style_head.pattern = bg
# 创建一个excel
excel = xlwt.Workbook()
# 添加工作区
sheet = excel.add_sheet("分类ID")
# 标题信息
head = ["1级分类","2级分类","3级分类","4级分类","5级分类","6级分类",'FAQID','FAQ问题','用户标签','答案类型','FAQ回答','答案关联问','关联FAQID','关联FAQ问题','FAQ相似问句','自定义属性','禁用标识']
for index,value in enumerate(head):
    sheet.write(0,index,value,style_head)








conn = MySQLdb.connect(host = "127.0.0.1",user = "root",password = "123456",database = "bot",charset = "utf8")

cursor = conn.cursor()
categorySql = "select * from onlinefaqs limit 10000"
cursor.execute(categorySql)
result = cursor.fetchall()
cursor.close()

list = []
def getParent(parentList,parentId):
    if parentId !=0:
        faqSql = "select * from categories where id = " + str(parentId)
        cursor_ = conn.cursor()
        cursor_.execute(faqSql)
        result_ = cursor_.fetchall()
        parent = result_[0][4]
        parentName = result_[0][1]
        parentList.append(parentName)
        return getParent(parentList,parent)
    else:
        return parentList

def getParentName(parentList):
    parent1 = ''
    parent2 = ''
    parent3 = ''
    parent4 = ''
    parent5 = ''
    parent6 = ''
    if len(parentList) == 5:
        parent5 = parentList[4]
        parent4 = parentList[3]
        parent3 = parentList[2]
        parent2 = parentList[1]
        parent1 = parentList[0]
    elif len(parentList) == 4:
        parent4 = parentList[3]
        parent3 = parentList[2]
        parent2 = parentList[1]
        parent1 = parentList[0]
    elif len(parentList) == 3:
        parent3 = parentList[2]
        parent2 = parentList[1]
        parent1 = parentList[0]
    elif len(parentList) == 2:
        parent2 = parentList[1]
        parent1 = parentList[0]
    elif len(parentList) == 1:
        parent1 = parentList[0]
    return parent1,parent2,parent3,parent4,parent5,parent6

notfoundCount = 0
for i in range(len(result)):
    faqId = result[i][1]
    label = ''
    type = result[i][2]
    type = '富文本'
    categoryName = result[i][3]
    faqQuestion = result[i][4]
    try:
        faqAnswer_ = ast.literal_eval(result[i][6])
        faqAnswer = faqAnswer_[0]['answer']
    except:
        faqAnswer = ''

    relationFAQID = ''
    relationFAQQuestion = ''
    relationFaq = ''
    #print('######第####',i,"####行########")
    try:
        # if i == 18:
        #     print(i)
        #json_data = result[i][5].replace(r"\\","\\")  #.replace('\r', '\\r').replace('\n', '\\n')
        #similarQuestion_ = json.loads(json_data) #, strict=False #.replace('\r', '\\r').replace('\n', '\\n')
        similarQuestion_ = HQJsonUtils.parjson(result[i][5])
        if len(similarQuestion_) > 0:
            similarQuestion = similarQuestion_[0]
        else:
            similarQuestion = ''
    except Exception as e:
        print('######第####', i, "####行########",e)
        similarQuestion = ''

    faqSql = "select * from categories where name = " + "'" + categoryName + "'"
    cursor_ = conn.cursor()
    cursor_.execute(faqSql)
    result_ = cursor_.fetchall()
    if len(result_) == 0:
        #print('第  ###  ', i, '  ### 行  ')
        notfoundCount += 1
        print('分类  ', categoryName, '  没有找到    ','    第  ###  ', i, '  ### 行  ','   总共   ',notfoundCount)
        #print(result_)
        continue
    cursor_.close()

    parent = result_[0][4]
    list.clear()
    parentList = getParent(list, parent)
    parent1,parent2,parent3,parent4,parent5,parent6 = getParentName(parentList)
    #print(parent1,'##',parent2,'##',parent3,'##',parent4,'##',parent5,'##',parent6,' ## ',faqId,faqQuestion,label,type,faqAnswer,relationQuestion,relationFaq,similarQuestion)
    result_list = [parent1,parent2,parent3,parent4,parent5,parent6,faqId,faqQuestion,label,type,faqAnswer,relationFAQID,relationFAQQuestion,relationFaq,similarQuestion]
    index = i + 1
    for k in range(len(result_list)):
        sheet.write(index, k, result_list[k])

conn.close()
excel.save("/Users/yangchiher/Desktop/hq_excel.xlsx")
