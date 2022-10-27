import spacy
import pandas as pd
from nltk.wsd import lesk
from collections import Counter
from tabulate import tabulate

def get_supersense_from_file():
    supersense = dict()
    with open('../resources/csi_data/wn_synset2csi.txt', 'r') as file:
        for line in file:
            split_line = line.split()
            supersense[split_line[0]] = split_line[1]
    return supersense

csi_dict = get_supersense_from_file()

def get_sentences_from_file():
    sentences = list()
    df = pd.read_csv('../resources/get.csv', header=None)
    for sentence in df[1].tolist():
        sentences.append(sentence.replace('<s>', '').replace('</s>', '').replace('\'\'', '\'').strip().lower())
    return sentences

def parser_verbs(sentences, verbo):
    nlp = spacy.load('en_core_web_sm')
    sentence_analysis = list()
    for sentence in sentences:
        doc = nlp(sentence)
        dictionary = dict.fromkeys(['sentence','subj','obj','super_subj', 'super_obj'])
        dictionary['sentence'] = sentence
        for token in doc:
            if 'nsubj' in token.dep_ and token.head.lemma_ == verbo:
                if token.pos_ != 'PRON':
                    dictionary['subj'] = token.text
                else: dictionary['subj'] = 'human'
                if dictionary['subj'] is not None:
                    dictionary['super_subj'] = get_supersense(dictionary['sentence'], dictionary['subj'])
            if 'dobj' in token.dep_ and token.head.lemma_ == verbo:
                if token.pos_ != 'PRON':
                    dictionary['obj'] = token.text
                else: dictionary['obj'] = 'human'
                if dictionary['obj'] is not None:
                    dictionary['super_obj'] = get_supersense(dictionary['sentence'], dictionary['obj'])
        sentence_analysis.append(dictionary)
    print('finito1')
    return sentence_analysis

def get_supersense(sentence, word):
    supersense = None
    lesk_synset = lesk(sentence, word)
    if lesk_synset is not None:
        synset_offset = str(lesk_synset.offset())
        for synset_code, supersense_descr in csi_dict.items():
            if synset_offset in synset_code:
                supersense = str(supersense_descr)
                break
    return supersense

sentences=get_sentences_from_file()
sentence_analysis = parser_verbs(sentences, 'get')

def meanings(sentence_analysis):
    supersense_list_valency_two = list()
    supersense_list_valency_one_subj = list()
    supersense_list_valency_one_obj = list()
    tmp = 0
    tmp_subj = 0
    tmp_obj =0
    for dicti in sentence_analysis:
        if dicti['subj'] is not None and dicti['obj'] is not None and dicti['super_subj'] is not None and dicti['super_obj'] is not None:
            combination = (dicti['super_subj'], dicti['super_obj'])
            supersense_list_valency_two.append(combination)
            tmp += 1
        elif dicti['subj'] is not None and dicti['obj'] is None and dicti['super_subj'] is not None:
            combination = (dicti['super_subj'], dicti['super_obj'])
            supersense_list_valency_one_subj.append(combination)
            tmp_subj += 1
        elif dicti['subj'] is None and dicti['obj'] is not None and dicti['super_obj'] is not None:
            combination = (dicti['super_subj'], dicti['super_obj'])
            supersense_list_valency_one_obj.append(combination)
            tmp_obj += 1
    supersense_list_valency_two = create_percentage(supersense_list_valency_two, tmp)
    supersense_list_valency_one_subj = create_percentage(supersense_list_valency_one_subj, tmp_subj)
    supersense_list_valency_one_obj = create_percentage(supersense_list_valency_one_obj, tmp_obj)
    table1 = pd.DataFrame.from_dict(supersense_list_valency_two)
    print()
    print('valenza 2 in '+ str(tmp)+' frasi.')
    print()
    print(tabulate(table1, headers=['Combination [Subject - Object]', 'Count', 'Percentage'], tablefmt='fancy_grid'))
    print()
    print('valenza 1 con solo soggetto in '+ str(tmp_subj)+' frasi.')
    print()
    table2 = pd.DataFrame.from_dict(supersense_list_valency_one_subj)
    print(tabulate(table2, headers=['Combination [Subject - Object]', 'Count', 'Percentage'], tablefmt='fancy_grid'))
    print()
    print('valenza 1 con solo oggetto in '+ str(tmp_obj)+' frasi.')
    print()
    table3 = pd.DataFrame.from_dict(supersense_list_valency_one_obj)
    print(tabulate(table3, headers=['Combination [Subject - Object]', 'Count', 'Percentage'], tablefmt='fancy_grid'))
    
def create_percentage(combination_list, tmp):
    percentage_list = list()
    counts_valency_two = Counter(combination_list)
    sorted_combination_dict = dict(sorted(counts_valency_two.items(), key=lambda x: x[1], reverse=True)[:20])
    for values in sorted_combination_dict.values():
        percentage_list.append(str(round(((values/tmp)*100),3))+'%')
    sorted_combination_dict = {'combination' : list(sorted_combination_dict.keys()), 
                                    'count' : list(sorted_combination_dict.values()), 
                                    'percentage' : percentage_list}
    return sorted_combination_dict

meanings = meanings(sentence_analysis)