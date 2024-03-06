import random
import os
from gtts import gTTS

def loe_failist(file_path):
    """loeb failist
    """
    with open(file_path,'r',encoding="utf-8") as file:
        sonad=[line.strip() for line in file]
    return sonad
def kirjuta(file_path,sonad):
    """lubab kirjutada failis
    """
    with open(file_path,'w',encoding="utf-8") as file:
        for sona in sonad:
            file.write(sona+'\n')
def tolge_vene(sona):
    """tolgib eesti keelest vene keele
    """
    if sona in estonian_to_russian:
        return estonian_to_russian[sona]
    else:
        print("Sona pole leitud")
        lisa_sona=input("Soovite lisada sona? jah/ei ").strip().lower()
        if lisa_sona=="jah":
            tolge=input("Sisesta tolge vene keeles ").strip()
            estonian_to_russian[sona]=tolge
            kirjuta("rus.txt",list(estonian_to_russian.keys()))
            kirjuta("est.txt",list(estonian_to_russian.values()))
            print("Sona on edukalt lisatud")
            return tolge
        else:
            return None
def tolge_est(sona):
    if sona in russian_to_estonian:
        return russian_to_estonian[sona]
    else:
        print("Sona pole leitud")
        lisa_sona=input("Soovite lisada sona? jah/ei ").strip().lower()
        if lisa_sona=="jah":
            tolge = input("Sisesta tolge vene keeles: ").strip()
            russian_to_estonian[sona]=tolge
            kirjuta("est.txt", list(russian_to_estonian.keys()))
            kirjuta("rus.txt", list(russian_to_estonian.values()))
            print("Sona on edukalt lisatud")
            return tolge
        else:
            return None
def test_():
    kokku_sonad=len(russian_to_estonian)
    oiged_vastused=0
    for russian_word,estonian_word in russian_to_estonian.items():
        print(f"Tolgi '{russian_word}' eesti keele ")
        answer = input("Tolge: ").strip().lower()
        if answer == estonian_word.lower():
            print("Oige")
            oiged_vastused+=1
        else:
            print("Vale")
    tapsus=(oiged_vastused / kokku_sonad) * 100
    print(f"Вы правильно перевели {oiged_vastused} из {kokku_sonad} слов. Точность: {tapsus}%")
def koneleja(sona):
    keel = "ru" if sona in russian_words else "et"
    tts = gTTS(text=sona, lang=keel)
    tts.save("temp.mp3")
    os.system("start temp.mp3")

russian_words=loe_failist("rus.txt")
estonian_words=loe_failist("est.txt")
russian_to_estonian={}
estonian_to_russian={}
for russian,estonian in zip(russian_words, estonian_words):
    russian_to_estonian[russian]=estonian
    estonian_to_russian[estonian]=russian
while True:
    print("\n1. Tolgi vene keele")
    print("2. Rolgi eesti keele")
    print("3. Test")
    print("4. Koneleja")
    print("5. Valju")
    vastus=input("Vali tegevus: ").strip()
    if vastus=='1':
        estonian_word=input("Sisesta sona eesti keeles: ").strip()
        tolge=tolge_vene(estonian_word)
        if tolge:
            print(f"Togle vene keeles: {tolge}")
    elif vastus=='2':
        russian_word=input("Sisesta sona vene keeles: ").strip()
        tolge=tolge_est(russian_word)
        if tolge:
            print(f"Перевод на эстонский: {tolge}")
    elif vastus=='3':
        test_()
    elif vastus=="4":
        sona=input("Sisesta sona: ")
        koneleja(sona)
    elif vastus=='5':
        print("Tsauki")
        break
    else:
        print("viga")
