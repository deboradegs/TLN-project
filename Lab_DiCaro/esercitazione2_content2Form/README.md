## Esercitazione #2 - Content-to-Form

### Consegna
Usando i dati sulle definizioni date per ogni concetto presente all'interno del file `definizioni.xlsx` estrarre  
da WordNet il synset più appropriato.

### Concetti
Il file `definizioni.xlsx` contenente le definizioni è mappato in un dizionario associando le keys ai concetti.  

### Estrazione dei synset
I synset sono stati estratti da WordNet seguendo il principio del *genus*.  
Date le definizioni, per ogni concetto, si sono estratte le *common words* e in seguito estratti i synset e i loro iponimi.  

### Classificazione dei synset
Per classificare i synset si è calcolato un valore di rank in modo da identificare quelli che più si avvicinano al concetto.  
Il valore di rank è calcolato tramite la funzione `Weighted Overlap`.

#### Weighted Overlap Score
Questa funzione confronta due vettori restituendo uno score di somiglianza.  
In particolare confronta la somiglianza tra il vettore delle *common word* e il vettore delle *context word*.

### Risultati

```
----- Best 5 sense for Emotion -----

| Synset                      | Definition                                                |   Weighted Overlap Score |
|-----------------------------+-----------------------------------------------------------+--------------------------|
| Synset('emotion.n.01')      | Any strong feeling                                        |                     0.25 |
| Synset('enthusiasm.n.01')   | A feeling of excitement                                   |                     0.25 |
| Synset('expectation.n.03')  | The feeling that something is about to happen             |                     0.25 |
| Synset('fearlessness.n.01') | Feeling no fear                                           |                     0.25 |
| Synset('disapproval.n.01')  | A feeling of disliking something or what someone is doing |                     0.25 |
```
```
----- Best 5 sense for Person -----

| Synset                 | Definition                   |   Weighted Overlap Score |
|------------------------+------------------------------+--------------------------|
| Synset('person.n.01')  | A human being                |                 0.333333 |
| Synset('living.a.01')  | Pertaining to living persons |                 0.333333 |
| Synset('life.n.08')    | A living person              |                 0.333333 |
| Synset('abjurer.n.01') | A person who abjures         |                 0.25     |
| Synset('anomaly.n.02') | A person who is unusual      |                 0.25     |
```
```
----- Best 5 sense for Revenge -----

| Synset                      | Definition                                  |   Weighted Overlap Score |
|-----------------------------+---------------------------------------------+--------------------------|
| Synset('indignation.n.01')  | A feeling of righteous anger                |                 0.5      |
| Synset('infuriation.n.01')  | A feeling of intense anger                  |                 0.5      |
| Synset('irascibility.n.01') | A feeling of resentful anger                |                 0.5      |
| Synset('dander.n.02')       | A feeling of anger and animosity            |                 0.285714 |
| Synset('umbrage.n.01')      | A feeling of anger caused by being offended |                 0.25     |
```
```
----- Best 5 sense for Brick -----

| Synset                           | Definition                                        |   Weighted Overlap Score |
|----------------------------------+---------------------------------------------------+--------------------------|
| Synset('packing_material.n.01')  | Any material used especially to protect something |                 0.4      |
| Synset('packaging.n.03')         | Material used to make packages                    |                 0.4      |
| Synset('roofing.n.01')           | Material used to construct a roof                 |                 0.4      |
| Synset('bedding_material.n.01')  | Material used to provide a bed for animals        |                 0.333333 |
| Synset('coloring_material.n.01') | Any material used for its color                   |                 0.333333 |
```



