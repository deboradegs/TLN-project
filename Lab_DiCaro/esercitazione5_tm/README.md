## Esercitazione #5 - "TM" - Implementazione di un esercizio di Topic Modeling

### DataSet
Il dataset utilizzato è ***ConventionData2012***, una trascrizione di una convention politica tenutasi in America.  
Viene recuperato attraverso *scattertext*.

### Pre-processing
Le sentence all'interno del dataset sono processate rimuovendo le stopwords e la punteggiatura, infine ogni parola estratta viene lemmatizzata.

### Dictionary
Il dizionario contiene il mapping tra le parole e i loro id.  
La sua creazione è stata realizzata tramite la classe `Dictionary` di `gensim.corpora`, che prende in input la trasctizione pre-processata.

### Corpus
Il corpus è stato creato con l'utilizzo della funzione `doc2bow` della classe `Dictionary`, e come parametro riceve il dizionario precedentemente creato.  
`doc2bow` converto il dizionario nel formato ***bag-of-words (BoW)***, semplicemente una lista di tuple `(token_id, token_count)`.

### Model
Come modello è stato usato ***Latent Dirichlet Allocation*** fornito dalla libreria `gensim.models`, con parametro `num_topics = 20`.


#### Visualization
- Rappresentazione grafica dei topics prodotti dal modello.
- Wordcloud del documento
