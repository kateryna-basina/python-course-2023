#Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.
#Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input ("Zadej prosim kod soucastky: ") #zeptejme co chci uzivatel koupit a ulozime v promenne "kod"

#Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

if kod not in sklad:
    print ("Bohuzel, součástka není skladem.") 

mnozstvi = int(input("Zadej prosim mnozstvi soucastky: ")) #zeptejme uzivatele jake mnozstvi polozky on chci koupit a ulozime do promenne "mnozstvi"

#Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.

if sklad[kod] < mnozstvi:
    print(f"Lze prodat pouze omezené množství kusů: {sklad[kod]}.")
    sklad.pop(kod)  #odstranime polozku ze skladu

#Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

else: 
    print("Poptávku lze uspokojit v plné výši.")
    sklad[kod] -= mnozstvi  #odbereme to mnozstvi, ktere nakoupil uzivatel, od polozky

print("Sklad:", sklad) #vytiskneme, co nam na sklade este zustalo
