kerdes=input("Milyen változót szeretne átváltani? (liter/deciliter):").lower()
mennyiseg=float(input("Hány l/dl tejet szeretne?"))

if kerdes == "liter":
    eredmeny= mennyiseg*10
    print(f"{mennyiseg} liter= {int(eredmeny)} deciliter.")
elif kerdes == "deciliter":
    eredmeny= mennyiseg/10
    print(f"{mennyiseg} deciliter = {int(eredmeny)} liter.")
else:
    print("Érvénytelen mértékegység. Kérem adjon meg litert vagy decilitert.")



