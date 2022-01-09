
def dominira(a, b):
    return sum([a[x] >= b[x] for x in range(len(b))]) == len(b) # vrne true, če točka a dominira točko b

def izracun_pareto_fronte(mnozica): #funkcija iz dane množice vrne dve množici: točke 1. pareto fronte in vse dominirane točke
    pareto_fronta = set()
    dominirane_tocke = set()
    kandidat_indeks = 0

    while len(mnozica) != 0:
        kandidat = list(mnozica)[kandidat_indeks] #vzamemo točko in jo odstranimo iz množice
        mnozica.remove(kandidat)
        i = 0
        ni_dominirana = True #indikator, ki preverja ali je ta točka dominirana

        while i < len(mnozica):
            tocka = list(mnozica)[i]
            if dominira(kandidat, tocka): #preverimo, ali naša izbrana točka (kandidat) dominira ostale točke. Če katero izmed njih dominira, tisto točko damo v množico dominiranih točki in jo odstranimo iz osnovne množice, saj je ne rabimo več pregledovati.
                mnozica.remove(tocka)
                dominirane_tocke.add(tuple(tocka))
            elif dominira(tocka, kandidat): #če najdemo točko, ki dominira našega kandidata, lahko kandidata damo v množico dominiranih točk in spremenimo vrednost indikatorja.
                dominirane_tocke.add(tuple(kandidat))
                ni_dominirana = False
            else:
                i += 1

        if ni_dominirana:   #če ne najdemo točke ki bi dominirala našega kandidata pomeni, da je le ta v skyline-u (pareto fronta)
            pareto_fronta.add(tuple(kandidat))
        
    return pareto_fronta, dominirane_tocke

def izracun_n_pareto_front(mnozica, n): # 2., 3., 4., ... pareto fronte izračunamo rekurzivno z uporabo prejšnje funkcije. Množico razbijamo na pareto fronto in dominirane točke, dokler ne pridemo do prazne množice ali pa dobimo vse zahtevane pareto fronte, ki smo jih želeli (želeno globino določimo s parametrom n).
    if len(mnozica) == 0:   #Zaustavitveni pogoj 1: porabimo vse elemente množice
        return set()
    elif n < 1:
        return set()    #Zaustavitveni pogoj 2: pridemo do želene globine.
    else:
        pareto, dom = izracun_pareto_fronte(mnozica)
        print(len(pareto))  #Opazujemo število točk v pareto fronth. Za lažje opazovanje število točk jih sproti izpisujemo.
        return pareto, izracun_n_pareto_front(dom, n-1)

testna_mnozica = {(13, 4, -5), (32, 7, 587), (3, 8, 13), (24, -841, -5), (-98, 8, 0), (234, 34, 2), (3, 4, 654), (3, 54, 24)}
print(izracun_n_pareto_front(testna_mnozica, 2))