import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
from collections import Counter
from tabulate import tabulate
import heapq
from nltk.wsd import lesk


def data_to_dict():
    return pd.read_excel('../resources/definizioni.xlsx', index_col=0).T.to_dict('list')

lemmatizer = WordNetLemmatizer()
#stemming = SnowballStemmer('english')
stop_words = stopwords.words('english')
stop_words.extend(['someone', 'something', 'e', 'e.g', 'u', 'ha', 'e.i', 'others', "'s","wa"])
string_punctuation = string.punctuation + '’'

def stem_lem(text):
    words = list()
    for word in word_tokenize(str(text).lower()):
        lemma = lemmatizer.lemmatize(word)
        #stemma = stemming.stem(lemma)
        if lemma not in stop_words and lemma not in string_punctuation:
            words.append(lemma)
    return words

def disambiguation(dictionary: dict, num_common_word):
    concept_common_words = dict()
    concept_common_synset = dict()
    for concept, definitions in dictionary.items():
        hyperonym_dict = dict()
        stemma_list = list()
        for definition in definitions:
            lesk_word_list = list()
            lesk_synset_list = list()
            stemma_list.extend(stem_lem(definition))
            for word in stemma_list:
                lesk_synset = lesk(str(definition), str(word))
                if lesk_synset is not None:
                    lesk_synset_list.append(lesk_synset)
                    [lesk_word_list.append(str(lemma.name())) for lemma in lesk_synset.lemmas()]
        counts = Counter(lesk_synset_list)
        migliori = heapq.nlargest(num_common_word, counts, key=counts.get)
        for syns in migliori:
            hyper = syns.hypernyms()
            if not hyper:
                hyperonym_dict[syns]=syns
            else:
                hyperonym_dict[syns]=hyper[0]
        concept_common_synset[concept] = hyperonym_dict
        counts = Counter(lesk_word_list)
        concept_common_words[concept] = heapq.nlargest(num_common_word, counts, key=counts.get)
    return concept_common_words, concept_common_synset


df_dict = data_to_dict()
concept_common_words, concept_common_synset= disambiguation(df_dict, 4)
# print()
# print(concept_common_synset)
# print()


def get_synset_score_disamb():
    synset_context = dict()
    synset_score = dict()
    for concept, dicts in concept_common_synset.items():
        synset_list = list()
        lemma_score_list = list()
        for syns, hyper in dicts.items():     
            lemma_list = list()
            #print(syns.lemmas())
            [lemma_list.append(str(lemma.name())) for lemma in syns.lemmas()]
            lemma_score_list.append(lemma_list[0])
            synsets_lemma = wn.synsets(lemma_list[0])
            # print('yooooooooooooooooooooooooooooooooooooooo')
            # print(synsets_lemma)
            for sn in synsets_lemma:
                hyper_list_tmp = sn.hypernyms()
                if not hyper_list_tmp:
                    hyper_tmp=sn
                else:
                    hyper_tmp=hyper_list_tmp[0]
                # print()
                # print(hyper_tmp)
                # print(dicts[syns])
                if hyper_tmp == dicts[syns]:
                    # print('ENTRATO')
                    synset_list.append(sn)
        # print()
        # print(lemma_score_list)
        # print(synset_list)
        #synset_list = list(dict.fromkeys(synset_list))
        hyponyms_list = list()
        for synset in synset_list:
          hyponyms_list.extend(synset.hyponyms())
        hyponyms_list = list(dict.fromkeys(hyponyms_list))
        synset_list.extend(hyponyms_list)
        synset_list = list(dict.fromkeys(synset_list))
        context_list = list()
        for synset in synset_list:
            context_list.extend(stem_lem(synset.definition()))
            for example in synset.examples():
                context_list.extend(stem_lem(example))
            context_list = list(dict.fromkeys(context_list))
            synset_context[synset] = context_list
        # print('il contesto èèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèè')
        # print(context_list)
        # counts = Counter(context_list)
        # migliori = heapq.nlargest(5, counts, key=counts.get)
       
        # print('Le migliori sonoooooooooooooooooooooooooooooooo')
        # print(migliori)
            score_dict = dict()
            sortedDict = list()
            for synset, contexts in synset_context.items():
                overlap = set(contexts) & set(lemma_score_list)
                score_dict[synset] = round(float(len(overlap) / (len(set(contexts) | set(lemma_score_list)))),3)
                #score_dict[synset] = round(float((len(overlap)) / (len(set(lemma_score_list)))),3)
            sortedDict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:5]
            synset_score[concept] = sortedDict
    return synset_score
            
synset_score= get_synset_score_disamb()





# def print_table1(synset_score: dict):
#     for concept, synsets in synset_score.items():
#             to_print = dict()
#             for synset in synsets:
#                 synset_name = str(synset[0])
#                 to_print[synset_name] = {'Definition': synset[0].definition().capitalize(), 'Score': synset[1]}
#             table = pd.DataFrame.from_dict(to_print, orient='index')
#             print()
#             print(f'----- Best 5 sense for {concept} -----')
#             print()
#             print(tabulate(table, headers=['Synset', 'Definition', 'Score'], tablefmt='fancy_grid'))
#             print()



# def get_synset_score():
#     synset_context = dict()
#     synset_score = dict()
#     for concept, words in concept_common_words.items():
#         synset_list = list()
#         for word in words:
#             synset_list.extend(wn.synsets(word))
#         synset_list = list(dict.fromkeys(synset_list))
#         hyponyms_list = list()
#         for synset in synset_list:
#            hyponyms_list.extend(synset.hyponyms())
#         hyponyms_list = list(dict.fromkeys(hyponyms_list))
#         synset_list.extend(hyponyms_list)
#         synset_list = list(dict.fromkeys(synset_list))
#         for synset in synset_list:
#             context_list = list()
#             context_list.extend(stem_lem(synset.definition()))
#             for example in synset.examples():
#                 context_list.extend(stem_lem(example))
#             context_list = list(dict.fromkeys(context_list))  
#             synset_context[synset] = context_list
#         score_dict = dict()
#         sortedDict = list()
#         for synset, contexts in synset_context.items():
#             overlap = set(contexts) & set(words)
#             #print(len(overlap))
#             score_dict[synset] = round(float(len(overlap) / (len(set(contexts) | set(words)))),3)
#             #score_dict[synset] = round(float((len(overlap)) / (len(set(words)))),3)
#         sortedDict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:5]
#         synset_score[concept] = sortedDict
#     return synset_score

# synset_score2 = get_synset_score()


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

#print_table(synset_score2)

print_table(synset_score)
