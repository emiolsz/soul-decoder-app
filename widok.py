# widok.py - Dynamiczny formularz konstelacji rodzeństwa i przodków
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Soul Decoder App - Matrix</title>
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
        .btn-pdf { background: #104F55; margin-top: 15px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #4A154B; }
        .card.karma { border-left-color: #C0392B; }
        .card.tikkun { border-left-color: #27AE60; background: #F4FBF7; }
        .card.match { border-left-color: #2980b9; background: #e3f2fd; grid-column: span 2; font-weight: bold; }
        .num { font-size: 22px; font-weight: bold; color: #4A154B; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Soul Decoder App</h1>
        <p class="sub">Analiza Konstelacji Rodzeństwa i Dziedziczenia po Przodkach</p>
        
        <form method="POST">
            <div class="grid">
                <div>
                    <fieldset>
                        <legend>Osoba 1 (Ty)</legend>
                        <div class="form-group"><label>Imię:</label><input type="text" name="imie1" value="{{ imie1 }}" required></div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur1" value="{{ data_ur1 }}" required></div>
                    </fieldset>
                </div>
                <div>
                    <fieldset>
                        <legend>Osoba 2 (Rodzeństwo / Brat)</legend>
                        <div class="form-group"><label>Imię:</label><input type="text" name="imie2" value="{{ imie2 }}" required></div>
                        <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="data_ur2" value="{{ data_ur2 }}" required></div>
                    </fieldset>
                </div>
            </div>

            <div class="grid">
                <div>
                    <fieldset>
                        <legend>Przodek A (np. Prababcia)</legend>
                        <div class="form-group"><label>Relacja:</label><input type="text" name="p_relA" value="{{ p_relA }}"></div>
                        <div class="form-group"><label>Data Urodzenia Przodka:</label><input type="date" name="p_urA" value="{{ p_urA }}"></div>
                    </fieldset>
                </div>
                <div>
                    <fieldset>
                        <legend>Przodek B (np. Pradziadek)</legend>
                        <div class="form-group"><label>Relacja:</label><input type="text" name="p_relB" value="{{ p_relB }}"></div>
                        <div class="form-group"><label>Data Urodzenia Przodka:</label><input type="date" name="p_urB" value="{{ p_urB }}"></div>
                    </fieldset>
                </div>
            </div>
            
            <button type="submit" class="btn">Uruchom Analizę Konstelacji Rodowej</button>
        </form>

        {% if p1 %}
        <hr style="margin: 30px 0; border: 0; border-top: 1px solid #eee;">
        
        <!-- MATRYCA ANALIZY WĘZŁÓW REZONANSU -->
        <h2>🧬 Analiza Rezonansu i Przekazu Rodowego</h2>
        <div class="grid">
            {% for m in mecze %}
            <div class="card match">🎯 {{ m }}</div>
            {% endfor %}
        </div>

        <h2>👥 Profile Indywidualne Rodzeństwa</h2>
        <div class="grid">
            <div class="card">
                <h3>{{ imie1 }}</h3>
                Tikkun (Wyzwanie): <span class="num">{{ p1.Tikkun }}</span> ({{ dict[p1.Tikkun].litera }})<br>
                <small>{{ dict[p1.Tikkun].znaczenie }}</small>
            </div>
            <div class="card">
                <h3>{{ imie2 }}</h3>
                Tikkun (Wyzwanie): <span class="num">{{ p2.Tikkun }}</span> ({{ dict[p2.Tikkun].litera }})<br>
                <small>{{ dict[p2.Tikkun].znaczenie }}</small>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

