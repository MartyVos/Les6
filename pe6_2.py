lijst = eval(input("Geef een lijst met minimaal 10 strings: "))
lengte = len(lijst)
n_lijst = []

for x in range(lengte):
    if len(lijst[x]) == 4:
        n_lijst.append(lijst[x])

print("De nieuw-gemaakte lijst met alle vier-letter strings is:")
print(n_lijst)
