# app.py - Serce platformy dekodowania duszy wg 22 energii kabały

# 1. PEŁNA BAZA DANYCH ARCHETYPÓW (22 ENERGIE ALFABETU HEBRAJSKIEGO)
KABALA_DICTIONARY = {
    1: {"litera": "Alef", "archetyp": "Mag / Pionier", "znaczenie": "Początek, czysty potencjał, wola stworzenia, impuls, niezależność.", "cien": "Egoizm, chaos, brak uziemienia, agresja."},
    2: {"litera": "Bet", "archetyp": "Kapłanka / Dom", "znaczenie": "Intuicja, dualizm, wewnętrzne schronienie, mądrość, przyjmowanie.", "cien": "Zależność emocjonalna, skrytość, lęki, bierność."},
    3: {"litera": "Gimel", "archetyp": "Cesarzowa / Wielbłąd", "znaczenie": "Obfitość, kreacja, ekspresja, radość życia, dawanie z serca.", "cien": "Próżność, blokada twórcza, powierzchowność, rozrzutność."},
    4: {"litera": "Dalet", "archetyp": "Cesarz / Drzwi", "znaczenie": "Struktura, fundament, autorytet, stabilność materialna, ochrona.", "cien": "Despotyzm, sztywność myślenia, lęk przed stratą kontroli."},
    5: {"litera": "He", "archetyp": "Papież / Okno", "znaczenie": "Duchowy nauczyciel, tradycja, głęboki wgląd, zasady moralne, przekaz.", "cien": "Dogmatyzm, fanatyzm, manipulacja wiedzą, poczucie wyższości."},
    6: {"litera": "Vav", "archetyp": "Kochankowie / Gwóźdź", "znaczenie": "Harmonia, relacje, wybory serca, piękno, odpowiedzialność społeczna.", "cien": "Perfekcjonizm, zależność od opinii innych, paraliż decyzyjny."},
    7: {"litera": "Zajin", "archetyp": "Rydwan / Miecz", "znaczenie": "Zwycięstwo, determinacja, ruch do przodu, pokonanie przeszkód.", "cien": "Idenie po trupach, narcyzm, brak kierunku, wewnętrzny pośpiech."},
    8: {"litera": "Chet", "archetyp": "Sprawiedliwość / Płot", "znaczenie": "Równowaga, prawo przyczyny i skutku, karma, prawda, obiektywizm.", "cien": "Surowy osąd, brak elastyczności, urazy, poczucie niesprawiedliwości."},
    9: {"litera": "Tet", "archetyp": "Eremita / Wąż / Kosz", "znaczenie": "Wewnętrzne światło, mądrość samotnika, samopoznanie, cierpliwość.", "cien": "Izolacja, aspołeczność, lęk przed światem, zgorzknienie."},
    10: {"litera": "Jod", "archetyp": "Koło Fortuny / Dłoń", "znaczenie": "Przeznaczenie, cykle życia, boska iskra, impuls do zmiany, zaufanie.", "cien": "Poczucie utknięcia, opór przed zmianą, hazardowe podejście do życia."},
    11: {"litera": "Chaf", "archetyp": "Moc / Dłoń zgięta", "znaczenie": "Wewnętrzna siła, opanowanie instynktów, pasja, transformacja energii.", "cien": "Agresja, tłumienie emocji, bezsilność, tyrania."},
    12: {"litera": "Lamed", "archetyp": "Wisielec / Bat", "znaczenie": "Nowa perspektywa, poświęcenie, zatrzymanie, oświecenie, altruizm.", "cien": "Ofiarność na siłę, poczucie bycia ofiarą, paraliż, męczeństwo."},
    13: {"litera": "Mem", "archetyp": "Śmierć / Woda", "znaczenie": "Głęboka transformacja, odrodzenie, puszczenie starego, oczyszczenie.", "cien": "Lęk przed zmianą, toksyczne przywiązanie, stagnacja, autodestrukcja."},
    14: {"litera": "Nun", "archetyp": "Umiarkowanie / Ryba", "znaczenie": "Alchemia duchowa, równowaga, cierpliwość, przepływ, harmonia duszy.", "cien": "Brak umiaru, niestabilność emocjonalna, wewnętrzne rozbicie."},
    15: {"litera": "Samech", "archetyp": "Diabeł / Podpora", "znaczenie": "Cień, materializm, magnetyzm, potęga kreacji materialnej, instynkty.", "cien": "Uzależnienia, manipulacja, zniewolenie, obsesje, toksyczna władza."},
    16: {"litera": "Ajin", "archetyp": "Wieża / Oko", "znaczenie": "Wyzwolenie, zburzenie fałszywych struktur, nagłe przebudzenie, prawda.", "cien": "Katastrofizm, duma przed upadkiem, nagły kryzys psychiczny."},
    17: {"litera": "Cadi", "archetyp": "Gwiazda / Haczyk", "znaczenie": "Nadzieja, przeznaczenie, inspiracja, połączenie z kosmosem, talent.", "cien": "Naiwność, utrata wiary, czarnowidztwo, brak uznania dla siebie."},
    18: {"litera": "Kof", "archetyp": "Księżyc / Tył głowy", "znaczenie": "Podświadomość, iluzja, głęboka intuicja, praca z cieniem, sny.", "cien": "Zagubienie w iluzjach, lęki nocne, oszustwa, depresyjność."},
    19: {"litera": "Resz", "archetyp": "Słońce / Głowa", "znaczenie": "Jasność, sukces, radość, prawda, witalność, realizacja.", "cien": "Egoocentryzm, narcyzm, wypalenie, oślepienie sukcesem."},
    20: {"litera": "Szin", "archetyp": "Sąd Ostateczny / Ząb", "znaczenie": "Przebudzenie, powołanie, odrodzenie rodziny, rozliczenie przeszłości.", "cien": "Poczucie winy, brak wybaczenia, ignorowanie powołania."},
    21: {"litera": "Taw", "archetyp": "Świat / Krzyż", "znaczenie": "Spełnienie, integracja, globalny sukces, zamknięcie cyklu, dom duszy.", "cien": "Ograniczenia geograficzne lub mentalne, lęk przed wyjściem do świata."},
    22: {"litera": "Mente", "archetyp": "Głupiec / Zero", "znaczenie": "Czyste zaufanie, wolność, podróż duszy, brak schematów, spontaniczność.", "cien": "Nierozwaga, nieodpowiedzialność, ucieczka od rzeczywistości."}
}

# 2. LOGIKA MATEMATYCZNA
def redukuj_do_22(liczba):
    if liczba == 0:
        return 22  # W systemie 22 energii zero (Głupiec) często mapowane jest jako 22
    while liczba > 22:
        liczba = sum(int(cyfra) for cyfra in str(liczba))
    return liczba

def generuj_profil(dzien, miesiac, rok):
    prawa = redukuj_do_22(dzien)
    lewa = redukuj_do_22(miesiac)
    
    # Głęboka Osobowość (Suma cyfr roku)
    suma_roku = sum(int(cyfra) for cyfra in str(rok))
    gleboka = redukuj_do_22(suma_roku)
    
    # Talent (Prawa + Lewa + Głęboka)
    talent = redukuj_do_22(prawa + lewa + gleboka)
    
    # Węzeł Oporu (Absolutna wartość z różnicy: Głęboka - Lewa)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    
    # Tikkun (Absolutna wartość z różnicy: Węzeł - Prawa)
    tikkun = redukuj_do_22(abs(wezel - prawa))
    
    return {
        "Prawa Strona": prawa,
        "Lewa Strona": lewa,
        "Głęboka Osobowość": gleboka,
        "Talent": talent,
        "Węzeł Oporu": wezel,
        "Tikkun": tikkun
    }

# 3. INTERFEJS KONSOLOWY (DO SZYBKIEGO TESTOWANIA)
if __name__ == "__main__":
    d, m, r = 6, 11, 1974
    profil = generuj_profil(d, m, r)
    
    print(f"\n=== PROFIL DUSZY DLA {d}.{m}.{r} ===")
    for klucz, val in profil.items():
        info = KABALA_DICTIONARY[val]
        print(f"\n📍 {klucz}: Liczba {val} ({info['litera']})")
        print(f"   Archetyp: {info['archetyp']}")
        print(f"   Jasna Strona: {info['znaczenie']}")
        print(f"   Aspekt Cienia: {info['cien']}")
