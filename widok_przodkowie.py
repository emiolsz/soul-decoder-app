# widok_przodkowie.py - Dynamiczne rysowanie kafelków dla n-uczestników konstelacji oraz ukryty formularz PDF
HTML_TEMPLATE_END = """
        <!-- PEŁNA ANALIZA KAŻDEGO Z PUNKTÓW U KAŻDEJ AKTYWNEJ OSOBY TOWARZYSZĄCEJ -->
        {% if aktywne_profile_wynik %}
        <h2 class="profile-title profile-title.przodek">📜 Pełna Analiza Architektury Dołączonych Członków Konstelacji</h2>
        <div class="grid">
            {% for item in aktywne_profile_wynik %}
            <div class="card" style="border-left-color: #104F55;">
                <h3>{{ item.imie or item.rel }} ({{ item.rel }})</h3>
                <div class="mini-grid">
                    <div class="mini-card">Dar<strong>{{ item.prof.Prawa }}</strong></div>
                    <div class="mini-card">Karma<strong>{{ item.prof.Lewa }}</strong></div>
                    <div class="mini-card">Talent<strong>{{ item.prof.Talent }}</strong></div>
                    <div class="mini-card">Głęboka<strong>{{ item.prof.Gleboka }}</strong></div>
                    <div class="mini-card" style="color:#d35400;">Węzeł<strong>{{ item.prof.Wezel }}</strong></div>
                    <div class="mini-card" style="color:#27ae60;">Tikkun<strong>{{ item.prof.Tikkun }}</strong></div>
                </div>
                
                {% if item.posag %}
                <div class="card transgresja" style="margin-top:12px; padding:10px; border-left-width: 3px; font-size:12px;">
                    <strong>Posag z Przejścia:</strong> {{ item.posag.Transformacja }}<br>
                    <strong>Zasób rodowy:</strong> {{ dict[item.posag.Transformacja].posag }}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        
        <!-- CENTRUM WYDRUKU PDF -->
        <hr style="margin: 40px 0; border: 0; border-top: 2px solid #ccc;">
        <h2>🖨️ Centrum Eksportu: Raport Architektury Kodu Duszy</h2>
        <form action="/pobierz-pdf" method="POST" style="background: #FAF9F6; padding: 20px; border-radius: 8px; border: 2px dashed #4A154B;">
            <input type="hidden" name="d_imie1" value="{{ imie1 }}"><input type="hidden" name="d_ur1" value="{{ data_ur1 }}"><input type="hidden" name="d_sm1" value="{{ data_sm1 }}">
            <input type="hidden" name="d_ile_osob" value="{{ ile_osob }}">
            
            {% for i in range(ile_osob) %}
            <input type="hidden" name="d_rel_{{ i }}" value="{{ aktywne_role[i] if i < aktywne_role|length else 'Brat' }}">
            <input type="hidden" name="d_imie_{{ i }}" value="{{ aktywne_imiona[i] if i < aktywne_imiona|length else '' }}">
            <input type="hidden" name="d_ur_{{ i }}" value="{{ aktywne_ur[i] if i < aktywne_ur|length else '' }}">
            <input type="hidden" name="d_sm_{{ i }}" value="{{ aktywne_sm[i] if i < aktywne_sm|length else '' }}">
            {% endfor %}
            
            <div class="form-group">
                <label>Wybierz wariant pliku do wydruku (Czcionka: Natywna Helvetica PL Premium):</label>
                <select name="typ_wydruku" style="padding: 10px; border: 2px solid #4A154B; font-weight: bold; background: #FFFDF9;">
                    <option value="PELNY">Pełny Raport Konstelacji Relacji (Pełna paleta 6 punktów dla Ciebie i wszystkich {{ ile_osob }} wybranych osób)</option>
                    <option value="OSOBISTY">Tylko Mój Profil Opisowy (Wyłącznie Twoja osobista matryca 6 punktów)</option>
                </select>
            </div>
            <button type="submit" class="btn" style="background: #4A154B;">📥 Pobierz Raport Architektury Kodu Duszy (PDF)</button>
        </form>
        {% endif %}
    </div>
</body>
</html>
"""

