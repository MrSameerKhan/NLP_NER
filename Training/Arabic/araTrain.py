import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import numpy as np
import BIGRU
import time
import re
import gensim
import gensim.models.keyedvectors as word2vec
from keras.utils import to_categorical
import pandas as pd
import matplotlib.pyplot as plt
from seqeval.metrics import accuracy_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score

print("Word Embedding is loading")
embedding = word2vec.KeyedVectors.load_word2vec_format('word_embedding/wiki.ar.vec', binary=False)		 # Word embedding path
print("Word Embedding is loaded")

dump_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~’،ـ؟؛«» '

def clean_word(word):

    word = word.translate(str.maketrans({key: None for key in dump_chars}))
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    word = re.sub(p_tashkeel,"", word)
    
    return word


def load_data():

    path = 'Dataset/35SentToken.txt'
    f = open(path, 'r')
    sents = f.read().split('\n. O\n')
    f.close()

    words = [None]*len(sents)
    tokens = [None]*len(sents)

    for i, sent in enumerate(sents):
        sent = sent.split('\n')
        words[i] = []
        tokens[i] = []

        for word in sent:
            line = word.rsplit(' ', 1)
            line[0] = clean_word(line[0])
            
            if len(line[0]) > 0:
                words[i].append(line[0])
                tokens[i].append(line[1])                    
                
    return [d for d in words if len(d) > 0], [d for d in tokens if len(d) > 0]

# load data
sents, labels = load_data()

tag_classes = ["B-ANAME", "B-AFIRST","B-AFATHER", "B-AGRANDPA","B-ATHEFAMILY",
               "B-ANATIONALITY", "B-AID",  "B-AMOBILE", "B-ADATE" ,"B-ABIRTH",
               "B-AEXPIRY","B-AJOB","B-ACLIENT", "B-ABRANCH", "B-ATITLE",
               "B-APLACE","B-AISSUE","B-ACIC", "B-ANO", "B-AGENDER",
               "B-AIQAMA", "B-AMALE", "B-AFEMALE","B-ASAUDI","B-AOTHER",
               "B-APASSPORT","B-ASINGLE","B-AMARRIED","B-ACITY", "B-APOSTAL",
               "B-ACODE","B-ABOX","B-ASCHOOL", "B-APRE", "B-AGRADUATE",
               "B-APOST","B-ASIDE","B-AWORK","B-APREFERRED","B-ALANGUAGE",
               "B-AENGLISH","B-AARABIC","O"]							# Tags 

# embed words
for i, sent in enumerate(sents):
    for j, word in enumerate(sent):
        try:
            sents[i][j] = embedding[word]
        except KeyError:
            sents[i][j] = embedding['unk']

# embed labels
for i, tokens in enumerate(labels):
    labels[i] = [to_categorical(tag_classes.index(tag), num_classes=len(tag_classes)) for tag in tokens]
    
        
# pad sequences
max_sent_length = 212
sents_lengths = []
for i, sent in enumerate(sents):
    sents_lengths.append(len(sent))
    l = max_sent_length - len(sent)
    sents[i] += [[0]*300]*l
    

for i, label in enumerate(labels):
    l = max_sent_length - len(label)
    labels[i] += [[0]*42+[0]]*l											# Num of classes excluding "O"


# tf metrics wrapper
def as_keras_metric(method):
    import functools
    from keras import backend as K
    @functools.wraps(method)
    def wrapper(self, args, **kwargs):
        """ Wrapper for turning tensorflow metrics into keras metrics """
        value, update_op = method(self, args, **kwargs)
        K.get_session().run(tf.local_variables_initializer())
        with tf.control_dependencies([update_op]):
            value = tf.identity(value)
        return value
    return wrapper

#%%
train_x, train_y = sents[:29000], labels[:29000]						# split the train and test datset
test_x, test_y = sents[29001:], labels[29001:]
####################


#####################


# build model
train_model, crf_layer = BIGRU.build_model()
train_model.compile(optimizer="adam", loss=crf_layer.loss_function, metrics=[crf_layer.accuracy, as_keras_metric(tf.metrics.precision), as_keras_metric(tf.metrics.recall), as_keras_metric(tf.contrib.metrics.f1_score)])
train_model.summary()

# train model

history = train_model.fit(np.array(train_x,dtype='float64'),np.array(train_y,dtype='float64'), epochs=20, verbose=1)
# save weights
train_model.save_weights('model/weight_CA_35S.hd5f')								# weight  file path

#%%


# testing
pred = train_model.predict(np.array(test_x,dtype='float64'))
pred_x = []
pred_y = []
for i, sent in enumerate(pred):
    pred_x.append([tag_classes[np.argmax(w)] for w in pred[i][:sents_lengths[i]]])
    pred_y.append([tag_classes[np.argmax(w)] for w in test_y[i][:sents_lengths[i]]])
    
print(classification_report(pred_y, pred_x))
print('f1_score: ')
print(f1_score(pred_y, pred_x))

