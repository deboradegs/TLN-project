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
viene calcolata l'intersezione tra gli esempi del contesto del synset e le parole più frequenti per quel concetto, dividendo la lunghezza di questa lista (per la lungheza degli esempi unita alla lunghezza della lista di parole più frequenti OPPURE per num_common_word, ovvero il numero di parole più frequenti considerate).

### Funzione - print_table()
Stampa la tabella degli score dei synset per ogni concetto, aggiungendo la definizione.

## Risultati
```
----- Best 5 sense for Emotion -----

╒═════════════════════════════╤═══════════════════════════════════════════════╤═════════╕
│ Synset                      │ Definition                                    │   Score │
╞═════════════════════════════╪═══════════════════════════════════════════════╪═════════╡
│ Synset('emotion.n.01')      │ Any strong feeling                            │    0.25 │
├─────────────────────────────┼───────────────────────────────────────────────┼─────────┤
│ Synset('enthusiasm.n.01')   │ A feeling of excitement                       │    0.25 │
├─────────────────────────────┼───────────────────────────────────────────────┼─────────┤
│ Synset('expectation.n.03')  │ The feeling that something is about to happen │    0.25 │
├─────────────────────────────┼───────────────────────────────────────────────┼─────────┤
│ Synset('fearlessness.n.01') │ Feeling no fear                               │    0.25 │
├─────────────────────────────┼───────────────────────────────────────────────┼─────────┤
│ Synset('agitation.n.03')    │ The feeling of being agitated; not calm       │    0.2  │
╘═════════════════════════════╧═══════════════════════════════════════════════╧═════════╛


----- Best 5 sense for Person -----

╒════════════════════════╤══════════════════════════════╤═════════╕
│ Synset                 │ Definition                   │   Score │
╞════════════════════════╪══════════════════════════════╪═════════╡
│ Synset('person.n.01')  │ A human being                │   0.333 │
├────────────────────────┼──────────────────────────────┼─────────┤
│ Synset('living.a.01')  │ Pertaining to living persons │   0.333 │
├────────────────────────┼──────────────────────────────┼─────────┤
│ Synset('life.n.08')    │ A living person              │   0.333 │
├────────────────────────┼──────────────────────────────┼─────────┤
│ Synset('abjurer.n.01') │ A person who abjures         │   0.25  │
├────────────────────────┼──────────────────────────────┼─────────┤
│ Synset('anomaly.n.02') │ A person who is unusual      │   0.25  │
╘════════════════════════╧══════════════════════════════╧═════════╛


----- Best 5 sense for Revenge -----

╒════════════════════════════╤══════════════════════════════════╤═════════╕
│ Synset                     │ Definition                       │   Score │
╞════════════════════════════╪══════════════════════════════════╪═════════╡
│ Synset('indignation.n.01') │ A feeling of righteous anger     │   0.5   │
├────────────────────────────┼──────────────────────────────────┼─────────┤
│ Synset('infuriation.n.01') │ A feeling of intense anger       │   0.5   │
├────────────────────────────┼──────────────────────────────────┼─────────┤
│ Synset('dander.n.02')      │ A feeling of anger and animosity │   0.286 │
├────────────────────────────┼──────────────────────────────────┼─────────┤
│ Synset('emotion.n.01')     │ Any strong feeling               │   0.25  │
├────────────────────────────┼──────────────────────────────────┼─────────┤
│ Synset('enthusiasm.n.01')  │ A feeling of excitement          │   0.25  │
╘════════════════════════════╧══════════════════════════════════╧═════════╛


----- Best 5 sense for Brick -----

╒══════════════════════════════════╤═══════════════════════════════════════════════════╤═════════╕
│ Synset                           │ Definition                                        │   Score │
╞══════════════════════════════════╪═══════════════════════════════════════════════════╪═════════╡
│ Synset('packing_material.n.01')  │ Any material used especially to protect something │   0.4   │
├──────────────────────────────────┼───────────────────────────────────────────────────┼─────────┤
│ Synset('packaging.n.03')         │ Material used to make packages                    │   0.4   │
├──────────────────────────────────┼───────────────────────────────────────────────────┼─────────┤
│ Synset('roofing.n.01')           │ Material used to construct a roof                 │   0.4   │
├──────────────────────────────────┼───────────────────────────────────────────────────┼─────────┤
│ Synset('bedding_material.n.01')  │ Material used to provide a bed for animals        │   0.333 │
├──────────────────────────────────┼───────────────────────────────────────────────────┼─────────┤
│ Synset('coloring_material.n.01') │ Any material used for its color                   │   0.333 │
╘══════════════════════════════════╧═══════════════════════════════════════════════════╧═════════╛

