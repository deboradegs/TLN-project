## Esercitazione #4 - "Segmentation" - Implementazione di un sistema di document segmentation.

### Documento
Il documento è il riusltato dell'unione di diversi riassunti estratti da Wikipedia con la libreria [Wikipedia-API ](https://pypi.org/project/Wikipedia-API/).  
Per questo esempio sono stati estratti i riuassunti delle seguenti pagine: `Mold, Cristiano Ronaldo, Pope Francis, Isaac Newton`.

### Corpus
Il corpus è una lista di pseudo frasi di lunghezza pari al parametro preso in input.  
Per questa esercitazione si usano frasi da 50 parole.

### Calcolo della similarità
L'intero corpus viene trasformato in una matrice `term-document` generata con l'uso della classe `TfidfVectorizer` della libreria [sklearn.feature_extraction.text](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).  
La similarità delle frasi è calcolata con l'uso del metodo `cosine_similarity` messo a disposizione dalla libreria [sklearn.metrics.pairwise](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html),  
che prende in input la matrice `term-document` e genera una matrice contenente tutti i possibili valori di similarità  
tra le pseudo frasi del corpus.

### Linee di taglio
La valutazione delle linee di taglio viene effettuata solo sui valori di similarità di coppie di pseudo frasi.  
Sono state considerate diverse misure per trovare le linee di taglio, guidato dall'andamento dei valori plottati. 

#### Valori minimi che rappresentano picchi delle valli (viene considerato il cambio dell'andamento dei valori)
![](/Users/marius/Desktop/UniTo/magistrale/primo anno/TLN/DiCaro/laboratorio/esercitazione_segmentation/valley.png) <br>

#### Minimi valori estremi, considerando un intorno (radius) di vicini
![](/Users/marius/Desktop/UniTo/magistrale/primo anno/TLN/DiCaro/laboratorio/esercitazione_segmentation/mins.png)
