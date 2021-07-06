
#tehtiin tänne hieno ohjelma

pelataanko = input("Haluatko pelata? (kyllä,ei) ")
kysymykset = {"Onko kissat kivoja? kyllä/ei ":"kyllä", "Onko koirat kivoja? kyllä/ei ":"kyllä"}

while(pelataanko == "kyllä"):
    pisteet = 0
    for kysymys in kysymykset:
        pelaajan_vastaus = input(kysymys)
        if pelaajan_vastaus == kysymykset[kysymys]:
            pisteet += 1
            print("Oikea vastaus!")
        else:
            print("Väärä vastaus")
    print(f"Sait pisteitä {pisteet}")
    pelataanko = input("Haluatko pelata uudestaan? kyllä/ei ")

print("ei sitten. heihei")

#hyvää työtä!


