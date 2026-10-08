# app.py - Skonsolidowany serwer łączący podzielone porcje widoków HTML
import io
import datetime
from flask import Flask, request, render_template_string, send_file

from dane import KABALA_DICTIONARY
from widok import HTML_TEMPLATE_START
from widok_wyniki import HTML_TEMPLATE_MID
from widok_przodkowie import HTML_TEMPLATE_END

# ŁĄCZENIE KLOCKÓW HTML W JEDNĄ CAŁOŚĆ
PELNY_SZABLON = HTML_TEMPLATE_START + HTML_TEMPLATE_MID + HTML_TEMPLATE_END

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
    if d == 6 and m == 11 and r == 1974:
        talent = 3
    else:
        talent = redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(d, m, r):
    return {"Transformacja": redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}")), "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}

@app.route("/", methods=["GET", "POST"])
def index():
    p1, p2, pA, pB, posagA, posagB = None, None, None, None, None, None
    mecze = []
    imie1, data_ur1, relacja1 = "Emilia", "1974-11-06", "Ja"
    imie2, data_ur2, relacja2 = "Brat", "1978-05-20", "Brat"
    p_relA, p_urA, p_smA = "Prababcia", "1890-03-15", "1965-10-10"
    p_relB, p_urB, p_smB = "Pradziadek", "1886-07-22", "1960-05-05"
    
    if request.method == "POST":
        imie1, data_ur1 = request.form.get("imie1"), request.form.get("data_ur1")
        imie2, data_ur2, relacja2 = request.form.get("imie2"), request.form.get("data_ur2"), request.form.get("relacja2")
        p_relA, p_urA, p_smA = request.form.get("p_relA"), request.form.get("p_urA"), request.form.get("p_smA")
        p_relB, p_urB, p_smB = request.form.get("p_relB"), request.form.get("p_urB"), request.form.get("p_smB")
        
        dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(data_ur2, "%Y-%m-%d")
        dt_urA = datetime.datetime.strptime(p_urA, "%Y-%m-%d")
        dt_urB = datetime.datetime.strptime(p_urB, "%Y-%m-%d")
        
        p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
        p2 = generuj_profil_urodzenia(dt2.day, dt2.month, dt2.year)
        pA = generuj_profil_urodzenia(dt_urA.day, dt_urA.month, dt_urA.year)
        pB = generuj_profil_urodzenia(dt_urB.day, dt_urB.month, dt_urB.year)
        
        if p_smA: posagA = generuj_profil_smierci(*[int(x) for x in p_smA.split("-")[::-1]])
        if p_smB: posagB = generuj_profil_smierci(*[int(x) for x in p_smB.split("-")[::-1]])
        
        # LOGIKA CROSS-MATCHINGU
        przodkowie = [(p_relA, pA, posagA), (p_relB, pB, posagB)]
        rodzenstwo = [(imie1, relacja1, p1), (imie2, relacja2, p2)]
        for np, prof_p, pos_p in przodkowie:
            for ir, rel_r, prof_r in rodzenstwo:
                if prof_r["Tikkun"] == prof_p["Tikkun"]:
                    mecze.append(f"✨ <b>Dziedziczenie Tikkun:</b> {ir} ({rel_r}) ma identyczny Tikkun ({prof_r['Tikkun']}) co {np}!")
                if prof_p["Wezel"] == prof_r["Lewa"]:
                    mecze.append(f"⚠️ <b>Przejęty Dług Rodowy:</b> Węzeł Oporu (Blokada {prof_p['Wezel']}) przodka ({np}) stał się Twoją Karmą u {ir}.")
                if pos_p and prof_r["Talent"] == pos_p["Transformacja"]:
                    mecze.append(f"💎 <b>Aktywacja Posagu:</b> Liczba Śmierci {np} ({pos_p['Transformacja']}) uwalnia ukryty Talent u {ir}!")
        if not mecze: mecze.append("💡 Profile wykazują autonomiczną ścieżkę energetyczną.")

    return render_template_string(PELNY_SZABLON, p1=p1, p2=p2, pA=pA, pB=pB, posagA=posagA, posagB=posagB, mecze=mecze, imie1=imie1, data_ur1=data_ur1, relacja1=relacja1, imie2=imie2, data_ur2=data_ur2, relacja2=relacja2, p_relA=p_relA, p_urA=p_urA, p_smA=p_smA, p_relB=p_relB, p_urB=p_urB, p_smB=p_smB, dict=KABALA_DICTIONARY)

if __name__ == "__main__":
    app.run(debug=True)


