
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

