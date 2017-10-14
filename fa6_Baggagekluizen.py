def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt", "r")
    aantal = len(file.readlines())
    over = 12 - aantal
    file.close()
    print("Er zijn nog", over, "kluizen over.")


def nieuwe_kluis():
    kluis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nr = []
    file = open("kluizen.txt", "r")
    regel = len(file.readlines())
    file.seek(0)

    for x in range(12):
        if regel > x:
            nr.append(int(file.readline().split(";")[0]))
            kluis.remove(nr[x])
    file.close()

    file1 = open("kluizen.txt", "a")
    if regel != 12:
        wachtwoord = input("Voer een wachtwoord in: ")
        mijnKluis = kluis[0]
        print("Jouw kluisnummer is", mijnKluis)
        file1.write("\n")
        file1.write(str(mijnKluis))
        file1.write(";")
        file1.write(wachtwoord)
    else:
        print("Er zijn geen vrije kluizen.")
    file1.close()


def kluis_openen():
    mijnKluis = input("Voer uw kluisnummer in: ")
    wachtwoord = input("Voer uw wachtwoord in: ")
    temp = []
    gegevens = []
    file = open("kluizen.txt", "r")
    file.seek(0)

    for x in range(12):
        temp.append(file.readline().split("\n")[0])
        gegevens.append(temp[x].split(";"))

        if mijnKluis in gegevens[x][0]:
            if wachtwoord in gegevens[x][1]:
                print("Baggagekluis", mijnKluis, "is geopend.")
                break
            elif wachtwoord not in gegevens[x][1]:
                print("Kluisnummer of wachtwoord verkeerd ingevoerd.")
    file.close()


stop = 0
while stop != 1:
    print("1        Toon het aantal vrije kluizen.\n2        Vraag een kluis aan.\n3        Kluis openen.")
    print("4        Kluis verwijderen.\n5        Stoppen")
    keuze = eval(input("Kies een optie: "))

    if type(keuze) == int and keuze == 1:
        toon_aantal_kluizen_vrij()
    elif type(keuze) == int and keuze == 2:
        nieuwe_kluis()
    elif type(keuze) == int and keuze == 3:
        kluis_openen()
    elif type(keuze) == int and keuze == 4:
        print("NIKS")
    elif type(keuze) == int and keuze == 5:
        print("Tot ziens")
        stop = 1
    else:
        print("Voer een geldig getal in.")
        stop = 0
