#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:18:41 2019

@author: zyclyx
"""

from nltk.tokenize import word_tokenize

text = open("Dataset/37Sent.txt")								# change the path of the sentence dataset
text = text.read()

word_token = word_tokenize(text)

finalList = []

f = open("Dataset/37Token.txt", "w+")								# path for saving the NER.txt
	
for i in word_token :
    if i == "العميل":
        final = i +" "+"B-ACIC"
        f.write(final +"\n")
        finalList.append(final)
        
    elif i == "العضوية":
        final = i + " " + "B-AMEMBERSHIP"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "المركز":
        final = i + " " + "B-ACENTER"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "الأول":
        final = i + " " + "B-AFIRST"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الأب‎":
        final = i + " " + "B-ASECOND"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الجد":
        final = i + " " + "B-ATHIRD"									# change the labels according to the processes
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "العائلة":
        final = i + " " + "B-AFAMILY"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الاسم":
        final = i + " " + "B-ANAME"
        f.write(final + "\n")
        finalList.append(final)
        
        
    elif i == "الجنسية":
        final = i + " " + "B-ANATIONALITY"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "جوال":
        final = i + " " + "B-AMOBILE"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "اقامة":
        final = i + " " + "B-AIQAMA"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "بطاقة":
        final = i + " " + "B-ASAUDI"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "أخرى":
        final = i + " " + "B-AOTHER"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "مكان":
        final = i + " " + "B-APLACE"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الاصدار":
        final = i + " " + "B-AISSUE"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "تاريخ":
        final = i + " " + "B-ADATE"
        f.write(final + "\n")
        finalList.append(final)
        
        
    elif i == "الميلاد":
        final = i + " " + "B-ABIRTH"
        f.write(final + "\n")
        finalList.append(final)

    elif i == "الانتهاء":
        final = i + " " + "B-AEXPIRY"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "العمل":
        final = i + " " + "B-AEMPLOYER"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "الوظيفة":
        final = i + " " + "B-AJOB"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "المدينة":
        final = i + " " + "B-ACITY"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "البريدى":
        final = i + " " + "B-APOSTAL"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الرمز":
        final = i + " " + "B-ACODE"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "صندوق":
        final = i + " " + "B-ABOX"
        f.write(final + "\n")
        finalList.append(final)
        
        
    elif i == "اعمال":
        final = i + " " + "B-ABUSINESS"
        f.write(final + "\n")
        finalList.append(final)

    elif i == "مدخرة":
        final = i + " " + "B-ASAVINGS"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "مقدار":
        final = i + " " + "B-ATOTAL"
        f.write(final + "\n")
        finalList.append(final)
    elif i == "الراتب":
        final = i + " " + "B-AINCOME"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "الجنس":
        final = i + " " + "B-AGENDER"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "ذكر":
        final = i + " " + "B-AMALE"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "أنثى":
        final = i + " " + "B-AFEMALE"
        f.write(final + "\n")
        finalList.append(final)
        
    elif i == "عنوان":
        final = i + " " + "B-AADDRESS"
        f.write(final + "\n")
        finalList.append(final)
        
        
    elif i == "جهة":
        final = i + " " + "B-ASIDE"
        f.write(final + "\n")
        finalList.append(final)        

    elif i == "الرقم":
        final = i + " " + "B-ANO"
        f.write(final + "\n")
        finalList.append(final)       
    elif i == "الشهري":
        final = i + " " + "B-AMONTHLY"
        f.write(final + "\n")
        finalList.append(final)       
    elif i == "اسم":
        final = i + " " + "B-ANAME"
        f.write(final + "\n")
        finalList.append(final)       
    elif i == "المهنة":
        final = i + " " + "B-AJOB"
        f.write(final + "\n")
        finalList.append(final)       
    elif i == "البريد":
        final = i + " " + "B-APOSTAL"
        f.write(final + "\n")
        finalList.append(final)       
    elif i == "راتب":
        final = i + " " + "B-AINCOME"
        f.write(final + "\n")
        finalList.append(final)          
    elif i== "صاحب":
        final = i + " " + "B-ASIDE"
        f.write(final + "\n")
        finalList.append(final)   
    else :
        final = i +" " + "O"
        f.write (final+ "\n")
        finalList.append(final)
     


f.close()
        
