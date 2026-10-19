import json
import re

def clean_txt(t):
    if not t or t in ['-', 'None', 'undefined']:
        return "No especificado en ficha de origen"
    t = str(t).strip()
    return t

def build_data():
    with open('especificaciones_data.json', 'r', encoding='utf-8') as f:
        raw = json.load(f)

    # 13 target models
    target_models = [
        {"id": "Z16A", "tab": "Z9 Comercial 4WD MT (Z16A)", "name": "DONGFENG Z9 COMERCIAL · 4WD MT", "model": "Z9", "version": "Z16A Comercial 4WD MT", "traction": "4WD (Doble Tracción 4x4)", "badge": "12 TON PICK-UP", "tipo": "Pick-up Comercial Doble Cabina", "marca": "DONGFENG"},
        {"id": "Z20A", "tab": "Z9 Comercial 4WD AT (Z20A)", "name": "DONGFENG Z9 COMERCIAL · 4WD AT", "model": "Z9", "version": "Z20A Comercial 4WD 8AT", "traction": "4WD (Doble Tracción 4x4)", "badge": "HEAVY DUTY 8AT", "tipo": "Pick-up Comercial Doble Cabina", "marca": "DONGFENG"},
        {"id": "Z42A", "tab": "Z9 Passenger 4WD 8AT (Z42A)", "name": "DONGFENG Z9 PASSENGER · 4WD 8AT", "model": "Z9 Passenger", "version": "Z42A Euro 6 High Spec", "traction": "4WD Inteligente con Modos", "badge": "PREMIUM PASSENGER", "tipo": "Pick-up Pasajeros Doble Cabina Confort", "marca": "DONGFENG"},
        {"id": "X21B", "tab": "Z9 Hybrid PHEV 4WD (X21B)", "name": "DONGFENG Z9 P20 HYBRID PHEV · 4WD", "model": "Z9 Hybrid PHEV", "version": "X21B P20 PHEV 135KM UPR", "traction": "4WD Eléctrico Híbrido 4DHT", "badge": "PHEV 800 Nm TORQUE", "tipo": "Pick-up Híbrida Enchufable (PHEV)", "marca": "DONGFENG"},
        {"id": "Z11A", "tab": "Rich 6 4x2 5MT (Z11A)", "name": "DONGFENG RICH 6 · 4X2 5MT", "model": "Rich 6", "version": "Z11A Doble Cabina Gasolina 2.4L", "traction": "4x2 (Tracción Trasera 2WD)", "badge": "PLATAFORMA NISSAN", "tipo": "Pick-up Utilitaria de Carga Doble Cabina", "marca": "DONGFENG"},
        {"id": "Z22A", "tab": "Rich 6 4x4 5MT (Z22A)", "name": "DONGFENG RICH 6 · 4X4 5MT", "model": "Rich 6", "version": "Z22A Doble Cabina Off-Road 2.4L", "traction": "4x4 (Doble Tracción con Reductora)", "badge": "OFF-ROAD REFORZADA", "tipo": "Pick-up Todo Terreno Doble Cabina", "marca": "DONGFENG"},
        {"id": "Y38G", "tab": "Rich 6 PRO 4x4 8AT (Y38G)", "name": "DONGFENG RICH 6 PRO NUEVO · 4X4 8AT", "model": "Rich 6 PRO", "version": "Y38G Turbo 2.0T Automática 8AT", "traction": "4x4 (Tracción Integral 4WD)", "badge": "TURBO MITSUBISHI 8AT", "tipo": "Pick-up Alta Potencia Doble Cabina", "marca": "DONGFENG"},
        {"id": "Y38E", "tab": "Rich 6 PRO 4x4 6MT (Y38E)", "name": "DONGFENG RICH 6 PRO NUEVO · 4X4 6MT", "model": "Rich 6 PRO", "version": "Y38E Turbo 2.0T Manual 6MT", "traction": "4x4 (Tracción Integral 4WD)", "badge": "TURBO 360 Nm 6MT", "tipo": "Pick-up Alta Potencia Doble Cabina", "marca": "DONGFENG"},
        {"id": "W91A", "tab": "Paladin 4x2 8AT (W91A)", "name": "DONGFENG PALADIN SUV · 4X2 8AT", "model": "Paladin SUV", "version": "W91A STD 2.0TD Automática 8AT", "traction": "4x2 (Tracción Trasera RWD)", "badge": "SUV CHASIS ESCALERA", "tipo": "SUV Todoterreno Chasis Independiente", "marca": "DONGFENG"},
        {"id": "W92B", "tab": "Paladin 4x4 8AT (W92B)", "name": "DONGFENG PALADIN SUV · 4X4 8AT (MID)", "model": "Paladin SUV", "version": "W92B MID 4WD Automática 8AT", "traction": "4x4 (Tracción 4WD con Modos)", "badge": "SUV OFF-ROAD 4X4", "tipo": "SUV Todoterreno Chasis Independiente", "marca": "DONGFENG"},
        {"id": "W92C", "tab": "Paladin 4x4 8AT ADAS (W92C)", "name": "DONGFENG PALADIN SUV · 4X4 8AT (ADAS UPR)", "model": "Paladin SUV", "version": "W92C UPR 4WD Flagship con ADAS", "traction": "4x4 (Tracción 4WD con Bloqueo)", "badge": "FLAGSHIP LUXURY 4X4", "tipo": "SUV Todoterreno Premium con ADAS", "marca": "DONGFENG"},
        {"id": "T5-LUX", "tab": "T5 EVO Luxury 7DCT (T5-LUX)", "name": "FORTHING T5 EVO · 1.5TD LUXURY 7DCT", "model": "T5 EVO", "version": "1.5TD Luxury Doble Embrague 7DCT", "traction": "FWD (Tracción Delantera)", "badge": "SPORT SUV 195 HP", "tipo": "SUV Deportivo Urbano Compacto", "marca": "FORTHING / DONGFENG"},
        {"id": "T5-EXC", "tab": "T5 EVO Exclusive 7DCT (T5-EXC)", "name": "FORTHING T5 EVO · 1.5TD EXCLUSIVE 7DCT", "model": "T5 EVO", "version": "1.5TD Exclusive ADAS 7DCT", "traction": "FWD (Tracción Delantera)", "badge": "EXCLUSIVE ADAS TECH", "tipo": "SUV Deportivo de Alta Gama con ADAS", "marca": "FORTHING / DONGFENG"}
    ]

    # Map cards
    card_map = {}
    for m in raw['models']:
        for r in m.get('rows', []):
            cat = r['category']['es']
            p = r['param_name']['es']
            for cid, val in r['values']['es'].items():
                if cid not in card_map:
                    card_map[cid] = {}
                k = f"{cat}::{p}".strip()
                if val not in ['-', 'None', '']:
                    card_map[cid][k] = val

    out_models = []
    for tm in target_models:
        cid = tm["id"]
        specs = card_map.get(cid, {})
        m_item = {**tm, "specs": specs}
        out_models.append(m_item)

    with open('fichas_parsed.json', 'w', encoding='utf-8') as f:
        json.dump(out_models, f, ensure_ascii=False, indent=2)
    print(f"Generated fichas_parsed.json with {len(out_models)} vehicles.")

if __name__ == '__main__':
    build_data()
