"""
Ensamblador del visualizador HTML autonomo interactivo.
Coordina la lectura del JSON y la union de modulos de presentacion.
"""

import json
from html_template import get_html_head, get_html_body_header
from html_script import get_client_script

JSON_PATH = r"C:\Users\planchartglobal\code\ep\especificaciones_data.json"
HTML_PATH = r"C:\Users\planchartglobal\code\ep\especificaciones_modelos.html"


def build_html():
    print(f"Leyendo datos desde {JSON_PATH}...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    json_str = json.dumps(data, ensure_ascii=False)

    html_parts = [
        get_html_head(),
        get_html_body_header(),
        get_client_script(json_str),
    ]

    full_html = "\n".join(html_parts)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Visualizador HTML generado con exito en {HTML_PATH}")
    print(f"Tamano del archivo generado: {len(full_html)} bytes")


if __name__ == "__main__":
    build_html()
