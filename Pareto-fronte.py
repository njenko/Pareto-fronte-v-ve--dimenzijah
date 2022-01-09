from numpy import random, linalg

def dominira(a, b):
    return sum([a[x] >= b[x] for x in range(len(b))]) == len(b) # vrne true, če točka a dominira točko b

def izracun_pareto_fronte(mnozica): #funkcija iz dane množice vrne dve množici: točke 1. pareto fronte in vse dominirane točke
    pareto_fronta = set()
    dominirane_tocke = set()

    while len(mnozica) != 0:
        kandidat = list(mnozica)[0] #vzamemo točko in jo odstranimo iz množice
        mnozica.remove(kandidat)
        i = 0
        ni_dominirana = True #indikator, ki preverja ali je ta točka dominirana

        while i < len(mnozica):
            tocka = list(mnozica)[i]
            if dominira(kandidat, tocka): #preverimo, ali naša izbrana točka (kandidat) dominira ostale točke. Če katero izmed njih dominira, tisto točko damo v množico dominiranih točki in jo odstranimo iz osnovne množice, saj je ne rabimo več pregledovati.
                mnozica.remove(tocka)
                dominirane_tocke.add(tuple(tocka))
                i += 1
            elif dominira(tocka, kandidat): #če najdemo točko, ki dominira našega kandidata, lahko kandidata damo v množico dominiranih točk in spremenimo vrednost indikatorja.
                dominirane_tocke.add(tuple(kandidat))
                ni_dominirana = False
                break
            else:
                i += 1

        if ni_dominirana:   #če ne najdemo točke ki bi dominirala našega kandidata pomeni, da je le ta v skyline-u (pareto fronta)
            pareto_fronta.add(tuple(kandidat))
        
        if len(mnozica) == 0:
            break
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


def random_krogla(stevilo_tock, d, radij=1):
    mnozica_tock = set()
    for i in range(stevilo_tock):    
        rand_smer = random.uniform(low=-1, high=1, size=d) #generiramo nakljucni vektor dimenzije d
        rand_smer /= linalg.norm(rand_smer, axis=0) #vektor normiramo
        rand_dolzina = random.uniform(low=0, high=1) # vektor pomnožimo z naključno vrednostjo med 0 in 1, da dobimo točko v notranjosti d dimenzionalne enotske krogle
        tocka = tuple(radij * (rand_smer * rand_dolzina)) #če bi želeli gledati večjo kroglo lahko spremenimo tudi vrednost radija.
        mnozica_tock.add(tocka)
    return mnozica_tock


testne_tocke50_1 = random_krogla(50, 3)
testne_tocke50_2 = random_krogla(50, 3)
testne_tocke50_3 = random_krogla(50, 3)
testne_tocke50_4 = random_krogla(50, 3)
testne_tocke50_5 = random_krogla(50, 3)
testne_tocke50_6 = random_krogla(50, 3)
testne_tocke50_7 = random_krogla(50, 3)
testne_tocke50_8 = random_krogla(50, 3)
testne_tocke50_9 = random_krogla(50, 3)
testne_tocke50_10 = random_krogla(50, 3)

izracun_n_pareto_front(testne_tocke50_1, 5)
izracun_n_pareto_front(testne_tocke50_2, 5)
izracun_n_pareto_front(testne_tocke50_3, 5)
izracun_n_pareto_front(testne_tocke50_4, 5)
izracun_n_pareto_front(testne_tocke50_5, 5)
izracun_n_pareto_front(testne_tocke50_6, 5)
izracun_n_pareto_front(testne_tocke50_7, 5)
izracun_n_pareto_front(testne_tocke50_8, 5)
izracun_n_pareto_front(testne_tocke50_9, 5)
izracun_n_pareto_front(testne_tocke50_10, 5)