# Esercizio 6 - frutta con la m
Esercizio in cui si specifica una categoria (ad es.“fruit” oppure “at supermarket” (più difficile)) assieme ad una lettera di inizio parola. Creare un gioco in cui il sistema crea combinazioni casuali di input e prova a sfidare sul tempo un utente

## Idea
Quando il gioco inizia, viene scelta randomicamente la domanda di partenza (*get_random_category*). Se viene scelto 'type of', il programma andrà a pescare a caso una categoria dalla lista di iperonimi (*get_random_hyponym*), se viene scelto 'parts of', pescherà dalla lista di olonimi (*get_random_meronym*), con una lettera casuale.
Se quella categoria non ha iponimi/meronimi, verrà eseguita una nuova scelta randomica che ne abbia almeno uno.

Mentre l'utente digita le sue risposte, il computer crea una lista di iponimi/meronimi (usando WordNet) (*find_hyponym*, *find_meronym*).

Scaduto il tempo, verrà mostrato lo score: per il computer il massimo, per l'utente si controllerà quante parole ha trovato rispetto a quelle del computer.

## Funzioni
### Funzione - get_random_category()
Sceglie randomicamente tra 'types of' (per iponimi) e 'part of' (per meronimi)

### Funzione - get_random_hyponym()
Apre il file  `hyponyms.txt` e sceglie randomicamente una parola. Chiamando la funzione *find_hyponym* verifica se esistono iponimi per quell'iperonimo su Wordnet, e se non ne esistono, continua a cambiare iperonimo finchè non ne trova.

### Funzione - get_random_meronym()
Apre il file  `meronyms.txt` e sceglie randomicamente una parola. Chiamando la funzione *find_meronym* verifica se esistono meronimi per quell'olonimo su Wordnet, e se non ne esistono, continua a cambiare olonimo finchè non ne trova.

### Funzione - timer()
Implementa un countdown interattivo prima che inizi il gioco

### Funzione - game_computer()
Inizia il ragionamento del computer, a seconda che debba trovare iponimi o meronimi

### Funzione - find_hyponym(hyp, letter)
Cerca i synset dell'iperonimo e per quei synset cerca gli iponimi. Se iniziano con la lettera scelta, li aggiunge alla lista di risposte del computer.

### Funzione - find_meronym(mer, letter)
Cerca i synset dell'olonimo e per quei synset cerca i meronimi. Se iniziano con la lettera scelta, li aggiunge alla lista di risposte del computer.

### Funzione get_scores()
Calcola il punteggio dell'utente, confrontando quante parole ha inserito di quelle che ha trovato il computer.

## Risultati
Game starts.
Write as many words as possible in 30 secs!

Enter all the parts of:
------body------
With letter:
------r------


 The game will start in 6 seconds

 Insert word: res  

STOP!
----------- SCORE ----------
    - Your Score: 0.0
    - Your Words: ['res']

    - AI Score: 10
    - AI Words: ['respiratory_system', 'rear', 'rear_end', 'rump']
elisachierchiello@MBP-di-Elisa esercitazione6_fruttaconlam % 
