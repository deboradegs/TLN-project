## Esercizio 7: frutta con la m
Esercizio in cui si specifica una categoria (ad es.“fruit” oppure “at supermarket” (più difficile)) assieme ad una lettera di inizio parola. Creare un gioco in cui il sistema crea combinazioni casuali di input e prova a sfidare sul tempo un utente

## Idea
Quando il gioco inizia, viene scelta randomicamente la domanda di partenza (get_random_category). Se viene scelto 'type of', il programma andrà a pescare a caso una categoria dalla lista di iperonimi (get_random_hyponym), se viene scelto 'parts of', pescherà dalla lista di meronimi (get_random_meronym), con una lettera casuale.
Se quella categoria non ha iponimi/meronimi, verrà eseguita una nuova scelta randomica che ne abbia almeno uno.

Mentre l'utente digita le sue risposte, il computer crea una lista di iponimi/meronimi (usando WordNet) (find_hyponym, find_meronym).

Scaduto il tempo, verrà mostrato lo score: per il computer il massimo, per l'utente si controllerà quante parole ha trovato rispetto a quelle del computer.