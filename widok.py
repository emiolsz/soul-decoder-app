# widok.py - PORCJA 1: Style, Profil Główny ze statusem oraz Suwak Liczby Osób
HTML_TEMPLATE_START = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Soul Decoder App</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; margin: 0; padding: 25px; color: #333; }
        .container { max-width: 1050px; background: white; margin: 0 auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { color: #4A154B; text-align: center; margin-bottom: 5px; }
        .sub { text-align: center; color: #7f8c8d; margin-bottom: 25px; }
        fieldset { border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; background: #fff; }
        legend { font-weight: bold; color: #2c3e50; padding: 0 10px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; font-weight: 600; font-size: 13px; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; background: white; }
        .suwak-container { background: #FAF5FA; border: 2px solid #4A154B; padding: 15px; border-radius: 8px; margin: 20px 0; }
        .suwak-title { font-weight: bold; color: #4A154B; margin-bottom: 8px; display: block; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #4A154B; margin-bottom: 10px; }
        .card.karma { border-left-color: #C0392B; }
        .card.wezel { border-left-color: #D35400; background: #FFF5EE; }
        .card.tikkun { border-left-color: #27AE60; background: #F4FBF7; }
        .card.transgresja { border-left-color: #104F55; background: #f0f4f8; }
        .card.match { border-left-color: #2980b9; background: #e3f2fd; font-weight: bold; color: #154360; padding: 12px; border-radius: 6px; }
        .num { font-size: 22px; font-weight: bold; color: #4A154B; }
        .profile-title { background: #4A154B; color: white; padding: 8px 12px; border-radius: 6px; margin-top: 25px; margin-bottom: 15px; }
        .profile-title.przodek { background: #104F55; }
        .mini-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
        .mini-card { background: #fff; padding: 10px; border-radius: 6px; border: 1px solid #eee; text-align: center; font-size: 12px; }
        .mini-card strong { display: block; font-size: 16px; color: #4A154B; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Soul Decoder App</h1>
        <p class="sub">Matryce Przeznaczenia i Wielopokoleniowe Konstelacje Relacji (Maksymalnie 10 Osób)</p>
        
        <form method="POST">
            <!-- PROFIL GŁÓWNY (Z WYBOREM STATUSU) -->
            <fieldset style="border-color: #4A154B; background: #FAF5FA;">
                <legend style="color: #4A154B;">Profil Główny</legend>
                <div class="grid">
                    <div class="form-group"><label>Imię / Oznaczenie:</label><input type="text" name="imie1" value="{{ imie1 }}" required></div>
                    <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur1" value="{{ data_ur1 }}" min="1800-01-01" required></div>
                    <div class="form-group">
                        <label>Status osoby:</label>
                        <select name="status1" onchange="this.form.submit()">
                            <option value="ZYJE" {% if status1 == "ZYJE" %}selected{% endif %}>Osoba żyjąca</option>
                            <option value="TRANSGRESJA" {% if status1 == "TRANSGRESJA" %}selected{% endif %}>Osoba nieżyjąca (Po transformacji)</option>
                        </select>
                    </div>
                    {% if status1 == "TRANSGRESJA" %}
                    <div class="form-group"><label>Data Transformacji (Przejścia):</label><input type="date" name="data_sm1" value="{{ data_sm1 }}" min="1800-01-01" required></div>
                    {% else %}
                    <input type="hidden" name="data_sm1" value="">
                    {% endif %}
                </div>
            </fieldset>

            <!-- SUWAK LICZBY UCZESTNIKÓW -->
            <div class="suwak-container">
                <span class="suwak-title">Liczba osób do dołączenia do analizy (Maksymalnie 10): {{ ile_osob }}</span>
                <input type="range" name="ile_osob" min="1" max="10" value="{{ ile_osob }}" step="1" onchange="this.form.submit()" style="cursor: pointer; accent-color: #4A154B;">
            </div>

            <h3 style="color:#104F55; border-bottom: 2px solid #104F55; padding-bottom:5px;">2. Konstelacja Relacji</h3>
            <div class="grid">
"""





