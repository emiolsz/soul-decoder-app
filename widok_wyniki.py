# widok_wyniki.py - PORCJA 2: Kafelki wyników dla Ciebie i rodzeństwa
HTML_TEMPLATE_MID = """
        {% if p1 %}
        <hr style="margin: 40px 0; border: 0; border-top: 2px solid #ccc;">
        <h2>🧬 Rezultaty Inteligentnego Mapowania Krzyżowego</h2>
        <div style="margin-bottom: 25px; display: grid; gap: 10px;">
            {% for m in mecze %}
            <div class="card match">{{ m|safe }}</div>
            {% endfor %}
        </div>

        <h2>👥 Matryce Indywidualne Rodzeństwa</h2>
        <div class="grid">
            <div class="card" style="border-left-width:8px;">
                <h3>{{ imie1 }} (Ja)</h3>
                <strong>Dar (Prawa):</strong> {{ p1.Prawa }} | <strong>Karma (Lewa):</strong> {{ p1.Lewa }}<br>
                <strong>Talent:</strong> {{ p1.Talent }} | <strong>Głęboka:</strong> {{ p1.Gleboka }}<br>
                <strong>Węzeł Oporu:</strong> {{ p1.Wezel }} | <strong>Tikkun:</strong> {{ p1.Tikkun }}
            </div>
            <div class="card" style="border-left-width:8px; border-left-color:#2980b9;">
                <h3>{{ imie2 }} ({{ relacja2 }})</h3>
                <strong>Dar (Prawa):</strong> {{ p2.Prawa }} | <strong>Karma (Lewa):</strong> {{ p2.Lewa }}<br>
                <strong>Talent:</strong> {{ p2.Talent }} | <strong>Głęboka:</strong> {{ p2.Gleboka }}<br>
                <strong>Węzeł Oporu:</strong> {{ p2.Wezel }} | <strong>Tikkun:</strong> {{ p2.Tikkun }}
            </div>
        </div>
"""
