import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
from collections import Counter
from tabulate import tabulate
import heapq

lemmatizer = WordNetLemmatizer()
stemming = SnowballStemmer('english')
stop_words = stopwords.words('english')
stop_words.extend(['someone', 'something', 'e', 'e.g', 'u', 'ha', 'e.i', 'others', "'s"])
string_punctuation = string.punctuation + '’'

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

df_dict = data_to_dict()
concept_common_words = frequency(df_dict, 5)
#print(concept_common_words)

def get_synset_context():
    synset_context = dict()
    for concept, words in concept_common_words.items():
        synset_list = list()
        for word in words:
            synset_list.extend(wn.synsets(word))
        synset_list = list(dict.fromkeys(synset_list))
        hyponyms_list = list()
        for synset in synset_list:
            hyponyms_list.extend(synset.hyponyms())
        hyponyms_list = list(dict.fromkeys(hyponyms_list))
        synset_list.extend(hyponyms_list)
        synset_list = list(dict.fromkeys(synset_list))
        for synset in synset_list:
            context_list = list()
            context_list.extend(stem_lem(synset.definition()))
            for example in synset.examples():
                context_list.extend(stem_lem(example))
            context_list = list(dict.fromkeys(context_list))  
            synset_context[synset] = context_list
    return synset_context

synset_context = get_synset_context()
print(synset_context)

