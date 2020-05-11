#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:28:11 2020

@author: zyclyx
"""

#Tensorflow GPU utilization and diasble console warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

#Packages for English Models
from ner import Parser


#Packages for Arabic Models
import numpy as np
import BIGRU
import re
import gensim.models.keyedvectors as word2vec

inputPath = "متزوج‎"

def predictEnglish(inputPath):
    
    #engText = open(inputPath,'r', encoding='utf-8')  # read the input text from tesseract
    #engText = engText.read()
    
    par = Parser()                          # load the trained weights
    par.load_models("weightCA")
    
    engPred = par.predict(inputPath)                # predict the input
    
    return engPred
    


def clean_word(word):
    
    dump_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~’،ـ؟؛«» '
    
    word = word.translate(str.maketrans({key: None for key in dump_chars}))
    
    #remove tashkeel
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    word = re.sub(p_tashkeel,"", word)
    
    return word




def predictArabic(inputPath):
    
    
    
    embedding = word2vec.KeyedVectors.load_word2vec_format('word_embedding/wiki.ar.vec', binary=False)
    
    #araText = open(inputPath,'r', encoding='utf-8')
    #araText = araText.read()
    araText = inputPath.split()

    araText = ' '.join(key for key in araText)    
    araText = re.sub("\u200e|\u200f","",araText)
    araText= araText.split(" ")
    
    sent = []
    X = []
    for i, word in enumerate(araText):
        word = clean_word(word)
        if len(word) > 0:
            sent.append(word)
            try:
                X.append(embedding[word])
            except KeyError:
                X.append(embedding['unk'])

    X += [[0]*300]*(212 - len(sent))
    
    
    test_model, _ = BIGRU.build_model()
    test_model.load_weights('weightCA/weight.hd5f')							# weight file
    pred = test_model.predict(np.array([X]))
    
    tag_classes = ["B-ANAME", "B-AFIRST","B-AFATHER", "B-AGRANDPA","B-ATHEFAMILY",
               "B-ANATIONALITY", "B-AID",  "B-AMOBILE", "B-ADATE" ,"B-ABIRTH",
               "B-AEXPIRY","B-AJOB","B-ACLIENT", "B-ABRANCH", "B-ATITLE",
               "B-APLACE","B-AISSUE","B-ACIC", "B-ANO", "B-AGENDER",
               "B-AIQAMA", "B-AMALE", "B-AFEMALE","B-ASAUDI","B-AOTHER",
               "B-APASSPORT","B-ASINGLE","B-AMARRIED","B-ACITY", "B-APOSTAL",
               "B-ACODE","B-ABOX","B-ASCHOOL", "B-APRE", "B-AGRADUATE",
               "B-APOST","B-ASIDE","B-AWORK","B-APREFERRED","B-ALANGUAGE",
               "B-AENGLISH","B-AARABIC","O"]	
    
    
    table_data = []
    for i, word in enumerate(sent):
        table_data.append([word, tag_classes[np.argmax(pred[0][i])]])
    
    return table_data


    
print(predictEnglish(inputPath))

print(predictArabic(inputPath))

predictionEnglish = predictEnglish(inputPath)
predictionArabic = predictArabic(inputPath)








