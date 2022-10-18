from itertools import count
#import resource
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
from collections import Counter
from tabulate import tabulate
import heapq
import re


def data_to_dict():
    return pd.read_excel('../resources/definizioni.xlsx', index_col=0).T.to_dict('list')

def stem_lem (string_list: list):
    word_list=list()
    lemma_list = list()
    stemma_list = list()
    wnl = WordNetLemmatizer()
    stw = SnowballStemmer('english')
    for parola in string_list:
            parola = str(parola)
            parola = parola.lower()
            parola = parola.translate(str.maketrans('', '', string.punctuation))
            for word in word_tokenize(parola):
                if not word in stopwords.words('english'):
                    word_list.append(word)
    for i in word_list:
        lemma_list.append(wnl.lemmatize(i))
    for lemma in lemma_list:
        stemma_list.append(stw.stem(lemma))
    return stemma_list
    
def frequency(dictionary: dict, num_common_word):
    frequency = dict()
    for concept, definitions in dictionary.items():
        
        stemma_list = stem_lem(definitions)
        #print(stemma_list)
        counts = Counter(stemma_list)
        frequency[concept] = heapq.nlargest(num_common_word, counts, key=counts.get)
        #print(counts)
    return frequency


def word_in_sentence(dictionary: dict, frequency: dict):
    concept_score = dict()
    for concept1, words in frequency.items():
        score_list = dict()
        for word in words:
            counter = 0
            for concept, definitions in dictionary.items():
                if concept == concept1:
                    cleaned_definitions = stem_lem(definitions)
                    for definition in cleaned_definitions:
                        if str(word) in str(definition):
                            counter+=1
            score_list[word] = counter/len(definitions)
        concept_score[concept1] = score_list
    return concept_score

def overlap_words(dictionary: dict, word1, word2):
    frequent_words = frequency(dictionary, 10)
    overlaps = list()
    my_words = {key: frequent_words[key] for key in frequent_words.keys()
       & {word1, word2}}
    for commons in my_words[word1]:
        for commons2 in my_words[word2]:
            if commons == commons2:
                overlaps.append(commons)
    print(my_words)
    print (overlaps)


df_dict = data_to_dict()
df_dict_freq = frequency(df_dict, 5)
scores = word_in_sentence(df_dict, df_dict_freq)
overlap_concrete = overlap_words(df_dict, 'Emotion', 'Revenge')
table = pd.DataFrame.from_dict(df_dict_freq, orient='index')
#print(tabulate(table, headers=['Concept', 'Most frequent word', '2nd', '3rd', '4th', '5th'], tablefmt='fancy_grid'))
#print(scores)
