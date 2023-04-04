jmeno_a_prijmeni = input ("Zadej svoje jmeno a prijmeni: ")
jmeno_split = jmeno_a_prijmeni.split()
print (jmeno_split)
jmeno_count = len (jmeno_split[0])
print (jmeno_count)
prijmeni_inicial = jmeno_split[1][0].capitalize()
prijmeni_capitalized = jmeno_split[1].capitalize()

if jmeno_count > 5:
    jmeno_inicial = jmeno_split[0][0].capitalize()
    print ((f"{jmeno_inicial}. {prijmeni_capitalized}"))
else:
    jmeno_capitalized = jmeno_split[0].capitalize()
    print (f"{jmeno_capitalized},{prijmeni_capitalized}")