## Esercitazione #5 - "TM" - Implementazione di un esercizio di Topic Modeling

### DataSet
Il dataset utilizzato è ***[20 Newsgroups](http://qwone.com/~jason/20Newsgroups)***, una raccolta di circa 20.000 documenti di newsgroup, suddivisi (quasi) uniformemente in 20 diversi newsgroup.  
Non è presente una versione fisica del dataset poiché viene recuperato da sklearn, e per ogni email al suo interno non vengono considerati  
`header`, `footer` e `quotes` per evitare overfitting sui metadati.

### Pre-processing
Le sentence all'interno del dataset sono processate rimuovendo le stopwords e la punteggiatura, infine ogni parola estratta viene lemmatizzata.

### Dictionary
Il dizionario contiene il mapping tra le parole e i loro id.  
La sua creazione è stata realizzata tramite la classe `Dictionary` di `gensim.corpora`, che prende in input le news pre-processate.

### Corpus
Il corpus è stato creato con l'utilizzo della funzione `doc2bow` della classe `Dictionary`, e come parametro riceve il dizionario precedentemente creato.  
`doc2bow` converto il dizionario nel formato ***bag-of-words (BoW)***, semplicemente una lista di tuple `(token_id, token_count)`.

### Model
Come modello è stato usato ***Latent Dirichlet Allocation*** fornito dalla libreria `gensim.model`, con parametro `num_topics = 20`.

### Risultati

#### Topics
La seguente tabella mostra la classifica dei topics ordinata in modo decrescente sul punteggio di coerenza.  
Per ogni topic vengono mostrate le prime cinque parole, ognuna con la propria probabilità.
```
---------- Topics with the highest coherence score ----------
    - Number of top words to be extracted from each topic: 5

|   # | (Probability, ID)   | (Probability, ID)     | (Probability, ID)   | (Probability, ID)     | (Probability, ID)     |   Coherence score |
|-----+---------------------+-----------------------+---------------------+-----------------------+-----------------------+-------------------|
|   1 | (0.047, 'jesus')    | (0.04, 'faith')       | (0.039, 'bible')    | (0.032, 'christians') | (0.025, 'christian')  |          -1.1278  |
|   2 | (0.027, 'soldiers') | (0.025, 'military')   | (0.024, 'villages') | (0.024, 'war')        | (0.019, 'killed')     |          -1.38668 |
|   3 | (0.031, 'national') | (0.027, 'president')  | (0.025, 'press')    | (0.025, 'april')      | (0.024, 'white')      |          -1.42876 |
|   4 | (0.031, 'program')  | (0.026, 'space')      | (0.018, 'data')     | (0.016, 'files')      | (0.015, 'free')       |          -1.87359 |
|   5 | (0.062, 'people')   | (0.045, 'god')        | (0.031, 'evidence') | (0.024, 'reason')     | (0.018, 'course')     |          -1.89403 |
|   6 | (0.052, 'public')   | (0.047, 'government') | (0.034, 'law')      | (0.031, 'code')       | (0.019, 'private')    |          -1.98277 |
|   7 | (0.043, 'drive')    | (0.037, 'system')     | (0.022, 'card')     | (0.021, 'windows')    | (0.02, 'list')        |          -2.11999 |
|   8 | (0.061, 'time')     | (0.023, 'help')       | (0.017, 'bad')      | (0.017, 'lot')        | (0.016, 'post')       |          -2.15181 |
|   9 | (0.04, 'file')      | (0.033, 'source')     | (0.026, 'subject')  | (0.025, 'university') | (0.024, 'posting')    |          -2.23329 |
|  10 | (0.018, 'local')    | (0.016, 'matter')     | (0.016, 'pretty')   | (0.015, 'days')       | (0.014, 'death')      |          -2.44155 |
|  11 | (0.1, 'key')        | (0.067, 'chip')       | (0.043, 'master')   | (0.041, 'serial')     | (0.034, 'encryption') |          -2.50129 |
|  12 | (0.069, 'power')    | (0.04, 'type')        | (0.033, 'stuff')    | (0.032, 'model')      | (0.032, 'sale')       |          -2.65807 |
|  13 | (0.111, 'physical') | (0.057, 'security')   | (0.047, 'books')    | (0.034, 'body')       | (0.029, 'looked')     |          -2.66835 |
|  14 | (0.064, 'senses')   | (0.043, 'support')    | (0.034, 'copy')     | (0.032, 'drives')     | (0.03, 'received')    |          -2.82466 |
|  15 | (0.046, 'black')    | (0.044, 'picture')    | (0.044, 'york')     | (0.043, 'chicago')    | (0.026, 'speaking')   |          -2.8871  |
|  16 | (0.044, 'team')     | (0.037, 'game')       | (0.029, 'car')      | (0.028, 'mail')       | (0.023, 'games')      |          -2.93032 |
|  17 | (0.101, 'advance')  | (0.083, 'news')       | (0.029, 'bunch')    | (0.024, 'rational')   | (0.024, 'koresh')     |          -3.96299 |
|  18 | (0.078, 'test')     | (0.066, 'graphics')   | (0.036, 'selling')  | (0.024, 'spacecraft') | (0.024, 'planet')     |          -5.65772 |
|  19 | (0.071, 'function') | (0.036, 'drug')       | (0.023, 'helps')    | (0.02, 'fee')         | (0.019, 'boys')       |          -9.27428 |
|  20 | (0.185, 'max')      | (0.038, 'rsa')        | (0.031, 'des')      | (0.027, 'died')       | (0.02, 'drugs')       |         -11.0872  |
```

#### Prediction
Le seguenti immagini mostrano il contenuto del documento e il topic con la massima probabilità associata a esso.  
Il topic che più rappresenta il documento, viene estratto prendendo quello con la massima probabilità tra tutta la distribuzione.
```
---------- Document #90 ----------

Does anyone know what processor the Atari 2600 used? What I'm looking for is th
e pin-outs for the Atari 2600.... the schematics for it it... does anyone have
any idea where I could find this or any related information? This is very impor
tant. Also, are the ROM chips that were used fo rthe 2600 games still available
, or were they propreitary? Please email me with any responces, as this is very
 important.. Thanks a million...

BTW- Anyone who works/has worked for Atari, I could really use your help with i
nfo on the old 2600, please email me if you are willing to help me.... thatnks
alot!!

---------- Prediction ----------

    - Best topic: 5
    - Accuracy 22.494 %
    - Topic keywords: ['program', 'space', 'data', 'files', 'free', 'current', 'running', 'programs', 'window', 'include']
```

```
---------- Document #3411 ----------

In response to a lot of email I've gotten, I need to clarify my position.

I am not in favor of paganism.

I am not in favor of the Easter Bunny or other non-Christian aspects of
Easter as presently celebrated.  (Incidentally, Easter eggs are not
non-Christian; they are a way of ending the Lenten fast.)

My point was to distinguish between
  (1) intentionally worshipping a pagan deity, and
  (2) doing something which may once have had pagan associations, but
nowadays is not understood or intended as such.

Many people who are doing (2) are being accused of (1).

It would be illogical to claim that one is "really" worshipping a
pagan deity without knowing it.  Worship is a matter of intention.
One cannot worship without knowing that one is doing so.

---------- Prediction ----------

    - Best topic: 19
    - Accuracy 22.351 %
    - Topic keywords: ['people', 'god', 'evidence', 'reason', 'course', 'israel', 'read', 'true', 'question', 'life']

```

#### Visualization
Rappresentazione grafica dei topics prodotti dal modello.
<img src="../assets/tm/topic_data_visualization.png">