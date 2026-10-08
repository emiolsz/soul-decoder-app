# widok_formularz2.py - PORCJA 2: Dynamiczna pętla generująca od 1 do 10 ramek uczestników
HTML_TEMPLATE_FORM2 = """
                {% for i in range(ile_osob) %}
                <fieldset style="border-color: #104F55;">
                    <legend style="color: #104F55;">Osoba {{ i + 1 }}</legend>
                    <div class="form-group">
                        <label>Relacja / Pokrewieństwo:</label>
                        <select name="p_rel_{{ i }}">
                            <!-- Odczyt zapamiętanej roli z listy przesłanej z serwera -->
                            {% set wybrana_rola = aktywne_role[i] if i < aktywne_role|length else "Brat" %}
                            <option value="Brat" {% if wybrana_rola == "Brat" %}selected{% endif %}>Brat</option>
                            <option value="Siostra" {% if wybrana_rola == "Siostra" %}selected{% endif %}>Siostra</option>
                            <option value="Partner" {% if wybrana_rola == "Partner" %}selected{% endif %}>Partner</option>
                            <option value="Partnerka" {% if wybrana_rola == "Partnerka" %}selected{% endif %}>Partnerka</option>
                            <option value="Mąż" {% if wybrana_rola == "Mąż" %}selected{% endif %}>Mąż</option>
                            <option value="Żona" {% if wybrana_rola == "Żona" %}selected{% endif %}>Żona</option>
                            <option value="Syn" {% if wybrana_rola == "Syn" %}selected{% endif %}>Syn</option>
                            <option value="Córka" {% if wybrana_rola == "Córka" %}selected{% endif %}>Córka</option>
                            <option value="Bratanek" {% if wybrana_rola == "Bratanek" %}selected{% endif %}>Bratanek</option>
                            <option value="Siostrzeniec" {% if wybrana_rola == "Siostrzeniec" %}selected{% endif %}>Siostrzeniec</option>
                            <option value="Mama" {% if wybrana_rola == "Mama" %}selected{% endif %}>Mama (Linia Rodziców)</option>
                            <option value="Ojciec" {% if wybrana_rola == "Ojciec" %}selected{% endif %}>Ojciec (Linia Rodziców)</option>
                            <option value="Ciotka" {% if wybrana_rola == "Ciotka" %}selected{% endif %}>Ciotka</option>
                            <option value="Wujek" {% if wybrana_rola == "Wujek" %}selected{% endif %}>Wujek</option>
                            <option value="Babcia" {% if wybrana_rola == "Babcia" %}selected{% endif %}>Babcia (Mama taty/mamy)</option>
                            <option value="Dziadek" {% if wybrana_rola == "Dziadek" %}selected{% endif %}>Dziadek (Tata taty/mamy)</option>
                            <option value="Prababcia" {% if wybrana_rola == "Prababcia" %}selected{% endif %}>Prababcia (Babcia taty/mamy)</option>
                            <option value="Pradziadek" {% if wybrana_rola == "Pradziadek" %}selected{% endif %}>Pradziadek (Dziadek taty/mamy)</option>
                            <option value="Brat dziadka" {% if wybrana_rola == "Brat dziadka" %}selected{% endif %}>Brat dziadka</option>
                            <option value="Siostra babci" {% if wybrana_rola == "Siostra babci" %}selected{% endif %}>Siostra babci</option>
                        </select>
                    </div>
                    <div class="form-group"><label>Imię:</label><input type="text" name="p_imie_{{ i }}" value="{{ aktywne_imiona[i] if i < aktywne_imiona|length else '' }}"></div>
                    <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_ur_{{ i }}" value="{{ aktywne_ur[i] if i < aktywne_ur|length else '' }}" min="1800-01-01"></div>
                    <div class="form-group"><label>Data Transformacji (Opcjonalnie):</label><input type="date" name="p_sm_{{ i }}" value="{{ aktywne_sm[i] if i < aktywne_sm|length else '' }}" min="1800-01-01"></div>
                </fieldset>
                {% endfor %}
            </div>
            <button type="submit" name="akcja_dekoduj" value="TAK" class="btn" style="margin-top: 20px;">Uruchom Pełne Mapowanie Konstelacji i Przekazów Krzyżowych</button>
        </form>
"""

