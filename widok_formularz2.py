# widok_formularz2.py - PORCJA 2: Konfiguracja Osoby B i zamknięcie formularza HTML
HTML_TEMPLATE_FORM2 = """
                <fieldset style="border-color: #104F55;">
                    <legend style="color: #104F55;"><input type="checkbox" name="chk_pB" {% if chk_pB %}checked{% endif %}> Dołącz Osobę B</legend>
                    <div class="form-group">
                        <label>Relacja / Pokrewieństwo:</label>
                        <select name="p_relB">
                            <option value="Brat" {% if p_relB == "Brat" %}selected{% endif %}>Brat</option>
                            <option value="Siostra" {% if p_relB == "Siostra" %}selected{% endif %}>Siostra</option>
                            <option value="Partner" {% if p_relB == "Partner" %}selected{% endif %}>Partner</option>
                            <option value="Partnerka" {% if p_relB == "Partnerka" %}selected{% endif %}>Partnerka</option>
                            <option value="Mąż" {% if p_relB == "Mąż" %}selected{% endif %}>Mąż</option>
                            <option value="Żona" {% if p_relB == "Żona" %}selected{% endif %}>Żona</option>
                            <option value="Syn" {% if p_relB == "Syn" %}selected{% endif %}>Syn</option>
                            <option value="Córka" {% if p_relB == "Córka" %}selected{% endif %}>Córka</option>
                            <option value="Bratanek" {% if p_relB == "Bratanek" %}selected{% endif %}>Bratanek</option>
                            <option value="Siostrzeniec" {% if p_relB == "Siostrzeniec" %}selected{% endif %}>Siostrzeniec</option>
                            <option value="Mama" {% if p_relB == "Mama" %}selected{% endif %}>Mama</option>
                            <option value="Ojciec" {% if p_relB == "Ojciec" %}selected{% endif %}>Ojciec</option>
                            <option value="Ciotka" {% if p_relB == "Ciotka" %}selected{% endif %}>Ciotka</option>
                            <option value="Wujek" {% if p_relB == "Wujek" %}selected{% endif %}>Wujek</option>
                            <option value="Babcia" {% if p_relB == "Babcia" %}selected{% endif %}>Babcia</option>
                            <option value="Dziadek" {% if p_relB == "Dziadek" %}selected{% endif %}>Dziadek</option>
                            <option value="Prababcia" {% if p_relB == "Prababcia" %}selected{% endif %}>Prababcia</option>
                            <option value="Pradziadek" {% if p_relB == "Pradziadek" %}selected{% endif %}>Pradziadek</option>
                            <option value="Brat dziadka" {% if p_relB == "Brat dziadka" %}selected{% endif %}>Brat dziadka</option>
                            <option value="Siostra babci" {% if p_relB == "Siostra babci" %}selected{% endif %}>Siostra babci</option>
                        </select>
                    </div>
                    <div class="form-group"><label>Imię:</label><input type="text" name="p_imieB" value="{{ p_imieB }}"></div>
                    <div class="form-group"><label>Data Urodzenia:</label><input type="date" name="p_urB" value="{{ p_urB }}" min="1800-01-01"></div>
                    <div class="form-group"><label>Data Transformacji (Opcjonalnie):</label><input type="date" name="p_smB" value="{{ p_smB }}" min="1800-01-01"></div>
                </fieldset>
            </div>
            <button type="submit" class="btn">Uruchom Mapowanie Relacji i Przekazów Krzyżowych</button>
        </form>
"""
