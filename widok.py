# widok.py - Kod wyglądu HTML/CSS dla aplikacji Flask
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Soul Decoder App</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; margin: 0; padding: 30px; color: #333; }
        .container { max-width: 800px; background: white; margin: 0 auto; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { color: #4A154B; text-align: center; margin-bottom: 5px; }
        .sub { text-align: center; color: #7f8c8d; margin-bottom: 25px; }
        fieldset { border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; }
        legend { font-weight: bold; color: #2c3e50; padding: 0 10px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; font-weight: 600; }
        input { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
        .btn { display: inline-block; width: 100%; padding: 12px; background: #4A154B; color: white; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-align: center; text-decoration: none; }
        .btn:hover { background: #330f34; }
        .btn-pdf { background: #104F55; margin-top: 15px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #4A154B; }
        .card.karma { border-left-color: #C0392B; }
        .card.posag { border-left-color: #104F55; background: #f0f4f8; grid-column: span 2; }
        .num { font-size: 22px; font-weight: bold; color: #4A154B; }
        .card.karma .num { color: #C0392B; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Soul Decoder App</h1>
        <p class="sub">Tradycja Kabalistyczna i Analiza Wielopokoleniowa</p>
        <form method="POST">
            <fieldset>
                <legend>Dane Użytkownika</legend>
                <div class="form-group"><label>Imię i Nazwisko:</label><input type="text" name="imie" value="{{ imie }}" required></div>
                <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur" value="{{ data_ur }}" required></div>
            </fieldset>
            <fieldset>
                <legend>Opcjonalnie: Linia Męska</legend>
                <div class="form-group"><label>Data Śmierci Ojca/Przodka:</label><input type="date" name="data_sm" value="{{ data_sm }}"></div>
            </fieldset>
            <button type="submit" class="btn">Dekoduj Matrycę Duszy</button>
        </form>
        {% if profil %}
        <hr style="margin: 30px 0; border: 0; border-top: 1px solid #eee;">
        <h2>Wyniki Analizy dla: {{ imie }}</h2>
        <div class="grid">
            <div class="card"><span class="num">{{ profil.Prawa }}</span> — <strong>Dar (Prawa Strona)</strong> ({{ dict[profil.Prawa].litera }})<br>{{ dict[profil.Prawa].znaczenie }}</div>
            <div class="card karma"><span class="num">{{ profil.Lewa }}</span> — <strong>Karma (Lewa Strona)</strong> ({{ dict[profil.Lewa].litera }})<br>{{ dict[profil.Lewa].cien }}</div>
            <div class="card"><span class="num">{{ profil.Talent }}</span> — <strong>Talent (Kreacja)</strong> ({{ dict[profil.Talent].litera }})<br>{{ dict[profil.Talent].znaczenie }}</div>
            <div class="card karma"><span class="num">{{ profil.Gleboka }}</span> — <strong>Głęboka Osobowość</strong> ({{ dict[profil.Gleboka].litera }})<br>{{ dict[profil.Gleboka].cien }}</div>
            {% if posag %}
            <div class="card posag"><span class="num" style="color: #104F55;">{{ posag.Transformacja }}</span> — <strong>Transformacja Śmierci Przodka</strong> ({{ dict[posag.Transformacja].litera }})<br><strong>Posag rodowy:</strong> {{ dict[posag.Transformacja].posag }}</div>
            {% endif %}
        </div>
        <form action="/pobierz-pdf" method="POST">
            <input type="hidden" name="imie" value="{{ imie }}"><input type="hidden" name="data_ur" value="{{ data_ur }}"><input type="hidden" name="data_sm" value="{{ data_sm }}">
            <button type="submit" class="btn btn-pdf">📥 Pobierz Raport PDF do Druku</button>
        </form>
        {% endif %}
    </div>
</body>
</html>
"""
