""" 
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti: Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.'''
"""
#Zeptame uzivatele na jeho cislo
cislo_uzivatele = input ("Zadejte telefonni cislo pro sms: ") 

def overovani_cisla (cislo_uzivatele):  #tento program bude overovat cislo: estli cislo je devítimístné nebo třináctimístné, vraci "True"
    if len(cislo_uzivatele) == 9:
        return True
    elif len(cislo_uzivatele) == 13 and cislo_uzivatele[:4]== "+420":
        return True
    return False 
    
result = overovani_cisla(cislo_uzivatele) #estli uzivatel zadal nespravne cislo, vrati mu "False" a spravu,ze cislo je nespravne, a pak program ukonci
if not result:
    print("Cislo neni spravne")
    exit ()
else:
    sms = input ("Zadejte Vas text pro sms: ") #Zeptejme uzivatele na spravu, jaku on chci poslat a spocitame cenu
    pocet_blokov = (len(sms) // 180)  #calculating number of blocks
    def spocitat_cenu (sms):
        if len(sms) % 180 ==  0:
            cena_sms = pocet_blokov * 3
        else:
            cena_sms = (pocet_blokov * 3) + 3
        return (cena_sms)

cena_sms = spocitat_cenu (sms)
print (f"Cena sms je {cena_sms} Kc")   

