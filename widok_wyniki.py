# widok_wyniki.py - Wyświetlanie korelacji i pełnej matrycy Profilu Głównego z Posagiem
HTML_TEMPLATE_MID = """
        {% if p1 %}
        <hr style="margin: 40px 0; border: 0; border-top: 2px solid #ccc;">
        
        <h2>🧬 Rezultaty Inteligentnego Mapowania Krzyżowego Konstelacji</h2>
        <div style="margin-bottom: 25px; display: grid; gap: 10px;">
            {% for m in mecze %}
            <div class="card match">{{ m|safe }}</div>
            {% endfor %}
        </div>

        <h2>👥 Osobista Matryca Architektury Duszy (Profil Główny)</h2>
        <div class="grid">
            <div class="card" style="border-left-width: 8px;">
                <h3>{{ imie1 }} (Profil Główny)</h3>
                <strong>Dar (Prawa Strona):</strong> <span class="num">{{ p1.Prawa }}</span><br>
                <strong>Karma (Lewa Strona):</strong> <span class="num" style="color:#C0392B;">{{ p1.Lewa }}</span><br>
                <strong>Talent (Kreacja):</strong> <span class="num">{{ p1.Talent }}</span><br>
                <strong>Głęboka Osobowość:</strong> <span class="num">{{ p1.Gleboka }}</span><br>
                <strong>Węzeł Oporu (Blokada):</strong> <span class="num" style="color:#D35400;">{{ p1.Wezel }}</span><br>
                <strong>Tikkun (Wyzwanie):</strong> <span class="num" style="color:#27AE60;">{{ p1.Tikkun }}</span>
                
                {% if posag1 %}
                <div class="card transgresja" style="margin-top:15px; border-left-width: 3px;">
                    <strong>Posag z Przejścia Profilu Głównego:</strong> <span class="num" style="color:#104F55;">{{ posag1.Transformacja }}</span><br>
                    <small>Esencja uwalniana: {{ dict[posag1.Transformacja].posag }}</small>
                </div>
                {% endif %}
            </div>
        </div>
"""

