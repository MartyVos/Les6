def seizoen(maand):
    if 3 <= maand <= 5:
        print("Lente")
    elif 6 <= maand <= 8:
        print("Zomer")
    elif 9 <= maand <= 11:
        print("Herfst")
    elif maand == 12 or (1 <= maand <= 2):
        print("Winter")


c = 1
while c == 1:
    x = eval(input("Voer een een getal in. 1 t/m 12: "))
    if x <= 0 or x >= 13:
        c = 1
    else:
        seizoen(x)
        c = 0
