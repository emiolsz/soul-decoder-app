# analiza_opisowa.py - opisy premium dla 22 wibracji

ANALIZY = {
0: {
        "Prawa": "Aktywuje czysty stan Ain Sof. Twoim kosmicznym darem jest absolutna wolność od rodowych uwarunkowań i nieskończony potencjał kreacji.",
        "Lewa": "Lekcja braku schematów. Wyzwaniem jest porzucenie lęku przed pustką i nauczenie się ufania procesowi życia bez sztywnych planów.",
        "Talent": "Uniwersalny multiplikator. Twój talent pozwala Ci błyskawicznie adaptować się do każdych warunków i zaczynać wszystko od nowa.",
        "Gleboka": "Twoja esencja to Tabula Rasa – czysta, niezapisana karta. Nie ograniczają Cię żadne ziemskie definicje ani blokady.",
        "Wezel": "Opór objawia się jako totalny chaos, brak odpowiedzialności lub ucieczka od rzeczywistości w iluzję.",
        "Tikkun": "Główną misją jest zamanifestowanie pełnej wolności oraz pokazanie rodowi, że można żyć bez niesienia jakiegokolwiek ciężaru.",
        "Posag": "Stan Ain Sof i pełna absolucja rodowa. Przodek wyzerował licznik i pozostawia rodzinie pole wolne od duchowego sabotażu."
    },
    2: {
        "Prawa": "Strumień głębokiej intuicji i empatii. Twoim darem jest unikalny radar na emocje innych oraz dar naturalnego uzdrawiania obecnością.",
        "Lewa": "Lekcja radzenia sobie ze skrajnym emocjonalizmem, skrytością, lękami rodzinnymi oraz uzależnieniem od opinii innych.",
        "Talent": "Wybitny strateg i dyplomata. Twój talent to umiejętność czytania między wierszami i budowania harmonijnych sojuszy.",
        "Gleboka": "W głębi duszy jesteś Kapłanką – strażniczką tajemnic i wewnętrznej mądrości, która ufa cichemu głosowi prowadzenia.",
        "Wezel": "Blokada aktywuje się jako paraliżujący lęk przed odrzuceniem lub całkowite wycofanie się z relacji i ucieczka w samotność.",
        "Tikkun": "Wyzwanie ewolucyjne polega na zbudowaniu silnych, zdrowych granic psychicznych i zaufaniu własnemu wewnętrznemu głosowi.",
        "Posag": "Potencjał relacyjności, partnerstwa i mądrości. Przodek uczy ród domykania spraw ugodowych w pełnym szacunku."
    },
    5: {
        "Prawa": "Strumień duchowego przewodnictwa i mądrości. Twoim darem jest łatwość przyswajania i przekazywania wiedzy o głębokim sensie istnienia.",
        "Lewa": "Lekcja wyjścia z dogmatyzmu, fanatyzmu przekonań oraz tendencji do moralizowania i oceniania innych ludzi.",
        "Talent": "Naturalny nauczyciel i mentor. Twój talent to umiejętność tłumaczenia skomplikowanych prawd w prosty, transformujący sposób.",
        "Gleboka": "Twoja esencja to archetyp Nauczyciela. Dążysz do życia opartego na autentycznych zasadach moralnych i głębokim wglądzie.",
        "Wezel": "Punkt oporu objawia się jako kompleks wyższości intelektualnej lub przeciwnie – paraliżujący lęk, że wciąż wiesz za mało.",
        "Tikkun": "Misja zakłada transformację wiedzy teoretycznej w żywą mądrość serca oraz naukę tolerancji dla odmiennych ścieżek życia.",
        "Posag": "Energia wolności, transformacji i zmian. Często oznacza odejście, które uczy ród elastyczności i odpuszczania kontroli."
    },
    7: {
        "Prawa": "Potężny nurt determinacji i zwycięstwa. Dar polega na niezłomnej sile parcia do przodu i umiejętności pokonywania wszelkich przeszkód.",
        "Lewa": "Lekcja opanowania wewnętrznego pośpiechu, pychy, narcyzmu oraz tendencji do 'idącego po trupach' parcia do celu.",
        "Talent": "Wizjoner i zdobywca. Twój talent manifestuje się poprzez umiejętność wyznaczania jasnych kierunków i mobilizowania innych do działania.",
        "Gleboka": "Esencją Twojej duszy jest archetyp Wojownika Światła. Żyjesz w ciągłym ruchu, dążąc do ewolucji i ciągłego przekraczania barier.",
        "Wezel": "Blokada to lęk przed porażką, który paraliżuje Cię przed podjęciem jakiegokolwiek działania, lub chaos i działanie bez planu.",
        "Tikkun": "Wyzwanie polega na integracji wewnętrznego spokoju i zrozumieniu, że droga do celu jest ważniejsza niż samo trofeum.",
        "Posag": "Potencjał duchowy, intelektualny i przełamywanie stagnacji rodowej. Dusza pozostawia przestrzeń do głębokich wglądów."
    },
        8: {
        "Prawa": "Strumień równowagi, prawdy i obiektywizmu. Twoim kosmicznym darem jest naturalne zrozumienie prawa przyczyny i skutku oraz bezbłędny zmysł sprawiedliwości.",
        "Lewa": "Wyzwanie zakłada przepracowanie surowego osądu wobec siebie i innych, puszczenie zadawnionych urazów oraz uzdrowienie poczucia głębokiej niesprawiedliwości.",
        "Talent": "Mistrzostwo w porządkowaniu chaosu i godzeniu skrajności. Masz wrodzony talent do obiektywnej oceny sytuacji, strategii oraz struktur prawno-formalnych.",
        "Gleboka": "Twoja esencja to archetyp Sprawiedliwości. Dążysz do prawdy, przejrzystości i harmonii, stając się filarem stabilności dla swojego otoczenia.",
        "Wezel": "Opór manifestuje się jako skrajna sztywność moralna, nieustępliwość, krytykanctwo lub paraliż przed podjęciem decyzji ze strachu przed błędem.",
        "Tikkun": "Główną misją naprawczą jest zamiana surowego, chłodnego osądu w mądre wyrozumienie oraz nauka elastyczności w relacjach międzyludzkich.",
        "Posag": "Sprawiedliwość i równowaga karmiczna. Przodek pozostawia w polu rodu czystą matrycę prawdy, domykając i rozliczając dawne krzywdy pokoleniowe."
    },
    9: {
        "Prawa": "Nurt wewnętrznego światła i mądrości samotnika. Twoim kosmicznym darem jest głęboki wgląd, cierpliwość oraz zdolność czerpania wiedzy z własnego wnętrza.",
        "Lewa": "Lekcja wymaga zmierzenia się z lękiem przed opuszczeniem, tendencją do całkowitej izolacji społecznej oraz zgorzknieniem wynikającym z niezrozumienia.",
        "Talent": "Wybitny analityk i doradca duchowy. Twój talent to zdolność głębokiej syntezy wiedzy, prowadzenie innych przez kryzysy oraz naturalne wyciszanie emocji.",
        "Gleboka": "W głębi duszy jesteś Eremitą – poszukiwaczem prawdy absolutnej, który potrzebuje przestrzeni i ciszy, aby naładować swoje wewnętrzne baterie.",
        "Wezel": "Blokada objawia się jako aspołeczność, ucieczka od realnego świata w intelektualizm oraz lęk przed pokazaniem światu swojej autentycznej wrażliwości.",
        "Tikkun": "Misja zakłada wyjście ze swojej jaskini samotności, aby dzielić się wypracowanym wewnętrznym światłem i mądrością z potrzebującymi ludźmi.",
        "Posag": "Potencjał duchowy i mądrość syntezy. Przodek pozostawia po sobie przestrzeń do głębokich wglądów, uwalniając ród od powierzchownych dążeń materialnych."
    },
    10: {
        "Prawa": "Strumień przeznaczenia i boskiej iskry. Twoim kosmicznym darem jest naturalne zaufanie do cykli życia oraz lekkość w poruszaniu się po spiralach zmian.",
        "Lewa": "Wyzwanie zakłada przepracowanie syndromu 'ofiary losu', lęku przed nieznanym oraz poczucia permanentnego utknięcia w niesprzyjających warunkach.",
        "Talent": "Generowanie impulsów do transformacji. Masz wrodzony talent do chwytania właściwych momentów, intuicyjnego wyczuwania szans oraz potężną siłę manifestacji.",
        "Gleboka": "Twoja esencja to archetyp Koła Fortuny – dynamicznego punktu zwrotnego, który uczy otoczenie, że każda zmiana niesie w sobie ukryte błogosławieństwo.",
        "Wezel": "Opór aktywuje się jako chorobliwa walka z naturalnym biegiem wydarzeń, hazardowe podejście do życia lub całkowity paraliż przed podjęciem ryzyka.",
        "Tikkun": "Głównym wyzwaniem ewolucyjnym jest odpuszczenie neurotycznej kontroli i odbudowanie głębokiego, niezłomnego zaufania do prowadzenia wyższej mądrości.",
        "Posag": "Potężna moc manifestacji i transformacji skrajności. Przodek uwalnia pole rodu z dawnych stagnacji, zostawiając impuls do dynamicznej ewolucji."
    },
    11: {
        "Prawa": "Potężny nurt wewnętrznej siły, pasji i witalności. Twój kosmiczny dar to niezłomność, magnetyzm osobisty oraz zdolność regeneracji w każdych warunkach.",
        "Lewa": "Lekcja wymaga opanowania destrukcyjnej agresji (zarówno zewnętrznej, jak i autoagresji), tłumienia emocji oraz radzenia sobie z lękiem przed bezsilnością.",
        "Talent": "Transformacja surowej energii życiowej. Masz wrodzony talent do uzdrawiania poprzez dotyk, motywowania innych oraz zarządzania wielkimi zasobami energetycznymi.",
        "Gleboka": "W głębi duszy jesteś archetypem Mocy – osobą o czystym sercu, która potrafi okiełznać najdziksze instynkty za pomocą łagodności i miłości.",
        "Wezel": "Blokada manifestuje się jako tyrania wobec otoczenia, wybuchy tłumionego gniewu lub permanentne wycieńczenie energetyczne spowodowane walką z samym sobą.",
        "Tikkun": "Misja polega na integracji własnej siły z wrażliwością, rezygnacji z rozwiązań siłowych na rzecz mądrego współczucia i ochrony słabszych.",
        "Posag": "Posag niezłomności i potężnej ochrony energetycznej. Przodek pozostawia potomkom zasób ogromnej odporności psychofizycznej i siły życiowej."
    },
    12: {
        "Prawa": "Strumień nowej perspektywy i bezwarunkowego altruizmu. Twoim kosmicznym darem jest unikalne postrzeganie świata oraz zdolność dostrzegania ukrytych znaczeń.",
        "Lewa": "Wyzwanie zakłada przepracowanie syndromu męczennika, tendencji do stawiania się w roli ofiary oraz paraliżu decyzyjnego w krytycznych momentach.",
        "Talent": "Duchowe oświecenie i zmiana paradygmatów. Twój talent pozwala Ci znajdować genialne rozwiązania poprzez zatrzymanie się i spojrzenie na problem pod zupełnie innym kątem.",
        "Gleboka": "Twoja esencja to archetyp Wisielca – mędrca, który wie, kiedy należy odpuścić działanie w materii na rzecz głębokiej transformacji wewnętrznej.",
        "Wezel": "Opór aktywuje się jako wymuszone poświęcanie się dla innych, ucieczka w cierpiętnictwo lub całkowity paraliż uniemożliwiający ruch do przodu.",
        "Tikkun": "Główną misją naprawczą jest uzdrowienie rodowych programów ofiarności, nauka zdrowego egoizmu oraz transformacja stagnacji w nową mądrość.",
        "Posag": "Uwalnianie rodowych poświęceń i zmiana optyki. Przodek pozostawia dar głębokiej empatii, ucząc ród wolności od dawnych schematów udręki."
    },
    13: {
        "Prawa": "Nurt głębokiej, radykalnej transformacji i odrodzenia. Twój kosmiczny dar to umiejętność puszczania tego, co stare, i bezlitosne oczyszczanie przestrzeni pod nowe.",
        "Lewa": "Lekcja wymaga zmierzenia się z paraliżującym lękiem przed zmianą, toksycznym przywiązywaniem się do form oraz lękiem przed symboliczną stratą.",
        "Talent": "Alchemia i regeneracja pola. Masz wrodzony talent do przeprowadzania struktur, systemów lub ludzi przez procesy głębokiego kryzysu i odrodzenia.",
        "Gleboka": "W głębi duszy reprezentujesz archetyp Transformacji. Jesteś katalizatorem zmian, który nie pozwala na stagnację i fikcję w swoim otoczeniu.",
        "Wezel": "Blokada objawia się jako chorobliwy opór przed ewolucją, trzymanie się destrukcyjnych relacji lub popadanie w stany głębokiej apatii i marazmu.",
        "Tikkun": "Misja zakłada pełne zrozumienie, że koniec jest jedynie początkiem nowego cyklu, oraz naukę zaufania do procesów naturalnego puszczania i odradzania.",
        "Posag": "Głębokie oczyszczenie pola rodowego. Przodek zdołał przetransformować dawne, ciężkie uwarunkowania materialne w czystą mądrość i wolność dla potomnych."
    },
    14: {
        "Prawa": "Strumień duchowej alchemii, harmonii i umiaru. Twoim kosmicznym darem jest wrodzona zdolność do łagodzenia napięć, cierpliwość oraz idealne wyczucie proporcji.",
        "Lewa": "Wyzwanie dotyczy skrajnej niestabilności emocjonalnej, braku umiaru w jakiejkolwiek dziedzinie życia oraz wewnętrznego rozbicia na skrajności.",
        "Talent": "Harmonizowanie skonfliktowanych przestrzeni. Twój talent manifestuje się poprzez płynne łączenie różnych energii, talent uzdrowicielski oraz sztukę dyplomacji.",
        "Gleboka": "Twoja najgłębsza esencja to archetyp Umiarkowania – anioła stróża harmonii, który wnosi spokój, równowagę i wyważenie wszędzie, gdzie się pojawi.",
        "Wezel": "Opór aktywuje się jako emocjonalny chaos, popadanie w skrajności (od euforii do głębokiego smutku) lub wewnętrzne lenistwo maskowane spokojem.",
        "Tikkun": "Głównym wyzwaniem ewolucyjnym jest odnalezienie wewnętrznego punktu ciszy (alchemicznego środka) oraz integracja rozproszonych aspektów osobowości.",
        "Posag": "Alchemia, wyciszenie i harmonia duszy. Przodek pozostawia w posagu pole wolne od skrajnych dramatów, przynosząc kosmiczny spokój linii rodowej."
    },
    15: {
        "Prawa": "Potężny nurt magnetyzmu osobistego, charyzmy i kreacji materialnej. Twój dar to ogromna siła przyciągania, witalność oraz zdolność zarządzania materią.",
        "Lewa": "Lekcja wymaga przepracowania mechanizmów manipulacji, uzależnień (własnych lub cudzych), obsesji oraz lęku przed zniewoleniem materialnym.",
        "Talent": "Mistrzostwo w manifestacji ziemskiej i praca z cieniem. Masz wrodzony talent do dostrzegania ukrytych motywów, psychologii oraz budowania potęgi materialnej.",
        "Gleboka": "W głębi duszy jesteś Strażnikiem Charyzmy. Posiadasz ogromny rezerwuar energii, który właściwie ukierunkowany potrafi kreować wielkie rzeczy na ziemi.",
        "Wezel": "Blokada manifestuje się jako uwikłanie w toksyczne układy władzy, ucieczka w destrukcyjne nałogi lub chorobliwa żądza kontroli nad otoczeniem.",
        "Tikkun": "Misja zakłada pełne wyzwolenie własnej woli spod uwarunkowań materii i lęków, transformację cienia i użycie charyzmy do wyzwalania innych.",
        "Posag": "Potężna siła kreacji materialnej i magnetyzmu. Przodek pozostawia w spadku zdolność budowania dobrobytu, z wyzwaniem zachowania czystości intencji."
    },
        16: {
        "Prawa": "Strumień gwałtownego wyzwolenia, prawdy i burzenia fałszywych struktur. Twoim darem jest odwaga do stawania w prawdzie i oczyszczania przestrzeni z iluzji.",
        "Lewa": "Wyzwanie zakłada przepracowanie katastrofizmu, lęku przed nagłym kryzysem życiowym oraz dumy, która blokuje przed proszeniem o pomoc.",
        "Talent": "Architekt przełomów. Twój talent to zdolność do błyskawicznego podnoszenia się z najtrudniejszych kryzysów i budowania swojego życia na nowo, na skale.",
        "Gleboka": "Twoja esencja to archetyp Wieży – punktu przebudzenia, który poprzez dynamiczne wydarzenia kruszy to, co było sztuczne, uwalniając czyste światło duszy.",
        "Wezel": "Punkt oporu objawia się jako chorobliwe trzymanie się fasadowego wizerunku, lęk przed rozpadem starych schematów lub skłonność do autodestrukcji.",
        "Tikkun": "Główną misją naprawczą jest nauka elastyczności, pokory wobec zmian oraz zrozumienie, że każde zburzenie starej formy to akt kosmicznego wyzwolenia.",
        "Posag": "Gwałtowne oczyszczenie i wyzwolenie prawdy rodowej. Przodek zburzył fałszywe fasady pokoleniowe, zostawiając potomkom fundament absolutnej autentyczności."
    },
    17: {
        "Prawa": "Nurt niezłomnej nadziei, kosmicznego wsparcia i czystego talentu. Twój dar to artystyczna lub duchowa inspiracja oraz głęboka wiara w prowadzenie.",
        "Lewa": "Lekcja wymaga zmierzenia się z utratą wiary w sens życia, skłonnością do czarnowidztwa, naiwnością oraz permanentnym brakiem uznania dla samego siebie.",
        "Talent": "Inspiracja i magnetyzm twórczy. Masz wrodzony talent artystyczny, wizjonerski lub uzdrowicielski, który potrafi wnosić światło i nadzieję w życie innych.",
        "Gleboka": "W głębi duszy jesteś Gwiazdą – istotą powołaną do lśnienia swoim autentycznym światłem, która przypomina otoczeniu o istnieniu wyższego porządku.",
        "Wezel": "Blokada manifestuje się jako paraliżująca niewiara we własne możliwości, lęk przed wyjściem z cienia lub ucieczka w świat nierealnych mrzonek i fantazji.",
        "Tikkun": "Wyzwanie polega na pełnym uziemieniu swoich talentów, odważnym pokazaniu ich światu oraz odbudowaniu głębokiego poczucia własnej unikalnej wartości.",
        "Posag": "Kosmiczne wsparcie i czysty talent rodowy. Przodek pozostawia w polu rodu wibrację nieskończonej nadziei, inspiracji i artystycznego natchnienia."
    },
    18: {
        "Prawa": "Strumień głębokiej podświadomości, intuicji i mistycznej wrażliwości. Twój dar to zdolność czytania snów, silna intuicja oraz praca z materią niewidzialną.",
        "Lewa": "Wyzwanie dotyczy zagubienia w iluzjach, głębokich, niewytłumaczalnych lęków rodowych, stanów depresyjnych oraz ucieczki przed realnym życiem.",
        "Talent": "Praca z cieniem i głęboka psychologia. Twój talent to umiejętność nawigowania po najciemniejszych zakamarkach ludzkiej psychiki i transformowanie lęku w mądrość.",
        "Gleboka": "Twoja esencja to archetyp Księżyca – głębokiego oceanu podświadomości, który przyciąga magię, intuicję i głębokie, tajemne zrozumienie procesów życia.",
        "Wezel": "Opór aktywuje się jako paraliż przed własną intuicją, podatność na manipulacje psychiczne lub zatracenie granicy między fikcją a rzeczywistością.",
        "Tikkun": "Główną misją naprawczą jest rozproszenie rodowych lęków za pomocą światła świadomości, uziemienie intuicji i wyjście z iluzji do czystej prawdy.",
        "Posag": "Dostęp do głębokiej mądrości podświadomości. Przodek przetransformował dawne lęki rodowe, zostawiając potomkom potężny radar intuicyjny i instynkt."
    },
    19: {
        "Prawa": "Potężny, czysty nurt jasności, sukcesu, witalności i radości. Twój kosmiczny dar to wewnętrzne słońce, optymizm oraz zdolność ogrzewania i wspierania innych.",
        "Lewa": "Lekcja wymaga przepracowania skrajnego egocentryzmu, narcyzmu, lęku przed oceną oraz tendencji do emocjonalnego wypalania siebie lub otoczenia.",
        "Talent": "Lider i kreator obfitości. Masz wrodzony talent do osiągania sukcesów z lekkością, jasnego klarowania sytuacji oraz wnoszenia energii życia wszędzie, gdzie się pojawi.",
        "Gleboka": "W głębi duszy reprezentujesz archetyp Słońca. Twoją esencją jest czysta radość, realizacja, prawda i chęć tworzenia zintegrowanych, szczęśliwych przestrzeni.",
        "Wezel": "Blokada manifestuje się jako paniczny lęk przed porażką i krytyką, paraliż decyzyjny lub oślepienie własnym sukcesem kosztem relacji z bliskimi.",
        "Tikkun": "Misja zakłada naukę świecenia własnym światłem bez potrzeby dominacji, dzielenie się sukcesem w pełnej pokorze oraz odnalezienie źródła witalności w sercu.",
        "Posag": "Światło, witalność i uniwersalny sukces. Przodek pozostawia w posagu czystą energię radości, powodzenia materialnego oraz jasności dla całego rodu."
    },
    20: {
        "Prawa": "Strumień głębokiego przebudzenia, powołania i odrodzenia rodowego. Twoim kosmicznym darem jest umiejętność rozliczania i transformowania przeszłości.",
        "Lewa": "Wyzwanie dotyczy niesienia rodowych programów poczucia winy, braku wybaczenia wobec przodków oraz ignorowania głosu własnego autentycznego powołania.",
        "Talent": "Uzdrowiciel linii rodowej i mediator pokoleń. Twój talent to zdolność do wyciągania mądrych wniosków z dawnych błędów oraz inicjowanie głębokich transformacji rodzinnych.",
        "Gleboka": "Twoja najgłębsza esencja to archetyp Sądu Ostatecznego – momentu transformacji, w którym dusza budzi się do swojej prawdziwej tożsamości i misji ziemskiej.",
        "Wezel": "Opór aktywuje się jako permanentne tkwienie w przeszłości, rozpamiętywanie dawnych krzywd, lęk przed zmianą statusu lub odrzuceniem przez system rodzinny.",
        "Tikkun": "Głównym wyzwaniem ewolucyjnym jest dokonanie pełnego, głębokiego wybaczenia w strukturach rodu, odcięcie toksycznych pętli przeszłości i pójście za głosem powołania.",
        "Posag": "Przebudzenie, absolucja i odrodzenie systemowe. Przodek dokonał ostatecznego rozliczenia przeszłości, zostawiając potomkom pole wolne od rodowych długów."
    },
    21: {
        "Prawa": "Strumień pełnego spełnienia, globalnego sukcesu i uniwersalnej integracji. Twój kosmiczny dar to brak barier mentalnych i łatwość odnajdywania się w świecie.",
        "Lewa": "Lekcja wymaga przepracowania lęku przed wyjściem do świata, przełamania ograniczeń geograficznych lub narodowościowych oraz lęku przed ostatecznym sukcesem.",
        "Talent": "Kosmopolita i integrator systemów. Masz wrodzony talent do łączenia ludzi o skrajnie odmiennych poglądach, podróży, handlu międzynarodowego i domykania cykli.",
        "Gleboka": "Esencją Twojej duszy jest archetyp Świata – stan pełnej harmonii, w którym czujesz, że całe uniwersum jest Twoim domem, a Ty jesteś we właściwym miejscu i czasie.",
        "Wezel": "Blokada manifestuje się jako nakładanie na siebie sztucznych, ciasnych ograniczeń, lęk przed ekspansją lub poczucie wyobcowania i braku swojego miejsca na ziemi.",
        "Tikkun": "Misja zakłada ostateczne zamknięcie i podsumowanie wielkich cykli ewolucyjnych, wyjście poza wszelkie ramy i ograniczenia oraz celebrację pełnego spełnienia duszy.",
        "Posag": "Pełne domknięcie cyklu ziemskiego. Przodek pozostawia potomkom uniwersalny posag mądrości, globalnego sukcesu oraz absolutnej wolności mentalno-geograficznej."
    },
    22: {
        "Prawa": "Strumień czystego zaufania, spontaniczności i absolutnej wolności od schematów. Twój dar to odwaga do zaczynania od zera i pełna niezależność ducha.",
        "Lewa": "Wyzwanie dotyczy skrajnej nierozwagi, braku odpowiedniości za własne czyny, ucieczki od realiów życia oraz lęku przed jakimkolwiek zobowiązaniem.",
        "Talent": "Niezależny podróżnik duszy. Twój talent manifestuje się poprzez genialną, nieskrępowaną niczym kreatywność, spontaniczne znajdowanie wyjść i czyste zaufanie prowadzeniu.",
        "Gleboka": "Twoja esencja to archetyp Głupca (Mente / Zero) – istoty, która idzie przez życie z lekkim sercem, wiedząc, że nie posiada nic i jednocześnie ma dostęp do wszystkiego.",
        "Wezel": "Opór aktywuje się jako infantylizm, wieczny bunt bez powodu, unikanie dorosłości lub destrukcyjne igranie z losem dla chwilowego poczucia wolności.",
        "Tikkun": "Główną misją naprawczą jest nauka dojrzałej wolności – takiej, która nie rani innych, oraz zamanifestowanie czystego zaufania bez uciekania od ziemskich realiów.",
        "Posag": "Tabula Rasa i pełna absolucja rodowa. Przodek wyzerował wszelkie liczniki dłużne, pozostawiając rodzinie stan neutralności, kosmicznego spokoju i czystego potencjału."
    }
}



def pobierz_analize_premium(numer, klucz):
    """Zwraca opis premium; dla niepełnych wpisów korzysta z bazy podstawowej."""
    wpis = ANALIZY.get(numer, {})
    if klucz in wpis:
        return wpis[klucz]
    from dane import KABALA_DICTIONARY
    bazowy = KABALA_DICTIONARY.get(numer, {})
    mapa = {
        "Prawa": "znaczenie",
        "Lewa": "cien",
        "Talent": "znaczenie",
        "Gleboka": "archetyp",
        "Wezel": "cien",
        "Tikkun": "znaczenie",
        "Posag": "posag",
    }
    return bazowy.get(mapa.get(klucz, "znaczenie"), "Brak opisu.")
