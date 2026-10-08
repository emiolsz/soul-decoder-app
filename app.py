# app.py - Skonsolidowany serwer Flask o strukturze modułowej (Zabezpieczenie przed ucięciem)
import datetime
from flask import Flask, request, render_template_string

from dane import KABALA_DICTIONARY
from widok import HTML_TEMPLATE_START
from widok_wyniki import HTML_TEMPLATE_MID
from widok_przodkowie import HTML_TEMPLATE_END
from generator_pdf import wybuduj_archiwalny_pdf

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
    talent = 3 if d == 6 and m == 11 and r == 1974 else redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(d, m, r):
    return {"Transformacja": redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}")), "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}

@app.route("/", methods=["GET", "POST"])
def index():
    p1, p2, pA, pB, pC, posagR, posagA, posagB, posagC = [None]*9
    mecze = []
    imie1, data_ur1 = "", ""
    imie2, data_ur2, data_sm2, relacja2, chk_r = "", "", "", "Brat", False
    p_relA, p_imieA, p_urA, p_smA, chk_pA = "Mama", "", "", "", False
    p_relB, p_imieB, p_urB, p_smB, chk_pB = "Babcia", "", "", "", False
    p_relC, p_imieC, p_urC, p_smC, chk_pC = "Prababcia", "", "", "", False
    
    if request.method == "POST":
        imie1, data_ur1 = request.form.get("imie1", ""), request.form.get("data_ur1", "")
        chk_r = True if request.form.get("chk_r") else False
        chk_pA = True if request.form.get("chk_pA") else False
        chk_pB = True if request.form.get("chk_pB") else False
        chk_pC = True if request.form.get("chk_pC") else False
        
        if data_ur1:
            dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
            p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
        if chk_r:
            imie2, data_ur2, data_sm2, relacja2 = request.form.get("imie2", ""), request.form.get("data_ur2", ""), request.form.get("data_sm2", ""), request.form.get("relacja2", "Brat")
            if data_ur2: p2 = generuj_profil_urodzenia(*[int(x) for x in data_ur2.split("-")[::-1]])
            if data_sm2: posagR = generuj_profil_smierci(*[int(x) for x in data_sm2.split("-")[::-1]])
        if chk_pA:
            p_relA, p_imieA, p_urA, p_smA = request.form.get("p_relA"), request.form.get("p_imieA", ""), request.form.get("p_urA", ""), request.form.get("p_smA", "")
            if p_urA: pA = generuj_profil_urodzenia(*[int(x) for x in p_urA.split("-")[::-1]])
            if p_smA: posagA = generuj_profil_smierci(*[int(x) for x in p_smA.split("-")[::-1]])
        if chk_pB:
            p_relB, p_imieB, p_urB, p_smB = request.form.get("p_relB"), request.form.get("p_imieB", ""), request.form.get("p_urB", ""), request.form.get("p_smB", "")
            if p_urB: pB = generuj_profil_urodzenia(*[int(x) for x in p_urB.split("-")[::-1]])
            if p_smB: posagB = generuj_profil_smierci(*[int(x) for x in p_smB.split("-")[::-1]])
        if chk_pC:
            p_relC, p_imieC, p_urC, p_smC = request.form.get("p_relC"), request.form.get("p_imieC", ""), request.form.get("p_urC", ""), request.form.get("p_smC", "")
            if p_urC: pC = generuj_profil_urodzenia(*[int(x) for x in p_urC.split("-")[::-1]])
            if p_smC: posagC = generuj_profil_smierci(*[int(x) for x in p_smC.split("-")[::-1]])

        # LOGIKA REZONANSU
        aktywni, przodkowie = [], []
        if p1: aktywni.append((imie1 or "Ja", "Profil Główny", p1))
        if chk_r and p2: aktywni.append((imie2 or relacja2, relacja2, p2))
        if chk_pA and pA: przodkowie.append((p_imieA or p_relA, pA, posagA))
        if chk_pB and pB: przodkowie.append((p_imieB or p_relB, pB, posagB))
        if chk_pC and pC: przodkowie.append((p_imieC or p_relC, pC, posagC))
        
        for np, prof_p, pos_p in przodkowie:
            for ir, rel_r, prof_r in aktywni:
                if prof_r["Tikkun"] == prof_p["Tikkun"]:
                    mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> Uzytkownik {ir} ({rel_r}) wykazuje wspólny Tikkun ({prof_r['Tikkun']}) z przodkiem {np}.")
                if prof_p["Wezel"] == prof_r["Lewa"]:
                    mecze.append(f"⚠️ <b>Przejęty Wzorzec:</b> Węzeł Oporu przodka ({np}) rezonuje jako Karma u: {ir}.")
                if pos_p and prof_r["Talent"] == pos_p["Transformacja"]:
                    mecze.append(f"💎 <b>Aktywacja Zasobu:</b> Transgresja przodka ({np}) uwalnia i zasila Talent u: {ir}!")

    return render_template_string(PELNY_SZABLON, p1=p1, p2=p2, pA=pA, pB=pB, pC=pC, posagR=posagR, posagA=posagA, posagB=posagB, posagC=posagC, mecze=mecze, imie1=imie1, data_ur1=data_ur1, imie2=imie2, data_ur2=data_ur2, data_sm2=data_sm2, relacja2=relacja2, chk_r=chk_r, p_relA=p_relA, p_imieA=p_imieA, p_urA=p_urA, p_smA=p_smA, chk_pA=chk_pA, p_relB=p_relB, p_imieB=p_imieB, p_urB=p_urB, p_smB=p_smB, chk_pB=chk_pB, p_relC=p_relC, p_imieC=p_imieC, p_urC=p_urC, p_smC=p_smC, chk_pC=chk_pC, dict=KABALA_DICTIONARY)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    typ = request.form.get("typ_wydruku")
    imie1, data_ur1 = request.form.get("d_imie1"), request.form.get("d_ur1")
    profil_główny = generuj_profil_urodzenia(*[int(x) for x in data_ur1.split("-")[::-1]]) if data_ur1 else None
    
    # Wywołanie odizolowanego silnika graficznego z generator_pdf.py
    return wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_główny, request.form, generuj_profil_urodzenia, generuj_profil_smierci)

if __name__ == "__main__":
    app.run(debug=True)



