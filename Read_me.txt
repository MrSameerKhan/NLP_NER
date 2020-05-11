NLP:


Training:

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   English  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Preprocessing:

python3 eng_sentence_2_NER.py

Training :

python3 engTrain.py

preprocess.py and validation.py are the dependency files for engTrain.py

Dataset : This includes dataset of sentences.txt and after preprocessing NERTag.txt

word_embedding : It consists of Glove word embedding

model : the output weight file will be saved in this directory




$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Arabic $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


Preprocessing:

python3 ara_sentence_2_NER.py

Training:

python3 araTrain.py

BiGRU.py is the dependency file for araTrain.py

Dataset : This includes dataset of sentences.txt and after preprocessing NERTag.txt

word_embedding : It consists of word2Vec embedding

model : the output weight file will be saved in this directory
