# generator_pdf.py - Dynamiczny moduł PDF dla n-uczestników z suwaka z obsługą czcionki Helvetica PL
import io
import datetime
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from dane import KABALA_DICTIONARY
from analiza_opisowa import pobierz_analize_premium

def dodaj_tlo_vintage(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#FBF8EB'))
    canvas.rect(0, 0, doc.pagesize, doc.pagesize, fill=True, stroke=False)
    canvas.restoreState()

def wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request_form, funkcja_profil, funkcja_smierc):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    story, styles = [], getSampleStyleSheet()
    
    tytul = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=colors.HexColor('#2C3E50'), alignment=1, spaceAfter=25)
    naglowek = ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#1A1A1A'), spaceBefore=14, spaceAfter=8)
    txt = ParagraphStyle('X', fontName='Helvetica', fontSize=9, leading=14, textColor=colors.HexColor('#2B2B2B'))
    b_txt = ParagraphStyle('B', fontName='Helvetica-Bold', fontSize=9, leading=14, textColor=colors.HexColor('#000000'))
    
    story.append(Paragraph("RAPORT ARCHITEKTURY KODU DUSZY", tytul))
    story.append(Paragraph(f"Data rejestru: {datetime.datetime.now().strftime('%d.%m.%Y')} | Autoryzacja: Systemowa", txt))
    story.append(Spacer(1, 15))
    
    osoby = []
    if data_ur1:
        osoby.append((imie1 or "Ja", "Profil Główny", profil_glowny, request_form.get("d_sm1")))
        
    if typ == "PELNY":
        ile_osob = int(request_form.get("d_ile_osob", 1))
        for i in range(ile_osob):
            r_rel = request_form.get(f"d_rel_{i}")
            r_imie = request_form.get(f"d_imie_{i}")
            r_ur = request_form.get(f"d_ur_{i}")
            r_sm = request_form.get(f"d_sm_{i}")
            
            if r_ur and len(r_ur.split("-")) == 3:
                pX_u = [int(x) for x in r_ur.split("-")]
                prof_u = funkcja_profil(pX_u[2], pX_u[1], pX_u[0])
                osoby.append((r_imie or r_rel, r_rel, prof_u, r_sm))

    for nazwa, rel, prof, d_smierci in osoby:
        story.append(Paragraph(f"--------------------------------------------------------------------------------", txt))
        story.append(Paragraph(f"REJESTR METRYCZNY: {nazwa.upper()} ({rel.upper()})", naglowek))
        story.append(Paragraph(f"--------------------------------------------------------------------------------", txt))
        
        pozycje_wzor = [
            ("Prawa Strona (Dar)", prof["Prawa"], "Prawa"), ("Lewa Strona (Karma)", prof["Lewa"], "Lewa"),
            ("Talent (Kreacja)", prof["Talent"], "Talent"), ("Głęboka Osobowość", prof["Gleboka"], "Gleboka"),
            ("Węzeł Oporu (Blokada)", prof["Wezel"], "Wezel"), ("Tikkun (Lekcja Duszy)", prof["Tikkun"], "Tikkun")
        ]
        for etykieta, num, klucz_premium in pozycje_wzor:
            info = KABALA_DICTIONARY[num]
            story.append(Paragraph(f"<b>• {etykieta} — Wibracja {num} ({info['litera']})</b>", b_txt))
            story.append(Paragraph(f"  {pobierz_analize_premium(num, klucz_premium)}", txt))
            story.append(Spacer(1, 4))
            
        if d_smierci and len(d_smierci.split("-")) == 3:
            p_s = [int(x) for x in d_smierci.split("-")]
            pos = funkcja_smierc(p_s[2], p_s[1], p_s[0])
            t_info = KABALA_DICTIONARY[pos["Transformacja"]]
            story.append(Spacer(1, 5))
            story.append(Paragraph(f"<b>• Data Transgresji (Przejścia):</b> Wibracja {pos['Transformacja']} ({t_info['litera']})", b_txt))
            story.append(Paragraph(f"  {pobierz_analize_premium(pos['Transformacja'], 'Posag')}", txt))
        story.append(Spacer(1, 10))

    doc.build(story, onFirstPage=dodaj_tlo_vintage, onLaterPages=dodaj_tlo_vintage)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=f"Raport_Kodu_Duszy_{typ}.pdf", mime="application/pdf")




