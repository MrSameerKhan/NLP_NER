#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:18:41 2019

@author: sameer
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
    elif i== "صاحب":
        final = i + " " + "B-ASIDE"
        f.write(final + "\n")
        finalList.append(final)   
    else :
        final = i +" " + "O"
        f.write (final+ "\n")
        finalList.append(final)
     


f.close()
        
