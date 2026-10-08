# app.py - Główny silnik uruchomieniowy platformy Flask
import io
import datetime
from flask import Flask, request, render_template_string, send_file

# Importy z naszych mniejszych porcji plików
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
    talent = redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(d, m, r):
    transformacja = redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}"))
    return {"Transformacja": transformacja, "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}

@app.route("/", methods=["GET", "POST"])
def index():
    profil, posag = None, None
    imie, data_ur, data_sm = "Emilia Olszewska", "1974-11-06", "1995-10-14"
    if request.method == "POST":
        imie = request.form.get("imie")
        data_ur = request.form.get("data_ur")
        data_sm = request.form.get("data_sm")
        dt_ur = datetime.datetime.strptime(data_ur, "%Y-%m-%d")
        profil = generuj_profil_urodzenia(dt_ur.day, dt_ur.month, dt_ur.year)
        if data_sm:
            dt_sm = datetime.datetime.strptime(data_sm, "%Y-%m-%d")
            posag = generuj_profil_smierci(dt_sm.day, dt_sm.month, dt_sm.year)
    return render_template_string(HTML_TEMPLATE, profil=profil, posag=posag, imie=imie, data_ur=data_ur, data_sm=data_sm, dict=KABALA_DICTIONARY)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    imie = request.form.get("imie")
    dt_ur = datetime.datetime.strptime(request.form.get("data_ur"), "%Y-%m-%d")
    p_ur = generuj_profil_urodzenia(dt_ur.day, dt_ur.month, dt_ur.year)
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story, styles = [], getSampleStyleSheet()
    
    tytul = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#4A154B'), alignment=1, spaceAfter=20)
    txt = ParagraphStyle('X', fontName='Helvetica', fontSize=10, leading=14)
    
    story.append(Paragraph("PROFIL KABALISTYCZNY DRZEWA DUSZY", tytul))
    story.append(Paragraph(f"<b>Analiza dla:</b> {imie} (Ur. {dt_ur.strftime('%d.%m.%Y')})", txt))
    story.append(Spacer(1, 15))
    
    t_dane = [[Paragraph("Pozycja", txt), Paragraph("Wibracja", txt), Paragraph("Opis Potencjalu", txt)]]
    for k, v in [("Prawa Strona (Dar)", p_ur["Prawa"]), ("Lewa Strona (Karma)", p_ur["Lewa"]), ("Talent (Kreacja)", p_ur["Talent"]), ("Gleboka Osobowosc", p_ur["Gleboka"])]:
        t_dane.append([Paragraph(k, txt), Paragraph(str(v), txt), Paragraph(KABALA_DICTIONARY[v]["znaczenie"] if "Karma" not in k else KABALA_DICTIONARY[v]["cien"], txt)])
        
    t = Table(t_dane, colWidths=[120, 60, 320])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F2E6F2')), ('VALIGN', (0,0), (-1,-1), 'TOP'), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0'))]))
    story.append(t)
    
    doc.build(story)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="Raport.pdf", mime="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)
