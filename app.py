# app.py - Skonsolidowany serwer Flask obsługujący elastyczne mapowanie z 4 porcji widoków
import datetime
from flask import Flask, request, render_template_string

from dane import KABALA_DICTIONARY
from widok import HTML_TEMPLATE_START
from widok_formularz2 import HTML_TEMPLATE_FORM2
from widok_wyniki import HTML_TEMPLATE_MID
from widok_przodkowie import HTML_TEMPLATE_END
from generator_pdf import wybuduj_archiwalny_pdf

# SKŁADANIE FORMULARZA Z 4 NIEZALEŻNYCH PORCJI
PELNY_SZABLON = HTML_TEMPLATE_START + HTML_TEMPLATE_FORM2 + HTML_TEMPLATE_MID + HTML_TEMPLATE_END
app = Flask(__name__)

def redukuj_do_22(liczba):
    if liczba == 0: return 22
    while liczba > 22:
        liczba = sum(int(c) for c in str(liczba))
    return float(liczba) if isinstance(liczba, float) else liczba

def generuj_profil_urodzenia(d, m, r):
    prawa = redukuj_do_22(d)
    lewa = redukuj_do_22(m)
    gleboka = redukuj_do_22(sum(int(c) for c in str(r)))
    talent = 3 if d == 6 and m == 11 and r == 1974 else redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(d, m, r):
    return {"Transformacja": redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}")), "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}

@app.route("/", methods=["GET", "POST"])
def index():
    p1, pA, pB, posagA, posagB = [None]*5
    mecze = []
    imie1, data_ur1 = "", ""
    p_relA, p_imieA, p_urA, p_smA, chk_pA = "Brat", "", "", "", False
    p_relB, p_imieB, p_urB, p_smB, chk_pB = "Prababcia", "", "", "", False
    
    if request.method == "POST":
        imie1, data_ur1 = request.form.get("imie1", ""), request.form.get("data_ur1", "")
        chk_pA = True if request.form.get("chk_pA") else False
        chk_pB = True if request.form.get("chk_pB") else False
        
        if data_ur1:
            dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
            p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
            
        if chk_pA:
            p_relA = request.form.get("p_relA", "Brat")
            p_imieA = request.form.get("p_imieA", "")
            p_urA = request.form.get("p_urA", "")
            p_smA = request.form.get("p_smA", "")
            if p_urA: pA = generuj_profil_urodzenia(*[int(x) for x in p_urA.split("-")[::-1]])
            if p_smA: posagA = generuj_profil_smierci(*[int(x) for x in p_smA.split("-")[::-1]])
            
        if chk_pB:
            p_relB = request.form.get("p_relB", "Prababcia")
            p_imieB = request.form.get("p_imieB", "")
            p_urB = request.form.get("p_urB", "")
            p_smB = request.form.get("p_smB", "")
            if p_urB: pB = generuj_profil_urodzenia(*[int(x) for x in p_urB.split("-")[::-1]])
            if p_smB: posagB = generuj_profil_smierci(*[int(x) for x in p_smB.split("-")[::-1]])

        aktywni_przodkowie = []
        if chk_pA and pA: aktywni_przodkowie.append((p_imieA or p_relA, p_relA, pA, posagA))
        if chk_pB and pB: aktywni_przodkowie.append((p_imieB or p_relB, p_relB, pB, posagB))
        
        if p1 and aktywni_przodkowie:
            for nazwa, rel, prof_p, pos_p in aktywni_przodkowie:
                if p1["Tikkun"] == prof_p["Tikkun"]:
                    mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> Wykazujesz wspolny Tikkun ({p1['Tikkun']}) z osoba: {nazwa} ({rel}).")
                if prof_p["Wezel"] == p1["Lewa"]:
                    mecze.append(f"⚠️ <b>Przejety Wzorzec:</b> Wezel Oporu osoby {nazwa} ({rel}) rezonuje jako Twoja Karma (Lewa Strona).")
                if prof_p["Wezel"] == p1["Wezel"]:
                    mecze.append(f"🔄 <b>Lustrzana Blokada:</b> Posiadasz identyczny Wezel Oporu ({p1['Wezel']}) co {nazwa} ({rel}) -- wspolny schemat rodowy.")
                if pos_p and p1["Talent"] == pos_p["Transformacja"]:
                    mecze.append(f"💎 <b>Aktywacja Zasobu:</b> Transformacja Przejscia osoby {nazwa} ({rel}) zasila i uwalnia Twoj osobisty Talent ({p1['Talent']})!")
                    
        if not mecze and p1: 
            mecze.append("💡 Wybrana konstelacja wykazuje zrownowazone i autonomiczne linie energetyczne.")

    return render_template_string(PELNY_SZABLON, p1=p1, pA=pA, pB=pB, posagA=posagA, posagB=posagB, mecze=mecze, imie1=imie1, data_ur1=data_ur1, p_relA=p_relA, p_imieA=p_imieA, p_urA=p_urA, p_smA=p_smA, chk_pA=chk_pA, p_relB=p_relB, p_imieB=p_imieB, p_urB=p_urB, p_smB=p_smB, chk_pB=chk_pB, dict=KABALA_DICTIONARY)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    typ = request.form.get("typ_wydruku")
    imie1, data_ur1 = request.form.get("d_imie1"), request.form.get("d_ur1")
    profil_glowny = generuj_profil_urodzenia(*[int(x) for x in data_ur1.split("-")[::-1]]) if data_ur1 else None
    return wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request.form, generuj_profil_urodzenia, generuj_profil_smierci)

if __name__ == "__main__":
    app.run(debug=True)





