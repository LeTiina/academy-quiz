#tehdään tänne hieno ohjelma

pelataanko = input("Haluatko pelata? (kyllä,ei)")
kysymykset = {"Onko kissat kivoja?":"kyllä", "Onko koirat kivoja?":"kyllä"}

while(pelataanko == "kyllä"):
    pisteet = 0
    for kysymys,vastaus in kysymykset:
        pelaajan_vastaus = input(kysymys)
            if pelaajan_vastaus == vastaus:
                pisteet += 1
                print("Oikea vastaus!")
            else:
                print("Väärä vastaus")
    


