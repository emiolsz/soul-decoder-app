# widok.py - Dynamiczny formularz konstelacji rodzeństwa i przodków z funkcją select
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Soul Decoder App - Konstelacje</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; margin: 0; padding: 25px; color: #333; }
        .container { max-width: 900px; background: white; margin: 0 auto; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { color: #4A154B; text-align: center; margin-bottom: 5px; }
        .sub { text-align: center; color: #7f8c8d; margin-bottom: 25px; }
        fieldset { border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; }
        legend { font-weight: bold; color: #2c3e50; padding: 0 10px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; font-weight: 600; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; background: white; }
        .btn { display: inline-block; width: 100%; padding: 12px; background: #4A154B; color: white; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; text-align: center; text-decoration: none; }
        .btn:hover { background: #330f34; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #4A154B; }
        .card.match { border-left-color: #27AE60; background: #F4FBF7; grid-column: span 2; font-weight: bold; font-size: 15px; color: #1E6038; }
        .num { font-size: 22px; font-weight: bold; color: #4A154B; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Soul Decoder App</h1>
        <p class="sub">Wielopokoleniowe Matryce Dziedziczenia i Konstelacje Rodzeństwa</p>
        
        <form method="POST">
            <!-- SEKCJA POTOMKÓW (RODZEŃSTWO) -->
            <div class="grid">
                <div>
                    <fieldset>
                        <legend>Osoba 1</legend>
                        <div class="form-group">
                            <label>Relacja:</label>
                            <select name="relacja1">
                                <option value="Ja" {% if relacja1 == "Ja" %}selected{% endif %}>Ja</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Imię:</label><input type="text" name="imie1" value="{{ imie1 }}" required></div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur1" value="{{ data_ur1 }}" required></div>
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
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur2" value="{{ data_ur2 }}" required></div>
                    </fieldset>
                </div>
            </div>

            <!-- SEKCJA PRZODKÓW -->
            <div class="grid">
                <div>
                    <fieldset>
                        <legend>Przodek A</legend>
                        <div class="form-group">
                            <label>Wybierz relację:</label>
                            <select name="p_relA">
                                <option value="Prababcia" {% if p_relA == "Prababcia" %}selected{% endif %}>Prababcia</option>
                                <option value="Babcia" {% if p_relA == "Babcia" %}selected{% endif %}>Babcia</option>
                                <option value="Mama" {% if p_relA == "Mama" %}selected{% endif %}>Mama</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urA" value="{{ p_urA }}" required></div>
                    </fieldset>
                </div>
                <div>
                    <fieldset>
                        <legend>Przodek B</legend>
                        <div class="form-group">
                            <label>Wybierz relację:</label>
                            <select name="p_relB">
                                <option value="Pradziadek" {% if p_relB == "Pradziadek" %}selected{% endif %}>Pradziadek</option>
                                <option value="Dziadek" {% if p_relB == "Dziadek" %}selected{% endif %}>Dziadek</option>
                                <option value="Ojciec" {% if p_relB == "Ojciec" %}selected{% endif %}>Ojciec</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urB" value="{{ p_urB }}" required></div>
                    </fieldset>
                </div>
            </div>
            
            <button type="submit" class="btn">Uruchom Analizę Mapy Dziedziczenia</button>
        </form>

        {% if p1 %}
        <hr style="margin: 30px 0; border: 0; border-top: 1px solid #eee;">
        
        <h2>🧬 Wykryte Połączenia i Transgresje Rodowe</h2>
        <div class="grid" style="grid-template-columns: 1fr;">
            {% for m in mecze %}
            <div class="card match">{{ m }}</div>
            {% endfor %}
        </div>

        <h2>👥 Wyliczone Profile Główne</h2>
        <div class="grid">
            <div class="card">
                <h3>{{ imie1 }} ({{ relacja1 }})</h3>
                <strong>Tikkun (Wyzwanie):</strong> <span class="num">{{ p1.Tikkun }}</span> ({{ dict[p1.Tikkun].litera }})<br>
                <small>{{ dict[p1.Tikkun].znaczenie }}</small>
            </div>
            <div class="card">
                <h3>{{ imie2 }} ({{ relacja2 }})</h3>
                <strong>Tikkun (Wyzwanie):</strong> <span class="num">{{ p2.Tikkun }}</span> ({{ dict[p2.Tikkun].litera }})<br>
                <small>{{ dict[p2.Tikkun].znaczenie }}</small>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


