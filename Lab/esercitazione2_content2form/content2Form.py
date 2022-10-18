import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
from collections import Counter
from tabulate import tabulate
import heapq

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
    #for lemma in lemma_list:
        #stemma_list.append(stw.stem(lemma))
    return lemma_list
    
def frequency(dictionary: dict, num_common_word):
    frequency = dict()
    for concept, definitions in dictionary.items():
        stemma_list = stem_lem(definitions)
        #print(stemma_list)
        counts = Counter(stemma_list)
        frequency[concept] = heapq.nlargest(num_common_word, counts, key=counts.get)
        #print(counts)
    return frequency


def get_context(frequency: dict):
    context = dict()
    definitions = list()
    hyponyms = list()
    for concept, words in frequency.items():
        synset_list = list()
        for word in words: 
            synset_list.extend(wn.synsets(word))
        synset_list = list(dict.fromkeys(synset_list))
        for i in synset_list:
            hyponyms.extend(i.hyponyms())
        hyponyms = list(dict.fromkeys(hyponyms))
        synset_list.extend(hyponyms)
        synset_list = list(dict.fromkeys(synset_list))
        for i in synset_list:
            definitions.append((stem_lem(i.definition())))
            definitions.extend(i.examples())
            context[i] = definitions
    print(type(context))
    return context



df_dict = data_to_dict()
concept_common_words = frequency(df_dict, 5)
synset = get_context(concept_common_words)
#print(synset)
#table = pd.DataFrame.from_dict(synset, orient='index')
#print(tabulate(table, headers=['Concept', 'definition'], tablefmt='fancy_grid'))

