#Gestisci Archivio Offline
from JsonFunction import CreaJSONfile, LeggiJSONfile

#FUNZIONI ARCHIVIO
def GetArchivioJS(NomeArchivio):
    Archivio=LeggiJSONfile(NomeArchivio)
    return Archivio

def UpdateArchivioJS(NomeArchivio, Archivio, GenericData, Libreria):
    Archivio={"Generiche":GenericData,"Libreria":Libreria}
    CreaJSONfile(NomeArchivio,Archivio)

def GetDatiLibro(Libreria, ISBN):
    ritorno=Libreria[ISBN]
    return ritorno
    

#FUNZIONI LIBRERIA
def CheckLibroJS(Libreria, ISBN):
    #Libreria=Archivio["Libreria"]
    Libri=Libreria.keys()
    LibroPresente=False
    if ISBN in Libri:
        LibroPresente=True
    return LibroPresente

def AumentaQtyJS(Libreria, ISBN, qty):
    Libreria[ISBN]["Qty"]+=qty
    return Libreria

def AddLibroJS(Libreria, ISBN, Libro):
    Libreria[ISBN]=Libro
    return Libreria

def GetLibroRowJS(Libreria, ISBN):
    Row=Libreria[ISBN]["Row"]
    return Row

def GetLibroQty(Libreria, ISBN):
    Qty=Libreria[ISBN]["Qty"]
    return Qty


#FUNZIONI GENERICHE
def AumentaIDJS(Generiche):
    #Generiche=ArchivioEnaudi["Generiche"]
    Generiche["LastID"]+=1
    return Generiche

def GetIDJS(Generiche):
    #Generiche=ArchivioEnaudi["Generiche"]
    ID=Generiche["LastID"]
    return ID

def AumentaRowJS(Generiche):
    Generiche["LastRow"]+=1
    return Generiche

def GetLastRowJS(Generiche):
    Row=Generiche["LastRow"]
    return Row


def InizializzaArchivio():
    GenericData={"LastID":0,"LastRow":0}
    Libro2={"Row":0,"Nome":"Er Patata","Autore":"Er Patata","Editore":"Er Patata","Costo":69.96,"Qty":0}
    Libreria={'ERPATATA':Libro2}
    ArchivioEnaudi={"Generiche":GenericData,"Libreria":Libreria}
    UpdateArchivioJS('Archivio.json', ArchivioEnaudi, GenericData, Libreria)

#InizializzaArchivio()
    
