# Esercizio #2 - Content-to-Form
Usando i dati sulle definizioni date per ogni concetto presente all'interno del file `definizioni.xlsx` estrarre da WordNet il synset più appropriato.

## Concetti
Il file `definizioni.xlsx` contenente le definizioni è mappato in un dizionario associando le keys ai concetti.  

## Estrazione dei synset
I synset sono stati estratti da WordNet seguendo il principio del genus.  
Date le definizioni, per ogni concetto, estraiamo il lemma delle num_common_word parole più frequenti. 
Per ogni parola più frequente di ogni concetto, attraverso WordNet, estraggo i synset e da questi gli iponimi. Da questa lista prendendo la definizione e gli esempi di ogni componente, vado a creare il contesto.

## Score dei synset
Per assegnare uno score ai synset abbiamo utilizzato una funzione che identifica la somiglianza tra contesto trovato e parole più frequenti (lo score più alto lo avrà il synset il cui contesto assomiglia di più alle nostre definizioni).
Da qui, verranno estratti i 5 synset con score più alto.

### Funzione - data_to_dict():
Questa funzione crea un dizionario nella forma [concetto-lista definizioni] partendo dal file Excel.

### Funzione - frequency(dictionary, num_common_word)
Restituisce un dizionario in cui ogni concetto è assegnato alle num_common_word parole più frequenti nelle rispettive definizioni.

### Funzione - get_synset_score()
Preso ogni concetto: 
per ogni parola più frequente per quel concetto viene creata una lista di synset;
per ogni synset viene creata una lista di iponimi;
per ogni synset e iponimo viene generato il contesto.
A partire dal contesto, vengono presi gli esempi.
A ciascun synset verrà assegnato uno score nel seguente modo:
viene calcolata l'intersezione tra gli esempi del contesto del synset e le parole più frequenti per quel concetto, dividendo la lunghezza di questa lista per num_common_word, ovvero il numero di parole più frequenti considerate.

### Funzione - print_table()
Stampa la tabella degli score dei synset per ogni concetto, aggiungendo la definizione.

## Risultati
```

----- Best 5 sense for Emotion -----

╒═══════════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════╤═════════╕
│ Synset                    │ Definition                                                                               │   Score │
╞═══════════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════╪═════════╡
│ Synset('feel.v.05')       │ Have a feeling or perception about oneself in reaction to someone's behavior or attitude │   0.667 │
├───────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('affection.n.01')  │ A positive feeling of liking                                                             │   0.667 │
├───────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('feeling.n.01')    │ The experiencing of affective and emotional states                                       │   0.333 │
├───────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('impression.n.01') │ A vague idea in which some confidence is placed                                          │   0.333 │
├───────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('spirit.n.02')     │ The general atmosphere of a place or situation and the effect that it has on people      │   0.333 │
╘═══════════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════╧═════════╛


----- Best 5 sense for Person -----

╒═══════════════════════╤══════════════════════════════════════════════════╤═════════╕
│ Synset                │ Definition                                       │   Score │
╞═══════════════════════╪══════════════════════════════════════════════════╪═════════╡
│ Synset('human.a.02')  │ Relating to a person                             │   0.667 │
├───────────────────────┼──────────────────────────────────────────────────┼─────────┤
│ Synset('world.n.08')  │ All of the living human inhabitants of the earth │   0.667 │
├───────────────────────┼──────────────────────────────────────────────────┼─────────┤
│ Synset('person.n.01') │ A human being                                    │   0.667 │
├───────────────────────┼──────────────────────────────────────────────────┼─────────┤
│ Synset('person.n.02') │ A human body (usually including the clothing)    │   0.667 │
├───────────────────────┼──────────────────────────────────────────────────┼─────────┤
│ Synset('living.a.01') │ Pertaining to living persons                     │   0.667 │
╘═══════════════════════╧══════════════════════════════════════════════════╧═════════╛


----- Best 5 sense for Revenge -----

╒════════════════════════════╤═════════════════════════════════════════════╤═════════╕
│ Synset                     │ Definition                                  │   Score │
╞════════════════════════════╪═════════════════════════════════════════════╪═════════╡
│ Synset('dander.n.02')      │ A feeling of anger and animosity            │   0.667 │
├────────────────────────────┼─────────────────────────────────────────────┼─────────┤
│ Synset('fury.n.01')        │ A feeling of intense anger                  │   0.667 │
├────────────────────────────┼─────────────────────────────────────────────┼─────────┤
│ Synset('indignation.n.01') │ A feeling of righteous anger                │   0.667 │
├────────────────────────────┼─────────────────────────────────────────────┼─────────┤
│ Synset('infuriation.n.01') │ A feeling of intense anger                  │   0.667 │
├────────────────────────────┼─────────────────────────────────────────────┼─────────┤
│ Synset('umbrage.n.01')     │ A feeling of anger caused by being offended │   0.667 │
╘════════════════════════════╧═════════════════════════════════════════════╧═════════╛


----- Best 5 sense for Brick -----

╒══════════════════════════╤═════════════════════════════════════════════════════════════════════════════════════════════════╤═════════╕
│ Synset                   │ Definition                                                                                      │   Score │
╞══════════════════════════╪═════════════════════════════════════════════════════════════════════════════════════════════════╪═════════╡
│ Synset('material.n.01')  │ The tangible substance that goes into the makeup of a physical object                           │   0.667 │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('material.n.02')  │ Information (data or ideas or observations) that can be used or reworked into a finished form   │   0.667 │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('moon.n.02')      │ Any object resembling a moon                                                                    │   0.667 │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('property.n.05')  │ Any movable articles or objects used on the set of a play or movie                              │   0.667 │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ Synset('aggregate.n.02') │ Material such as sand or gravel used with cement and water to make concrete, mortar, or plaster │   0.667 │
╘══════════════════════════╧═════════════════════════════════════════════════════════════════════════════════════════════════╧═════════╛

