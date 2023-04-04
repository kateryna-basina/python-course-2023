#Zeptame uzivatele na jeho jmeno a ulozime v promenne jmeno_a_prijmeni
jmeno_a_prijmeni = input ("Zadej svoje jmeno a prijmeni: ")

#Všechna písmena velká 

jmeno_a_prijmeni_upper = jmeno_a_prijmeni.upper()
print (jmeno_a_prijmeni_upper)

#všechna písmena malá

jmeno_a_prijmeni_lower = jmeno_a_prijmeni.lower()
print (jmeno_a_prijmeni_lower)

#standardní varianta - první písmeno velké, další malá 

jmeno_split = jmeno_a_prijmeni.split() #udelame array
print (jmeno_split) 
jmeno_capitalized = jmeno_split[0].capitalize() #obratime se na prvni slovo v array
prijmeni_capitalized = jmeno_split[1].capitalize() #obratime se na druhy slovo v array
print (jmeno_capitalized, prijmeni_capitalized)

#iniciály

jmeno_inicial = jmeno_split[0][0].capitalize() #obratime se na prvni pismeno v array
prijmeni_inicial = jmeno_split[1][0].capitalize() #obratime se na druhy pismeno v array
print (f"{jmeno_inicial}. {prijmeni_inicial}.")

#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)

jmeno_count = len (jmeno_split[0]) #spocitame kolik znaku ma jmeno
print (jmeno_count)
if jmeno_count > 5:
    jmeno_inicial = jmeno_split[0][0].capitalize() #estli jmeno ma vic nez 5 znaku, zobrazime inicial a prijmeni
    print ((f"{jmeno_inicial}. {prijmeni_capitalized}")) 
else:
    jmeno_capitalized = jmeno_split[0].capitalize()
    print (f"{jmeno_capitalized} {prijmeni_capitalized}") #eslti jmeno ma mine 5 znaku, zobrazime vsechno jak je 