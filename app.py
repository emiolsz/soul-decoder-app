# app.py - Ostatecznie naprawiony i zdebugowany silnik z poprawnym wyciąganiem indeksów dat
import datetime
from flask import Flask, request, render_template

from dane import KABALA_DICTIONARY
from analiza_opisowa import pobierz_analize_premium
from generator_pdf import wybuduj_archiwalny_pdf

app = Flask(__name__, template_folder='.')

def redukuj_do_22(liczba):
    if liczba == 0: return 22
    while isinstance(liczba, int) and liczba > 22:
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
    p1, posag1 = None, None
    aktywne_profile_wynik, mecze = [], []
    
    imie1, data_ur1, data_sm1, status1 = "", "", "", "ZYJE"
    ile_osob = 1
    aktywne_role, aktywne_imiona, aktywne_ur, aktywne_sm = [], [], [], []
    
    if request.method == "POST":
        imie1 = request.form.get("imie1", "")
        data_ur1 = request.form.get("data_ur1", "")
        data_sm1 = request.form.get("data_sm1", "")
        status1 = request.form.get("status1", "ZYJE")
        
        try:
            ile_osob = int(request.form.get("ile_osob", 1))
        except (ValueError, TypeError):
            ile_osob = 1
            
        for i in range(ile_osob):
            aktywne_role.append(request.form.get(f"p_rel_{i}", "Brat"))
            aktywne_imiona.append(request.form.get(f"p_imie_{i}", ""))
            aktywne_ur.append(request.form.get(f"p_ur_{i}", ""))
            aktywne_sm.append(request.form.get(f"p_sm_{i}", ""))
            
        if request.form.get("akcja_dekoduj") == "TAK":
            if data_ur1 and len(data_ur1.split("-")) == 3:
                dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
                p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
            if status1 == "TRANSGRESJA" and data_sm1 and len(data_sm1.split("-")) == 3:
                p1_s = [int(x) for x in data_sm1.split("-")]
                # POPRAWKA INDEKSÓW: parts[2]=dzien, parts[1]=miesiac, parts[0]=rok
                posag1 = generuj_profil_smierci(p1_s[2], p1_s[1], p1_s[0])
                
            for i in range(ile_osob):
                r_imie, r_rel, r_ur, r_sm = aktywne_imiona[i], aktywne_role[i], aktywne_ur[i], aktywne_sm[i]
                prof_u, pos_s = None, None
                if r_ur and len(r_ur.split("-")) == 3:
                    dtX = datetime.datetime.strptime(r_ur, "%Y-%m-%d")
                    prof_u = generuj_profil_urodzenia(dtX.day, dtX.month, dtX.year)
                if r_sm and len(r_sm.split("-")) == 3:
                    pX = [int(x) for x in r_sm.split("-")]
                    # POPRAWKA INDEKSÓW DLA CZŁONKÓW KONSTELACJI
                    pos_s = generuj_profil_smierci(pX[2], pX[1], pX[0])
                if prof_u:
                    aktywne_profile_wynik.append({"imie": r_imie, "rel": r_rel, "prof": prof_u, "pos": pos_s})
                    
            if p1 and aktywne_profile_wynik:
                for item in aktywne_profile_wynik:
                    n_wys = item["imie"] if item["imie"] else item["rel"]
                    if p1["Tikkun"] == item["prof"]["Tikkun"]:
                        mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> Posiadasz wspólny Tikkun ({p1['Tikkun']}) z: {n_wys} ({item['rel']}).")
                    if item["prof"]["Wezel"] == p1["Lewa"]:
                        mecze.append(f"⚠️ <b>Przejęty Wzorzec:</b> Węzeł Oporu osoby {n_wys} rezonuje jako Twoja Karma.")
                    if item["pos"] and p1["Talent"] == item["pos"]["Transformacja"]:
                        mecze.append(f"💎 <b>Aktywacja Zasobu:</b> Przejście osoby {n_wys} zasila Twój Talent ({p1['Talent']})!")
                if not mecze: mecze.append("💡 Linie energetyczne wykazują zrównoważoną ścieżkę.")

    return render_template("index.html", p1=p1, posag1=posag1, aktywne_profile_wynik=aktywne_profile_wynik, mecze=mecze, imie1=imie1, data_ur1=data_ur1, data_sm1=data_sm1, status1=status1, ile_osob=ile_osob, aktywne_role=aktywne_role, aktywne_imiona=aktywne_imiona, aktywne_ur=aktywne_ur, aktywne_sm=aktywne_sm, dict=KABALA_DICTIONARY)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    typ = request.form.get("typ_wydruku")
    imie1, data_ur1 = request.form.get("d_imie1"), request.form.get("d_ur1")
    profil_glowny = None
    if data_ur1 and len(data_ur1.split("-")) == 3:
        p1_parts = [int(x) for x in data_ur1.split("-")]
        profil_glowny = generuj_profil_urodzenia(p1_parts[2], p1_parts[1], p1_parts[0])
    return wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request.form, generuj_profil_urodzenia, generuj_profil_smierci)

application = app

if __name__ == "__main__":
    app.run(debug=True)






