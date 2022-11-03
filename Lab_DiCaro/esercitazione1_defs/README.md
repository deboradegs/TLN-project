## Esercitazione #1 - "Defs" - Misurazione dell'overlap lessicale tra una serie di definizioni per concetti generici/specifici e concreti/astratti.

### Concetti
All'interno della directory resource è presente il file `definizioni.xlsx` contenente un numero finito di definizioni per ogni concetto.  
I concetti da analizzare si dividono in due categorie:
- Concreti:
  - Person (generico)
  - Brick (specifico)
- Astratti
  - Emotion (generico)
  - Revenge (specifico)

### Funzione - stem_lem(text)
Crea un dizionario con chiavi corrispondenti ai concetti da analizzare, contenenti una lista delle 5 parole più frequenti estratte dalle rispettive definizioni.  
Il processo di estrazione delle parole inizia rimuovendo la punteggiatura e le stopwords da ogni definizione e termina con il conteggio della frequenza di ogni parola estratta.
![Screenshot (321)](https://user-images.githubusercontent.com/66359850/199749976-d84a8097-7c14-441c-bfb7-7a726e95a645.png)

### Funzione - get_definitions_overlap_score()
Calcola l'overlap score sfruttando le 5 cinque parole più frequenti precedentemente estratte per ogni concetto.  
Lo score è dato dalla somma della frequenza di ogni parola all'interno delle definizioni, normalizzato per il numero totale di definizioni disponibili per un dato concetto.

### Funzione - get_concept_overlap_score()
Calcola l'overlap score tra coppie di concetti facendo la media dello score.

### Risultati
```
-------- The five most common words in each definition by concept --------

| Concept   | 1       | 2      | 3        | 4         | 5            |
|-----------+---------+--------+----------+-----------+--------------|
| Emotion   | feeling | human  | feel     | something | state        |
| Person    | human   | person | living   | entity    | individual   |
| Revenge   | someone | anger  | feeling  | action    | reaction     |
| Brick     | used    | object | material | build     | construction |


-------- Definitions overlap score for each concept --------

| Concept   |   Score |
|-----------+---------|
| Emotion   |   0.253 |
| Person    |   0.252 |
| Revenge   |   0.267 |
| Brick     |   0.523 |


-------- Concept overlap score --------

| Concept           |   Score |
|-------------------+---------|
| concrete-concrete |  0.3875 |
| abstract-abstract |  0.26   |
| generic-generic   |  0.2525 |
| specific-specific |  0.395  |
```
