tabor= input("Adja meg a hét nevét: ")

kcal= []
while len(kcal) < 5:
    napikcal= float(input(f"Kérjem adja meg {len(kcal)+1 } a napi kalóriamennyiséget: "))
    kcal.append(napikcal)
    if len(kcal) >= 5:
        moreinfo= input("Szeretne még több adatot megadni? (i/n): ").lower()
        if moreinfo != "igen":
            break
átlagkcal= sum(kcal) / len(kcal)


print(f"\nA hét neve: {tabor}.")
print(f"\nAz átlagosan elégetett kalóriák naponta: {int(átlagkcal)}.")


