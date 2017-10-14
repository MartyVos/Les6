invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split("-")

for x in range(len(lijst)):
    lijst[x] = int(lijst[x])

ln = len(lijst)
mn = int(min(lijst))
mx = int(max(lijst))
som = int(sum(lijst))
gem = som / ln

lijst.sort()

print("Gesorteerde list van ints:", lijst)
print("Grootste getal:", mx, "en Kleinste getal:", mn)
print("Aantal getallen:", ln, "en Som van de getallen:", som)
print("Gemiddelede:", gem)
