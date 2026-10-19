# -*- coding: utf-8 -*-
"""Compila los 13 modelos unificando data_models_meta, data_sheet1 y data_sheet2."""

import json
from data_models_meta import TARGET_MODELS_BASE
from data_sheet1 import get_sheet1_sections
from data_sheet2 import get_sheet2_sections

def assemble_all():
    models = []
    for base in TARGET_MODELS_BASE:
        cid = base["id"]
        tab = base["tab"]
        s1 = get_sheet1_sections(cid, tab)
        s2 = get_sheet2_sections(cid, tab)
        
        m_full = {
            **base,
            "s1": s1,
            "s2": s2
        }
        models.append(m_full)

    with open('fichas_ready.json', 'w', encoding='utf-8') as f:
        json.dump(models, f, ensure_ascii=False, indent=2)
    print(f"Ensamblados exitosamente {len(models)} modelos en fichas_ready.json")

if __name__ == '__main__':
    assemble_all()
