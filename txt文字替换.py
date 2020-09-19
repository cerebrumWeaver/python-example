import os
filePath = 'C:/Users/Administrator/Downloads/'
filenames=os.listdir(filePath)
# print(filenames)
for filename in filenames:
    if(filename.endswith(".txt")):
        file = open(r'C:/Users/Administrator/Downloads/'+filename, 'r',encoding="utf-8")
        try:
            string=file.read()
        finally:
            file.close()
        print("-----------------------------------------------------原始文章-----------------------------------------------------------------")
        print(string)
        str1=string.replace("治疗","医治")
        str2=str1.replace("疾病","病")
        str3=str2.replace("苏州","宁波")
        str4=str3.replace("教师","")
        str5=str4.replace("学生","")
        str6=str5.replace("企业","")
        str7=str6.replace("中国","")
        str8=str7.replace("国家","")
        str9=str8.replace("我国","")
        str10=str9.replace("发展","")
        str11=str10.replace("进行","")
        str12=str11.replace("网络","")
        str13=str12.replace("研究","")
        str14=str13.replace(" ","")
        str15=str14.replace("社会","")
        str16=str15.replace("我们","")
        str17=str16.replace("他们","")
        str18=str17.replace('','')
        str19=str18.replace('华研','')
        str20=str19.replace('瑞金','')
        
        print("-----------------------------------------------------替换后的文章-----------------------------------------------------------------")
        print(str20)

        # file = open(r'C:/Users/Administrator/Downloads/filename', 'w',encoding="utf-8")
        try:
            # coding=UTF-8,写入多行取消注释即可
            target=r"C:/Users/Administrator/Desktop/targetArticle/"+filename
            with open(target, 'w',encoding="UTF-8") as file_object:
                file_object.write(str20)
                # file_object.write("Add two words")
        finally:
            file.close()