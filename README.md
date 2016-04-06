# ToolService

---LEGGIMI---

Inserire config.yml e client.py nella stessa cartella.

1.loggare con utente: admin e password: admin in modo da entrare altrimenti ti scollega.

2.ISTRUZIONI PER Config.yml:

Cambiare la voce dell'host [] con un'altro indirizzo ip se si vuole connettere.
Per esempio:

host [102.145.3.5]

lo cambio con: 

host[127.0.0.1]


3. Istruzioni comandi per client:

usare questi comandi:

add nomeservizio (per aggiungere il servizio)

remove nomeservizio (per scollegare il servizio)


--ESEMPIO:

add mysql



NB: qualsiasi altro comando sarà visto come errore, e se si comanda di collegare o scollegare un servizio che non esiste sarà restituito errore
