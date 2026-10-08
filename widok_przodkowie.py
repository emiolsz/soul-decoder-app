# widok_przodkowie.py - PORCJA 3: Pełne tabele przodków i domknięcie HTML
HTML_TEMPLATE_END = """
        <h2 class="profile-title profile-title.przodek">📜 Pełne Matryce Urodzeniowe Przodków</h2>
        <div class="grid">
            <div class="card" style="border-left-color: #104F55;">
                <h3>{{ p_relA }} (Urodzenie)</h3>
                <div class="mini-grid">
                    <div class="mini-card">Dar<strong>{{ pA.Prawa }}</strong></div>
                    <div class="mini-card">Karma<strong>{{ pA.Lewa }}</strong></div>
                    <div class="mini-card">Talent<strong>{{ pA.Talent }}</strong></div>
                    <div class="mini-card">Głęboka<strong>{{ pA.Gleboka }}</strong></div>
                    <div class="mini-card">Węzeł<strong>{{ pA.Wezel }}</strong></div>
                    <div class="mini-card">Tikkun<strong>{{ pA.Tikkun }}</strong></div>
                </div>
            </div>
            <div class="card" style="border-left-color: #104F55;">
                <h3>{{ p_relB }} (Urodzenie)</h3>
                <div class="mini-grid">
                    <div class="mini-card">Dar<strong>{{ pB.Prawa }}</strong></div>
                    <div class="mini-card">Karma<strong>{{ pB.Lewa }}</strong></div>
                    <div class="mini-card">Talent<strong>{{ pB.Talent }}</strong></div>
                    <div class="mini-card">Głęboka<strong>{{ pB.Gleboka }}</strong></div>
                    <div class="mini-card">Węzeł<strong>{{ pB.Wezel }}</strong></div>
                    <div class="mini-card">Tikkun<strong>{{ pB.Tikkun }}</strong></div>
                </div>
            </div>
        </div>

        <h2 class="profile-title profile-title.przodek">💀 Analiza Przejścia i Posagów Energetycznych</h2>
        <div class="grid">
            {% if posagA %}
            <div class="card" style="background:#f0f4f8; border-left: 5px solid #104F55;">
                <h3>{{ p_relA }} (Posag)</h3>
                <strong>Transformacja Śmierci:</strong> {{ posagA.Transformacja }}<br>
                <strong>Esencja dla Rodu:</strong> {{ dict[posagA.Transformacja].posag }}
            </div>
            {% endif %}
            {% if posagB %}
            <div class="card" style="background:#f0f4f8; border-left: 5px solid #104F55;">
                <h3>{{ p_relB }} (Posag)</h3>
                <strong>Transformacja Śmierci:</strong> {{ posagB.Transformacja }}<br>
                <strong>Esencja dla Rodu:</strong> {{ dict[posagB.Transformacja].posag }}
            </div>
            {% endif %}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""
