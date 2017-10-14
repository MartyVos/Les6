def gemiddelde_per_student(studentencijfers):
    antw = []
    for x in range(len(studentencijfers)):
        som = sum(studentencijfers[x])
        ln = len(studentencijfers[x])
        antw.append(som / ln)
    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    lijst = gemiddelde_per_student(studentencijfers)
    som = sum(lijst)
    ln = len(lijst)
    antw = som / ln
    return antw


studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
