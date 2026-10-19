# -*- coding: utf-8 -*-
"""Definición base de metadatos, cotas y dimensiones de los 13 modelos."""

TARGET_MODELS_BASE = [
    {
        "id": "Z16A", "tab": "Z9 Comercial 4WD MT (Z16A)",
        "title_h1": "DONGFENG Z9 COMERCIAL · 4WD MT", "title_h2": "DONGFENG Z9 COMERCIAL",
        "vehiculo": "Pick-up Comercial Doble Cabina", "marca": "DONGFENG", "modelo": "Z9 Comercial",
        "version": "Z16A (Euro 6 4WD MT)", "traccion": "4WD (Tracción 4x4 Manual)",
        "badge_text": "12 TON PICK-UP", "badge_sub": "COMERCIAL 4WD MT",
        "diagram_label": "Z9 4WD (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.300 mm (Distancia entre ejes)", "B": "1.310 mm (Voladizo trasero con tolva)",
            "C": "5.520 mm (Longitud total de carrocería)", "D": "910 mm (Eje delantero a cabina)",
            "E": "1.100 mm (Altura plataforma de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.650 mm (Ancho de vía delantera / trasera)", "H": "1.950 mm (Altura total de vehículo)",
            "I": "1.520 mm (Largo útil de compartimiento de carga)"
        },
        "extra_dim": {
            "longitud": "5.520 mm", "ancho": "1.960 mm", "alto": "1.950 mm",
            "distancia_ejes": "3.300 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.310 mm",
            "despeje": "240 mm (sin carga) / 209 mm (con carga)", "radio_giro": "6.75 m"
        }
    },
    {
        "id": "Z20A", "tab": "Z9 Comercial 4WD AT (Z20A)",
        "title_h1": "DONGFENG Z9 COMERCIAL · 4WD AT", "title_h2": "DONGFENG Z9 COMERCIAL",
        "vehiculo": "Pick-up Comercial Doble Cabina", "marca": "DONGFENG", "modelo": "Z9 Comercial",
        "version": "Z20A (Euro 6 4WD 8AT)", "traccion": "4WD (Tracción 4x4 Automática)",
        "badge_text": "HEAVY DUTY 8AT", "badge_sub": "COMERCIAL 4WD AT",
        "diagram_label": "Z9 4WD 8AT (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.300 mm (Distancia entre ejes)", "B": "1.310 mm (Voladizo trasero)",
            "C": "5.520 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.100 mm (Altura plataforma de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.650 mm (Trocha Delantera / Trasera)", "H": "1.950 mm (Altura total)",
            "I": "1.520 mm (Largo interior tolva)"
        },
        "extra_dim": {
            "longitud": "5.520 mm", "ancho": "1.960 mm", "alto": "1.950 mm",
            "distancia_ejes": "3.300 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.310 mm",
            "despeje": "240 mm / 209 mm", "radio_giro": "6.75 m"
        }
    },
    {
        "id": "Z42A", "tab": "Z9 Passenger 4WD 8AT (Z42A)",
        "title_h1": "DONGFENG Z9 PASSENGER · 4WD 8AT", "title_h2": "DONGFENG Z9 PASSENGER",
        "vehiculo": "Pick-up Doble Cabina de Pasajeros", "marca": "DONGFENG", "modelo": "Z9 Passenger",
        "version": "Z42A (High Confort Euro 6)", "traccion": "4WD Inteligente con Modos",
        "badge_text": "PREMIUM PASSENGER", "badge_sub": "LUXURY PICK-UP 4WD",
        "diagram_label": "Z9 PASSENGER 4WD (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.300 mm (Distancia entre ejes)", "B": "1.310 mm (Voladizo trasero con paragolpes)",
            "C": "5.520 mm (Longitud total)", "D": "910 mm (Eje delantero a cabina)",
            "E": "1.080 mm (Altura piso de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.650 mm (Vía Delantera / Trasera)", "H": "1.950 mm (Altura total)",
            "I": "1.520 mm (Largo tolva de carga)"
        },
        "extra_dim": {
            "longitud": "5.520 mm", "ancho": "1.960 mm", "alto": "1.950 mm",
            "distancia_ejes": "3.300 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.310 mm",
            "despeje": "240 mm / 224 mm", "radio_giro": "6.75 m"
        }
    },
    {
        "id": "X21B", "tab": "Z9 Hybrid PHEV 4WD (X21B)",
        "title_h1": "DONGFENG Z9 HYBRID PHEV · 4WD", "title_h2": "DONGFENG Z9 HYBRID PHEV",
        "vehiculo": "Pick-up Híbrida Enchufable (PHEV)", "marca": "DONGFENG", "modelo": "Z9 P20 PHEV",
        "version": "X21B (PHEV 135KM UPR 4DHT)", "traccion": "4WD Eléctrico Híbrido Avanzado",
        "badge_text": "PHEV 800 Nm TORQUE", "badge_sub": "135 KM EV RANGE",
        "diagram_label": "Z9 HYBRID PHEV (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.300 mm (Distancia entre ejes)", "B": "1.310 mm (Voladizo trasero)",
            "C": "5.520 mm (Longitud exterior)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.090 mm (Altura plataforma de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.650 mm (Ancho de vía)", "H": "1.950 mm (Altura exterior)",
            "I": "1.520 mm (Largo compartimiento tolva)"
        },
        "extra_dim": {
            "longitud": "5.520 mm", "ancho": "1.960 mm", "alto": "1.950 mm",
            "distancia_ejes": "3.300 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.310 mm",
            "despeje": "243 mm / 232 mm", "radio_giro": "13.5 m (diámetro)"
        }
    },
    {
        "id": "Z11A", "tab": "Rich 6 4x2 5MT (Z11A)",
        "title_h1": "DONGFENG RICH 6 · 4X2 5MT", "title_h2": "DONGFENG RICH 6",
        "vehiculo": "Pick-up Utilitaria de Carga Doble Cabina", "marca": "DONGFENG", "modelo": "Rich 6",
        "version": "Z11A (Gasolina 2.4L 2WD 5MT)", "traccion": "4x2 (Tracción Trasera 2WD)",
        "badge_text": "PLATAFORMA NISSAN", "badge_sub": "UTILITARIA 2.4L 5MT",
        "diagram_label": "RICH 6 4X2 (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.150 mm (Distancia entre ejes)", "B": "1.230 mm (Voladizo trasero)",
            "C": "5.290 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.050 mm (Altura piso de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Trocha Delantera / Trasera)", "H": "1.810 mm (1.850 mm con rieles)",
            "I": "1.510 mm (Largo de tolva)"
        },
        "extra_dim": {
            "longitud": "5.290 mm", "ancho": "1.850 mm", "alto": "1.810 mm",
            "distancia_ejes": "3.150 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.230 mm",
            "despeje": "207 mm", "radio_giro": "6.4 m"
        }
    },
    {
        "id": "Z22A", "tab": "Rich 6 4x4 5MT (Z22A)",
        "title_h1": "DONGFENG RICH 6 · 4X4 5MT", "title_h2": "DONGFENG RICH 6",
        "vehiculo": "Pick-up Todo Terreno Doble Cabina", "marca": "DONGFENG", "modelo": "Rich 6",
        "version": "Z22A (Gasolina 2.4L 4WD 5MT)", "traccion": "4x4 (Tracción 4WD con Reductora)",
        "badge_text": "OFF-ROAD REFORZADA", "badge_sub": "DOBLE TRACCIÓN 4X4",
        "diagram_label": "RICH 6 4X4 (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.150 mm (Distancia entre ejes)", "B": "1.230 mm (Voladizo trasero)",
            "C": "5.290 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.060 mm (Altura tolva al piso)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Trocha Delantera / Trasera)", "H": "1.810 mm",
            "I": "1.510 mm (Largo de tolva)"
        },
        "extra_dim": {
            "longitud": "5.290 mm", "ancho": "1.850 mm", "alto": "1.810 mm",
            "distancia_ejes": "3.150 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.230 mm",
            "despeje": "207 mm", "radio_giro": "6.4 m"
        }
    },
    {
        "id": "Y38G", "tab": "Rich 6 PRO 4x4 8AT (Y38G)",
        "title_h1": "DONGFENG RICH 6 PRO · 4X4 8AT", "title_h2": "DONGFENG RICH 6 PRO",
        "vehiculo": "Pick-up Alta Potencia Doble Cabina", "marca": "DONGFENG", "modelo": "Rich 6 PRO Nuevo",
        "version": "Y38G Turbo (2.0TD 168 kW 8AT)", "traccion": "4x4 (Tracción Integral 4WD)",
        "badge_text": "TURBO MITSUBISHI 8AT", "badge_sub": "360 Nm · 8 SPEED AT",
        "diagram_label": "RICH 6 PRO 8AT (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.150 mm (Distancia entre ejes)", "B": "1.250 mm (Voladizo trasero)",
            "C": "5.310 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.060 mm (Altura tolva al piso)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Ancho de vía F/R)", "H": "1.810 mm",
            "I": "1.510 mm (Largo interior tolva)"
        },
        "extra_dim": {
            "longitud": "5.310 mm", "ancho": "1.850 mm", "alto": "1.810 mm",
            "distancia_ejes": "3.150 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.250 mm",
            "despeje": "207 mm", "radio_giro": "6.4 m"
        }
    },
    {
        "id": "Y38E", "tab": "Rich 6 PRO 4x4 6MT (Y38E)",
        "title_h1": "DONGFENG RICH 6 PRO · 4X4 6MT", "title_h2": "DONGFENG RICH 6 PRO",
        "vehiculo": "Pick-up Alta Potencia Doble Cabina", "marca": "DONGFENG", "modelo": "Rich 6 PRO Nuevo",
        "version": "Y38E Turbo (2.0TD 168 kW 6MT)", "traccion": "4x4 (Tracción Integral 4WD)",
        "badge_text": "TURBO 360 Nm 6MT", "badge_sub": "2.0TD MANUAL 6 VEL",
        "diagram_label": "RICH 6 PRO 6MT (DIMENSIONES EN MM)",
        "cotas": {
            "A": "3.150 mm (Distancia entre ejes)", "B": "1.250 mm (Voladizo trasero)",
            "C": "5.310 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "1.060 mm (Altura piso de carga)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Vía delantera y trasera)", "H": "1.810 mm",
            "I": "1.510 mm (Largo de tolva)"
        },
        "extra_dim": {
            "longitud": "5.310 mm", "ancho": "1.850 mm", "alto": "1.810 mm",
            "distancia_ejes": "3.150 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.250 mm",
            "despeje": "207 mm", "radio_giro": "6.4 m"
        }
    },
    {
        "id": "W91A", "tab": "Paladin 4x2 8AT (W91A)",
        "title_h1": "DONGFENG PALADIN SUV · 4X2 8AT", "title_h2": "DONGFENG PALADIN SUV",
        "vehiculo": "SUV Todoterreno con Chasis de Escalera", "marca": "DONGFENG", "modelo": "Paladin SUV",
        "version": "W91A STD (2.0TD Turbo 8AT)", "traccion": "4x2 (Tracción Trasera RWD)",
        "badge_text": "SUV CHASIS ESCALERA", "badge_sub": "CONFORT URBANO 8AT",
        "diagram_label": "PALADIN SUV 4X2 (DIMENSIONES EN MM)",
        "cotas": {
            "A": "2.850 mm (Distancia entre ejes)", "B": "1.122 mm (Voladizo trasero)",
            "C": "4.882 mm (Longitud total exterior)", "D": "910 mm (Eje frontal a cabina)",
            "E": "850 mm (Altura umbral maletero)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Trocha F/R)", "H": "1.875 mm (Altura total con barras)",
            "I": "1.100 mm (Profundidad de maletero)"
        },
        "extra_dim": {
            "longitud": "4.882 mm", "ancho": "1.850 mm", "alto": "1.875 mm",
            "distancia_ejes": "2.850 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.122 mm",
            "despeje": "215 mm", "radio_giro": "5.7 m"
        }
    },
    {
        "id": "W92B", "tab": "Paladin 4x4 8AT (W92B)",
        "title_h1": "DONGFENG PALADIN SUV · 4X4 8AT", "title_h2": "DONGFENG PALADIN SUV",
        "vehiculo": "SUV Todoterreno con Chasis Independiente", "marca": "DONGFENG", "modelo": "Paladin SUV",
        "version": "W92B MID (2.0TD Turbo 4WD 8AT)", "traccion": "4x4 (Tracción 4WD con Modos)",
        "badge_text": "SUV OFF-ROAD 4X4", "badge_sub": "TODO TERRENO MID 8AT",
        "diagram_label": "PALADIN SUV 4X4 MID (DIMENSIONES EN MM)",
        "cotas": {
            "A": "2.850 mm (Distancia entre ejes)", "B": "1.122 mm (Voladizo trasero)",
            "C": "4.882 mm (Longitud total exterior)", "D": "910 mm (Eje frontal a cabina)",
            "E": "850 mm (Altura piso maletero)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Trocha Delantera/Trasera)", "H": "1.875 mm",
            "I": "1.100 mm (Profundidad de maletero)"
        },
        "extra_dim": {
            "longitud": "4.882 mm", "ancho": "1.850 mm", "alto": "1.875 mm",
            "distancia_ejes": "2.850 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.122 mm",
            "despeje": "215 mm", "radio_giro": "5.7 m"
        }
    },
    {
        "id": "W92C", "tab": "Paladin 4x4 8AT ADAS (W92C)",
        "title_h1": "DONGFENG PALADIN SUV · 4X4 8AT ADAS", "title_h2": "DONGFENG PALADIN SUV",
        "vehiculo": "SUV Todoterreno Premium con Asistencias ADAS", "marca": "DONGFENG", "modelo": "Paladin SUV",
        "version": "W92C UPR (Flagship 4WD ADAS)", "traccion": "4x4 (4WD con Bloqueo de Diferencial Trasero)",
        "badge_text": "FLAGSHIP LUXURY 4X4", "badge_sub": "PANTALLA 12'' & ADAS",
        "diagram_label": "PALADIN SUV 4X4 FLAGSHIP (DIMENSIONES EN MM)",
        "cotas": {
            "A": "2.850 mm (Distancia entre ejes)", "B": "1.122 mm (Voladizo trasero)",
            "C": "4.882 mm (Longitud total)", "D": "910 mm (Eje frontal a cabina)",
            "E": "850 mm (Altura piso maletero)", "F": "910 mm (Voladizo delantero)",
            "G": "1.570 mm (Trocha Delantera/Trasera)", "H": "1.875 mm",
            "I": "1.100 mm (Profundidad maletero)"
        },
        "extra_dim": {
            "longitud": "4.882 mm", "ancho": "1.850 mm", "alto": "1.875 mm",
            "distancia_ejes": "2.850 mm", "voladizo_del": "910 mm", "voladizo_tras": "1.122 mm",
            "despeje": "215 mm", "radio_giro": "5.7 m"
        }
    },
    {
        "id": "T5-LUX", "tab": "T5 EVO Luxury 7DCT (T5-LUX)",
        "title_h1": "FORTHING T5 EVO · 1.5TD LUXURY 7DCT", "title_h2": "FORTHING T5 EVO",
        "vehiculo": "SUV Deportivo Compacto de Alta Gama", "marca": "FORTHING (DONGFENG)", "modelo": "T5 EVO",
        "version": "1.5TD Luxury (Doble Embrague 7DCT)", "traccion": "FWD (Tracción Delantera)",
        "badge_text": "SPORT SUV 195 HP", "badge_sub": "MITSUBISHI 4A95TD",
        "diagram_label": "T5 EVO SPORT SUV (DIMENSIONES EN MM)",
        "cotas": {
            "A": "2.715 mm (Distancia entre ejes)", "B": "960 mm (Voladizo trasero)",
            "C": "4.565 mm (Longitud total exterior)", "D": "890 mm (Eje frontal al mamparo)",
            "E": "740 mm (Altura piso maletero)", "F": "890 mm (Voladizo delantero)",
            "G": "1.590 mm (Trocha delantera / trasera)", "H": "1.690 mm (Altura deportiva)",
            "I": "920 mm (Profundidad piso maletero)"
        },
        "extra_dim": {
            "longitud": "4.565 mm", "ancho": "1.860 mm", "alto": "1.690 mm",
            "distancia_ejes": "2.715 mm", "voladizo_del": "890 mm", "voladizo_tras": "960 mm",
            "despeje": "195 mm", "radio_giro": "5.4 m"
        }
    },
    {
        "id": "T5-EXC", "tab": "T5 EVO Exclusive 7DCT (T5-EXC)",
        "title_h1": "FORTHING T5 EVO · 1.5TD EXCLUSIVE 7DCT", "title_h2": "FORTHING T5 EVO",
        "vehiculo": "SUV Deportivo Tecnológico con ADAS", "marca": "FORTHING (DONGFENG)", "modelo": "T5 EVO",
        "version": "1.5TD Exclusive (ADAS L2+ 7DCT)", "traccion": "FWD (Tracción Delantera)",
        "badge_text": "EXCLUSIVE ADAS TECH", "badge_sub": "SEGURIDAD ACTIVA L2+",
        "diagram_label": "T5 EVO EXCLUSIVE (DIMENSIONES EN MM)",
        "cotas": {
            "A": "2.715 mm (Distancia entre ejes)", "B": "960 mm (Voladizo trasero)",
            "C": "4.565 mm (Longitud total)", "D": "890 mm (Eje frontal al mamparo)",
            "E": "740 mm (Altura piso maletero)", "F": "890 mm (Voladizo delantero)",
            "G": "1.590 mm (Trocha delantera / trasera)", "H": "1.690 mm",
            "I": "920 mm (Profundidad piso maletero)"
        },
        "extra_dim": {
            "longitud": "4.565 mm", "ancho": "1.860 mm", "alto": "1.690 mm",
            "distancia_ejes": "2.715 mm", "voladizo_del": "890 mm", "voladizo_tras": "960 mm",
            "despeje": "195 mm", "radio_giro": "5.4 m"
        }
    }
]
