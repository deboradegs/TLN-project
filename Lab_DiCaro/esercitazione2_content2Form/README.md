## Esercizio #2 - Content-to-Form
Usando i dati sulle definizioni date per ogni concetto presente all'interno del file `definizioni.xlsx` estrarre da WordNet il synset più appropriato.

### Concetti
Il file `definizioni.xlsx` contenente le definizioni è mappato in un dizionario associando le keys ai concetti.  

### Estrazione dei synset
I synset sono stati estratti da WordNet seguendo il principio del genus.  
Date le definizioni, per ogni concetto, abbiamo le 3 parole più frequenti e in seguito per i lemmi di ogni parola abbiamo estratto i synset e gli iponimi dei synset, generando il contesto.  

### Score dei synset
Per assegnare uno score ai synset abbiamo utilizzato una funzione che identifica la somiglianza tra contesto trovato e parole più frequenti (lo score più alto lo avrà il synset il cui contesto assomiglia di più alle nostre definizioni).
Da qui, verranno estratti i 5 synset con score più alto.

## Funzione - data_to_dict():
Questa funzione crea un dizionario nella forma concetto-definizione partendo dal file Excel.

## Funzione - frequency(dictionary, frequenza)
Restituisce un dizionario che per ogni concetto ha le |frequenza| parole più frequenti per ogni definizione.

## Funzione - get_synset_context()
Preso ogni concetto, presa ogni parola più frequente



### Risultati

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
