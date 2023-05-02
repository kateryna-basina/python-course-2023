""" Mějme zadaný následující seznam naměřených teplot. 
Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
"""
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#1. Vytvoř seznam průměrných teplot pro každý den.

prumerne_teploty = [sum (den) / len (den) for den in teploty]
print (f'Prumerne teploty jsou: {prumerne_teploty}')

# 2. Vytvoř seznam ranních teplot.

ranni_teploty = [den[0] for den in teploty]
print (f'Ranni teploty jsou: {ranni_teploty}')

# 3. Vytvoř seznam nočních teplot.

nocni_teploty = [den[3] for den in teploty]
print (f'Nocni teploty jsou: {nocni_teploty}')

# 4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_a_nocni_teploty = [[den[1], den[3]] for den in teploty]
print (f'Poledni a nocni teploty jsou: {poledni_a_nocni_teploty}')