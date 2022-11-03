from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import random
import string
import requests
import spacy
import time

nlp = spacy.load("en_core_web_sm")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
letter = random.choice(letters)
categories = ['types of', 'parts of']



def timer():
    print()
    time_left = 10
    timeout_start = time.time()
    while time.time() < timeout_start + 11:
        if time_left != 0:
            print('\r', f'The game will start in {time_left} seconds', end='')
        else:
            print('\r', f'Game started!', end='')
        time_left -= 1
        time.sleep(1)
    print()
    print()

def find_hyponym(hyp, letter):
    answers = list()
    answers_def=list()
    synsets = wn.synsets(hyp)
    for syn in synsets:
        answers.extend(syn.hyponyms())
    for hyposyn in answers:
        for lemma in hyposyn.lemmas():
            name = lemma.name()
            if name.startswith(letter):
                answers_def.append(name)
    #print(answers_def)
    return answers_def


def find_meronym(mer, letter):
    answers = list()
    answers_def=list()
    synsets = wn.synsets(mer)
    for syn in synsets:
        answers.extend(syn.part_meronyms())
    for merosyn in answers:
        for lemma in merosyn.lemmas():
            name = lemma.name()
            if name.startswith(letter):
                answers_def.append(name)
    #print(answers_def)
    return answers_def

def get_random_hyponym():
    hyponyms = list()
    answers_provv=list()
    file = open(f'hyponyms.txt', 'r')
    for word in file:
        hyponyms.append(word.strip('\n'))
    file.close()
    hypo = random.choice(hyponyms)
    answers_provv = find_hyponym(hypo, letter)
    if (len(answers_provv) == 0):
        hypo=get_random_hyponym()
    return hypo


def get_random_meronym():
    meronyms = list()
    answers_provv = list()
    file = open(f'meronyms.txt', 'r')
    for word in file:
        meronyms.append(word.strip('\n'))
    file.close()
    mero = random.choice(meronyms)
    answers_provv = find_meronym(mero, letter)
    if (len(answers_provv) == 0):
        mero=get_random_meronym()
    return mero



def get_random_category():
    category = random.choice(categories) 
    return category




def game_computer():
    answers = list()
    if random_category == 'types of':
        answers = find_hyponym(hyponym, letter)

    if random_category == 'parts of':
        answers = find_meronym(meronym, letter)
    
    return answers


def get_scores(computer, user):
    final_user_words = [word for word in user if word is not None and word.startswith(letter)]
    score_for_word = len(computer)/10
    final_user_score = float()
    for word in computer:
        if word in final_user_words:
            final_user_score+=score_for_word
    print()
    print("STOP!")
    print(f'----------- SCORE ----------')
    print(f'    - Your Score: {final_user_score*10}')
    print(f'    - Your Words: {final_user_words}')
    print()
    print(f'    - AI Score: 10')
    print(f'    - AI Words: {computer}')

random_category = get_random_category()
hyponym = get_random_hyponym()
meronym = get_random_meronym()
answers_user = list()


        

if __name__ == '__main__':
    print("Game starts.\nWrite as many words as possible in 30 secs!")
    print()
    print("Enter all the " + random_category + ":")
    if random_category == 'types of':
        print("------" + hyponym + "------")
    if random_category == 'parts of':
        print("------" + meronym + "------")

    print("With letter:\n" + "------" + letter + "------\n")
    timer()
    timeout_start = time.time()

    while time.time() < timeout_start + 10:
        answers_user.append(str(input('Insert word: ')))

    answers_computer = game_computer()

    get_scores(answers_computer, answers_user)
