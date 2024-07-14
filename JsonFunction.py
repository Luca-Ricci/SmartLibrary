import json

def CreaJSONfile(NomeFile,DizContenuto):
    with open(NomeFile, "w") as outfile:
        json.dump(DizContenuto, outfile)

def LeggiJSONfile(NomeFile):
    with open(NomeFile, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object


#Inventario = {332211:{"Nome":"Pluto","Autore":"Pippo","Prezzo":9,"Qty":1}}

#CreaJSONfile('prova.json',Libro)
#print(LeggiJSONfile('prova.json'))
