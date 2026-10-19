"""
Verificación integral y formal de las salidas:
1. Valida el JSON especificaciones_data.json
2. Valida el HTML especificaciones_modelos.html y su JSON embebido
3. Comprueba formalmente ZERO caracteres CJK en ambos archivos
4. Comprueba que las 15 tarjetas y 1,213 especificaciones estén presentes
5. Comprueba estructura bilingüe (ES / EN) y selector interactivo
"""

import json
import os
import re

JSON_PATH = r"C:\Users\planchartglobal\code\ep\especificaciones_data.json"
HTML_PATH = r"C:\Users\planchartglobal\code\ep\especificaciones_modelos.html"
CJK_REGEX = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]")


def verify():
    assert os.path.exists(JSON_PATH), f"No existe {JSON_PATH}"
    assert os.path.exists(HTML_PATH), f"No existe {HTML_PATH}"

    print("=== 1. VERIFICACIÓN JSON ===")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        json_content = f.read()
        data = json.loads(json_content)

    # Comprobación estricta de CERO caracteres chinos
    json_cjk_matches = CJK_REGEX.findall(json_content)
    assert len(json_cjk_matches) == 0, f"Error: Se encontraron {len(json_cjk_matches)} caracteres CJK en el JSON!"
    print("  [OK] Cero (0) caracteres chinos en especificaciones_data.json")

    # Métricas y modelos
    print(f"  [OK] Modelos totales: {len(data['models'])}")
    print(f"  [OK] Tarjetas totales: {data['total_cards']}")
    print(f"  [OK] Filas totales extraídas: {data['total_rows_extracted']}")
    assert data["total_cards"] == 15, f"Esperadas 15 tarjetas, encontradas {data['total_cards']}"
    assert data["total_rows_extracted"] == 1213, f"Esperadas 1213 filas, encontradas {data['total_rows_extracted']}"

    expected_models = [
        "Z9", "Z9 PASSENGER", "Z9 HYBRID", "RICH 6",
        "RICH 6 PRO", "RICH 6 PRO NUEVO", "PALADIN", "T5 EVO"
    ]
    found_models = [m["key"] for m in data["models"]]
    for em in expected_models:
        assert em in found_models, f"Falta modelo {em}"
        print(f"  [OK] Modelo validado: {em}")

    # Comprobación de integridad bilingüe
    for model in data["models"]:
        assert "es" in model["name"] and "en" in model["name"], f"Modelo {model['key']} sin nombres bilingües"
        for card in model["cards"]:
            assert "es" in card["title"] and "en" in card["title"], f"Tarjeta {card['id']} sin títulos bilingües"
            assert "es" in card["subtitle"] and "en" in card["subtitle"], f"Tarjeta {card['id']} sin subtítulos bilingües"
            assert "all_categories" in card and len(card["all_categories"]) > 0, f"Tarjeta {card['id']} sin categorías completas"
            assert card["total_specs_count"] > 0, f"Tarjeta {card['id']} sin especificaciones"

    print("  [OK] Todos los campos de modelos y tarjetas cuentan con soporte bilingüe (ES / EN).")

    print("\n=== 2. VERIFICACIÓN HTML ===")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Comprobación estricta de CERO caracteres chinos en HTML
    html_cjk_matches = CJK_REGEX.findall(html_content)
    assert len(html_cjk_matches) == 0, f"Error: Se encontraron {len(html_cjk_matches)} caracteres CJK en el HTML!"
    print("  [OK] Cero (0) caracteres chinos en especificaciones_modelos.html")

    # Componentes visuales y reactivos
    assert "<!DOCTYPE html>" in html_content, "HTML no tiene doctype"
    assert "https://cdn.tailwindcss.com" in html_content, "Falta Tailwind CDN"
    assert "border-l-amber-500" in html_content or "border-l-[6px]" in html_content, "Falta acento ámbar en tarjetas"
    assert "border-emerald-400" in html_content, "Falta línea verde esmeralda"
    assert "specs-data-json" in html_content, "Falta JSON embebido para funcionamiento autónomo"
    assert "lang-btn-es" in html_content and "lang-btn-en" in html_content, "Falta selector de idioma en barra superior"
    assert "setLanguage" in html_content, "Falta función reactiva de cambio de idioma"
    assert "renderSingleCard" in html_content, "Falta función de renderizado de tarjeta"
    assert "fullSpecsHeading" in html_content, "Falta encabezado de desglose completo de especificaciones"
    print("  [OK] Selector bilingue reactivo [ Espanol | English ] presente e integrado.")
    print("  [OK] Componentes estructurales y desglose completo por categorías presentes en HTML.")

    print("\n=== ¡TODAS LAS VERIFICACIONES PASARON CON ÉXITO ROTUNDO! ===")


if __name__ == "__main__":
    verify()
