# widok.py - PORCJA 1: Style CSS, Profil Główny oraz Konfiguracja Osoby A
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
        legend { font-weight: bold; color: #2c3e50; padding: 0 10px; display: flex; align-items: center; gap: 8px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; font-weight: 600; font-size: 13px; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; background: white; }
        input[type="checkbox"] { width: auto; margin-right: 5px; transform: scale(1.1); cursor: pointer; }
        .btn { display: inline-block; width: 100%; padding: 14px; background: #4A154B; color: white; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-align: center; }
        .btn:hover { background: #330f34; }
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
        <p class="sub">Matryce Przeznaczenia i Konstelacje Relacji Pola Rodowego</p>
        
        <form method="POST">
            <fieldset style="border-color: #4A154B; background: #FAF5FA;">
                <legend style="color: #4A154B;">Profil Główny (Podstawa Analizy)</legend>
                <div class="grid">
                    <div class="form-group"><label>Imię / Oznaczenie:</label><input type="text" name="imie1" value="{{ imie1 }}" required></div>
                    <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur1" value="{{ data_ur1 }}" min="1800-01-01" required></div>
                </div>
            </fieldset>

            <h3 style="color:#104F55; border-bottom: 2px solid #104F55; padding-bottom:5px; margin-top:25px;">2. Konstelacja Relacji (Zaznacz osoby do analizy)</h3>
            
            <div class="grid">
                <fieldset style="border-color: #104F55;">
                    <legend style="color: #104F55;"><input type="checkbox" name="chk_pA" {% if chk_pA %}checked{% endif %}> Dołącz Osobę A</legend>
                    <div class="form-group">
                        <label>Relacja / Pokrewieństwo:</label>
                        <select name="p_relA">
                            <option value="Brat" {% if p_relA == "Brat" %}selected{% endif %}>Brat</option>
                            <option value="Siostra" {% if p_relA == "Siostra" %}selected{% endif %}>Siostra</option>
                            <option value="Partner" {% if p_relA == "Partner" %}selected{% endif %}>Partner</option>
                            <option value="Partnerka" {% if p_relA == "Partnerka" %}selected{% endif %}>Partnerka</option>
                            <option value="Mąż" {% if p_relA == "Mąż" %}selected{% endif %}>Mąż</option>
                            <option value="Żona" {% if p_relA == "Żona" %}selected{% endif %}>Żona</option>
                            <option value="Syn" {% if p_relA == "Syn" %}selected{% endif %}>Syn</option>
                            <option value="Córka" {% if p_relA == "Córka" %}selected{% endif %}>Córka</option>
                            <option value="Bratanek" {% if p_relA == "Bratanek" %}selected{% endif %}>Bratanek</option>
                            <option value="Siostrzeniec" {% if p_relA == "Siostrzeniec" %}selected{% endif %}>Siostrzeniec</option>
                            <option value="Mama" {% if p_relA == "Mama" %}selected{% endif %}>Mama</option>
                            <option value="Ojciec" {% if p_relA == "Ojciec" %}selected{% endif %}>Ojciec</option>
                            <option value="Ciotka" {% if p_relA == "Ciotka" %}selected{% endif %}>Ciotka</option>
                            <option value="Wujek" {% if p_relA == "Wujek" %}selected{% endif %}>Wujek</option>
                            <option value="Babcia" {% if p_relA == "Babcia" %}selected{% endif %}>Babcia</option>
                            <option value="Dziadek" {% if p_relA == "Dziadek" %}selected{% endif %}>Dziadek</option>
                            <option value="Prababcia" {% if p_relA == "Prababcia" %}selected{% endif %}>Prababcia</option>
                            <option value="Pradziadek" {% if p_relA == "Pradziadek" %}selected{% endif %}>Pradziadek</option>
                            <option value="Brat dziadka" {% if p_relA == "Brat dziadka" %}selected{% endif %}>Brat dziadka</option>
                            <option value="Siostra babci" {% if p_relA == "Siostra babci" %}selected{% endif %}>Siostra babci</option>
                        </select>
                    </div>
                    <div class="form-group"><label>Imię:</label><input type="text" name="p_imieA" value="{{ p_imieA }}"></div>
                    <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urA" value="{{ p_urA }}" min="1800-01-01"></div>
                    <div class="form-group"><label>Data Transformacji (Opcjonalnie):</label><input type="date" name="p_smA" value="{{ p_smA }}" min="1800-01-01"></div>
                </fieldset>
"""




