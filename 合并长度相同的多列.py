col1 = ['java','C++','python']
col2 = ['springboot','MFC','tensorflow']
col3 = ['web开发','界面','张量计算']
for language, frame, description in zip(col1,col2,col3):
    print(language,frame,description)