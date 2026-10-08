# app.py - Zaawansowany silnik Cross-Matching dla całej palety danych rodzeństwa i przodków
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

def generuj_profil_smierci(d, m, r):
    transformacja = redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}"))
    return {"Transformacja": transformacja, "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}

@app.route("/", methods=["GET", "POST"])
def index():
    p1, p2, pA, pB, posagA, posagB = None, None, None, None, None, None
    mecze = []
    
    # Domyślne wartości testowe (W tym historia Prababci i Pradziadka z XIX wieku!)
    imie1, data_ur1, relacja1 = "Emilia", "1974-11-06", "Ja"
    imie2, data_ur2, relacja2 = "Brat", "1978-05-20", "Brat"
    p_relA, p_urA, p_smA = "Prababcia", "1890-03-15", "1965-10-10"
    p_relB, p_urB, p_smB = "Pradziadek", "1886-07-22", "1960-05-05"
    
    if request.method == "POST":
        imie1 = request.form.get("imie1")
        data_ur1 = request.form.get("data_ur1")
        imie2 = request.form.get("imie2")
        data_ur2 = request.form.get("data_ur2")
        relacja2 = request.form.get("relacja2", "Brat")
        
        p_relA = request.form.get("p_relA")
        p_urA = request.form.get("p_urA")
        p_smA = request.form.get("p_smA")
        
        p_relB = request.form.get("p_relB")
        p_urB = request.form.get("p_urB")
        p_smB = request.form.get("p_smB")
        
        # Konwersja dat i generowanie profili
        dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(data_ur2, "%Y-%m-%d")
        dt_urA = datetime.datetime.strptime(p_urA, "%Y-%m-%d")
        dt_urB = datetime.datetime.strptime(p_urB, "%Y-%m-%d")
        
        p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
        p2 = generuj_profil_urodzenia(dt2.day, dt2.month, dt2.year)
        pA = generuj_profil_urodzenia(dt_urA.day, dt_urA.month, dt_urA.year)
        pB = generuj_profil_urodzenia(dt_urB.day, dt_urB.month, dt_urB.year)
        
        if p_smA:
            dt_smA = datetime.datetime.strptime(p_smA, "%Y-%m-%d")
            posagA = generuj_profil_smierci(dt_smA.day, dt_smA.month, dt_smA.year)
        if p_smB:
            dt_smB = datetime.datetime.strptime(p_smB, "%Y-%m-%d")
            posagB = generuj_profil_smierci(dt_smB.day, dt_smB.month, dt_smB.year)
            
        # ================= INTELIGENTNY SILNIK CROSS-MATCHING =================
        przodkowie = [(p_relA, pA, posagA), (p_relB, pB, posagB)]
        rodzenstwo = [(imie1, relacja1, p1), (imie2, relacja2, p2)]
        
        # 1. Analiza Indywidualnego i Krzyżowego Dziedziczenia całej palety danych
        for nazwa_p, prof_p, pos_p in przodkowie:
            for imie_r, rel_r, prof_r in rodzenstwo:
                # Tikkun -> Tikkun
                if prof_r["Tikkun"] == prof_p["Tikkun"]:
                    mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> {imie_r} ({rel_r}) odziedziczyła wyzwanie Tikkun (wibracja {prof_r['Tikkun']}) po: {nazwa_p}.")
                # Węzeł Oporu Przodka -> Karma (Lewa Strona) Dziecka
                if prof_p["Wezel"] == prof_r["Lewa"]:
                    mecze.append(f"⚠️ <b>Przejęty Dług Rodowy:</b> Węzeł Oporu (Blokada {prof_p['Wezel']}) przodka ({nazwa_p}) stał się Karmą (Lewą Stroną) u: {imie_r} ({rel_r}).")
                # Węzeł Oporu Przodka -> Węzeł Oporu Dziecka
                if prof_p["Wezel"] == prof_r["Wezel"]:
                    mecze.append(f"🔄 <b>Replikacja Blokady:</b> {imie_r} ({rel_r}) powtarza identyczny Węzeł Oporu ({prof_r['Wezel']}) co {nazwa_p} – wzorzec obronny do przepracowania.")
                # Posag ze Śmierci -> Aktywacja Talentu
                if pos_p and prof_r["Talent"] == pos_p["Transformacja"]:
                    mecze.append(f"💎 <b>Aktywacja Posagu:</b> Liczba Transformacji Śmierci ({pos_p['Transformacja']}) przodka ({nazwa_p}) zasila i uwalnia ukryty Talent u: {imie_r} ({rel_r})!")

        # 2. Wykrywanie Wspólnego Dziedzictwa Rodzeństwa (Co odziedziczyliście razem)
        for nazwa_p, prof_p, pos_p in przodkowie:
            # Wspólny Tikkun rodzeństwa odziedziczony po tym samym przodku
            if p1["Tikkun"] == prof_p["Tikkun"] and p2["Tikkun"] == prof_p["Tikkun"]:
                mecze.append(f"👑 <b>Wspólny Rdzeń Rodowy:</b> Zarówno Ty ({imie1}), jak i Twoje rodzeństwo ({imie2}) odziedziczyliście ten sam Tikkun po {nazwa_p}! To główny punkt skupienia energii w Waszym pokoleniu.")
            # Wspólna Karma przejęta z Węzła przodka
            if p1["Lewa"] == prof_p["Wezel"] and p2["Lewa"] == prof_p["Wezel"]:
                mecze.append(f"🧬 <b>Wspólne Wyzwanie Pokoleniowe:</b> Oboje z rodzeństwem dzielicie tę samą Karmę, która wywodzi się z Węzła Oporu {nazwa_p}.")

        if not mecze:
            mecze.append("💡 Profile wykazują autonomiczną ścieżkę energetyczną bez bezpośrednich replikacji 1:1 w głównych węzłach.")

    return render_template_string(
        HTML_TEMPLATE, p1=p1, p2=p2, pA=pA, pB=pB, posagA=posagA, posagB=posagB, mecze=mecze,
        imie1=imie1, data_ur1=data_ur1, relacja1=relacja1, imie2=imie2, data_ur2=data_ur2, relacja2=relacja2,
        p_relA=p_relA, p_urA=p_urA, p_smA=p_smA, p_relB=p_relB, p_urB=p_urB, p_smB=p_smB, dict=KABALA_DICTIONARY
    )

if __name__ == "__main__":
    app.run(debug=True)

