import os
import re
def main():
    filePath=r'C:/Users/Administrator/Desktop/html/'
    fileNames=fetchfileNames(filePath)  # 1
    # print(fileNames)
    for fileName in fileNames:
        if (fileName.endswith(".htm") and fileName.startswith("article")):
            # print(filePath+fileName)
            absoluteFilePath=filePath+fileName
            htmlString=openAndReadFile(absoluteFilePath)  # 2
            # print(htmlString)
            articleTitle=dataCleaning(htmlString)    # 3
            if articleTitle:
                openAndWriteFile(absoluteFilePath,articleTitle)  # 4
            
            


def fetchfileNames(filePath):   #1，获取路径下的所有文件名称
    return os.listdir(filePath)

def openAndReadFile(filePath):     #2，打开文件病读取内容
    file=open(filePath,'r',encoding='utf-8')
    try:
        htmlString=file.read()
    except expression as identifier:
        pass
    else:
        pass
    finally:
        file.close()
    return htmlString

def dataCleaning(htmlString):  #3，数据清洗
    # print(htmlString)
    pattern=re.compile(r'<title>.*</title>')
    list=re.findall(pattern,htmlString)

    # pattern2=re.compile(r'<meta name="keywords" content=".*">')
    pattern2=re.compile(r'<meta name="keywords" content="'+'.*'+'">')
    list2=re.findall(pattern2,htmlString)

    pattern3=re.compile(r'<meta name="description" content="'+'.*'+'">')
    list3=re.findall(pattern3,htmlString)
    # print("list2:"+list2[0])
    # print("list3:"+list3[0])
    this_htmlString=htmlString
    if len(list)>0:
        print(list)
        this_htmlString=this_htmlString.replace(list[0],'<title>{dede:field.title/}</title>')
        # firstList=list[0].replace('</title>','')
        # secondList=firstList.replace('title>','')
        # print(secondList)
        # htmlString.
    if len(list2)>0:
        print(list2)
        this_htmlString=this_htmlString.replace(list2[0],'<meta name="keywords" content="'+'{dede:field.keywords/}'+'">')
    
    if len(list3)>0:
        print(list3)
        return this_htmlString.replace(list3[0],'<meta name="description" content="'+'{dede:field.descriptionfunction=’html2text(@me)’/}'+'">')
    

def openAndWriteFile(absoluteFilePath,articleTitle):     #4，数据写入制定文件
    try:
        with open(absoluteFilePath, 'w',encoding="UTF-8") as file_object:
            file_object.write(articleTitle)
            print('文件写入成功')
            # except expression2 as identifier:
            #     pass
            # else:
            #     pass
    finally:
        # file_object.close()
        pass

if __name__ == "__main__":
    main()
