from random import *
def kasutajaandmed(n:list,p:list):
    """siin toimub registreerimine
    """
    print("sisestada andmeid või juhuslikult?")
    b=input("vastus: ")
    if b=="sisetage":
        nimi=input("sisetage nimi: ")       
    print("Kas sa tahad sisetada parool või random?")
    b=input("vastus:")
    if b=="sisetage":
        nimi=input("sisetage nimi: ")      
        parool=input("sisetage  salasõna maksimalselt 8 värtused: ")
        n=len(parool)
        while n<8:
            parool=input("salasõna on lühike. Palun kirjuta veel: ")
            n=len(parool)
    elif b=="random":
        login=input("Kirjutage teie nimi: ")
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        #print(str4)
        ls = list(str4)
        #print(ls)
        shuffle(ls)
        #print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = "".join([choice(ls) for x in range(12)])
    n.append(nimi)
    p.append(psword)
    return nimi,psword
 
def aut(n:list,p:list):
    """siin on autoriseerimine 
    """
    print("sisetage nimi j salasõna")
    nim=input("nimi: ")
    par=input("Salasõna: ")
    if nim in n and par in p:
        print("Tere tulemast!")
    else: 
        print("Ebaõiged andmed")
    return nim, par

def uss_nimi(n:list,vananimi:list,uusnimi:list):
    """Siin saab oma nimi kustutada.
    """
    if vananimi in n:
        index=n.index(vananimi)
        n[index]=uusnimi
        print("nimi on muudetud.")
    else:
        print("viga!")

def uss_salasõna(n,p,nimi,vanasalasõna,uussalasõna):
    """Siin saab oma parooli kustutada.
    """
    if nimi in n and vanasalasõna in p:
        index=n.index(nimi)
        p[index]=uussalasõna
        print("salasõna on muudetud")
    else:
        print("viga!")
        
def nimii(n,p,nimo):
    """Siin saab vaadata oma vana parooli.
    """
    if nimo in n:
        index=n.index(nimo)
        print(f"vana salasõna on:",p[index])
    else: 
        print("viga!")




