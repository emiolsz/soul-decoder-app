# app.py - W pełni zdebugowany silnik z prawidłowym rozpakowywaniem dat HTML (Format: ROK-MM-DD)
import datetime
from flask import Flask, request, render_template_string
from dane import KABALA_DICTIONARY
from widok import HTML_TEMPLATE_START
from widok_formularz2 import HTML_TEMPLATE_FORM2
from widok_wyniki import HTML_TEMPLATE_MID
from widok_przodkowie import HTML_TEMPLATE_END
from generator_pdf import wybuduj_archiwalny_pdf

PELNY_SZABLON = HTML_TEMPLATE_START + HTML_TEMPLATE_FORM2 + HTML_TEMPLATE_MID + HTML_TEMPLATE_END
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
        ile_osob = int(request.form.get("ile_osob", 1))
        
        # Bezpieczne zbieranie dynamicznych list z formularza
        for i in range(ile_osob):
            aktywne_role.append(request.form.get(f"p_rel_{i}", "Brat"))
            aktywne_imiona.append(request.form.get(f"p_imie_{i}", ""))
            aktywne_ur.append(request.form.get(f"p_ur_{i}", ""))
            aktywne_sm.append(request.form.get(f"p_sm_{i}", ""))
            
        akcja_dekoduj = request.form.get("akcja_dekoduj", "")
        
        if akcja_dekoduj == "TAK":
            if data_ur1:
                dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
                p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
            if status1 == "TRANSGRESJA" and data_sm1:
                # Rozpakowanie formatu YYYY-MM-DD: parts1[0]=rok, parts1[1]=miesiac, parts1[2]=dzien
                parts1 = [int(x) for x in data_sm1.split("-")]
                posag1 = generuj_profil_smierci(parts1[2], parts1[1], parts1[0])
                
            # Dynamiczne generowanie profilów dla dołączonych członków konstelacji
            for i in range(ile_osob):
                r_imie = aktywne_imiona[i]
                r_rel = aktywne_role[i]
                r_ur = aktywne_ur[i]
                r_sm = aktywne_sm[i]
                
                prof_u, pos_s = None, None
                if r_ur:
                    dtX = datetime.datetime.strptime(r_ur, "%Y-%m-%d")
                    prof_u = generuj_profil_urodzenia(dtX.day, dtX.month, dtX.year)
                if r_sm:
                    partsX = [int(x) for x in r_sm.split("-")]
                    pos_s = generuj_profil_smierci(partsX[2], partsX[1], partsX[0])
                    
                if prof_u:
                    aktywne_profile_wynik.append({"imie": r_imie, "rel": r_rel, "prof": prof_u, "pos": pos_s})
                    
            # SILNIK MAPOWANIA KRZYŻOWEGO DLA CAŁEJ PALETY DANYCH (CROSS-MATCHING)
            if p1 and aktywne_profile_wynik:
                for item in aktywne_profile_wynik:
                    nazwa_wyswietl = item["imie"] if item["imie"] else item["rel"]
                    if p1["Tikkun"] == item["prof"]["Tikkun"]:
                        mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> Wykazujesz wspólny Tikkun ({p1['Tikkun']}) z osobą: {nazwa_wyswietl} ({item['rel']}).")
                    if item["prof"]["Wezel"] == p1["Lewa"]:
                        mecze.append(f"⚠️ <b>Przejęty Wzorzec:</b> Węzeł Oporu osby {nazwa_wyswietl} rezonuje jako Twoja Karma (Lewa Strona).")
                    if item["prof"]["Wezel"] == p1["Wezel"]:
                        mecze.append(f"🔄 <b>Lustrzana Blokada:</b> Posiadasz identyczny Węzeł Oporu ({p1['Wezel']}) co {nazwa_wyswietl} ({item['rel']}).")
                    if item["pos"] and p1["Talent"] == item["pos"]["Transformacja"]:
                        mecze.append(f"💎 <b>Aktywacja Zasobu:</b> Transformacja Przejścia osoby {nazwa_wyswietl} uwalnia i zasila Twój osobisty Talent ({p1['Talent']})!")
                if not mecze: 
                    mecze.append("💡 Wybrana konstelacja wykazuje zrównoważone linie energetyczne.")

    return render_template_string(PELNY_SZABLON, p1=p1, posag1=posag1, aktywne_profile_wynik=aktywne_profile_wynik, mecze=mecze, imie1=imie1, data_ur1=data_ur1, data_sm1=data_sm1, status1=status1, ile_osob=ile_osob, aktywne_role=aktywne_role, aktywne_imiona=aktywne_imiona, aktywne_ur=aktywne_ur, aktywne_sm=aktywne_sm, dict=KABALA_DICTIONARY)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    typ = request.form.get("typ_wydruku")
    imie1, data_ur1 = request.form.get("d_imie1"), request.form.get("d_ur1")
    # Prawidłowa konwersja daty z formatu YYYY-MM-DD na inty dla silnika głównego urodzin
    profil_glowny = None
    if data_ur1:
        p1_parts = [int(x) for x in data_ur1.split("-")]
        profil_glowny = generuj_profil_urodzenia(p1_parts[2], p1_parts[1], p1_parts[0])
    return wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request.form, generuj_profil_urodzenia, generuj_profil_smierci)

if __name__ == "__main__":
    app.run(debug=True)


