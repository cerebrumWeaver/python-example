import xlrd
import xlwt
excle_path = r'C:/Users/Administrator/Desktop/test.xlsx'  #路径
workbook = xlrd.open_workbook(excle_path)     #打开excle表
sheet = workbook.sheet_by_name('sheet1')    #打开sheet表单页
domain_names = []
keywords = []
str = sheet.cell(0,0).value
print(type(str))
# print("类型："+sheet.cell(0, 0))
# for i in range(30):
#     keywords.append(sheet.cell(i, 0))
#     domain_names.append(sheet.cell(i, 1))

# print(domain_names.value)

# print(workbook.sheet_names())
# sheet=workbook.sheet_by_name('详细')
# row_num=sheet.nrows
# col_num=sheet.ncols
# cell_2_2=sheet.cell(6,3).value
# print('行数：'+str(row_num)+'\t'+'列数：'+str(col_num))
# print(cell_2_2)


























# url=https://m.sm.cn/s?q=宁波白癜风医院联系方式&by=submit&from=smor&tomode=center&safe=1
# 宁波白癜风医院联系方式