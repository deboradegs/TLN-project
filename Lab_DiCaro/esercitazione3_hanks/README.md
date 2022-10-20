## Esercitazione #3 - "Hanks" - Implementazione della teoria sulle valenze di Patrick Hanks.

### Verbo
Per svolgere l'esercitazione è stato scelto il verbo transitivo ***take***.  

### Corpus
Dalla piattaforma ***[Sketch Engine](https://www.sketchengine.eu/)*** sono state recuperate le prime 10.000 frasi ordinate per ***GDEX (Good Dictionary Examples)***.  
GDEX è un sistema di valutazione delle frasi in relazione alla loro idoneità a fungere da esempi di dizionario o  
da buoni esempi a fini didattici.  
All'interno della directory resource è disponibile si il file completo `take.csv` sia una versione ridotta  
`take_small.csv` contenente le prime 1000 frasi.

### Parsing
La fase di parsing è stata realizzata con l'uso della libreria ***[SpaCy](https://spacy.io/)*** tramite un parsing a dipendenze per ogni frase  
in modo da estrarre i due argomenti: ***subj e obj***.

### Disambiguazione
La disambiguazione di ogni argomento viene effettuata tramite l'algoritmo di Lesk usando la frase di appartenenza come contesto.  
In seguito, il synset fornito da Lesk viene utilizzato per estrarre il suo super-senso da ***[CSI (Coarse Sense Inventory)](https://sapienzanlp.github.io/csi/)***.  
All'interno della directory resource è disponibile il file `wn_synset2csi.txt` contenente il mapping tra wordnet e le label CSI,  
e ogni synset è individuato attraverso il proprio offset.  
Infine i super-sensi ottenuti vengono raggruppati per calcolarne la frequenza, e questo procedimento è applicato sia alle  
frasi con solo un argomento o entrambi.

### Risultati

```

-------- 2-ARGS (subj and obj) --------

There are 4854 sentences
    - number of meanings found: 4748
    - number of different meanings found: 771
    - 15 most common are:

| Subj                      | Obj                                  |   Count | Percentage   |
|---------------------------+--------------------------------------+---------+--------------|
| LANGUAGE_AND_LINGUISTICS_ | LANGUAGE_AND_LINGUISTICS_            |     453 | 9.54%        |
| LANGUAGE_AND_LINGUISTICS_ | TIME_                                |     209 | 4.40%        |
| LANGUAGE_AND_LINGUISTICS_ | SPACE_AND_TOUCH_                     |     196 | 4.13%        |
| LANGUAGE_AND_LINGUISTICS_ | HISTORY_                             |     130 | 2.74%        |
| LANGUAGE_AND_LINGUISTICS_ | PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_  |     130 | 2.74%        |
| LANGUAGE_AND_LINGUISTICS_ | BIOLOGY_                             |     120 | 2.53%        |
| LANGUAGE_AND_LINGUISTICS_ | MUSIC_SOUND_AND_DANCING_             |      97 | 2.04%        |
| LANGUAGE_AND_LINGUISTICS_ | EMOTIONS_                            |      87 | 1.83%        |
| LANGUAGE_AND_LINGUISTICS_ | ART_ARCHITECTURE_AND_ARCHAEOLOGY_    |      80 | 1.68%        |
| LANGUAGE_AND_LINGUISTICS_ | COMMUNICATION_AND_TELECOMMUNICATION_ |      68 | 1.43%        |
| LANGUAGE_AND_LINGUISTICS_ | MATHEMATICS_                         |      64 | 1.35%        |
| LANGUAGE_AND_LINGUISTICS_ | HEALTH_AND_MEDICINE_                 |      64 | 1.35%        |
| LANGUAGE_AND_LINGUISTICS_ | BUSINESS_ECONOMICS_AND_FINANCE_      |      64 | 1.35%        |
| LANGUAGE_AND_LINGUISTICS_ | POLITICS_GOVERNMENT_AND_NOBILITY_    |      62 | 1.31%        |
| LANGUAGE_AND_LINGUISTICS_ | NUMISMATICS_AND_CURRENCIES_          |      62 | 1.31%        |


-------- 1-ARGS (only subj) --------

There are 1167 sentences
    - number of meanings found: 1190
    - number of different meanings found: 39
    - 15 most common are:

| Subj                                 | Obj   |   Count | Percentage   |
|--------------------------------------+-------+---------+--------------|
| LANGUAGE_AND_LINGUISTICS_            | -     |     485 | 40.76%       |
| MEDIA_                               | -     |      51 | 4.29%        |
| BIOLOGY_                             | -     |      48 | 4.03%        |
| POLITICS_GOVERNMENT_AND_NOBILITY_    | -     |      44 | 3.70%        |
| ART_ARCHITECTURE_AND_ARCHAEOLOGY_    | -     |      44 | 3.70%        |
| BUSINESS_ECONOMICS_AND_FINANCE_      | -     |      37 | 3.11%        |
| MATHEMATICS_                         | -     |      34 | 2.86%        |
| PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_  | -     |      34 | 2.86%        |
| LAW_AND_CRIME_                       | -     |      32 | 2.69%        |
| NUMISMATICS_AND_CURRENCIES_          | -     |      31 | 2.61%        |
| CRAFT_ENGINEERING_AND_TECHNOLOGY_    | -     |      31 | 2.61%        |
| CULTURE_ANTHROPOLOGY_AND_SOCIETY_    | -     |      27 | 2.27%        |
| SPORT_GAMES_AND_RECREATION_          | -     |      26 | 2.18%        |
| MUSIC_SOUND_AND_DANCING_             | -     |      25 | 2.10%        |
| COMMUNICATION_AND_TELECOMMUNICATION_ | -     |      24 | 2.02%        |


-------- 1-ARGS (only obj) --------

There are 3292 sentences
    - number of meanings found: 3264
    - number of different meanings found: 42
    - 15 most common are:

| Subj   | Obj                                  |   Count | Percentage   |
|--------+--------------------------------------+---------+--------------|
| -      | LANGUAGE_AND_LINGUISTICS_            |     421 | 12.90%       |
| -      | PHILOSOPHY_PSYCHOLOGY_AND_BEHAVIOR_  |     234 | 7.17%        |
| -      | BIOLOGY_                             |     205 | 6.28%        |
| -      | SPACE_AND_TOUCH_                     |     176 | 5.39%        |
| -      | MUSIC_SOUND_AND_DANCING_             |     170 | 5.21%        |
| -      | EVALUATION_                          |     158 | 4.84%        |
| -      | EMOTIONS_                            |     141 | 4.32%        |
| -      | POLITICS_GOVERNMENT_AND_NOBILITY_    |     116 | 3.55%        |
| -      | COMMUNICATION_AND_TELECOMMUNICATION_ |      99 | 3.03%        |
| -      | MEDIA_                               |      94 | 2.88%        |
| -      | ART_ARCHITECTURE_AND_ARCHAEOLOGY_    |      93 | 2.85%        |
| -      | HEALTH_AND_MEDICINE_                 |      91 | 2.79%        |
| -      | BUSINESS_ECONOMICS_AND_FINANCE_      |      90 | 2.76%        |
| -      | MATHEMATICS_                         |      84 | 2.57%        |
| -      | GENERAL_                             |      76 | 2.33%        |

```



