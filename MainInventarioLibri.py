#Gestisci Inserimento nuovo Libro

from ArchivioJS import GetArchivioJS, CheckLibroJS, GetLibroRowJS, GetLibroQty, AumentaQtyJS, GetLastRowJS, AumentaRowJS, AddLibroJS, GetIDJS, AumentaIDJS, UpdateArchivioJS
from ArchivioOnline import AumentaQtyOnline, ConvertLibroJStoOnline, AddLibroOnline


def Inizializzazione():
    NomeArchivioJS='Archivio.json'

    ArchivioJS=GetArchivioJS(NomeArchivioJS)
    LibreriaJS=ArchivioJS['Libreria']
    GenericheJS=ArchivioJS['Generiche']





