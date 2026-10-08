# widok.py - PORCJA 1: Style i Formularz Wejściowy
HTML_TEMPLATE_START = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Soul Decoder App - Matrix</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; margin: 0; padding: 25px; color: #333; }
        .container { max-width: 1050px; background: white; margin: 0 auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { color: #4A154B; text-align: center; margin-bottom: 5px; }
        .sub { text-align: center; color: #7f8c8d; margin-bottom: 25px; }
        fieldset { border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; }
        legend { font-weight: bold; color: #2c3e50; padding: 0 10px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; font-weight: 600; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; background: white; }
        .btn { display: inline-block; width: 100%; padding: 12px; background: #4A154B; color: white; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-align: center; text-decoration: none; }
        .btn:hover { background: #330f34; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #4A154B; margin-bottom: 10px; }
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
        <p class="sub">Wielopokoleniowe Matryce Dziedziczenia i Konstelacje Rodzeństwa Matrix</p>
        
        <form method="POST">
            <div class="grid">
                <div>
                    <fieldset>
                        <legend>Osoba 1 (Ty)</legend>
                        <div class="form-group"><label>Imię:</label><input type="text" name="imie1" value="{{ imie1 }}" required></div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur1" value="{{ data_ur1 }}" min="1800-01-01" required></div>
                    </fieldset>
                </div>
                <div>
                    <fieldset>
                        <legend>Osoba 2 (Rodzeństwo)</legend>
                        <div class="form-group">
                            <label>Relacja:</label>
                            <select name="relacja2">
                                <option value="Brat" {% if relacja2 == "Brat" %}selected{% endif %}>Brat</option>
                                <option value="Siostra" {% if relacja2 == "Siostra" %}selected{% endif %}>Siostra</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Imię:</label><input type="text" name="imie2" value="{{ imie2 }}" required></div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur2" value="{{ data_ur2 }}" min="1800-01-01" required></div>
                    </fieldset>
                </div>
            </div>

            <div class="grid">
                <div>
                    <fieldset style="border-color: #104F55;">
                        <legend style="color: #104F55;">Przodek A</legend>
                        <div class="form-group">
                            <label>Relacja:</label>
                            <select name="p_relA">
                                <option value="Prababcia" {% if p_relA == "Prababcia" %}selected{% endif %}>Prababcia</option>
                                <option value="Babcia" {% if p_relA == "Babcia" %}selected{% endif %}>Babcia</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urA" value="{{ p_urA }}" min="1800-01-01" required></div>
                        <div class="form-group"><label>Data Śmierci:</label><input type="date" name="p_smA" value="{{ p_smA }}" min="1800-01-01"></div>
                    </fieldset>
                </div>
                <div>
                    <fieldset style="border-color: #104F55;">
                        <legend style="color: #104F55;">Przodek B</legend>
                        <div class="form-group">
                            <label>Relacja:</label>
                            <select name="p_relB">
                                <option value="Pradziadek" {% if p_relB == "Pradziadek" %}selected{% endif %}>Pradziadek</option>
                                <option value="Dziadek" {% if p_relB == "Dziadek" %}selected{% endif %}>Dziadek</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urB" value="{{ p_urB }}" min="1800-01-01" required></div>
                        <div class="form-group"><label>Data Śmierci:</label><input type="date" name="p_smB" value="{{ p_smB }}" min="1800-01-01"></div>
                    </fieldset>
                </div>
            </div>
            <button type="submit" class="btn">Uruchom Inteligentny Cross-Matching</button>
        </form>
"""



