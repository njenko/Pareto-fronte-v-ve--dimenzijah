from numpy import random, linalg

def random_ball(num_points, dimension, radius=1):

    # First generate random directions by normalizing the length of a
    # vector of random-normal values (these distribute evenly on ball).
    random_directions = random.uniform(size=(dimension))
    random_directions /= linalg.norm(random_directions, axis=0)
    # Second generate a random radius with probability proportional to
    # the surface area of a ball with a given radius.
    random_radii = 1 #random.random(num_points) ** (1/dimension)
    # Return the list of random (direction & length) points.
    #seznam_tock = radius * (random_directions * random_radii).T
    #mnozica_tock = set()
    #for element in seznam_tock:
    #    mnozica_tock.update(tuple(element))
    #return mnozica_tock
    return radius * (random_directions * random_radii).T

#krogla = random_ball(5, 3)
#print(krogla)

def random_krogla(stevilo_tock, d, radij=1):
    mnozica_tock = set()
    for i in range(stevilo_tock):    
        rand_smer = random.uniform(low=-1, high=1, size=d) #generiramo nakljucni vektor dimenzije d
        rand_smer /= linalg.norm(rand_smer, axis=0) #vektor normiramo
        rand_dolzina = random.uniform(low=0, high=1) # vektor pomnožimo z naključno vrednostjo med 0 in 1, da dobimo točko v notranjosti d dimenzionalne enotske krogle
        tocka = tuple(radij * (rand_smer * rand_dolzina)) #če bi želeli gledati večjo kroglo lahko spremenimo tudi vrednost radija.
        mnozica_tock.add(tocka)
    return mnozica_tock

print(random_krogla(50, 3))