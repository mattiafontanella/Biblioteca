import DB as DB
import main as M
import time
import sqlite3


def aggiungiLibro () :
    conn = sqlite3.connect("DB\Biblioteca.db")
    print("Inserisci ISBN del libro: \n")
    ISBN=input()
    print("Inserisci il titolo:\n ")
    Titolo = input()
    print("Inserisci anno di pubblicazione: \n")
    AnnoProduzione=input()
    print("Inserisci il numero di copie disponibili: \n")
    Copie = input()
    print("Inserisci autore del libro: \n")
    Autore = input()
    cur = conn.cursor()
    conn.execute("SELECT * FROM Categoria ")
    rows=conn.fetchall()
    for row in rows:
        print(row)
    print("Inserisci la categoria del libro tra quelle presenti nel elenco: \n"
          "Se non è presente premi invio\n ")

    scelta= input()



    if (scelta=="") :
        print("Inserisci il nome della categoria da aggiungere: \n")
        scelta=input()
        sql = "INSERT INTO Categoria(Nome) " \
              "VALUES(Diritto)"
        conn.execute(sql)

    cur.execute("SELECT IDCategoria FROM Categoria WHERE Nome =?",(scelta,))
    IDCategoria= cur.fetchall()
    sql = "INSERT INTO Libro(ISBN, IDCategoria, Autore, Titolo, AnnoProduzione, NumeroCopie) " \
          "VALUES()"
    conn.execute("INSERT INTO Libro(ISBN, IDCategoria, Autore, Titolo, AnnoProduzione, NumeroCopie) VALUES"),(ISBN,IDCategoria,Autore,Titolo,AnnoProduzione,Copie)

    M.menu()

def cancellaLibro () :
    global db_biblioteca
    global libriAggiuti
    i=0

    if (libriAggiuti==0) :
        print("Non ci sono libri della biblioteca \n")

    if (libriAggiuti==1):
        print("Devi aggiugere almeno 2 libri prima di eliminarne uno!")
    else :
        for i,diz in enumerate(db_biblioteca["Libro"]):
            print(i,"- ",diz)

        print("Inserisci il numero del libro da eliminare: ")
        numLib=input()
        try:
            db_biblioteca["Libro"].pop(int(numLib))
            libriAggiuti=libriAggiuti-1
        except ValueError:
            print("Inserisci un valore intero")
    M.menu()


def visualizzaInventario () :
    global db_biblioteca

    for diz in db_biblioteca["Libro"] :
        print(diz)

    M.menu()

def aggiungiUtente():
    global utentiAggiunti
    print("Inserisci il codice fiscale: \n")
    variabile=input().upper()
    db_biblioteca["Utente"][utentiAggiunti]["Tessera"]=variabile
    db_biblioteca["Utente"][utentiAggiunti]["Data_Registrazione"] = time.strftime("%d/%m/%Y")
    print("Inserisci il nome \n")
    db_biblioteca["Utente"][utentiAggiunti]["Nome"] = variabile
    print("Inserisci il cognome \n")
    db_biblioteca["Utente"][utentiAggiunti]["Cognome"] = variabile
    print("Se possibile inserire numero di telefono")
    db_biblioteca["Utente"][utentiAggiunti]["Recapiti"]["Telefono"] = variabile
    print("Se possibile inserire indirizzo di residenza")
    db_biblioteca["Utente"][utentiAggiunti]["Recapiti"]["Indirizzo"] = variabile
    print("Se possibile inserire E-mail")
    db_biblioteca["Utente"][utentiAggiunti]["Recapiti"]["E-mail"] = variabile
    M.menu()

def visualizzaUtenti():
    for diz in db_biblioteca["Utente"] :
        print(diz)
    M.menu()
def eliminaUtente():
    global db_biblioteca
    global utentiAggiunti
    i = 0

    if (utentiAggiunti == 0):
        print("Non ci sono libri della biblioteca \n")

    if (utentiAggiunti == 1):
        print("Devi aggiugere almeno 2 libri prima di eliminarne uno!")
    else:
        for i, diz in enumerate(db_biblioteca["Libro"]):
            print(i, "- ", diz)

        print("Inserisci il numero del libro da eliminare: ")
        numLib = input()
        try:
            db_biblioteca["Libro"].pop(int(numLib))
            libriAggiuti = utentiAggiunti - 1
        except ValueError:
            print("Inserisci un valore intero")
    M.menu()
