# Client-Server Network

## Team:
Composizione del team (sdona):
- Satriano Daniel (MAT = 919053)
- Cavallini Francesco (MAT = 920835)


## Repository:
Di seguito viene linkata la repository di Git-Lab
https://gitlab.com/processo-e-sviluppo-software/2023_assignment1_PythonPipeline.git


## Bibliografia:
Per eseguire l'assignment abbiamo optato di reperire il codice di un applicazione open-source. Il seguente link contiene il codice originale per l'implementazione dei file `client.py` e `server.py`: https://github.com/katmfoo/python-client-server

Dal link è possibile visualizzare il file [README.md](https://github.com/katmfoo/python-client-server/blob/master/README.md) nel quale vengono illustrate le funzionalità del programma.


## Stato di sviluppo
Vengono di seguito riportati gli obbiettivi per il completamento del progetto
### To-do:
- [x] `before_script`: Installazione di python sul git-lab
    
    Step necessario per l'installazione di:
    - *venv* 
        necessario per la creazione ed attivazione dell'ambiente virtuale python e l'esecuzione del codice. (sempre eseguito nella sezione di `before_script`)
    - *pip*. 
        necessario ad installare le dependencies
    
    Vengono poi aggiornate ed installate le librerie di sistema con `upgrade` e `update`.
- [x] `Build-job`: build del progetto
    
    Stage del progetto necessario per l'installazione delle dependencies dal file `requirements.txt`. 
    
    In questo job vengono installate le librerie tramite il comando `pip install` e dove gli script Python verranno eseguiti.
    
    Al momento il file delle dependencies è vuoto in quanto gli import utilizzati sono tutte librerie base di python, queste infatti sono:
    - `socket`
    - `threading`
    - `sys`
    
    Caso in cui verrebbe modificato il progetto rendendo necessario l'inserimento di altre dependencies sarà semplicemente possibile modificare il file `requirements.txt`

- [x] `Verify-job`: eseguire *Prospector* e *Bandit*
    
    Step necessario per il miglioramento del codice. 
    - L'esecuzione del prospector ci aiuta garantire il rispetto degli standard di codifica e fornisce approfondimenti su potenziali problemi prima di eseguire il codice. È uno strumento prezioso per mantenere la qualità del codice nei progetti Python.
    - L'esecuzione di bandit serve per rilevare e di conseguenza migliorare le possibili vulnerabilità del codice.
    Al momento si è solo provato a runnare il job ma non si sono apportate ancora modifiche per superare i controlli di *Prospector* e *Bandit*.
- [x] `Unit-test-job`: eseguire *pytest*
    
    Vengono eseguiti gli unit test sui metodi di entrambi client e server. Per far ciò è stato eseguito il comando `pytest`. Questo comando andrà a runnare entrambi i file di test test_client.py e test_server.py per andare ad eseguire i seguenti test:
    - 
    -  
- [ ] `Integration-test-job`: eseguire *pytest*
    
    Non ancora implementato
- [ ] `Package-job`: usare *setuptools* e *wheel* per creare Source Archive e Built Distribution
    
    Non ancora implementato
- [ ] `Release-job`: Pubblicare la Build Distribution a *PyPI* con *twine*
    
    Non ancora implementato
- [ ] `Docs-job`: scrittura manuale md + generazione sito web di documentazione
    
    Non ancora implementato
- [ ] `Deploy-job`: esecuzione del codice su una VM SSH
    
    Non ancora implementato
### Criticità
- Fino ad oggi (23/10/23) entrambi gli sudenti hanno solo seguito le lezioni di Data-Science in quanto immatricolati in quel corso. Abbiamo oggi iniziato a seguire le lezioni di informatica perchè desideriamo cambiare corso. Per i motivi appena citati non è stato possibile eseguire ulteriori punti del assignment.
