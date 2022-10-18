from itertools import count
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
from collections import Counter
from tabulate import tabulate
import heapq



def data_to_dict():
    return pd.read_excel('../resources/definizioni.xlsx', index_col=0).T.to_dict('list')

def stem_lem(text):
    lemmatizer = WordNetLemmatizer()
    stemming = SnowballStemmer('english')
    stop_words = stopwords.words('english')
    stop_words.extend(['someone', 'something', 'e', 'e.g', 'u', 'ha', 'e.i', 'others', "'s"])
    string_punctuation = string.punctuation + '’'
    words = list()
    for word in word_tokenize(str(text).lower()):
        lemma = lemmatizer.lemmatize(word)
        #stemma = stemming.stem(lemma)
        if lemma not in stop_words and lemma not in string_punctuation:
            words.append(lemma)
    #print(words)
    return words
    
def frequency(dictionary: dict, num_common_word):
    frequency = dict()
    for concept, definitions in dictionary.items():
        stemma_list = list()
        for definition in definitions:
            #print(definition)
            stemma_list.extend(stem_lem(definition))
        #print(stemma_list)
        counts = Counter(stemma_list)
        frequency[concept] = heapq.nlargest(num_common_word, counts, key=counts.get)
        #print(counts)
    return frequency


def word_in_sentence(dictionary: dict, frequency: dict):
    concept_score = dict()
    for concept1, words in frequency.items():
        sum = 0
        for word in words:
            counter = 0
            for concept, definitions in dictionary.items():
                if concept == concept1:
                    cleaned_definitions = stem_lem(definitions)
                    for definition in cleaned_definitions:
                        if str(word) in str(definition):
                            counter+=1
            sum += counter/len(definitions)
        concept_score[concept1] = round(sum/len(words),3)
    print(concept_score)
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
overlap_abstract = overlap_words(df_dict, 'Emotion', 'Revenge')
table = pd.DataFrame.from_dict(df_dict_freq, orient='index')
table2 = pd.DataFrame.from_dict(scores, orient='index')
print(tabulate(table, headers=['Concept', 1, 2, 3, 4, 5], tablefmt='fancy_grid'))
print()
print()
print(tabulate(table2, headers=['Concept', 'Score'], tablefmt='fancy_grid'))
#print(scores)