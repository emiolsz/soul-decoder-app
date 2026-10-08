# generator_pdf.py - stabilny generator PDF dla aktualnego formularza Soul Decoder
import io
import datetime
from xml.sax.saxutils import escape

from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from dane import KABALA_DICTIONARY
from analiza_opisowa import pobierz_analize_premium


def dodaj_tlo_vintage(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#FBF8EB"))
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=True, stroke=False)
    canvas.restoreState()


def _date_parts(value):
    """Zwraca (dzien, miesiac, rok) albo None dla pustej/błędnej daty."""
    if not value:
        return None
    try:
        dt = datetime.datetime.strptime(value, "%Y-%m-%d")
        return dt.day, dt.month, dt.year
    except (TypeError, ValueError):
        return None


def _safe(text):
    return escape(str(text or ""))


def _profil_z_daty(value, funkcja_profil):
    parts = _date_parts(value)
    if not parts:
        return None
    d, m, r = parts
    return funkcja_profil(d, m, r)


def _smierc_z_daty(value, funkcja_smierc):
    parts = _date_parts(value)
    if not parts:
        return None
    d, m, r = parts
    return funkcja_smierc(d, m, r)


def _dodaj_osobe(story, nazwa, relacja, prof, pos, naglowek, txt, b_txt):
    if not prof:
        return

    nazwa = nazwa or "Osoba"
    relacja = relacja or ""

    story.append(Paragraph("—" * 70, txt))
    naglowek_text = f"REJESTR METRYCZNY: {_safe(nazwa).upper()}"
    if relacja:
        naglowek_text += f" ({_safe(relacja).upper()})"
    story.append(Paragraph(naglowek_text, naglowek))
    story.append(Paragraph("—" * 70, txt))

    pozycje_wzor = [
        ("Prawa Strona (Dar)", "Prawa", "Prawa"),
        ("Lewa Strona (Karma)", "Lewa", "Lewa"),
        ("Talent (Kreacja)", "Talent", "Talent"),
        ("Głęboka Osobowość", "Gleboka", "Gleboka"),
        ("Węzeł Oporu (Blokada)", "Wezel", "Wezel"),
        ("Tikkun (Lekcja Duszy)", "Tikkun", "Tikkun"),
    ]

    for etykieta, pole, klucz_premium in pozycje_wzor:
        num = prof.get(pole)
        info = KABALA_DICTIONARY.get(num, {})
        litera = info.get("litera", "")
        opis = pobierz_analize_premium(num, klucz_premium) if num is not None else "Brak danych."
        story.append(Paragraph(
            f"<b>• {_safe(etykieta)} — Wibracja {num} ({_safe(litera)})</b>",
            b_txt,
        ))
        story.append(Paragraph(_safe(opis), txt))
        story.append(Spacer(1, 4))

    if pos:
        num = pos.get("Transformacja")
        info = KABALA_DICTIONARY.get(num, {})
        litera = info.get("litera", "")
        opis = pobierz_analize_premium(num, "Posag") if num is not None else "Brak danych."
        story.append(Spacer(1, 5))
        story.append(Paragraph(
            f"<b>• Data Transformacji (Przejścia):</b> Wibracja {num} ({_safe(litera)})",
            b_txt,
        ))
        story.append(Paragraph(_safe(opis), txt))

    story.append(Spacer(1, 10))


def wybuduj_archiwalny_pdf(
    typ,
    imie1,
    data_ur1,
    profil_glowny,
    request_form,
    funkcja_profil,
    funkcja_smierc,
):
    """Buduje raport na podstawie aktualnych pól d_* wysyłanych przez index.html."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
        title="Raport Architektury Kodu Duszy",
        author="Soul Decoder",
    )

    story = []
    tytul = ParagraphStyle(
        "T", fontName="Helvetica-Bold", fontSize=16, leading=20,
        textColor=colors.HexColor("#2C3E50"), alignment=1, spaceAfter=25,
    )
    naglowek = ParagraphStyle(
        "H", fontName="Helvetica-Bold", fontSize=12, leading=15,
        textColor=colors.HexColor("#1A1A1A"), spaceBefore=14, spaceAfter=8,
    )
    txt = ParagraphStyle(
        "X", fontName="Helvetica", fontSize=9, leading=14,
        textColor=colors.HexColor("#2B2B2B"),
    )
    b_txt = ParagraphStyle(
        "B", fontName="Helvetica-Bold", fontSize=9, leading=14,
        textColor=colors.HexColor("#000000"),
    )

    story.append(Paragraph("RAPORT ARCHITEKTURY KODU DUSZY", tytul))
    story.append(Paragraph(
        f"Data rejestru: {datetime.datetime.now().strftime('%d.%m.%Y')} | Autoryzacja: Systemowa",
        txt,
    ))
    story.append(Spacer(1, 15))

    osoby = []

    # Profil główny
    if profil_glowny:
        pos_glowny = _smierc_z_daty(request_form.get("d_sm1"), funkcja_smierc)
        osoby.append((imie1 or "Ja", "Profil Główny", profil_glowny, pos_glowny))

    # W aktualnym index.html osoby dodatkowe są wysyłane jako d_imie_0, d_ur_0 itd.
    if typ == "PELNY":
        try:
            ile = int(request_form.get("d_ile_osob", 0) or 0)
        except (TypeError, ValueError):
            ile = 0

        for i in range(ile):
            ur = request_form.get(f"d_ur_{i}", "")
            prof = _profil_z_daty(ur, funkcja_profil)
            if not prof:
                continue
            imie = request_form.get(f"d_imie_{i}", "") or "Osoba"
            rel = request_form.get(f"d_rel_{i}", "") or ""
            sm = request_form.get(f"d_sm_{i}", "")
            pos = _smierc_z_daty(sm, funkcja_smierc)
            osoby.append((imie, rel, prof, pos))

    for osoba in osoby:
        _dodaj_osobe(story, *osoba, naglowek, txt, b_txt)

    # Porównanie profilu głównego z osobami dodatkowymi.
    if typ == "PELNY" and len(osoby) > 1:
        story.append(Paragraph("=" * 70, txt))
        story.append(Paragraph("DODATEK ANALITYCZNY: PRZEKAZY KRZYŻOWE I WZORCE", naglowek))
        story.append(Paragraph("=" * 70, txt))

        p1_prof = osoby[0][2]
        for nazwa, rel, prof, pos in osoby[1:]:
            nazwa_s = _safe(nazwa)
            rel_s = _safe(rel)
            if p1_prof.get("Tikkun") == prof.get("Tikkun"):
                story.append(Paragraph(
                    f"<b>Linia Przekazu:</b> Profil Główny oraz {nazwa_s} ({rel_s}) "
                    f"realizują ten sam kod naprawy Tikkun ({p1_prof.get('Tikkun')}).",
                    txt,
                ))
            if prof.get("Wezel") == p1_prof.get("Lewa"):
                story.append(Paragraph(
                    f"<b>Przejęty Wzorzec:</b> Węzeł Oporu osoby {nazwa_s} "
                    f"rezonuje z Karmą (Lewą Stroną) Profilu Głównego.",
                    txt,
                ))
            if pos and p1_prof.get("Talent") == pos.get("Transformacja"):
                story.append(Paragraph(
                    f"<b>Aktywacja Pola:</b> Transformacja osoby {nazwa_s} "
                    f"rezonuje z kodem Talentu Profilu Głównego.",
                    txt,
                ))

    doc.build(story, onFirstPage=dodaj_tlo_vintage, onLaterPages=dodaj_tlo_vintage)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"Raport_Kodu_Duszy_{typ}.pdf",
        mimetype="application/pdf",
    )


