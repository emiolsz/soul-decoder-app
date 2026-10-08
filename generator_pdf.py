# generator_pdf.py - Stabilny moduł PDF oparty na natywnej czcionce Helvetica z obsługą polskich znaków
import io
import datetime
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def dodaj_tlo_vintage(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#FBF8EB')) # Szlachetny, pożółkły odcień papieru retro
    canvas.rect(0, 0, doc.pagesize, doc.pagesize, fill=True, stroke=False)
    canvas.restoreState()

def wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request_form, funkcja_profil, funkcja_smierc):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    story, styles = [], getSampleStyleSheet()
    
    # 📜 UŻYCIE NATYWNEJ HELVETICI - 100% BEZPIECZEŃSTWA DLA POLSKICH ZNAKÓW NA VERCELU
    tytul = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=colors.HexColor('#2C3E50'), alignment=1, spaceAfter=25)
    naglowek = ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#1A1A1A'), spaceBefore=14, spaceAfter=8)
    txt = ParagraphStyle('X', fontName='Helvetica', fontSize=9, leading=14, textColor=colors.HexColor('#2B2B2B'))
    b_txt = ParagraphStyle('B', fontName='Helvetica-Bold', fontSize=9, leading=14, textColor=colors.HexColor('#000000'))
    
    story.append(Paragraph("RAPORT ARCHITEKTURY KODU DUSZY", tytul))
    story.append(Paragraph(f"Data rejestru: {datetime.datetime.now().strftime('%d.%m.%Y')} | Autoryzacja: Systemowa", txt))
    story.append(Spacer(1, 15))
    
    osoby = []
    if data_ur1:
        osoby.append((imie1 or "Ja", "Profil Główny", profil_glowny, None))
        
    if typ == "PELNY":
        if request_form.get("d_chk_r") == "True" and request_form.get("d_ur2"):
            dt2, sm2 = datetime.datetime.strptime(request_form.get("d_ur2"), "%Y-%m-%d"), request_form.get("d_sm2")
            osoby.append((request_form.get("d_imie2") or "Rodzeństwo", request_form.get("d_rel2"), funkcja_profil(dt2.day, dt2.month, dt2.year), funkcja_smierc(*[int(x) for x in sm2.split("-")[::-1]]) if sm2 else None))
        for chk, prefix in [("d_chk_pA", "A"), ("d_chk_pB", "B"), ("d_chk_pC", "C")]:
            if request_form.get(f"d_{chk}") == "True" and request_form.get(f"d_ur{prefix}"):
                dtX, smX = datetime.datetime.strptime(request_form.get(f"d_ur{prefix}"), "%Y-%m-%d"), request_form.get(f"d_sm{prefix}")
                osoby.append((request_form.get(f"d_imie{prefix}") or f"Przodek {prefix}", request_form.get(f"d_rel{prefix}"), funkcja_profil(dtX.day, dtX.month, dtX.year), funkcja_smierc(*[int(x) for x in smX.split("-")[::-1]]) if smX else None))

    for nazwa, rel, prof, pos in osoby:
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
            
        if pos:
            t_info = KABALA_DICTIONARY[pos["Transformacja"]]
            story.append(Spacer(1, 5))
            story.append(Paragraph(f"<b>• Data Transgresji (Przejścia):</b> Wibracja {pos['Transformacja']} ({t_info['litera']})", b_txt))
            story.append(Paragraph(f"  {pobierz_analize_premium(pos['Transformacja'], 'Posag')}", txt))
        story.append(Spacer(1, 10))

    # DODATEK PORÓWNAWCZY DLA PEFFLNEGO RAPORTU
    if typ == "PELNY" and len(osoby) > 1:
        story.append(Paragraph(f"================================================================================", txt))
        story.append(Paragraph(f"DODATEK ANALITYCZNY: PRZEKAZY KRZYŻOWE I WZORCE", naglowek))
        story.append(Paragraph(f"================================================================================", txt))
        
        p1_prof = osoby[0][2]
        for nazwa, rel, prof, pos in osoby[1:]:
            if p1_prof["Tikkun"] == prof["Tikkun"]:
                story.append(Paragraph(f"🔍 <b>Linia Przekazu:</b> Profil Główny oraz {nazwa} ({rel}) realizują ten sam kod naprawy Tikkun ({p1_prof['Tikkun']}).", txt))
            if prof["Wezel"] == p1_prof["Lewa"]:
                story.append(Paragraph(f"🔍 <b>Przejęty Wzorzec:</b> Węzeł Oporu osoby {nazwa} zasila Karmę (Lewą Stronę) Profilu Głównego.", txt))
            if pos and p1_prof["Talent"] == pos["Transformacja"]:
                story.append(Paragraph(f"🔍 <b>Aktywacja Pola:</b> Transgresja przodka {nazwa} uwalnia i aktywuje ukryty kod Talentu w Profilu Głównym.", txt))
        story.append(Spacer(1, 10))

    doc.build(story, onFirstPage=dodaj_tlo_vintage, onLaterPages=dodaj_tlo_vintage)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=f"Raport_Kodu_Duszy_{typ}.pdf", mime="application/pdf")

