#Gestisci Archivio Online
from WriteGSheet import ReadWriteSheet

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SAMPLE_SPREADSHEET_ID = ""

#SAMPLE_RANGE_NAME = "Inventario!A1"

#ID	ISBN	Nome	Autore	Editore	Costo (Non scontato)

def ConvertLibroJStoOnline(LibroJS, ID, ISBN):
    #LibroJS={"ID":0,"Nome":"","Autore":"","Editore":"","Costo":0,"Qty":0}
    #LibroOnline=[ID, ISBN, Nome, Autore, Editore, Costo (Non scontato), Qty]
    Libro=[['','','','','','','']]
    Libro[0][0]=str(ID)
    Libro[0][1]=ISBN
    Libro[0][2]=LibroJS['Nome']
    Libro[0][3]=LibroJS['Autore']
    Libro[0][4]=LibroJS['Editore']
    Libro[0][5]=LibroJS['Costo']
    Libro[0][6]=LibroJS['Qty']
    return Libro
    
def AddLibroOnline(Row, Libro):
    SAMPLE_RANGE_NAME="Inventario!A"+str(Row)
    ReadWriteSheet(True, SCOPES, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, Libro)

def AumentaQtyOnline(Row, Qty):
    Quantita=[[str(Qty)]]
    SAMPLE_RANGE_NAME="Inventario!G"+str(Row)
    ReadWriteSheet(True, SCOPES, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, Quantita)
    
