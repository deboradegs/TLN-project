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
    return words

def frequency(dictionary: dict, num_common_word):
    frequency = dict()
    for concept, definitions in dictionary.items():
        stemma_list = list()
        for definition in definitions:
            stemma_list.extend(stem_lem(definition))
        counts = Counter(stemma_list)
        frequency[concept] = heapq.nlargest(num_common_word, counts, key=counts.get)
    return frequency

df_dict = data_to_dict()
concept_common_words = frequency(df_dict, 3)


def get_synset_context():
    synset_context = dict()
    synset_score = dict()
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
        score_dict = dict()
        sortedDict = list()
        for synset, contexts in synset_context.items():
            overlap = set(contexts) & set(words)
            score_dict[synset] = round(float(len(overlap)) / (len(set(contexts) | set(words))),3)
        sortedDict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:5]
        synset_score[concept] = sortedDict
    return synset_score

synset_score = get_synset_context()


def print_table(synset_score: dict):
    for concept, synsets in synset_score.items():
        to_print = dict()
        for synset in synsets:
            synset_name = str(synset[0])
            to_print[synset_name] = {'Definition': synset[0].definition().capitalize(), 'Score': synset[1]}
        table = pd.DataFrame.from_dict(to_print, orient='index')
        print()
        print(f'----- Best 5 sense for {concept} -----')
        print()
        print(tabulate(table, headers=['Synset', 'Definition', 'Score'], tablefmt='fancy_grid'))
        print()

print_table(synset_score)
