import json
with open ('body.json', encoding='utf-8') as file:
    soubor = json.load(file)

print(soubor)

prospeli = {}
for student, znamka in soubor.items():
    if znamka >= 60:
        prospeli[student] = "Pass"
    else: 
        prospeli[student] = "Fail"

with open ('prospeli.json', 'w') as file:
    json.dump(prospeli, file)

print (prospeli)