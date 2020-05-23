import openpyxl

# 处理ID为空的情况
path = '/Users/yangchiher/Desktop/文本机器人id整合5.9.xlsx'
wb = openpyxl.load_workbook(path)
sheet1 = wb['Sheet1']
ad = sheet1['AD']
for i in range(len(ad)):
    cell = ad[i]
    if(cell.value):
        print(i, str(cell.value))
        categoryId = cell.value
    else:
        cell.value = categoryId
wb.save(path)



