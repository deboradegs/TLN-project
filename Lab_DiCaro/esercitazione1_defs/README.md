## Esercitazione #1 - "Defs" - Misurazione dell'overlap lessicale tra una serie di definizioni per concetti generici/specifici e concreti/astratti.

### Concetti
All'interno della directory resource è presente il file `definizioni.xlsx` contenente un numero finito di definizioni per ogni concetto.  
I concetti da analizzare presentano la seguente suddivisione:
- Concreti:
  - Person (generico)
  - Brick (specifico)
- Astratti
  - Emotion (generico)
  - Revenge (specifico)

### Funzione - stem_lem(text)
Pulisce il testo da stop_words, punteggiatura e maiuscole e lo tokenizza, tuttavia non mette nella lista di token la parola originale pulita, ma il suo stemma, poiché abbiamo ritenuto più corretto a livello di overlap che la sovrapposizione tra parole non fosse influenzata dalle coniugazioni che ognuna di esse può avere. Abbiamo scelto lo stemma e non il lemma poiché il lemma non distingue tra verbo e sostantivo, però la nostra opinione è che se si sta parlando di, ad esempio, "feeling" o di "feel", l'argomento è sempre il sentimento, e quindi andrebbero considerate come la stessa parola.


### Funzione - frequency(dictionary, num_common_word)
Calcola la frequenza dei token nel testo e ritorna un dizionario con le prime num_common_word parole più frequenti per ogni concetto.

### Funzione - word_in_sentence(dictionary, frequency)
Calcola lo score delle parole più frequenti. L'idea è quella di contare in quante definizioni del nostro concetto la parolaè presente, lo score di ogni parola sarà quindi data dalla distribuzione della parola tra le definizioni (se una parola è presente in tutte le definizioni lo score sarà massimo).

### Funzione - overlap_words(dictionary, word1, word2)
Calcola l'overlap tra due concetti, facendo la media tra gli score di ogni concetto.
Commentata vi è una versione che calcola lo score prendendo in considerazione la distribuzione di ogni parola più frequente tra i due concetti, se quindi è equamente distribuita lo score è massimo.


### Risultati
```
-------- The five most common words in each definition by concept --------
╒═══════════╤════════╤════════╤═══════════╤══════════╤═════════╕
│ Concept   │ 1      │ 2      │ 3         │ 4        │ 5       │
╞═══════════╪════════╪════════╪═══════════╪══════════╪═════════╡
│ Emotion   │ feel   │ human  │ someth    │ state    │ live    │
├───────────┼────────┼────────┼───────────┼──────────┼─────────┤
│ Person    │ human  │ person │ live      │ individu │ certain │
├───────────┼────────┼────────┼───────────┼──────────┼─────────┤
│ Revenge   │ someon │ anger  │ feel      │ emot     │ action  │
├───────────┼────────┼────────┼───────────┼──────────┼─────────┤
│ Brick     │ use    │ build  │ construct │ object   │ materi  │
╘═══════════╧════════╧════════╧═══════════╧══════════╧═════════╛


-------- Definitions overlap score for each concept --------

╒═══════════╤═════════╕
│ Concept   │   Score │
╞═══════════╪═════════╡
│ Emotion   │   0.275 │
├───────────┼─────────┤
│ Person    │   0.281 │
├───────────┼─────────┤
│ Revenge   │   0.3   │
├───────────┼─────────┤
│ Brick     │   0.606 │
╘═══════════╧═════════╛



-------- Concept overlap score --------


╒═══════════════════════╤═════════╕
│ Concepts grouped by   │   Score │
╞═══════════════════════╪═════════╡
│ Concrete              │  0.4435 │
├───────────────────────┼─────────┤
│ Abstract              │  0.2875 │
├───────────────────────┼─────────┤
│ Generic               │  0.278  │
├───────────────────────┼─────────┤
│ Specific              │  0.453  │
╘═══════════════════════╧═════════╛
