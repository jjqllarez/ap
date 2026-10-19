"""
Extractor de especificaciones técnicas desde Excel con soporte bilingüe integral (ES / EN).
Garantiza 0 caracteres chinos y genera especificaciones_data.json.
"""

import os
import re
import json
import openpyxl

from model_configs import SHEET_CONFIGS
from translator import get_bilingual, clean_cjk

EXCEL_PATH = r"C:\Users\planchartglobal\code\ep\LISTA DE SPECIFICACIONES.xlsx"
JSON_OUTPUT_PATH = r"C:\Users\planchartglobal\code\ep\especificaciones_data.json"

def clean_cell_text(val):
    if val is None:
        return ""
    text = str(val).strip()
    return re.sub(r"\s+", " ", text)

def get_grid_with_merged_cells(ws):
    max_r = ws.max_row
    max_c = ws.max_column
    grid = [[ws.cell(r, c).value for c in range(1, max_c + 1)] for r in range(1, max_r + 1)]
    for rng in ws.merged_cells.ranges:
        min_col, min_row, max_col, max_row = rng.bounds
        top_val = ws.cell(min_row, min_col).value
        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if grid[r - 1][c - 1] is None:
                    grid[r - 1][c - 1] = top_val
    return grid

def extract_all_data():
    print("Iniciando extracción bilingüe desde:", EXCEL_PATH)
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    all_data = {
        "models": [],
        "total_rows_extracted": 0,
        "total_cards": 0,
    }

    total_rows = 0

    for sheet_name, cfg in SHEET_CONFIGS.items():
        if sheet_name not in wb.sheetnames:
            print(f"Alerta: Hoja '{sheet_name}' no encontrada en Excel")
            continue

        ws = wb[sheet_name]
        grid = get_grid_with_merged_cells(ws)

        sheet_rows = []
        current_cat_bilingual = {"es": "General", "en": "General"}

        for r_idx, row_cells in enumerate(grid):
            r_num = r_idx + 1
            c1_raw = clean_cell_text(row_cells[0]) if len(row_cells) > 0 else ""
            c2_raw = clean_cell_text(row_cells[1]) if len(row_cells) > 1 else ""
            c3_raw = clean_cell_text(row_cells[2]) if len(row_cells) > 2 else ""

            # Actualizar categoría
            if c1_raw and c1_raw.lower() != "none" and not c1_raw.startswith("Note:"):
                current_cat_bilingual = get_bilingual(c1_raw)

            has_data = any(row_cells[c] is not None and clean_cell_text(row_cells[c]) != "" for c in range(len(row_cells)))
            if not has_data:
                continue

            param_raw = c2_raw if c2_raw else c1_raw
            param_bilingual = get_bilingual(param_raw)
            subparam_bilingual = get_bilingual(c3_raw) if c3_raw else {"es": "", "en": ""}

            values_es = {}
            values_en = {}

            for v in cfg["versions"]:
                v_idx = v["col_idx"]
                raw_val = clean_cell_text(row_cells[v_idx]) if v_idx < len(row_cells) else ""
                val_bi = get_bilingual(raw_val)
                values_es[v["id"]] = val_bi["es"] if val_bi["es"] else "-"
                values_en[v["id"]] = val_bi["en"] if val_bi["en"] else "-"

            row_record = {
                "row_num": r_num,
                "category": current_cat_bilingual,
                "param_name": param_bilingual,
                "subparam_name": subparam_bilingual,
                "values": {
                    "es": values_es,
                    "en": values_en,
                },
            }
            sheet_rows.append(row_record)

        total_rows += len(sheet_rows)

        model_obj = {
            "key": cfg["model_key"],
            "sheet_name": clean_cjk(sheet_name),
            "name": cfg["model_name"],
            "category": cfg["category"],
            "vehicle_type": cfg["vehicle_type"],
            "fuel_badge": cfg["fuel_badge"],
            "total_sheet_rows": len(sheet_rows),
            "rows": sheet_rows,
            "cards": [],
        }

        # Construir tarjetas de cada versión
        for v in cfg["versions"]:
            v_id = v["id"]

            dim_caps = []
            powertrain = []
            chassis_safety = []
            equipment = []

            # Organizar categorías completas
            categories_dict = {}

            for r in sheet_rows:
                val_es = r["values"]["es"].get(v_id, "-")
                val_en = r["values"]["en"].get(v_id, "-")

                # Label bilingüe
                label_es = r["param_name"]["es"]
                if r["subparam_name"]["es"] and r["subparam_name"]["es"] != label_es:
                    label_es += f" ({r['subparam_name']['es']})"

                label_en = r["param_name"]["en"]
                if r["subparam_name"]["en"] and r["subparam_name"]["en"] != label_en:
                    label_en += f" ({r['subparam_name']['en']})"

                cat_key = r["category"]["es"]
                if cat_key not in categories_dict:
                    categories_dict[cat_key] = {
                        "category_name": r["category"],
                        "specs": [],
                    }

                spec_entry = {
                    "row_num": r["row_num"],
                    "param_name": r["param_name"],
                    "subparam_name": r["subparam_name"],
                    "label": {"es": label_es, "en": label_en},
                    "value": {"es": val_es, "en": val_en},
                }
                categories_dict[cat_key]["specs"].append(spec_entry)

                # Clasificación para bloques de resumen superior
                summary_item = {
                    "row": r["row_num"],
                    "label": {"es": label_es, "en": label_en},
                    "value": {"es": val_es, "en": val_en},
                }

                cat_lower = (r["category"]["en"] + " " + r["category"]["es"]).lower()
                param_lower = (label_en + " " + label_es).lower()

                if any(k in cat_lower or k in param_lower for k in [
                    "dimension", "largo", "ancho", "alto", "wheelbase", "ejes", "tread", "rodcha",
                    "cargo", "tolva", "clearance", "despeje", "turning radius", "giro",
                    "weight", "peso", "g.v.w", "curb", "payload", "carga", "fuel tank", "tanque",
                    "approach", "entrada", "salida", "gradeability", "seat", "asiento", "door", "puerta"
                ]):
                    dim_caps.append(summary_item)
                elif any(k in cat_lower or k in param_lower for k in [
                    "engine", "motor", "displacement", "cilindrada", "power", "potencia", "torque",
                    "fuel", "combustible", "transmission", "transmisión", "caja", "emission", "emisiones",
                    "speed", "velocidad", "intake", "aspiración", "energy", "dht", "phev", "hybrid", "híbrido"
                ]):
                    powertrain.append(summary_item)
                elif any(k in cat_lower or k in param_lower for k in [
                    "brake", "freno", "suspension", "suspensión", "drive", "tracción",
                    "safety", "seguridad", "airbag", "tyre", "tire", "neumático", "rim", "llanta",
                    "steering", "dirección", "abs", "esp", "esc", "tpms", "radar", "camera", "cámara"
                ]):
                    chassis_safety.append(summary_item)
                else:
                    equipment.append(summary_item)

            all_categories_list = list(categories_dict.values())

            card_obj = {
                "id": v_id,
                "badge_id": v["badge_id"],
                "model_key": cfg["model_key"],
                "model_name": cfg["model_name"],
                "title": v["title"],
                "subtitle": v["subtitle"],
                "fuel_badge": v["fuel_badge"],
                "tag": v["tag"],
                "category": cfg["category"],
                "vehicle_type": cfg["vehicle_type"],
                "highlights": v["highlights"],
                "summary_blocks": {
                    "dimensions": dim_caps[:7],
                    "powertrain": powertrain[:7],
                    "chassis_safety": chassis_safety[:7],
                    "equipment": equipment[:7],
                },
                "all_categories": all_categories_list,
                "total_specs_count": sum(len(c["specs"]) for c in all_categories_list),
            }
            model_obj["cards"].append(card_obj)
            all_data["total_cards"] += 1

        all_data["models"].append(model_obj)

    all_data["total_rows_extracted"] = total_rows
    print(f"Extracción finalizada: {total_rows} filas procesadas en {all_data['total_cards']} tarjetas.")

    # Guardar JSON garantizando 0 caracteres chinos
    with open(JSON_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    print("Archivo JSON guardado con éxito en:", JSON_OUTPUT_PATH)

    return all_data

if __name__ == "__main__":
    extract_all_data()
