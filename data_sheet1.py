# -*- coding: utf-8 -*-
"""Generador de secciones técnicas de la Hoja 1 para cada modelo."""

def get_sheet1_sections(cid, tab_name):
    # 1. MOTOR
    if cid in ["Z16A", "Z20A"]:
        motor = [
            ("Tipo", "4K31 / Gasolina 2.0 Turbo"),
            ("Admisión", "Turbo con intercooler de alta eficiencia"),
            ("Inyección", "Inyección directa GDI a alta presión"),
            ("Número de cilindros", "4 cilindros en línea, 16 válvulas DOHC"),
            ("Cilindrada", "2.0 L (1.997 cc)"),
            ("Potencia", "190 kW (255 HP) @ 5.500 rpm"),
            ("Torque", "400 Nm @ 1.800 - 3.500 rpm"),
            ("Norma de emisión", "Euro VI / Euro 6")
        ]
    elif cid == "Z42A":
        motor = [
            ("Tipo", "4K31TD / Gasolina 2.0 Turbo Premium"),
            ("Admisión", "Turbo intercooler de doble flujo"),
            ("Inyección", "Inyección directa GDI"),
            ("Número de cilindros", "4 cilindros en línea DOHC"),
            ("Cilindrada", "2.0 L (1.997 cc)"),
            ("Potencia", "190 kW (255 HP) @ 5.500 rpm"),
            ("Torque", "400 Nm @ 1.800 - 3.500 rpm"),
            ("Norma de emisión", "Euro 6b")
        ]
    elif cid == "X21B":
        motor = [
            ("Tipo", "PHEV Híbrido Enchufable / Motor 2.0T + Dual EV"),
            ("Admisión", "Turbo intercooler naftero + Módulos eléctricos"),
            ("Inyección", "Inyección directa GDI de alta precisión"),
            ("Potencia combinada", "240 kW (322 HP)"),
            ("Torque combinado", "800 Nm de par instantáneo"),
            ("Batería de tracción", "Iones de litio de alta capacidad"),
            ("Carga rápida", "46 min (DC Carga Rápida)"),
            ("Norma de emisión", "Euro 6d / Cero Emisiones (Modo EV)")
        ]
    elif cid in ["Z11A", "Z22A"]:
        motor = [
            ("Tipo", "2TZD / Gasolina aspirado 2.4L"),
            ("Admisión", "Aspiración natural de flujo transversal"),
            ("Inyección", "Inyección electrónica multipunto secuencial"),
            ("Número de cilindros", "4 cilindros en línea, 16 válvulas"),
            ("Cilindrada", "2.4 L (2.438 cc)"),
            ("Potencia", "116 kW (156 HP) @ 4.800 rpm"),
            ("Torque", "230 Nm @ 2.600 - 3.200 rpm"),
            ("Norma de emisión", "Euro 4 / Euro 5")
        ]
    elif cid in ["Y38G", "Y38E"]:
        motor = [
            ("Tipo", "Mitsubishi 4K31TD / 2.0 Turbo"),
            ("Admisión", "Turbocompresor con intercooler"),
            ("Inyección", "Inyección directa estratificada GDI"),
            ("Número de cilindros", "4 cilindros en línea DOHC"),
            ("Cilindrada", "2.0 L (1.997 cc)"),
            ("Potencia", "168 kW (225 HP) @ 5.600 rpm"),
            ("Torque", "360 Nm @ 1.400 - 4.000 rpm"),
            ("Norma de emisión", "Euro 5 / Euro 6")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        motor = [
            ("Tipo", "Mitsubishi 4K31 2.0TD / Turbo"),
            ("Admisión", "Turbocompresor de geometría avanzada"),
            ("Inyección", "Inyección directa GDI a alta presión"),
            ("Número de cilindros", "4 cilindros en línea DOHC 16V"),
            ("Cilindrada", "2.0 L (1.997 cc)"),
            ("Potencia", "168 kW (225 HP) @ 5.600 rpm"),
            ("Torque", "360 Nm @ 1.400 - 4.000 rpm"),
            ("Norma de emisión", "Euro 5 / Euro 6")
        ]
    else:  # T5-LUX, T5-EXC
        motor = [
            ("Tipo", "Shenyang Mitsubishi 4A95TD / 1.5TD"),
            ("Admisión", "Turbocharger con intercooler frontal"),
            ("Inyección", "Inyección directa GDI + DVVT"),
            ("Número de cilindros", "4 cilindros en línea, 16 válvulas"),
            ("Cilindrada", "1.5 L (1.481 cc)"),
            ("Potencia", "145 kW (195 HP) @ 5.600 rpm"),
            ("Torque", "285 Nm @ 1.500 - 4.000 rpm"),
            ("Norma de emisión", "Euro 6b")
        ]

    # 2. TRANSMISION
    if cid == "Z16A":
        trans = [
            ("Marca", "ZNA Dongfeng Heavy Duty"),
            ("Modelo", "6MT Manual de 6 velocidades"),
            ("Tipo", "Sincrónica de 6 marchas adelante + 1 reversa"),
            ("Tracción", "4WD conectable con reductora")
        ]
    elif cid in ["Z20A", "Z42A"]:
        trans = [
            ("Marca", "ZF Friedrichshafen AG"),
            ("Modelo", "8AT Automática de 8 marchas"),
            ("Tipo", "Automática secuencial inteligente con levas"),
            ("Gestión", "Modos de conducción Eco / Sport / Normal")
        ]
    elif cid == "X21B":
        trans = [
            ("Marca", "Dongfeng Dedicated Hybrid"),
            ("Modelo", "4DHT Híbrida Inteligente"),
            ("Tipo", "Transmisión multimodal serie-paralelo"),
            ("Gestión", "Control vectorial de par inteligente")
        ]
    elif cid in ["Z11A", "Z22A"]:
        trans = [
            ("Marca", "Zomax / Nissan Platform"),
            ("Modelo", "5MT Manual sincrónica"),
            ("Tipo", "5 velocidades hacia adelante + 1 reversa"),
            ("Tracción", "2WD Trasera" if cid == "Z11A" else "4WD con caja reductora")
        ]
    elif cid == "Y38G":
        trans = [
            ("Marca", "ZF / Dongfeng Power"),
            ("Modelo", "8AT Automática con bloqueo hidráulico"),
            ("Tipo", "8 velocidades adelante + reversa"),
            ("Tracción", "4x4 Part-Time con reductora (2H / 4H / 4L)")
        ]
    elif cid == "Y38E":
        trans = [
            ("Marca", "Dongfeng Power"),
            ("Modelo", "6MT Manual de 6 marchas"),
            ("Tipo", "Sincrónica con embrague reforzado"),
            ("Tracción", "4x4 Part-Time con reductora (2H / 4H / 4L)")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        trans = [
            ("Marca", "ZF 8AT Automatic"),
            ("Modelo", "8HP de 8 velocidades con convertidor de par"),
            ("Tipo", "Automática secuencial de alto torque"),
            ("Selector de terreno", "Modos Sport, Nieve, Arena, Lodo, ECO")
        ]
    else:  # T5 EVO
        trans = [
            ("Marca", "Magna / Gertrag 7DCT"),
            ("Modelo", "7DCT Doble embrague húmedo"),
            ("Tipo", "Automática secuencial deportiva de 7 marchas"),
            ("Respuesta", "Cambios de marcha en menos de 0.2 segundos")
        ]

    # 3. EMBRAGUE
    if "MT" in tab_name or cid in ["Z16A", "Z11A", "Z22A", "Y38E"]:
        embrague = [
            ("Tipo", "Monodisco en seco con resorte diafragma"),
            ("Control", "Hidráulico con bomba impulsora de asistencia"),
            ("Diámetro", "260 mm reforzado para alta torsión"),
            ("Marca", "Equipo original con certificación de fábrica")
        ]
    elif "DCT" in tab_name:
        embrague = [
            ("Tipo", "Doble embrague húmedo multidisco bañado en aceite"),
            ("Control", "Módulo electrohidráulico TCU de alta precisión"),
            ("Refrigeración", "Circuito de aceite presurizado de disipación"),
            ("Mantenimiento", "Libre de ajuste mecánico de disco")
        ]
    elif "DHT" in tab_name:
        embrague = [
            ("Tipo", "Embrague de desacople directo multimodo híbrido"),
            ("Control", "Gestión electrónica integrada por computadora"),
            ("Acoplamiento", "Transición suave entre modo EV y combustión"),
            ("Durabilidad", "Ciclo de vida extendido de alta durabilidad")
        ]
    else:
        embrague = [
            ("Tipo", "Convertidor de par hidráulico con embrague lock-up"),
            ("Control", "Gestión electrónica integrada a la transmisión"),
            ("Bloqueo", "Acople directo a velocidades de crucero"),
            ("Durabilidad", "Fluido sintético de larga duración")
        ]

    # 4. SISTEMA ELECTRICO
    if cid == "X21B":
        electrico = [
            ("Voltaje alto voltaje", "Sistema PHEV 350 V - 400 V nominal"),
            ("Batería de tracción", "Iones de litio de alta densidad 31.8 kWh"),
            ("Batería auxiliar", "12 V de ciclado profundo para electrónica"),
            ("Salida auxiliar V2L", "Toma externa 220 V / 6 kW para herramientas")
        ]
    else:
        electrico = [
            ("Batería", "12 V libre de mantenimiento de alto rendimiento (70-80 Ah)"),
            ("Alternador", "14 V / 120 A - 150 A de alta salida"),
            ("Arranque", "Motor de arranque eléctrico 12 V / 1.8 kW"),
            ("Fusibles y relés", "Caja central sellada contra agua y polvo IP67")
        ]

    # 5. PESOS
    if cid == "Z16A":
        pesos = [
            ("Tara", "2.205 kg"),
            ("Peso bruto vehicular", "3.380 kg"),
            ("Capacidad de carga", "1.175 kg (Servicio Pesado)"),
            ("Capacidad de remolque", "3.000 kg (con freno)")
        ]
    elif cid == "Z20A":
        pesos = [
            ("Tara", "2.280 kg"),
            ("Peso bruto vehicular", "3.145 kg"),
            ("Capacidad de carga", "865 kg"),
            ("Capacidad de remolque", "3.000 kg")
        ]
    elif cid == "Z42A":
        pesos = [
            ("Tara", "2.140 kg"),
            ("Peso bruto vehicular", "3.005 kg"),
            ("Capacidad de carga", "865 kg"),
            ("Pasajeros", "5 ocupantes")
        ]
    elif cid == "X21B":
        pesos = [
            ("Tara", "2.470 kg (2.509 kg equipada)"),
            ("Peso bruto vehicular", "3.235 kg"),
            ("Capacidad de carga", "765 kg útil"),
            ("Distribución", "50% delantero / 50% trasero")
        ]
    elif cid in ["Z11A", "Z22A"]:
        pesos = [
            ("Tara", "1.785 kg"),
            ("Peso bruto vehicular", "2.600 kg"),
            ("Capacidad de carga", "500 kg (hasta 815 kg reforzada)"),
            ("Pasajeros", "5 ocupantes")
        ]
    elif cid in ["Y38G", "Y38E"]:
        pesos = [
            ("Tara", "1.855 kg"),
            ("Peso bruto vehicular", "2.560 kg"),
            ("Capacidad de carga", "490 kg (hasta 705 kg reforzada)"),
            ("Pasajeros", "5 ocupantes")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        pesos = [
            ("Tara", "1.890 kg" if cid == "W91A" else "1.950 kg"),
            ("Peso bruto vehicular", "2.501 kg"),
            ("Capacidad de carga", "611 kg" if cid == "W91A" else "551 kg"),
            ("Capacidad de remolque", "2.500 kg")
        ]
    else:  # T5 EVO
        pesos = [
            ("Tara", "1.550 kg"),
            ("Peso bruto vehicular", "1.995 kg"),
            ("Capacidad de carga", "445 kg"),
            ("Volumen maletero", "480 L (expandible a 1.480 L)")
        ]

    # 6. SISTEMA COMBUSTIBLE
    if cid == "X21B":
        comb = [
            ("Tanque de combustible", "Tanque presurizado reforzado"),
            ("Capacidad", "73 Litros"),
            ("Batería eléctrica", "31.8 kWh litio ferrofosfato"),
            ("Autonomía combinada", "Más de 1.000 km (135 km modo EV puro)")
        ]
    elif cid in ["T5-LUX", "T5-EXC"]:
        comb = [
            ("Tanque de combustible", "Tanque liviano de polímero de seguridad"),
            ("Capacidad", "55 Litros"),
            ("Alimentación", "Bomba eléctrica de alta presión GDI (350 bar)")
        ]
    else:
        comb = [
            ("Tanque de combustible", "Tanque reforzado con protección inferior"),
            ("Capacidad", "73 Litros"),
            ("Alimentación", "Bomba sumergida con regulador de retorno y filtro")
        ]

    # 7. SISTEMA DE FRENOS
    if cid in ["Z11A", "Z22A", "Y38G", "Y38E"]:
        frenos = [
            ("Freno delantero", "Discos ventilados de servicio pesado"),
            ("Freno trasero", "Tambor autoajustable con zapatas de alta fricción"),
            ("Freno de estacionamiento", "Mecánico por cable sobre ruedas traseras"),
            ("Asistencias de serie", "ABS antibloqueo con distribución electrónica EBD")
        ]
    else:
        frenos = [
            ("Tipo general", "Frenos de disco en las cuatro ruedas (Four-Wheel Disc)"),
            ("Freno delantero", "Discos ventilados con cáliper flotante"),
            ("Freno trasero", "Discos macizos / ventilados de alta disipación"),
            ("Freno de estacionamiento", "Electrónico (EPB) con función Auto-Hold"),
            ("Asistencias de serie", "ABS, EBD, Asistente de frenado de pánico HBA / BOS")
        ]

    # 8. VOLUMEN DE FLUIDOS
    fluidos = [
        ("Aceite de motor", "5.0 L (Sintético SAE 5W-30 / 0W-20 API SP)"),
        ("Líquido refrigerante", "8.5 L (Refrigerante larga vida al 50%)"),
        ("Aceite de transmisión", "7.0 L (Fluido certificado para transmisión)"),
        ("Líquido de frenos", "1.0 L (DOT 4)"),
        ("Lavaparabrisas", "4.0 L")
    ]

    return {
        "motor": motor,
        "trans": trans,
        "embrague": embrague,
        "electrico": electrico,
        "pesos": pesos,
        "comb": comb,
        "frenos": frenos,
        "fluidos": fluidos
    }
