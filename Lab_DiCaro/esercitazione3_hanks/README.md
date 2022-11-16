# Esercizio #3 - Hanks 
Implementazione della teoria sulle valenze di Patrick Hanks

## Verbo
Per svolgere l'esercitazione è stato scelto il verbo transitivo *get*.  

## Corpus
Dalla piattaforma ***[Sketch Engine](https://www.sketchengine.eu/)*** abbiamo recuperato le prime 10.000 frasi ordinate per ***GDEX (Good Dictionary Examples)***.  
GDEX è un sistema di valutazione delle frasi in relazione alla loro idoneità a fungere da esempi di dizionario o da buoni esempi a fini didattici.  
All'interno della directory resource è disponibile si il file completo `get.csv` sia una versione ridotta  
`get_small.csv` contenente le prime 1000 frasi.

## Parsing
La fase di parsing è stata realizzata con l'uso della libreria ***[SpaCy](https://spacy.io/)*** tramite un parsing a dipendenze per ogni frase in modo da estrarre i due argomenti: ***subj e obj***.

## Disambiguazione
La disambiguazione di ogni argomento viene effettuata tramite l'algoritmo di Lesk usando la frase di appartenenza come contesto.  
In seguito, il synset fornito da Lesk viene utilizzato per estrarre il suo super-senso da ***[CSI (Coarse Sense Inventory)](https://sapienzanlp.github.io/csi/)***.  
All'interno della directory resource è disponibile il file `wn_synset2csi.txt` contenente il mapping tra wordnet e le label CSI, e ogni synset è individuato attraverso il proprio offset. 

## Supersensi
I super-sensi ottenuti vengono raggruppati per calcolarne la frequenza, e questo procedimento è applicato sia alle frasi con solo un argomento (*None-obj* oppure *sub-None*) che alle frasi con entrambi gli argomenti.

## Significati del verbo
Creiamo le combinazioni di tutti i supersensi divisi per valenza. Da queste liste andiamo a calcolare la percentuale di presenza di ogni combinazione e prendiamo le 20 più ricorrenti. Queste saranno i significati attribuibili al verbo.


## Funzioni
### Funzione - get_supersense_from_file()
Apre il file `wn_synset2csi.txt` e crea un dizionario con chiave: identificativo in Wordnet della parola e valore: supersenso corrispondente

### Funzione - get_sentences_from_file()
Apre il file `get.csv` e crea una lista contenente le frasi all'interno del file (estratte da SketchEngine)

### Funzione - parser_verbs(sentences, verbo)
Per ogni frase raccolta, crea un dizionario con l'analisi effettuata da spacy, aggiungendo il supersenso (*get_supersense*) del soggetto e il supersenso dell'oggetto.
Restituisce una lista di dizionari di ogni frase.

### Funzione - get_supersense(sentence, word)
Dopo aver disambiguato la parola all'interno della frase specificata come argomento attraverso la funzione *lesk*, viene raccolto l'offset del synset della parola disambiguata, e viene cercato il synset trovato all'interno del dizionario *csi_dict*

### Funzione - meanings(sentence_analysis)
Crea 3 tabelle: una per le frasi con valenza 2, e due per le frasi con valenza 1 (sub e obj), dove in ogni riga c'è la combinazione dei due supersensi (o del supersenso e None, nel caso di valenza 1), in più viene fatto un conteggio delle frasi trovate con i 3 tipi di valenza differenti.
Inoltre, sulla riga della combinazione dei supersensi abbiamo aggiunto le colonne conteggio e percentuale (*create_percentage*), per indicare quanto è presente quella combinazione nel corpus di frasi.

### Funzione - create_percentage(combination_list, tmp)
Conta le occorrenze di quella combinazione all'interno delle frasi con la valenza in questione, e crea la percentuale corrispondente, restituendo il tutto ordinato in senso decrescente.

## Risultati
```
valenza 2 in 2197 frasi.

╒════╤═════════════════════════════════════════════════════╤═════════╤══════════════╕
│    │ Combination [Subject - Object]                      │   Count │ Percentage   │
╞════╪═════════════════════════════════════════════════════╪═════════╪══════════════╡
│  0 │ ('BIOLOGY_', 'BIOLOGY_')                            │     407 │ 18.525%      │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  1 │ ('BIOLOGY_', 'PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_') │     137 │ 6.236%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  2 │ ('BIOLOGY_', 'MATHEMATICS_')                        │     123 │ 5.599%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  3 │ ('BIOLOGY_', 'CRAFT_ENGINEERING_AND_TECHNOLOGY_')   │      90 │ 4.096%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  4 │ ('BIOLOGY_', 'CULTURE_ANTHROPOLOGY_AND_SOCIETY_')   │      90 │ 4.096%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  5 │ ('BIOLOGY_', 'GENERAL_')                            │      69 │ 3.141%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  6 │ ('BIOLOGY_', 'BUSINESS_ECONOMICS_AND_FINANCE_')     │      64 │ 2.913%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  7 │ ('BIOLOGY_', 'LAW_AND_CRIME_')                      │      60 │ 2.731%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  8 │ ('BIOLOGY_', 'MEDIA_')                              │      50 │ 2.276%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│  9 │ ('BIOLOGY_', 'ART_ARCHITECTURE_AND_ARCHAEOLOGY_')   │      50 │ 2.276%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 10 │ ('BIOLOGY_', 'WARFARE_DEFENSE_AND_VIOLENCE_')       │      50 │ 2.276%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 11 │ ('BIOLOGY_', 'HEALTH_AND_MEDICINE_')                │      49 │ 2.23%        │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 12 │ ('BIOLOGY_', 'LANGUAGE_AND_LINGUISTICS_')           │      45 │ 2.048%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 13 │ ('BIOLOGY_', 'EDUCATION_AND_SCIENCE_')              │      45 │ 2.048%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 14 │ ('BIOLOGY_', 'MUSIC_SOUND_AND_DANCING_')            │      41 │ 1.866%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 15 │ ('BIOLOGY_', 'CHEMISTRY_AND_MINERALOGY_')           │      34 │ 1.548%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 16 │ ('BIOLOGY_', 'SPORT_GAMES_AND_RECREATION_')         │      30 │ 1.365%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 17 │ ('BIOLOGY_', 'SPACE_AND_TOUCH_')                    │      29 │ 1.32%        │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 18 │ ('BIOLOGY_', 'LITERATURE_AND_THEATRE_')             │      28 │ 1.274%       │
├────┼─────────────────────────────────────────────────────┼─────────┼──────────────┤
│ 19 │ ('BIOLOGY_', 'POLITICS_GOVERNMENT_AND_NOBILITY_')   │      27 │ 1.229%       │
╘════╧═════════════════════════════════════════════════════╧═════════╧══════════════╛

valenza 1 con solo soggetto in 2042 frasi.

╒════╤═══════════════════════════════════════════════╤═════════╤══════════════╕
│    │ Combination [Subject - Object]                │   Count │ Percentage   │
╞════╪═══════════════════════════════════════════════╪═════════╪══════════════╡
│  0 │ ('BIOLOGY_', None)                            │    1556 │ 76.2%        │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  1 │ ('CULTURE_ANTHROPOLOGY_AND_SOCIETY_', None)   │      66 │ 3.232%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  2 │ ('CRAFT_ENGINEERING_AND_TECHNOLOGY_', None)   │      41 │ 2.008%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  3 │ ('BUSINESS_ECONOMICS_AND_FINANCE_', None)     │      37 │ 1.812%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  4 │ ('POLITICS_GOVERNMENT_AND_NOBILITY_', None)   │      28 │ 1.371%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  5 │ ('GEOGRAPHY_AND_PLACES_', None)               │      21 │ 1.028%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  6 │ ('LAW_AND_CRIME_', None)                      │      21 │ 1.028%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  7 │ ('MATHEMATICS_', None)                        │      19 │ 0.93%        │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  8 │ ('COMPUTING_', None)                          │      18 │ 0.881%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  9 │ ('LANGUAGE_AND_LINGUISTICS_', None)           │      17 │ 0.833%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 10 │ ('PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_', None) │      16 │ 0.784%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 11 │ ('CHEMISTRY_AND_MINERALOGY_', None)           │      15 │ 0.735%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 12 │ ('EDUCATION_AND_SCIENCE_', None)              │      14 │ 0.686%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 13 │ ('SPORT_GAMES_AND_RECREATION_', None)         │      14 │ 0.686%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 14 │ ('GENERAL_', None)                            │      14 │ 0.686%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 15 │ ('MUSIC_SOUND_AND_DANCING_', None)            │      14 │ 0.686%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 16 │ ('RELIGION_MYSTICISM_AND_MYTHOLOGY_', None)   │      12 │ 0.588%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 17 │ ('TRANSPORT_AND_TRAVEL_', None)               │      12 │ 0.588%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 18 │ ('MEDIA_', None)                              │      11 │ 0.539%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 19 │ ('TEXTILE_FASHION_AND_CLOTHING_', None)       │      11 │ 0.539%       │
╘════╧═══════════════════════════════════════════════╧═════════╧══════════════╛

valenza 1 con solo oggetto in 1656 frasi.

╒════╤═══════════════════════════════════════════════╤═════════╤══════════════╕
│    │ Combination [Subject - Object]                │   Count │ Percentage   │
╞════╪═══════════════════════════════════════════════╪═════════╪══════════════╡
│  0 │ (None, 'BIOLOGY_')                            │     301 │ 18.176%      │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  1 │ (None, 'PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_') │     104 │ 6.28%        │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  2 │ (None, 'MATHEMATICS_')                        │      97 │ 5.857%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  3 │ (None, 'CRAFT_ENGINEERING_AND_TECHNOLOGY_')   │      91 │ 5.495%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  4 │ (None, 'BUSINESS_ECONOMICS_AND_FINANCE_')     │      75 │ 4.529%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  5 │ (None, 'LAW_AND_CRIME_')                      │      74 │ 4.469%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  6 │ (None, 'HEALTH_AND_MEDICINE_')                │      74 │ 4.469%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  7 │ (None, 'LANGUAGE_AND_LINGUISTICS_')           │      63 │ 3.804%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  8 │ (None, 'MEDIA_')                              │      62 │ 3.744%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│  9 │ (None, 'GENERAL_')                            │      58 │ 3.502%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 10 │ (None, 'EDUCATION_AND_SCIENCE_')              │      58 │ 3.502%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 11 │ (None, 'CULTURE_ANTHROPOLOGY_AND_SOCIETY_')   │      53 │ 3.2%         │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 12 │ (None, 'MUSIC_SOUND_AND_DANCING_')            │      51 │ 3.08%        │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 13 │ (None, 'ART_ARCHITECTURE_AND_ARCHAEOLOGY_')   │      40 │ 2.415%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 14 │ (None, 'POLITICS_GOVERNMENT_AND_NOBILITY_')   │      37 │ 2.234%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 15 │ (None, 'SPACE_AND_TOUCH_')                    │      36 │ 2.174%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 16 │ (None, 'SPORT_GAMES_AND_RECREATION_')         │      35 │ 2.114%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 17 │ (None, 'TEXTILE_FASHION_AND_CLOTHING_')       │      31 │ 1.872%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 18 │ (None, 'COMPUTING_')                          │      30 │ 1.812%       │
├────┼───────────────────────────────────────────────┼─────────┼──────────────┤
│ 19 │ (None, 'WARFARE_DEFENSE_AND_VIOLENCE_')       │      30 │ 1.812%       │
╘════╧═══════════════════════════════════════════════╧═════════╧══════════════╛
