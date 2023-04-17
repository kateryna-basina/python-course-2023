import json

#nacteme soubor a prevedeme ho na slovnik v pytonu

with open ('body.json', encoding='utf-8') as file:
    soubor = json.load(file)

print(soubor)

prospeli = {}  #vytvarime novy prazdny slovnik, kde budeme zobrazovat znamky "Pass" nebo "Fail"

for student, znamka in soubor.items(): #projdeme ten cely soubor cyklusom "for"
    if znamka >= 60:
        prospeli[student] = "Pass"
    else: 
        prospeli[student] = "Fail" #estli znamka je vice nebo ravna 60, student bude mit "Pass", jinak bude mit "Fail"
        
#ulozime nove znamky jako json soubor

with open ('prospeli.json', 'w') as file: 
    json.dump(prospeli, file)

print (prospeli) #zobrazime vysledek
