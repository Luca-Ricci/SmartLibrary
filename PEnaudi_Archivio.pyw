import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QWidget, QAction, QTabWidget,QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from MainInventarioLibri import Inizializzazione
from ArchivioJS import GetArchivioJS, CheckLibroJS, GetDatiLibro, GetLibroRowJS, GetLibroQty, AumentaQtyJS, GetLastRowJS, AumentaRowJS, AddLibroJS, GetIDJS, AumentaIDJS, UpdateArchivioJS
from ArchivioOnline import AumentaQtyOnline, ConvertLibroJStoOnline, AddLibroOnline
from RicercaDatiAuto import RicercaDati

#IMPLEMENTA CERCA
#IMPLEMENT CERCA PER ISBN AUTORE E TITOLO

#IMPLEMENTA RICERCA DATI DA LIBRERIA UNIVERSITARIA
#IMPLEMENTA RICERCA AUTOMATICA

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'AutoLibrary - Inventario'
        self.left = 0
        self.top = 0
        self.width =450
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


            
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()

    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.NomeArchivioJS='Archivio.json'

        self.ArchivioJS=GetArchivioJS(self.NomeArchivioJS)
        self.LibreriaJS=self.ArchivioJS['Libreria']
        print(self.LibreriaJS)
        self.GenericheJS=self.ArchivioJS['Generiche']

        
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Cerca")
        self.tabs.addTab(self.tab2,"Inserisci")
        
        # Create first tab
        self.tab1.layout = QGridLayout(self)

        self.ISBN_Titolo = QLabel()
        self.ISBN_Titolo.setText("Codice ISBN:")
        self.tab1.layout.addWidget(self.ISBN_Titolo, 0, 0)

        self.ISBN_Code = QLineEdit(parent=self)
        self.tab1.layout.addWidget(self.ISBN_Code, 0, 1)

        self.ISBN_NAME = QLabel()
        self.ISBN_NAME.setText("Nome:")
        self.tab1.layout.addWidget(self.ISBN_NAME, 1, 0)
        
        self.NAME_auto = QLineEdit(parent=self)
        self.tab1.layout.addWidget(self.NAME_auto, 1, 1)


        self.ISBN_QTY = QLabel()
        self.ISBN_QTY.setText("Qty:")
        self.tab1.layout.addWidget(self.ISBN_QTY, 2, 0)
        
        self.QTY_auto = QLineEdit(parent=self)
        self.tab1.layout.addWidget(self.QTY_auto, 2, 1)

        
        self.pushButton1 = QPushButton("Cerca")
        self.pushButton1.clicked.connect(self.CercaISBN)
        self.tab1.layout.addWidget(self.pushButton1, 3,0,1,2)
        self.tab1.setLayout(self.tab1.layout)


        # Create second tab
        self.tab2.layout = QGridLayout(self)

        self.Label_ISBN = QLabel()
        self.Label_ISBN.setText("Codice ISBN:")
        self.tab2.layout.addWidget(self.Label_ISBN, 0, 0)

        self.ISBN_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.ISBN_Tbox, 0, 1)


        self.LibroPresente = QLabel()
        self.LibroPresente.setText("      ")
        self.LibroPresente.setStyleSheet("QLabel"
                               "{"
                               "background-color : grey;"
                               "}") 
        self.tab2.layout.addWidget(self.LibroPresente, 0, 2)

        self.Label_Nome = QLabel()
        self.Label_Nome.setText("Nome Libro:")
        self.tab2.layout.addWidget(self.Label_Nome, 1, 0)

        self.Nome_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.Nome_Tbox, 1, 1)

        self.Label_Autore = QLabel()
        self.Label_Autore.setText("Nome Autore:")
        self.tab2.layout.addWidget(self.Label_Autore, 2, 0)

        self.Autore_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.Autore_Tbox, 2, 1)

        self.Label_Editore = QLabel()
        self.Label_Editore.setText("Editore:")
        self.tab2.layout.addWidget(self.Label_Editore, 3, 0)

        self.Editore_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.Editore_Tbox, 3, 1)

        self.Label_Costo = QLabel()
        self.Label_Costo.setText("Costo:")
        self.tab2.layout.addWidget(self.Label_Costo, 4, 0)

        self.Costo_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.Costo_Tbox, 4, 1)

        self.Label_Quantita = QLabel()
        self.Label_Quantita.setText("Quantità:")
        self.tab2.layout.addWidget(self.Label_Quantita, 5, 0)

        self.Quantita_Tbox = QLineEdit(parent=self)
        self.tab2.layout.addWidget(self.Quantita_Tbox, 5, 1)

        self.pushButton3 = QPushButton("Cerca Libro")
        self.pushButton3.clicked.connect(self.CercaLibro)
        self.tab2.layout.addWidget(self.pushButton3, 6,0)
        self.tab2.setLayout(self.tab2.layout)

        self.pushButton2 = QPushButton("Aggiungi Libro")
        self.pushButton2.clicked.connect(self.AggiungiLIBRO)
        self.tab2.layout.addWidget(self.pushButton2, 6,1)
        self.tab2.setLayout(self.tab2.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def CercaISBN(self):
        try:
            self.ISBN=self.ISBN_Code.text()    
            self.Dati=GetDatiLibro(self.LibreriaJS, self.ISBN)
            self.NAME_auto.setText(self.Dati['Nome'])
            self.QTY_auto.setText(str(self.Dati['Qty']))
        except Exception as error:
            print(error)

        
    
    def AggiungiISBN(self):
        self.ISBN=self.ISBN_Code.text()
        self.GiaPresente=CheckLibroJS(self.LibreriaJS, self.ISBN)
        print(self.GiaPresente)
        try:
            if self.GiaPresente:
                self.OnlineRow=GetLibroRowJS(self.LibreriaJS, self.ISBN)
                self.Qty=(GetLibroQty(self.LibreriaJS, self.ISBN))+int(self.QTY_auto.text())
                self.LibreriaJS=AumentaQtyJS(self.LibreriaJS, self.ISBN,int(self.QTY_auto.text()))
                AumentaQtyOnline(self.OnlineRow, self.Qty)
            UpdateArchivioJS(self.NomeArchivioJS, self.ArchivioJS, self.GenericheJS, self.LibreriaJS)
            print(self.LibreriaJS)
        except Exception as error:
            print(error)


    def CercaLibro(self):
        self.ISBN=self.ISBN_Tbox.text()
        self.StatoLibro=CheckLibroJS(self.LibreriaJS, self.ISBN)
        
        if self.StatoLibro:
            colore="green"
            self.Dati=GetDatiLibro(self.LibreriaJS, self.ISBN)
            self.Nome_Tbox.setText(self.Dati['Nome'])
            self.Autore_Tbox.setText(self.Dati['Autore'])
            self.Editore_Tbox.setText(self.Dati['Editore'])
            self.Costo_Tbox.setText(str(self.Dati['Costo']))

        else:
            colore="red"
            try:
                self.Dati=RicercaDati(self.ISBN)
                self.Nome_Tbox.setText(self.Dati['Nome'])
                self.Autore_Tbox.setText(self.Dati['Autore'])
                self.Editore_Tbox.setText(self.Dati['Editore'])
                self.Costo_Tbox.setText(str(self.Dati['Costo']))            
            except Exception as error:
                print(error)

            #9788842822349
        self.LibroPresente.setStyleSheet("QLabel"
                                         "{"
                                         "background-color : "+str(colore)+";"
                                         "}") 
            
    def AggiungiLIBRO(self):
        try:
            self.ISBN=self.ISBN_Tbox.text()
            self.NOME=self.Nome_Tbox.text()
            self.AUTORE=self.Autore_Tbox.text()
            self.EDITORE=self.Editore_Tbox.text()
            self.COSTO=float((self.Costo_Tbox.text()))
            self.QTY=int(self.Quantita_Tbox.text())

        
            self.LibroJS={"Row":0,"Nome":self.NOME,"Autore":self.AUTORE,"Editore":self.EDITORE,"Costo":self.COSTO,"Qty":self.QTY}
            self.LastRow=GetLastRowJS(self.GenericheJS)+1
            self.LibroJS["Row"]=self.LastRow+1
            self.GenericheJS=AumentaRowJS(self.GenericheJS)
            self.LibreriaJS=AddLibroJS(self.LibreriaJS, self.ISBN, self.LibroJS)
            self.LastId=GetIDJS(self.GenericheJS)+1
            self.LibroOnline=ConvertLibroJStoOnline(self.LibroJS, self.LastId, self.ISBN)
            self.GenericheJS=AumentaIDJS(self.GenericheJS)
            self.ritorno=AddLibroOnline(self.LastRow, self.LibroOnline)
            UpdateArchivioJS(self.NomeArchivioJS, self.ArchivioJS, self.GenericheJS, self.LibreriaJS)
        except Exception as error:
            print(error)

        
        


if __name__ == '__main__':   
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
