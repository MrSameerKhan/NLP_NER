
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import tree2conlltags
from pprint import pprint

# Read text file
text = open("Dataset/test.txt")					# change the path of train.txt / valid.txt / test.txt
text = text.read()

# Convert text to word
word_token = word_tokenize(text)

# performe POS Tagging
word_pos = pos_tag(word_token)

# Define pattern for POS
pattern = 'NP: {<DT>?<JJ>*<NN>}'

#Tag BOI for POS
cp = nltk.RegexpParser(pattern)
cs = cp.parse(word_pos)



#BOI Tagging on POS Tagging
iob_tagged = tree2conlltags(cs)



NER_List = []

for TupList in iob_tagged:
    con_tup_list = list(TupList)
    
    if TupList[0].upper() == "NAME" :
        con_tup_list.append("B-NAME")
    elif TupList[0].upper()== "FIRST" :
        con_tup_list.append("B-FIRST")
    elif TupList[0].upper()== "FATHER" :
        con_tup_list.append("B-FATHER")
    elif TupList[0].upper()== "GRANDPA" :
        con_tup_list.append("B-GRANDPA")
    elif TupList[0].upper()== "FAMILY" :
        con_tup_list.append("B-FAMILY")
    elif TupList[0].upper()== "NATIONALITY" :
        con_tup_list.append("B-NATIONALITY")			
    elif TupList[0].upper()== "MOBILE" :
        con_tup_list.append("B-MOBILE")
    elif TupList[0].upper()== "ID" :
        con_tup_list.append("B-ID")
    elif TupList[0].upper()== "DATE" :
        con_tup_list.append("B-DATE")
    elif TupList[0].upper()== "BIRTH" :
        con_tup_list.append("B-BIRTH")


    elif TupList[0].upper()== "EXPIRY" :
        con_tup_list.append("B-EXPIRY")
    elif TupList[0].upper()== "JOB" :
        con_tup_list.append("B-JOB")
    elif TupList[0].upper()== "CLIENT" :
        con_tup_list.append("B-CLIENT")
    elif TupList[0].upper()== "BRANCH" :
        con_tup_list.append("B-BRANCH")
    elif TupList[0].upper()== "TITLE" :
        con_tup_list.append("B-TITLE")
    elif TupList[0].upper()== "PLACE" :
        con_tup_list.append("B-PLACE")
    elif TupList[0].upper()== "ISSUE" :
        con_tup_list.append("B-ISSUE")
    elif TupList[0].upper()== "CIC" :
        con_tup_list.append("B-CIC")
    elif TupList[0].upper()== "ACCOUNT" :
        con_tup_list.append("B-ACCOUNT")
    elif TupList[0].upper()== "NO" :
        con_tup_list.append("B-NO")


    elif TupList[0].upper()== "GENDER" :
        con_tup_list.append("B-GENDER")
    elif TupList[0].upper()== "MALE" :
        con_tup_list.append("B-MALE")
    elif TupList[0].upper()== "FEMALE" :
        con_tup_list.append("B-FEMALE")
    elif TupList[0].upper()== "OTHER" :
        con_tup_list.append("B-OTHER")
    elif TupList[0].upper()== "SINGLE" :
        con_tup_list.append("B-SINGLE")
    elif TupList[0].upper()== "MARRIED" :
        con_tup_list.append("B-MARRIED")
    elif TupList[0].upper()== "CITY" :
        con_tup_list.append("B-CITY")
    elif TupList[0].upper()== "POSTAL" :
        con_tup_list.append("B-POSTAL")
    elif TupList[0].upper()== "CODE" :
        con_tup_list.append("B-CODE")
    elif TupList[0].upper()== "BOX" :
        con_tup_list.append("B-BOX")


    elif TupList[0].upper()== "SCHOOL" :
        con_tup_list.append("B-SCHOOL")
    elif TupList[0].upper()== "PRE" :
        con_tup_list.append("B-PRE")
    elif TupList[0].upper()== "GRADUATE" :
        con_tup_list.append("B-GRADUATE")
    elif TupList[0].upper()== "POST" :
        con_tup_list.append("B-POST")
    elif TupList[0].upper()== "EMPLOYER" :
        con_tup_list.append("B-EMPLOYER")
    elif TupList[0].upper()== "SOCIAL" :
        con_tup_list.append("B-SOCIAL")
    elif TupList[0].upper()== "CODE" :
        con_tup_list.append("B-CODE")
    elif TupList[0].upper()== "EDUCATION" :
        con_tup_list.append("B-EDUCATION")
    elif TupList[0].upper()== "SOURCE" :
        con_tup_list.append("B-SOURCE")
    elif TupList[0].upper()== "INCOME" :
        con_tup_list.append("B-INCOME")


    elif TupList[0].upper()== "CURRENT" :
        con_tup_list.append("B-CURRENT")
    elif TupList[0].upper()== "PREVIOUS" :
        con_tup_list.append("B-PREVIOUS")
    elif TupList[0].upper()== "SERVICE" :
        con_tup_list.append("B-SERVICE")
    elif TupList[0].upper()== "LEGACY" :
        con_tup_list.append("B-LEGACY")
    elif TupList[0].upper()== "COMMERCIAL" :
        con_tup_list.append("B-COMMERCIAL")
    elif TupList[0].upper()== "SAVINGS" :
        con_tup_list.append("B-SAVINGS")
    elif TupList[0].upper()== "PURPOSE" :
        con_tup_list.append("B-PURPOSE")
    elif TupList[0].upper()== "PERSONAL" :
        con_tup_list.append("B-PERSONAL")
    elif TupList[0].upper()== "PAYROLL" :
        con_tup_list.append("B-PAYROLL")
    elif TupList[0].upper()== "CREDIT" :
        con_tup_list.append("B-CREDIT")


    elif TupList[0].upper()== "LANGUAGE" :
        con_tup_list.append("B-LANGUAGE")
    elif TupList[0].upper()== "ARABIC" :
        con_tup_list.append("B-ARABIC")
    elif TupList[0].upper()== "ENGLISH" :
        con_tup_list.append("B-ENGLISH")
    elif TupList[0].upper()== "PASSPORT" :
        con_tup_list.append("B-PASSPORT")
    
    else :
        con_tup_list.append("O")
        
    con_list_tup = tuple(con_tup_list)
    
    NER_List.append(con_list_tup)
    

#Save POS-BOI Tag in text file
f = open("Dataset/testTAG.txt", "w+")							# Change the saving path trainTAG.txt / validTAG.txt / testTAG.txt

for i in NER_List :
    name = str(i[0])
    pos = str (i[1])
    chunk = str (i[2])
    ner = str(i[3])
    
    final = name+ " "+ pos+" "+ chunk+" "+ ner
    
    if name == ".":
        f.write(final+"\n"+"\n")
    elif name == "!":
        f.write(final+"\n"+"\n")
    elif name == "?":
        f.write(final+"\n"+"\n")
    else :
        f.write(final+"\n")
        
f.close()

