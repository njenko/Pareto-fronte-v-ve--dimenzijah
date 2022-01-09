
def dominira(a, b):
    return sum([a[x] >= b[x] for x in range(len(b))]) == len(b) # vrne true, če točka a dominira točko b

def izracun_pareto_fronte(mnozica):
    pareto_fronta = set()
    dominirane_tocke = set()
    kandidat_indeks = 0

    while len(mnozica) != 0:
        kandidat = list(mnozica)[kandidat_indeks]
        mnozica.remove(kandidat)
        i = 0
        ni_dominirana = True
        while i < len(mnozica):
            tocka = list(mnozica)[i]
            if dominira(kandidat, tocka):
                mnozica.remove(tocka)
                dominirane_tocke.add(tuple(tocka))
            elif dominira(tocka, kandidat):
                dominirane_tocke.add(tuple(kandidat))
                ni_dominirana = False
            else:
                i += 1

        if ni_dominirana:
            pareto_fronta.add(tuple(kandidat))
        
    return pareto_fronta, dominirane_tocke

def izracun_n_pareto_front(mnozica, n):
    if len(mnozica) == 0:
        return set()
    elif n < 1:
        return set()
    else:
        pareto, dom = izracun_pareto_fronte(mnozica)
        return pareto, izracun_n_pareto_front(dom, n-1)

testna_mnozica = {(1, 2, 3), (2, 4, 1), (5, 5, 5), (4, 4, 6)}
print(izracun_n_pareto_front(testna_mnozica, 2))