# Esercizio #2 - Content-to-Form
Usando i dati sulle definizioni date per ogni concetto presente all'interno del file `definizioni.xlsx` estrarre da WordNet il synset più appropriato.

## Concetti
Il file `definizioni.xlsx` contenente le definizioni è mappato in un dizionario associando le keys ai concetti.  

## Estrazione dei synset
I synset sono stati estratti da WordNet seguendo il principio del genus.
Per seguire il principio del genus, abbiamo filtrato il contesto prendendo solo i termini che hanno il primo livello di iperonimia in comune con le 5 parole più frequenti all'interno delle definizioni.

## Score dei synset
Per assegnare uno score ai synset abbiamo utilizzato una funzione che identifica la somiglianza tra contesto trovato dai synset e parole più frequenti (lo score più alto lo avrà il synset il cui contesto assomiglia di più alle nostre definizioni).
Da qui, verranno estratti i 5 synset con score più alto.

### Funzione - data_to_dict():
Questa funzione crea un dizionario nella forma [concetto-lista definizioni] partendo dal file Excel.

### Funzione - disambiguation(dictionary, num_common_word)
Effettua la disambiguazione (utilizzando lesk) di ogni parola.
Prese le 5 disambiguazioni più frequenti per ogni concetto e ne prende gli iperonimi. 
Restituisce un dizionario in cui viene associato ad ognuno di questi 5 il suo iperonimo.

### Funzione - get_synset_score_disamb()
Preso ogni concetto: 
per ogni synset più frequente per quel concetto viene presa la parola corrispondente (da synset a parola con lemma.name()), e ne viene creata una lista di synset;
per ogni synset della parola viene trovato l'iperonimo;
vengono confrontati gli iperonimi della parola disambiguata con gli iperonimi dei synset della disambiguazione e vengono presi soltanto i synset con iperonimo in comune (genus);
per ogni synset salvato con genus in comune, vengono presi gli iponimi e dagli iponimi viene generato il contesto (definizione lemmatizzata e esempi lemmatizzati).
A ciascun synset (con genus in comune) verrà assegnato uno score nel seguente modo:
viene calcolata l'intersezione tra il contesto del synset e le parole disambiguate più frequenti per quel concetto, dividendo la lunghezza di questa lista per num_common_word, ovvero il numero di parole più frequenti considerate.

### Funzione - print_table()
Stampa la tabella degli score dei synset per ogni concetto, aggiungendo la definizione.


## Seconda Idea:
Abbiamo notato che in molte definizioni è presente il genus e quindi, per come abbiamo selezionato il contesto, gli iponimi dovrebbero essere anche gli iponimi della parola che stiamo cercando. 
Per il principio del Genus-differentia dovrebbe quindi essere spesso presente la nostra parola → abbiamo pensato di contare le parole più frequenti in tutte le definizioni.

## Risultati:
```
----- Best 5 sense for Emotion -----

                                                                        Definition  Score
Synset('human.a.02')                                          Relating to a person   0.50
Synset('state.n.06')                            A state of depression or agitation   0.50
Synset('spirit.n.02')            The general atmosphere of a place or situation...   0.25
Synset('tactile_property.n.01')                      A property perceived by touch   0.25


----- Best 5 sense for Person -----

                                                              Definition  Score
Synset('person.n.01')                                      A human being  1.000
Synset('human.a.02')                                Relating to a person  0.667
Synset('live.v.07')           Pursue a positive and satisfying existence  0.667
Synset('person.n.03')  A grammatical category used in the classificat...  0.333
Synset('spirit.n.02')  The general atmosphere of a place or situation...  0.000


----- Best 5 sense for Revenge -----

                                                                        Definition  Score
Synset('emotion.n.01')                                          Any strong feeling   0.50
Synset('spirit.n.02')            The general atmosphere of a place or situation...   0.25
Synset('tactile_property.n.01')                      A property perceived by touch   0.25
Synset('state.n.06')                            A state of depression or agitation   0.25
Synset('person.n.01')                                                A human being   0.25


----- Best 5 sense for Brick -----

                                                                       Definition  Score
Synset('person.n.01')                                               A human being   0.75
Synset('natural_process.n.01')  A process existing in or produced by nature (r...   0.75
Synset('emotion.n.01')                                         Any strong feeling   0.75
Synset('object.n.05')           (computing) a discrete item that provides a de...   0.50
Synset('material.n.05')         A person judged suitable for admission or empl...   0.50
