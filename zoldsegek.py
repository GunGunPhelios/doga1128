from ast import main


class Zoldseg:
    def __init__(self,nev, ar, mennyiseg, termesev):
        self.nev=nev
        self.ar=int(ar)
        self.mennyiseg= int(mennyiseg)
        self.termesev= int(termesev)

    def __repr__(self):
        return f"{self.nev}; {self.ar}; {self.mennyiseg}; {self.termesev}"
    

def beolvasfile(filenev):
        Zoldsegek=[]
        with open (filenev, "r", encoding= "UTF-8") as file:
            for sor in file:
                nev,ar,mennyiseg,termesev= sor.strip().split(";")
                Zoldsegek.append(Zoldseg(nev,ar,mennyiseg,termesev))
        return Zoldsegek

def kiirkonzol(zoldsegek):
        print("A fájl tartalma: ")
        for zoldseg in zoldsegek:
            print(zoldseg)


def zoldsegek2015utan(zoldsegek):
        eredmeny=[zoldseg for zoldseg in zoldsegek if zoldseg.termesev> 2015]
        print("\nZöldségek amelyek 2015 után volt termésük: ")
        for zoldseg in eredmeny:
            print(zoldseg)
        return eredmeny

def legolcsobbzoldseg(zoldsegek):
        legolcsobb=min(zoldsegek, key=lambda z: z.ar)
        print(f"\nLegolcsóbb zöldség: {legolcsobb.nev}, ára: {legolcsobb.ar} Ft.")
        return legolcsobb
    
def paprikakezdo(zoldsegek):
        paprikalista=[zoldseg for zoldseg in zoldsegek if zoldseg.nev.lower().startswith("paprika")]
        print(f"\nZöldségek száma, amelyek neve 'paprika'-val kezdődik: {len(paprikalista)}")
        print("\nPaprika nevű zöldségek:")
        for zoldseg in paprikalista:
            print(zoldseg)
        return paprikalista
    
def kiirfajlba(filenev2,zoldsegek):
        with open(filenev2, "w", encoding="UTF-8") as file:
            for zoldseg in zoldsegek:
                file.write(f"{str(zoldseg)}\n")
            print(f"\n{filenev2} fájl létrehozva paprika nevű zöldségekkel.")
  
  
def main():
    zoldsegek = beolvasfile("C:/Users/Asus-01/Desktop/(Monty) Python/dolgozat 1128/zoldsegek.txt")
    kiirkonzol(zoldsegek)
    zoldsegek_2015 = zoldsegek2015utan(zoldsegek)
    legolcsobb = legolcsobbzoldseg(zoldsegek)
    paprika_lista = paprikakezdo(zoldsegek)
    kiirfajlba("zoldsegesWfajl.txt", paprika_lista)
        


if __name__ == "__main__":
    main()



