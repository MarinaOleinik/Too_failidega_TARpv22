def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

from gtts import gTTS
import os
def Heli(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
from random import *
def Teadmiste_kontroll(rus:list,est:list):
    p=0
    kokku=int(input("Mitu küsimust?"))
    for i in range(kokku):
        järjend=choice([rus,est])
        sõna=choice(järjend)
        print(f"{sõna} - ", end="")
        tõlke=input()
        if sõna in rus:
            i=rus.index(sõna)
            tõlke_kontroll=est[i]
        elif sõna in est:
            i=est.index(sõna)
            tõlke_kontroll=rus[i]
        if tõlke==tõlke_kontroll: 
            p+=1
            print("Õige")
        else:
            print("Vale")
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else:
        hinne="Väga halb!"
    return hinne