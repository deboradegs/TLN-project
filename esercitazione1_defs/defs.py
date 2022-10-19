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
        stemma = stemming.stem(lemma)
        if stemma not in stop_words and stemma not in string_punctuation:
            words.append(stemma)
    #print(words)
    return words
    
def frequency(dictionary: dict, num_common_word):
    frequency = dict()
    score_list = dict()
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
        score_list = dict()
        sum = 0
        for word in words:
            counter = 0
            for concept, definitions in dictionary.items():
                if concept == concept1:
                    cleaned_definitions = stem_lem(definitions)
                    for definition in cleaned_definitions:
                        if str(word) in str(definition):
                            counter+=1
            score_list[word] = dict({'word': word,
                                'score': counter/len(definitions)
                                })
            
            sum += counter/len(definitions)
        #print(score_list)
        #concept_score[concept1] = round(sum/len(words),3)
        #concept_score[concept1].update(score_list)
        concept_score[concept1] = {'score': round(sum/len(words),3),
                                   'score_list': dict(score_list) }
        dict(concept_score[concept1])
    #print(concept_score)
    return concept_score

def overlap_words(dictionary: dict, word1, word2):

    my_words = {key: dictionary[key] for key in dictionary.keys()
       & {word1, word2}}

    frequent_words = frequency(my_words, 10)
    most_score_words = word_in_sentence(my_words, frequent_words)
    word1_scores = dict(most_score_words[word1]['score_list'])
    word2_scores = dict(most_score_words[word2]['score_list'])

    score_for_words_word1 = list()
    for word in word1_scores:
        score_for_words_word1.append(list(word1_scores[word].values()))
    score_for_words_word1 = dict(score_for_words_word1)

    score_for_words_word2 = list()
    for word in word2_scores:
        score_for_words_word2.append(list(word2_scores[word].values()))
    score_for_words_word2 = dict(score_for_words_word2)
  
    overlaps= 0

    total_score = 0
    most_5_scored_word1 = dict()
    lista_alti = heapq.nlargest(10, score_for_words_word1.values())
    for keys in score_for_words_word1:
        if score_for_words_word1[keys] in lista_alti:
            most_5_scored_word1[keys] = score_for_words_word1[keys]

    most_5_scored_word2 = dict()
    lista_alti2 = heapq.nlargest(10, score_for_words_word2.values())
    for keys2 in score_for_words_word2:
        if score_for_words_word2[keys2] in lista_alti2:
            most_5_scored_word2[keys2] = score_for_words_word2[keys2]

    for commons in most_5_scored_word1.keys():
        for commons2 in most_5_scored_word2.keys():
            if commons == commons2:
            
                total_score += (most_5_scored_word1[commons]+most_5_scored_word2[commons2])/2
                overlaps +=1

    if overlaps != 0: 
        total_score = total_score/overlaps
        return total_score
    else:
        return 0
    #print(total_score)
   


  


df_dict = data_to_dict()

df_dict_freq = frequency(df_dict, 5)
table = pd.DataFrame.from_dict(df_dict_freq, orient='index')
print(tabulate(table, headers=['Concept', 1, 2, 3, 4, 5], tablefmt='fancy_grid'))

scores = word_in_sentence(df_dict, df_dict_freq)
for concept in scores:
    del scores[concept]['score_list']
    #del concept['score_list']
table2 = pd.DataFrame.from_dict(scores, orient='index')
print()
print()
print(tabulate(table2, headers=['Concept', 'Score'], tablefmt='fancy_grid'))

overlap_abstract = overlap_words(df_dict, 'Emotion', 'Revenge')
overlap_concrete = overlap_words(df_dict, 'Person', 'Brick')
overlap_generic = overlap_words(df_dict, 'Person', 'Emotion')
overlap_specific = overlap_words(df_dict, 'Revenge', 'Brick')
table3 =  [
    ['Concrete', overlap_concrete],
    ['Abstract', overlap_abstract],
    ['Generic', overlap_generic],
    ['Specific', overlap_specific]
]
print()
print()
print(tabulate(table3, headers=['Concepts grouped by', 'Score'], tablefmt='fancy_grid'))
#print(scores)