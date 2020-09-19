from seaborn.rcmod import set_style
import xlrd
import xlwt


excle_path = r'C:/Users/Administrator/Desktop/32.xls'  #路径
workbook = xlrd.open_workbook(excle_path)     #打开excle表
sheet = workbook.sheet_by_name('Sheet1')    #打开sheet表单页


domain_names = []
keywords = []
for i in range(130):
    keywords.append(sheet.cell(i, 0).value)
for i, keyword in enumerate(keywords):
        start = keyword.index('//')
        end = len(keyword)
        domain_names.append(keyword[start+2:end+1])

f = xlwt.Workbook() #创建工作簿
sheet1 = f.add_sheet(u'Sheet1',cell_overwrite_ok=False) #创建sheet
for i, name in enumerate(domain_names):
    # print(sheet.cell(0, 1).value)
    sheet1.write(i,1,label = name)
    print(name)
f.save(excle_path) #保存文件