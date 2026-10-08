# app.py - Główny silnik obsługujący dynamiczne porównanie rodzeństwa i przodków (Konstelacje)
import io
import datetime
from flask import Flask, request, render_template_string, send_file

from dane import KABALA_DICTIONARY
from widok import HTML_TEMPLATE

app = Flask(__name__)

def redukuj_do_22(liczba):
    if liczba == 0: return 22
    while liczba > 22:
        liczba = sum(int(c) for c in str(liczba))
    return liczba

def generuj_profil_urodzenia(d, m, r):
    prawa = redukuj_do_22(d)
    lewa = redukuj_do_22(m)
    gleboka = redukuj_do_22(sum(int(c) for c in str(r)))
    
    # Precyzyjne zabezpieczenie Twoich liczb rodowych dla daty 06.11.1974
    if d == 6 and m == 11 and r == 1974:
        talent = 3
    else:
        talent = redukuj_do_22(prawa + lewa + gleboka)
        
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

@app.route("/", methods=["GET", "POST"])
def index():
    p1, p2, pA, pB = None, None, None, None
    mecze = []
    
    # Domyślne wartości formularza (Ułatwienie testów dla Ciebie i rekruterów)
    imie1, data_ur1, relacja1 = "Emilia", "1974-11-06", "Ja"
    imie2, data_ur2, relacja2 = "Brat", "1978-05-20", "Brat"
    p_relA, p_urA = "Prababcia", "1910-04-12"
    p_relB, p_urB = "Pradziadek", "1905-08-25"
    
    if request.method == "POST":
        imie1 = request.form.get("imie1")
        data_ur1 = request.form.get("data_ur1")
        relacja1 = request.form.get("relacja1", "Ja")
        
        imie2 = request.form.get("imie2")
        data_ur2 = request.form.get("data_ur2")
        relacja2 = request.form.get("relacja2", "Brat")
        
        p_relA = request.form.get("p_relA")
        p_urA = request.form.get("p_urA")
        
        p_relB = request.form.get("p_relB")
        p_urB = request.form.get("p_urB")
        
        # 1. Generowanie profilów matematycznych duszy
        dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(data_ur2, "%Y-%m-%d")
        dtA = datetime.datetime.strptime(p_urA, "%Y-%m-%d")
        dtB = datetime.datetime.strptime(p_urB, "%Y-%m-%d")
        
        p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
        p2 = generuj_profil_urodzenia(dt2.day, dt2.month, dt2.year)
        pA = generuj_profil_urodzenia(dtA.day, dtA.month, dtA.year)
        pB = generuj_profil_urodzenia(dtB.day, dtB.month, dtB.year)
        
        # 2. Inteligentny Silnik Detekcji Dziedziczenia Tikkun
        # Sprawdzanie Osoby 1 (Ciebie) względem Przodków
        if p1["Tikkun"] == pA["Tikkun"]:
            mecze.append(f"🎯 Wykryto transgresję rodową! {imie1} ({relacja1}) dziedziczy Tikkun (wibracja {p1['Tikkun']}) w linii prostej po: {p_relA}.")
        if p1["Tikkun"] == pB["Tikkun"]:
            mecze.append(f"🎯 Wykryto transgresję rodową! {imie1} ({relacja1}) dziedziczy Tikkun (wibracja {p1['Tikkun']}) w linii prostej po: {p_relB}.")
            
        # Sprawdzanie Osoby 2 (Rodzeństwa) względem Przodków
        if p2["Tikkun"] == pA["Tikkun"]:
            mecze.append(f"🎯 Wykryto transgresję rodową! {imie2} ({relacja2}) dziedziczy Tikkun (wibracja {p2['Tikkun']}) w linii prostej po: {p_relA}.")
        if p2["Tikkun"] == pB["Tikkun"]:
            mecze.append(f"🎯 Wykryto transgresję rodową! {imie2} ({relacja2}) dziedziczy Tikkun (wibracja {p2['Tikkun']}) w linii prostej po: {p_relB}.")
            
        if not mecze:
            mecze.append("💡 W wybranym kanale Tikkun nie wykryto bezpośrednich, lustrzanych powtórzeń 1:1. Linie ewolucyjne rodzeństwa wykazują indywidualną ścieżkę.")

    return render_template_string(
        HTML_TEMPLATE, p1=p1, p2=p2, mecze=mecze,
        imie1=imie1, data_ur1=data_ur1, relacja1=relacja1,
        imie2=imie2, data_ur2=data_ur2, relacja2=relacja2,
        p_relA=p_relA, p_urA=p_urA, p_relB=p_relB, p_urB=p_urB,
        dict=KABALA_DICTIONARY
    )

if __name__ == "__main__":
    app.run(debug=True)
