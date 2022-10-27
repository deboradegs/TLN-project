from nltk.corpus import stopwords
import wikipedia
import wikipediaapi
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

stop_words = stopwords.words('english')

def get_page_from_wiki(title_list):
    documents = str()
    wiki_doc = wikipediaapi.Wikipedia('en')
    for title in title_list:
        documents = documents + ' ' + (wiki_doc.page(title).summary)
    return documents

#documents = get_page_from_wiki(['Chocolate', 'Cream', 'Icecream'])
#documents = get_page_from_wiki(['Chocolate', 'Car', 'Butterfly'])
documents = get_page_from_wiki(['Chocolate', 'Car', 'Cat', 'Louvre'])
print('\n\n ORIGINAL DOCUMENT: \n\n')
print(documents)
print('\n\n')

def split_paragraph(documents, len_split):
    splitted = [' '.join(documents.split(' ')[i:i+len_split]) for i in range(0, len(documents.split(' ')), len_split)]
    return splitted

paragraph = split_paragraph(documents, 45)
# for par in paragraph:
#     print(par + '\n\n')

def get_tf_idf(paragraph):
    vectorizer = TfidfVectorizer(stop_words=stop_words, token_pattern=r'(?u)\b[A-Za-z]+\b')
    tf_idf_matrix = pd.DataFrame(vectorizer.fit_transform(paragraph).toarray(),columns=vectorizer.get_feature_names_out())
    matrix = vectorizer.fit_transform(paragraph)
    similarity = cosine_similarity(matrix)

    similarity_two_phrase = list()
    for i in range(len(similarity) - 1):
        similarity_two_phrase.append(similarity[i][i + 1])
    y = np.array([item for item in similarity_two_phrase])
    
    mins, dicti= find_peaks(-y)
    new_y = np.sort(y[mins])
    new_y = new_y[:3]
    x = np.array([i for i in mins if y[i] in new_y])
    plt.vlines(x, ymin=0, ymax=0.6, color='red', label='breakpoints')
    plt.plot(similarity_two_phrase)
    plt.show()
    return x

x = get_tf_idf(paragraph)

def split_final(paragraph, x):
    final = str()
    count = 0
    x = np.append(x, len(paragraph)-1)
    for i in x:
        while count <=i:
            final = final + ' ' + paragraph[count]
            count+=1
        final = final + '\n\n\n\n\n'
    return final

final_document = split_final(paragraph, x)
print('SPLITTED DOCUMENT: \n\n')
print(final_document)
            