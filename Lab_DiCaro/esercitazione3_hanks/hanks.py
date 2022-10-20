import spacy
import pandas as pd
from nltk.wsd import lesk
from collections import Counter
from tabulate import tabulate
from spacy import displacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def get_supersense_from_file(word):
    supersese = str
    with open('../resources/csi_data/wn_synset2csi.txt', 'r') as file:
        for line in file:
            split_line = line.split()
            if word in split_line[0]: supersese = str(split_line[1])
    return supersese

def get_sentences_from_file():
    sentences = list()
    df = pd.read_csv('../resources/take.csv', header=None)
    for sentence in df[1].tolist():
        sentences.append(sentence.replace('<s>', '').replace('</s>', '').strip().lower())
    return sentences

def parser_verbs(sentences, verbo):
    nlp = spacy.load('en_core_web_sm')
    sentence_parser = list()
    for sentence in sentences:
        doc = nlp(sentence)
        dictionary = dict.fromkeys(['sentence'])
        dictionary['sentence'] = sentence
        subj = str
        obj = str
        #displacy.serve(doc, style='dep')
        for token in doc:
            print (token.text, token.pos_, token.head.lemma_, token.dep_)
            if not token.is_punct and not token.is_space:
                if 'nsubj' in token.dep_ and token.head.lemma_ == verbo:
                    subj = token.text
                    dictionary['super_subj'] = get_supersense(dictionary['sentence'],subj)
                if 'dobj' in token.dep_ and token.head.lemma_ == verbo:
                    obj = token.text
                    dictionary['super_obj'] = get_supersense(dictionary['sentence'],obj)
        print(dictionary)
        sentence_parser.append(dictionary)
    return sentence_parser

def get_supersense(sentence,word):
    supersense = ''
    if word is not None:
        lesk_synset = lesk(sentence, word)
        print(word, lesk_synset)
        if lesk_synset is not None:
            offset_synset = str(lesk_synset.offset())
            print(word, offset_synset)
            supersense = get_supersense_from_file(offset_synset)
        else : supersense = 'None'
    return supersense

sentences=get_sentences_from_file()
sentence_parser = parser_verbs(sentences, 'take')
