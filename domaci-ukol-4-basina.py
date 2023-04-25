'''Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.'''

#Zeptame uzivatele na jeho cislo
cislo_uzivatele = input ("Zadejte telefonni cislo pro sms: ") 

def overovani_cisla (cislo_uzivatele):  #tento program bude overovat cislo: estli cislo je devítimístné nebo třináctimístné, vraci "True"
    if len(cislo_uzivatele) == 9:
        return True
    elif len(cislo_uzivatele) == 13 and cislo_uzivatele[:4]== "+420":
        return True
    else:
        return False 
    
result = overovani_cisla(cislo_uzivatele) #estli uzivatel zadal nespravne cislo, vrati mu "False" a spravu,ze cislo je nespravne
if not result:
    print("Cislo neni spravne")
    
    
print(result)

#Zeptejme uzivatele na spravu, jaku on chci poslat a spocitame cenu
sms = input ("Zadejte Vas text pro sms: ")
znaky = len(sms)  
print (znaky)
cena_sms = (znaky / 180) * 3
cena_sms = round (cena_sms, 1)
print (f"Cena sms je {cena_sms} Kc")   

