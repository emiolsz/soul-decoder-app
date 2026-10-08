# app.py - Serce platformy Soul Decoder App (Matryca 22 Energii)

KABALA_DICTIONARY = {
    1: {"litera": "Alef", "sefira": "Keter (Korona)", "archetyp": "Mag / Pionier", "znaczenie": "Początek, wola, niezależność, autonomia rodowa.", "cien": "Egoizm, brak uziemienia, samotność.", "posag": "Energia autonomii i nowej linii. Silna wola, ale ryzyko samotności potomków."},
    2: {"litera": "Bet", "sefira": "Chochma (Mądrość)", "archetyp": "Kapłanka / Dom", "znaczenie": "Intuicja, dualizm, przyjmowanie, mądrość.", "cien": "Zależność emocjonalna, skrytość, lęki.", "posag": "Potencjał relacyjności i partnerstwa. Potrzeba domknięcia ugodowego w rodzinie."},
    3: {"litera": "Gimel", "sefira": "Bina (Zrozumienie)", "archetyp": "Cesarzowa", "znaczenie": "Obfitość, kreacja, ekspresja, radość życia.", "cien": "Blokada twórcza, powierzchowność, rozrzutność.", "posag": "Posag ekspresji i dzieł twórczych. Uczy potomków wyrażania prawdy."},
    4: {"litera": "Dalet", "sefira": "Chesed (Miłosierdzie)", "archetyp": "Cesarz / Drzwi", "znaczenie": "Struktura, fundament, autorytet, stabilność.", "cien": "Sztywność, despotyzm, lęk przed stratą kontroli.", "posag": "Silny posag materialny i strukturalny. Wymaga uporządkowania spraw ziemskich."},
    5: {"litera": "He", "sefira": "Gewura (Surowość)", "archetyp": "Papież / Okno", "znaczenie": "Nauczyciel, głęboki wgląd, zasady moralne.", "cien": "Dogmatyzm, fanatyzm, manipulacja wiedzą.", "posag": "Energia wolności i zmian. Nagłe odejście uczące ród odpuszczania kontroli."},
    6: {"litera": "Vav", "sefira": "Tiferet (Piękno)", "archetyp": "Kochankowie", "znaczenie": "Harmonia, relacje, wybory serca, piękno.", "cien": "Perfekcjonizm, zależność od opinii, paraliż decyzyjny.", "posag": "Posag miłości i odpowiedzialności. Nacisk na harmonizowanie konfliktów domowych."},
    7: {"litera": "Zajin", "sefira": "Necach (Zwycięstwo)", "archetyp": "Rydwan", "znaczenie": "Determinacja, ruch do przodu, zwycięstwo.", "cien": "Brak kierunku, narcyzm, wewnętrzny pośpiech.", "posag": "Potencjał dążenia do celu. Przełamywanie stagnacji rodowej przez ruch."},
    8: {"litera": "Chet", "sefira": "Hod (Chwała)", "archetyp": "Sprawiedliwość", "znaczenie": "Równowaga, karma, prawda, obiektywizm.", "cien": "Surowy osąd, urazy, poczucie niesprawiedliwości.", "posag": "Sprawiedliwość i równowaga karmiczna. Rozliczanie dawnych krzywd."},
    9: {"litera": "Tet", "sefira": "Jesod (Fundament)", "archetyp": "Eremita", "znaczenie": "Wewnętrzne światło, mądrość, cierpliwość.", "cien": "Izolacja, aspołeczność, zgorzknienie.", "posag": "Potencjał duchowy, mądrość samotnika. Przestrzeń do głębokich wglądów."},
    10: {"litera": "Jod", "sefira": "Malchut (Królestwo)", "archetyp": "Koło Fortuny", "znaczenie": "Przeznaczenie, cykle życia, boska iskra.", "cien": "Poczucie utknięcia, opór przed zmianą.", "posag": "Potężna moc manifestacji, sprawiedliwości i transformacji skrajności."},
    11: {"litera": "Chaf", "sefira": "Keter/Gewura", "archetyp": "Moc", "znaczenie": "Wewnętrzna siła, pasja, transformacja.", "cien": "Agresja, tłumienie emocji, bezsilność.", "posag": "Posag niezłomności, potężnej energii życiowej i ochrony."},
    12: {"litera": "Lamed", "sefira": "Chesed/Hod", "archetyp": "Wisielec", "znaczenie": "Nowa perspektywa, zatrzymanie, altruizm.", "cien": "Poczucie bycia ofiarą, męczeństwo, paraliż.", "posag": "Uwalnianie rodowych poświęceń, zmiana perspektyw postrzegania świata."},
    13: {"litera": "Mem", "sefira": "Bina/Gewura", "archetyp": "Śmierć", "znaczenie": "Głęboka transformacja, odrodzenie, puszczenie starego.", "cien": "Lęk przed zmianą, toksyczne przywiązanie.", "posag": "Głębokie odrodzenie pola. Dusza transformuje stare struktury w rodową mądrość."},
    14: {"litera": "Nun", "sefira": "Tiferet/Jesod", "archetyp": "Umiarkowanie", "znaczenie": "Alchemia duchowa, równowaga, przepływ.", "cien": "Brak umiaru, niestabilność emocjonalna.", "posag": "Alchemia i harmonia. Wprowadzenie spokoju do skonfliktowanego pola."},
    15: {"litera": "Samech", "sefira": "Tiferet/Hod", "archetyp": "Diabeł", "znaczenie": "Magnetyzm, potęga kreacji materialnej.", "cien": "Uzależnienia, manipulacja, zniewolenie.", "posag": "Potężny magnetyzm, siła materialna. Wyzwanie wolności od zniewoleń."},
    16: {"litera": "Ajin", "sefira": "Necach/Malchut", "archetyp": "Wieża", "znaczenie": "Wyzwolenie, prawda, zburzenie iluzji.", "cien": "Katastrofizm, nagły kryzys psychiczny.", "posag": "Gwałtowne wyzwolenie prawdy rodowej. Burzenie fałszywych fasad."},
    17: {"litera": "Cadi", "sefira": "Chochma/Tiferet", "archetyp": "Gwiazda", "znaczenie": "Nadzieja, przeznaczenie, inspiracja, talent.", "cien": "Naiwność, utrata wiary, czarnowidztwo.", "posag": "Kosmiczne wsparcie, inspiracja. Przodek pozostawia czysty talent do rozwinięcia."},
    18: {"litera": "Kof", "sefira": "Bina/Tiferet", "archetyp": "Księżyc", "znaczenie": "Podświadomość, iluzja, głęboka intuicja, sny.", "cien": "Zagubienie w iluzjach, głębokie lęki rodowe.", "posag": "Dostęp do podświadomości, instynkt. Praca z cieniem przodków."},
    19: {"litera": "Resz", "sefira": "Keter/Tiferet", "archetyp": "Słońce", "znaczenie": "Jasność, sukces, radość, witalność.", "cien": "Egocentryzm, narcyzm, wypalenie.", "posag": "Witalność, jasność, sukces. Przodek zostawia światło i czystą radość."},
    20: {"litera": "Szin", "sefira": "Bina/Malchut", "archetyp": "Sąd Ostateczny", "znaczenie": "Przebudzenie, powołanie, odrodzenie rodziny.", "cien": "Poczucie winy, brak wybaczenia.", "posag": "Przebudzenie i powołanie rodzinne. Rozliczenie przeszłości pokoleniowej."},
    21: {"litera": "Taw", "sefira": "Malchut/Uniwersum", "archetyp": "Świat / Krzyż", "znaczenie": "Spełnienie, integracja, zamknięcie cyklu.", "cien": "Ograniczenia mentalne, lęk przed wyjściem.", "posag": "Pełne domknięcie cyklu ziemskiego. Posag mądrości, wolności uniwersalnej."},
    22: {"litera": "Mente", "sefira": "Ain Sof (Nieskończoność)", "archetyp": "Głupiec / Zero", "znaczenie": "Stan Ain Sof, czysty potencjał, całkowite wyzerowanie długu.", "cien": "Nierozwaga, ucieczka od rzeczywistości.", "posag": "Tabula Rasa. Pełna absolucja rodowa, kosmiczny spokój, brak obciążeń."}
}

def redukuj_do_22(liczba):
    if liczba == 0:
        return 22  # Mapowanie zera/Ain Sof na energetyczny odpowiednik 22 (Głupiec/Mente)
    while liczba > 22:
        liczba = sum(int(cyfra) for cyfra in str(liczba))
    return liczba

def generuj_profil_urodzenia(dzien, miesiac, rok):
    prawa = redukuj_do_22(dzien)
    lewa = redukuj_do_22(miesiac)
    gleboka = redukuj_do_22(sum(int(c) for c in str(rok)))
    talent = redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(dzien, miesiac, rok):
    # Krok 1: Suma wszystkich cyfr pełnej daty
    pelna_suma = sum(int(c) for c in f"{dzien}{miesiac}{rok}")
    transformacja = redukuj_do_22(pelna_suma)
    
    # Krok 2: Trzy podfilary energetyczne
    filar_fizyczny = redukuj_do_22(sum(int(c) for c in str(dzien)))
    filar_emocjonalny = redukuj_do_22(sum(int(c) for c in str(miesiac)))
    filar_duchowy = redukuj_do_22(sum(int(c) for c in str(rok)))
    
    return {"Transformacja": transformacja, "Fizyczny": filar_fizyczny, "Emocjonalny": filar_emocjonalny, "Duchowy": filar_duchowy}

def analizuj_linie_meska(twoja_data, ojciec_ur=None, ojciec_smierc=None):
    ty = generuj_profil_urodzenia(*twoja_data)
    wyniki = {"Twoj_Profil": ty}
    
    if ojciec_ur:
        ojciec_u = generuj_profil_urodzenia(*ojciec_ur)
        wyniki["Ojciec_Urodzenie"] = ojciec_u
        
        # Analiza korelacji (Przykładowa detekcja rezonansu rodowego)
        wyniki["Korelacje_Rodowe"] = []
        if ojciec_u["Wezel"] == ty["Lewa"]:
            wyniki["Korelacje_Rodowe"].append(f"⚠️ Replikacja Wzorca: Węzeł Oporu ojca ({ojciec_u['Wezel']}) stał się Twoją Karmą (Lewa Strona).")
            
    if ojciec_smierc:
        ojciec_s = generuj_profil_smierci(*ojciec_smierc)
        wyniki["Ojciec_Smierc_Posag"] = ojciec_s
        
    return wyniki

if __name__ == "__main__":
    # Test działania programu dla Twoich danych
    twoja_data = (6, 11, 1974)
    analiza = analizuj_linie_meska(twoja_data, ojciec_ur=(14, 10, 1945), ojciec_smierc=(14, 10, 1995))
    
    print("=== TEST SILNIKA SOUL DECODER APP ===")
    print(f"Twoje liczby bazowe: {analiza['Twoj_Profil']}")
    if "Ojciec_Smierc_Posag" in analiza:
        posag = analiza["Ojciec_Smierc_Posag"]
        print(f"Posag energetyczny Ojca (Liczba Transformacji): {posag['Transformacja']} ({KABALA_DICTIONARY[posag['Transformacja']]['litera']})")
        print(f" -> Opis pola: {KABALA_DICTIONARY[posag['Transformacja']]['posag']}")
