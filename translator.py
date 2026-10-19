"""
Módulo de traducción y limpieza CJK (Separación de responsabilidades).
Carga el diccionario maestro cjk_translations.json y asegura 0 caracteres chinos.
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICT_PATH = os.path.join(BASE_DIR, "cjk_translations.json")

CJK_REGEX = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]")

_TRANSLATIONS = {}
if os.path.exists(DICT_PATH):
    with open(DICT_PATH, "r", encoding="utf-8") as f:
        _TRANSLATIONS = json.load(f)

def clean_brackets(s):
    if not s:
        return ""
    s = str(s).replace("（", "(").replace("）", ")").replace("【", "[").replace("】", "]")
    s = s.replace("：", ": ").replace("；", "; ").replace("，", ", ").replace("、", ", ")
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = s.replace("　", " ").replace("—", "-").replace("～", "~").replace("－", "-")
    return s


def clean_cjk(text):
    if not text:
        return ""
    text_clean = clean_brackets(text)
    no_cjk = CJK_REGEX.sub("", text_clean)
    no_cjk = re.sub(r"\s+", " ", no_cjk).strip(" :;,-_/")
    return no_cjk

def get_bilingual(text):
    """
    Retorna diccionario {'es': ..., 'en': ...} 100% libre de caracteres CJK.
    """
    if text is None:
        return {"es": "", "en": ""}
    
    raw = str(text).strip()
    if not raw:
        return {"es": "", "en": ""}
    
    # 1. Si no tiene caracteres chinos ni símbolos CJK, retornarlo tal cual
    if not CJK_REGEX.search(raw):
        clean_val = clean_brackets(raw).strip()
        return {"es": clean_val, "en": clean_val}
    
    # 2. Buscar en diccionario exacto
    if raw in _TRANSLATIONS:
        entry = _TRANSLATIONS[raw]
        return {
            "es": clean_cjk(entry["es"]),
            "en": clean_cjk(entry["en"])
        }
    
    # 3. Normalizado
    norm = clean_brackets(raw).strip()
    if norm in _TRANSLATIONS:
        entry = _TRANSLATIONS[norm]
        return {
            "es": clean_cjk(entry["es"]),
            "en": clean_cjk(entry["en"])
        }
    
    # 4. Fallback seguro: remover CJK y balancear
    fallback = clean_cjk(raw)
    if not fallback:
        fallback = "Not specified"
    return {"es": fallback, "en": fallback}

def translate_text(text, target_lang="es"):
    bilingual = get_bilingual(text)
    return bilingual.get(target_lang, bilingual["es"])
