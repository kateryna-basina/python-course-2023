'''Vytvoř program pro evidenci aut malé autopůjčovny. '''
""" Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené). """

class Auto: #Vytvarime tridu "Auto" a jeji atributy
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):  #Diky metode __init__ pridavame atributy 
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True  #na začátku je vozidlo vždy volné
    def get_info(self):    #Funkce get_info() vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.
        return f"Registracni znacka auta je {self.registracni_znacka} a typ vozidla je {self.typ_vozidla}."

    def pujc_auto(self): #Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."


vozidlo1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534) #vytvarime 2 auta jako objekty tridy "Auto"
vozidlo1.registracni_znacka = "4A2 3020"
vozidlo1.typ_vozidla = "Peugeot 403 Cabrio"
vozidlo1.najete_km = 47534
vozidlo1.dostupne = True

vozidlo2 = Auto ("1P3 4747", "Škoda Octavia", 41253)
vozidlo2.registracni_znacka = "1P3 4747"
vozidlo2.typ_vozidla = "Škoda Octavia"
vozidlo2.najete_km = 41253
vozidlo2.dostupne = True

pujcovna = input ("Vyber jake auto pujcis - Skodu nebo Peugeot: ") #zeptejme uzivatele kterou znacku chtel bych pujcit
if pujcovna == "Peugeot":
    auto = vozidlo1
elif pujcovna == "Skoda":
    auto = vozidlo2
else:
    print("Neplatna volba")

print(auto.get_info())
print(auto.pujc_auto())


