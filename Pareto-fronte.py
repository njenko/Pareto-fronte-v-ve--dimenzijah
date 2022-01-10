from numpy import random, linalg

#===============================================================================
# FUNKCIJE ZA RAČUNANJE PARETO FRONT
#===============================================================================

def dominira(a, b):
    return sum([a[x] >= b[x] for x in range(len(b))]) == len(b) # Vrne true, če točka a dominira točko b

def izracun_pareto_fronte(mnozica): # Funkcija iz dane množice vrne dve množici: točke 1. pareto fronte in vse dominirane točke
    pareto_fronta = set()
    dominirane_tocke = set()

    while len(mnozica) != 0:
        kandidat = list(mnozica)[0] # Vzamemo točko in jo odstranimo iz množice
        mnozica.remove(kandidat)
        i = 0
        ni_dominirana = True # Indikator, ki preverja ali je ta točka dominirana

        while i < len(mnozica):
            tocka = list(mnozica)[i]
            if dominira(kandidat, tocka): # Preverimo, ali naša izbrana točka (kandidat) dominira ostale točke. Če katero izmed njih dominira, tisto točko damo v množico dominiranih točki in jo odstranimo iz osnovne množice, saj je ne rabimo več pregledovati.
                mnozica.remove(tocka)
                dominirane_tocke.add(tuple(tocka))
                i += 1
            elif dominira(tocka, kandidat): # Če najdemo točko, ki dominira našega kandidata, lahko kandidata damo v množico dominiranih točk in spremenimo vrednost indikatorja.
                dominirane_tocke.add(tuple(kandidat))
                ni_dominirana = False
                break
            else:
                i += 1

        if ni_dominirana:   # Če ne najdemo točke ki bi dominirala našega kandidata pomeni, da je le ta v skyline-u (pareto fronta)
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


#===============================================================================
# GENERIRANJE PODATKOV
#===============================================================================

def random_krogla(stevilo_tock, d, radij=1):
    mnozica_tock = set()
    for i in range(stevilo_tock):    
        rand_smer = random.uniform(low=-1, high=1, size=d) # Generiramo nakljucni vektor dimenzije d
        rand_smer /= linalg.norm(rand_smer, axis=0) # Vektor normiramo
        rand_dolzina = random.uniform(low=0, high=1) # Vektor pomnožimo z naključno vrednostjo med 0 in 1, da dobimo točko v notranjosti d dimenzionalne enotske krogle
        tocka = tuple(radij * (rand_smer * rand_dolzina)) # Če bi želeli gledati večjo kroglo lahko spremenimo tudi vrednost radija.
        mnozica_tock.add(tocka)
    return mnozica_tock


def random_kocka(stevilo_tock, d, a=1): # a stranica kocke, d dimenzija prostora
    mnozica_tock = set()
    for i in range(stevilo_tock):
        rand_smer = random.uniform(low=0, high=a, size=d)
        tocka = tuple(rand_smer)
        mnozica_tock.add(tocka)
    return mnozica_tock

#===============================================================================
# EKSPERIMENTALNI DEL
#===============================================================================

# Za eno ponovitev eksperimenta najprej generiramo množico podatkov s funkcijo
# random_krogla ali funkcijo random_kocka, kjer kot parametre vstavimo število 
# točk ki jih želimo, dimenzijo prostora in pa velikost krogle/kocke. Kot 
# default je nastavljena enotska krogla in enotska kocka (radij=1 oz. stranica=1)

# Primer:
testne_tocke1 = random_krogla(200, 3)
testne_tocke2 = random_kocka(200, 3)

# Nato lahko na tej množici uporabimo funkcijo izracun_pareto_fronte, ki nam vrne 
# dvojec 1. pareto fronto in pa množice vseh dominiranih točk, ali pa 
# izracun_n_pareto_front, ki nam vrne vse pareto fronte do globine n oz. do 
# globine, kjer smo porabili vse točke.

#Primer:
(pareto, dominirane) = izracun_pareto_fronte(testne_tocke1)

#pareto_fronte_do_globine_5 = izracun_n_pareto_front(testne_tocke2, 5)

kocka1 = random_kocka(500, 5)
kocka2 = random_kocka(500, 5)
kocka3 = random_kocka(500, 5)
kocka4 = random_kocka(500, 5)
kocka5 = random_kocka(500, 5)
kocka6 = random_kocka(500, 5)
kocka7 = random_kocka(500, 5)
kocka8 = random_kocka(500, 5)
kocka9 = random_kocka(500, 5)
kocka10 = random_kocka(500, 5)
kocka11 = random_kocka(500, 5)
kocka12 = random_kocka(500, 5)
kocka13 = random_kocka(500, 5)
kocka14 = random_kocka(500, 5)
kocka15 = random_kocka(500, 5)
kocka16 = random_kocka(500, 5)
kocka17 = random_kocka(500, 5)
kocka18 = random_kocka(500, 5)
kocka19 = random_kocka(500, 5)
kocka20 = random_kocka(500, 5)

izracun_n_pareto_front(kocka1, 5)
izracun_n_pareto_front(kocka2, 5)
izracun_n_pareto_front(kocka3, 5)
izracun_n_pareto_front(kocka4, 5)
izracun_n_pareto_front(kocka5, 5)
izracun_n_pareto_front(kocka6, 5)
izracun_n_pareto_front(kocka7, 5)
izracun_n_pareto_front(kocka8, 5)
izracun_n_pareto_front(kocka9, 5)
izracun_n_pareto_front(kocka10, 5)
izracun_n_pareto_front(kocka11, 5)
izracun_n_pareto_front(kocka12, 5)
izracun_n_pareto_front(kocka13, 5)
izracun_n_pareto_front(kocka14, 5)
izracun_n_pareto_front(kocka15, 5)
izracun_n_pareto_front(kocka16, 5)
izracun_n_pareto_front(kocka17, 5)
izracun_n_pareto_front(kocka18, 5)
izracun_n_pareto_front(kocka19, 5)
izracun_n_pareto_front(kocka20, 5)