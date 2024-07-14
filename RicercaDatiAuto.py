import requests
from bs4 import BeautifulSoup
import time

def Pulisci_Stringa(Stringa):
    Stringa=Stringa.replace('\n','')
    while "  " in Stringa:
        Stringa=Stringa.replace('  ',' ')

    if len(Stringa) == 0:
        return ""
    
    if Stringa[0] == " ":
        Stringa=Stringa[1:]

    if Stringa[-1] == " ":
        Stringa=Stringa[:-1]
        
    return Stringa

def FiltraHTML(HTML,Start,Stop):
    ParmSTART=(HTML.find(Start))
    HTML=HTML[ParmSTART:]
    ParmStop=(HTML.find(Stop))
    Parm=HTML[len(Start):ParmStop]
    return Pulisci_Stringa(Parm)
    
def RicercaDati(ISBN):
    URL="https://www.libreriauniversitaria.it/ricerca/query/"+str(ISBN)+"/reparto/tutti"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    HTML=str(soup)
    
    Titolo=(FiltraHTML(HTML,' class="product-title">','</h3><div class="product-manufacturers">'))
    Autore=(FiltraHTML(HTML,'<span class="text">di</span>','</div><span class="separator">'))
    Autore=Pulisci_Stringa(Autore.replace('<span class="list-separator">,</span> ',','))
    Editore=(FiltraHTML(HTML,'<div class="product-publisher">','</div></div><div class="panel-bottom">'))
    Editore=Editore.replace('</div><span class="separator">-</span><div class="product-publication-year">','-')
    Costo=(FiltraHTML(HTML,'class="current-price">€','</span></div></div>'))
    if '</span><span class="catalog-price">€' in Costo:
        Costo=(FiltraHTML(HTML,'</span><span class="catalog-price">€ ','</span></div></div><div class'))

    Ritorno={"Nome": Pulisci_Stringa(Titolo), "Autore": Pulisci_Stringa(Autore), "Editore": Pulisci_Stringa(Editore),"Costo": Pulisci_Stringa(Costo)}
    return Ritorno




