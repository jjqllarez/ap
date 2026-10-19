# -*- coding: utf-8 -*-
"""Módulo con las especificaciones técnicas completas de los 3 nuevos modelos:
1. M09: MINIVAN PASAJEROS - 11 (Código: M09-4353Z-WN)
2. MINI-CS: 2T-MINI TRUCK - CS (Cabina Sencilla) (Código: VH24-625-WZ)
3. MINI-CD: 2T-MINI TRUCK - CD (Cabina Doble) (Código: VH24-627-WZ)
"""

NEW_MODELS_DATA = [
    {
        "id": "M09",
        "tab": "★ Minivan 11 Pasajeros (M09)",
        "title_h1": "DONGFENG MINIVAN PASAJEROS · 11 PUESTOS",
        "title_h2": "DONGFENG MINIVAN PASAJEROS",
        "vehiculo": "Transporte de Pasajeros / Minibús Utilitario",
        "marca": "DONGFENG",
        "modelo": "Minivan Pasajeros - 11",
        "version": "M09-4353Z-WN",
        "cabina": "Minivan cerrada integral 11 plazas (4 filas)",
        "traccion": "4x2 (Tracción Trasera - RWD)",
        "badge_text": "MINIVAN 11 PUESTOS",
        "badge_sub": "1.6L GASOLINA 5MT",
        "diagram_label": "MINIVAN M09 (DIMENSIONES EN MM)",
        "hero_image": "assets/minivan_m09_hero.jpg",
        "chassis_image": "assets/minivan_m09_plano.jpg",
        "cotas_title": "COTAS DEL CHASIS (MM)",
        "cotas_labels": {
            "A": "A · Distancia entre ejes",
            "B": "B · Voladizo trasero",
            "C": "C · Longitud total",
            "D": "D · Eje delantero a cabina (conductor)",
            "E": "E · Altura piso de carga / maletero",
            "F": "F · Voladizo delantero",
            "G": "G · Ancho de vía (Trocha Del. / Tras.)",
            "H": "H · Altura total",
            "I": "I · Largo zona compartimiento pasajeros"
        },
        "cotas": {
            "A": "3.000 mm",
            "B": "1.225 mm",
            "C": "5.135 mm",
            "D": "910 mm",
            "E": "680 mm",
            "F": "910 mm",
            "G": "1.445 mm / 1.420 mm",
            "H": "1.990 mm",
            "I": "3.100 mm"
        },
        "extra_dim": {
            "longitud": "5.135 mm",
            "ancho": "1.720 mm",
            "alto": "1.990 mm",
            "distancia_ejes": "3.000 mm",
            "voladizo_del": "910 mm",
            "voladizo_tras": "1.225 mm",
            "despeje": "170 mm",
            "radio_giro": "5.9 m"
        },
        "s1": {
            "motor": [
                ["Tipo / Modelo", "Motor 1.6L 4 cilindros en línea DOHC 16V MIVEC (Mitsubishi 4A92)"],
                ["Admisión", "Aspiración atmosférica multipunto secuencial"],
                ["Inyección", "Inyección electrónica multipunto de alta precisión (MPI)"],
                ["Cilindrada", "1.590 cc (1.6L)"],
                ["Diámetro x Carrera", "75,0 mm × 89,9 mm"],
                ["Potencia máxima", "122 HP (90 kW) @ 6.000 rpm"],
                ["Torque máximo", "151 Nm @ 4.000 rpm"],
                ["Combustible", "Gasolina regular sin plomo (91+ octanos)"],
                ["Norma de emisión", "Euro 4 / Euro 5"]
            ],
            "pesos": [
                ["Tara (Peso en vacío)", "1.660 kg"],
                ["Peso bruto vehicular (PBV)", "2.480 kg"],
                ["Capacidad de carga neta", "820 kg"],
                ["Capacidad de pasajeros", "11 ocupantes (incluyendo conductor)"]
            ],
            "trans": [
                ["Tipo", "Transmisión manual sincronizada"],
                ["Velocidades", "5 velocidades hacia adelante + 1 reversa (5MT)"],
                ["Tracción", "Tracción 4x2 Trasera (RWD con cardán y diferencial)"],
                ["Relación final", "Optimizada para transporte urbano y sub-urbano"]
            ],
            "embrague": [
                ["Tipo", "Monodisco seco con resorte de diafragma"],
                ["Accionamiento", "Control hidráulico de bajo esfuerzo"]
            ],
            "electrico": [
                ["Voltaje del sistema", "12 V de corriente continua"],
                ["Batería", "12 V / 60 Ah libre de mantenimiento"],
                ["Alternador", "12 V / 90 A con regulador integrado"]
            ],
            "comb": [
                ["Tanque de combustible", "Tanque de polímero de seguridad de alta resistencia"],
                ["Capacidad total", "55 Litros (14.5 Galones)"],
                ["Alimentación", "Bomba sumergida con filtro de alta eficiencia"]
            ],
            "frenos": [
                ["Sistema de frenos", "Hidráulico de doble circuito cruzado con servoasistencia por vacío"],
                ["Frenos delanteros", "Discos ventilados"],
                ["Frenos traseros", "Tambor autorregulable de alta fricción"],
                ["Asistencias de frenado", "ABS (Antibloqueo) + EBD (Distribución Electrónica)"],
                ["Freno de estacionamiento", "Mecánico por cable sobre ruedas traseras"]
            ],
            "fluidos": [
                ["Aceite de motor", "4.0 L (Sintético SAE 10W-40 / 5W-30)"],
                ["Líquido refrigerante", "6.5 L (Refrigerante larga vida al 50%)"],
                ["Aceite de transmisión", "2.1 L (SAE 75W-90 GL-4)"],
                ["Aceite de diferencial trasero", "1.5 L (SAE 80W-90 / 85W-90 GL-5)"],
                ["Líquido de frenos", "0.8 L (DOT 4)"],
                ["Lavaparabrisas", "2.5 L"]
            ]
        },
        "s2": {
            "cabina_dir": [
                ["Configuración de asientos", "11 plazas en 4 filas (distribución 2 + 3 + 3 + 3)"],
                ["Acceso a cabina", "Puerta lateral corrediza de gran apertura y compuerta trasera vertical"],
                ["Dirección", "Asistida hidráulicamente de piñón y cremallera"],
                ["Columna de dirección", "Colapsable con ajuste de inclinación vertical"],
                ["Visibilidad", "Amplia superficie acristalada panorámica con desempañador posterior"]
            ],
            "eje_del": [
                ["Tipo de eje", "Independiente tipo MacPherson"],
                ["Suspensión", "Resortes helicoidales con amortiguadores telescópicos y barra estabilizadora"],
                ["Capacidad de carga eje", "1.150 kg"],
                ["Rines", "Acero estampado 15 pulgadas con tazas decorativas (15×6.0J)"],
                ["Neumáticos", "195/70 R15C (Servicio de carga / transporte de pasajeros)"]
            ],
            "eje_tras": [
                ["Tipo de eje", "Eje rígido motriz con diferencial integrado"],
                ["Suspensión", "Ballestas longitudinales semielípticas multi-hoja con amortiguadores hidráulicos"],
                ["Capacidad de carga eje", "1.550 kg"],
                ["Rines", "Acero estampado 15 pulgadas"],
                ["Neumáticos", "195/70 R15C"]
            ],
            "chasis": [
                ["Estructura", "Carrocería autoportante monocasco reforzada de deformación programada"],
                ["Tratamiento anticorrosivo", "Fosfatizado e inmersión cataforética completa (E-coat)"],
                ["Protección inferior", "Protector de cárter y tratamiento anti-gravilla en bajos"]
            ],
            "interior": [
                ["Climatización", "Doble sistema de Aire Acondicionado (frontal e independiente con difusores para pasajeros traseros)"],
                ["Vidrios y seguros", "Alzacristales eléctricos delanteros y cierre centralizado con mando"],
                ["Audio y conectividad", "Radio AM/FM con reproductor USB, Bluetooth y parlantes integrados"],
                ["Seguridad pasiva", "Cinturones de seguridad de 3 puntos en plazas delanteras y cinturones para todas las plazas posteriores"],
                ["Instrumentación", "Panel digital con velocímetro, odómetro, tacómetro, nivel de combustible y alertas de mantenimiento"]
            ]
        }
    },
    {
        "id": "MINI-CS",
        "tab": "★ 2T Mini Truck CS (VH24-625-WZ)",
        "title_h1": "DONGFENG 2T-MINI TRUCK · CABINA SENCILLA",
        "title_h2": "DONGFENG 2T-MINI TRUCK CS",
        "vehiculo": "Camión Ligero Utilitario / Chasis con Tolva",
        "marca": "DONGFENG",
        "modelo": "2T-Mini Truck - CS",
        "version": "VH24-625-WZ",
        "cabina": "Cabina sencilla abatible 2 puestos",
        "traccion": "4x2 (Doble rodado trasero)",
        "badge_text": "2.0 TONELADAS CS",
        "badge_sub": "TURBODIÉSEL 2.3L 5MT",
        "diagram_label": "2T-MINI TRUCK CS (DIMENSIONES EN MM)",
        "hero_image": "",
        "chassis_image": "",
        "cotas": {
            "A": "2.800 mm (Distancia entre ejes)",
            "B": "1.500 mm (Voladizo trasero)",
            "C": "5.450 mm (Longitud total)",
            "D": "550 mm (Eje delantero a inicio de tolva)",
            "E": "820 mm (Altura plataforma de carga al piso)",
            "F": "1.150 mm (Voladizo delantero)",
            "G": "1.480 mm / 1.420 mm (Trocha Delantera / Trasera)",
            "H": "2.050 mm (Altura total de cabina)",
            "I": "3.400 mm (Largo útil de tolva de carga)"
        },
        "extra_dim": {
            "longitud": "5.450 mm",
            "ancho": "1.850 mm",
            "alto": "2.050 mm",
            "distancia_ejes": "2.800 mm",
            "voladizo_del": "1.150 mm",
            "voladizo_tras": "1.500 mm",
            "despeje": "190 mm",
            "radio_giro": "6.2 m"
        },
        "s1": {
            "motor": [
                ["Tipo / Denominación", "Motor Turbodiésel 2.3L 4 cilindros en línea"],
                ["Admisión", "Turbocompresor con intercooler aire-aire"],
                ["Inyección", "Inyección directa Common Rail de alta presión Bosch"],
                ["Cilindrada", "2.270 cc (2.3 L)"],
                ["Potencia máxima", "95 HP (70 kW) @ 3.200 rpm"],
                ["Torque máximo", "240 Nm @ 1.800 - 2.400 rpm"],
                ["Combustible", "Diésel automotriz"],
                ["Norma de emisión", "Euro 4 / Euro 5"]
            ],
            "pesos": [
                ["Tara (Peso en vacío)", "1.800 kg"],
                ["Peso bruto vehicular (PBV)", "3.800 kg"],
                ["Capacidad de carga útil", "2.000 kg (2.0 Toneladas netas homologadas)"],
                ["Dimensiones de tolva", "3.400 mm (largo) x 1.750 mm (ancho) x 380 mm (alto de baranda)"]
            ],
            "trans": [
                ["Tipo", "Transmisión manual mecánica sincronizada"],
                ["Velocidades", "5 velocidades hacia adelante + 1 reversa (5MT)"],
                ["Tracción", "4x2 posterior con eje cardánico reforzado"],
                ["Configuración trasera", "Doble rodado (Dual Rear Wheels) para alta estabilidad y soporte de carga"]
            ],
            "embrague": [
                ["Tipo", "Monodisco seco con accionamiento hidráulico"],
                ["Diámetro de plato", "260 mm de alta durabilidad"],
                ["Mando", "Servoasistido para desacople suave y progresivo"]
            ],
            "electrico": [
                ["Voltaje del sistema", "12 V de servicio pesado"],
                ["Batería", "12 V / 80 Ah de libre mantenimiento"],
                ["Alternador", "12 V / 85 A con corte inteligente"]
            ],
            "comb": [
                ["Tanque de combustible", "Tanque de acero con tapa con cerradura y protección antigolpes"],
                ["Capacidad total", "65 Litros (17.2 Galones)"],
                ["Sedimentador", "Filtro separador de agua primario con sensor y purga manual"]
            ],
            "frenos": [
                ["Sistema de frenos", "Hidráulico servoasistido con doble circuito independiente"],
                ["Frenos delanteros", "Discos ventilados de servicio pesado"],
                ["Frenos traseros", "Tambores autoajustables de alta fricción"],
                ["Freno auxiliar", "Freno de motor al escape de accionamiento neumático/electroválvula"],
                ["Asistencias", "Sistema ABS antibloqueo con sensor de carga en eje trasero"],
                ["Freno de estacionamiento", "Mecánico por cable sobre ruedas traseras"]
            ],
            "fluidos": [
                ["Aceite de motor", "5.5 L (Diésel 15W-40 CI-4 / CH-4)"],
                ["Líquido refrigerante", "8.0 L (Refrigerante larga vida al 50%)"],
                ["Aceite de transmisión", "2.8 L (SAE 80W-90 GL-5)"],
                ["Aceite de diferencial", "2.5 L (SAE 85W-140 GL-5)"],
                ["Líquido de frenos", "1.0 L (DOT 4)"]
            ]
        },
        "s2": {
            "cabina_dir": [
                ["Tipo de cabina", "Cabina frontal sobre motor, rebatible para fácil inspección"],
                ["Capacidad de pasajeros", "2 plazas (conductor + acompañante) con apoyacabezas"],
                ["Dirección", "Dirección hidráulica asistida de recirculación de bolas"],
                ["Columna de dirección", "Ajustable en inclinación y colapsable en impacto"],
                ["Espejos retrovisores", "Retrovisores dobles panorámicos de gran ángulo y visión de punto ciego"]
            ],
            "eje_del": [
                ["Tipo de eje", "Viga rígida forjada en sección I (Reverse Elliott)"],
                ["Suspensión", "Ballestas semielípticas de 6 hojas con amortiguadores hidráulicos telescópicos"],
                ["Capacidad de carga", "1.600 kg"],
                ["Rines", "Acero reforzado 15 pulgadas para servicio pesado"],
                ["Neumáticos", "185 R15 LT (8PR / Carga reforzada)"]
            ],
            "eje_tras": [
                ["Tipo de eje", "Eje rígido de servicio pesado con reducción simple cónica hipoide"],
                ["Configuración de rodado", "Doble rodado trasero (4 neumáticos posteriores)"],
                ["Suspensión", "Ballestas semielípticas multi-hoja principales (6 hojas) + auxiliares (5 hojas)"],
                ["Capacidad de carga", "2.800 kg"],
                ["Rines", "Acero reforzado 15 pulgadas"],
                ["Neumáticos", "185 R15 LT (doble rodado)"]
            ],
            "chasis": [
                ["Bastidor", "Vigas longitudinales de acero de alta resistencia tipo canal C con travesaños remachados"],
                ["Plataforma de carga", "Tolva metálica de piso acanalado de alta fricción con ganchos de amarre"],
                ["Compuertas de tolva", "Abatibles en 3 lados (lateral izquierdo, lateral derecho y compuerta posterior)"],
                ["Defensa trasera", "Barra de protección anti-empotramiento homologada"]
            ],
            "interior": [
                ["Climatización", "Aire acondicionado de fábrica con calefactor y desempañador"],
                ["Vidrios y seguros", "Alzacristales eléctricos y bloqueo central de puertas"],
                ["Audio e info-entretenimiento", "Radio AM/FM con puerto USB, entrada auxiliar y reloj digital"],
                ["Instrumentación", "Tablero análogo-digital con tacómetro, odómetro, temperatura y nivel de combustible"],
                ["Asientos", "Asiento de conductor regulable longitudinalmente tapizado en vinil de alta durabilidad"]
            ]
        }
    },
    {
        "id": "MINI-CD",
        "tab": "★ 2T Mini Truck CD (VH24-627-WZ)",
        "title_h1": "DONGFENG 2T-MINI TRUCK · CABINA DOBLE",
        "title_h2": "DONGFENG 2T-MINI TRUCK CD",
        "vehiculo": "Camión Ligero Utilitario / Chasis con Tolva Doble Cabina",
        "marca": "DONGFENG",
        "modelo": "2T-Mini Truck - CD",
        "version": "VH24-627-WZ",
        "cabina": "Cabina doble 4 puertas 5 plazas",
        "traccion": "4x2 (Doble rodado trasero)",
        "badge_text": "2.0 TON DOBLE CABINA",
        "badge_sub": "TURBODIÉSEL 2.3L 5MT",
        "diagram_label": "2T-MINI TRUCK CD (DIMENSIONES EN MM)",
        "hero_image": "",
        "chassis_image": "",
        "cotas": {
            "A": "3.300 mm (Distancia entre ejes)",
            "B": "1.300 mm (Voladizo trasero)",
            "C": "5.550 mm (Longitud total)",
            "D": "1.350 mm (Eje delantero a inicio de tolva tras cabina doble)",
            "E": "820 mm (Altura plataforma de carga)",
            "F": "1.150 mm (Voladizo delantero)",
            "G": "1.480 mm / 1.420 mm (Trocha Delantera / Trasera)",
            "H": "2.080 mm (Altura total de cabina)",
            "I": "2.600 mm (Largo útil de tolva de carga)"
        },
        "extra_dim": {
            "longitud": "5.550 mm",
            "ancho": "1.850 mm",
            "alto": "2.080 mm",
            "distancia_ejes": "3.300 mm",
            "voladizo_del": "1.150 mm",
            "voladizo_tras": "1.300 mm",
            "despeje": "190 mm",
            "radio_giro": "6.6 m"
        },
        "s1": {
            "motor": [
                ["Tipo / Denominación", "Motor Turbodiésel 2.3L 4 cilindros en línea"],
                ["Admisión", "Turbocompresor con intercooler aire-aire"],
                ["Inyección", "Inyección directa Common Rail Bosch alta presión"],
                ["Cilindrada", "2.270 cc (2.3 L)"],
                ["Potencia máxima", "95 HP (70 kW) @ 3.200 rpm"],
                ["Torque máximo", "240 Nm @ 1.800 - 2.400 rpm"],
                ["Combustible", "Diésel automotriz"],
                ["Norma de emisión", "Euro 4 / Euro 5"]
            ],
            "pesos": [
                ["Tara (Peso en vacío)", "1.980 kg"],
                ["Peso bruto vehicular (PBV)", "4.000 kg"],
                ["Capacidad de carga útil", "2.000 kg (2.0 Toneladas netas con 5 ocupantes)"],
                ["Dimensiones de tolva", "2.600 mm (largo) x 1.750 mm (ancho) x 380 mm (alto de baranda)"]
            ],
            "trans": [
                ["Tipo", "Transmisión manual mecánica sincronizada"],
                ["Velocidades", "5 velocidades hacia adelante + 1 reversa (5MT)"],
                ["Tracción", "4x2 posterior con eje de transmisión reforzado"],
                ["Configuración trasera", "Doble rodado (Dual Rear Wheels) para soporte de carga de 2 Toneladas"]
            ],
            "embrague": [
                ["Tipo", "Monodisco seco con accionamiento hidráulico"],
                ["Diámetro de plato", "260 mm de alta resistencia"],
                ["Mando", "Servoasistido para confort del conductor"]
            ],
            "electrico": [
                ["Voltaje del sistema", "12 V de servicio pesado"],
                ["Batería", "12 V / 80 Ah de libre mantenimiento"],
                ["Alternador", "12 V / 85 A con corte inteligente"]
            ],
            "comb": [
                ["Tanque de combustible", "Tanque de acero con tapa con cerradura y protección de chasis"],
                ["Capacidad total", "65 Litros (17.2 Galones)"],
                ["Sedimentador", "Filtro trampa de agua con sensor electrónico y purga manual"]
            ],
            "frenos": [
                ["Sistema de frenos", "Hidráulico servoasistido con doble circuito cruzado"],
                ["Frenos delanteros", "Discos ventilados de servicio pesado"],
                ["Frenos traseros", "Tambores autoajustables de alta fricción"],
                ["Freno auxiliar", "Freno de motor al escape"],
                ["Asistencias", "Sistema ABS antibloqueo con válvula sensora de carga (LSPV)"],
                ["Freno de estacionamiento", "Mecánico por cable sobre ruedas traseras"]
            ],
            "fluidos": [
                ["Aceite de motor", "5.5 L (Diésel 15W-40 CI-4 / CH-4)"],
                ["Líquido refrigerante", "8.0 L (Refrigerante larga vida al 50%)"],
                ["Aceite de transmisión", "2.8 L (SAE 80W-90 GL-5)"],
                ["Aceite de diferencial", "2.5 L (SAE 85W-140 GL-5)"],
                ["Líquido de frenos", "1.0 L (DOT 4)"]
            ]
        },
        "s2": {
            "cabina_dir": [
                ["Tipo de cabina", "Doble Cabina fija 4 puertas para 5 ocupantes"],
                ["Capacidad de pasajeros", "5 plazas (2 delanteras + 3 traseras con cinturones)"],
                ["Dirección", "Dirección hidráulica asistida de recirculación de bolas"],
                ["Columna de dirección", "Ajustable en ángulo y colapsable"],
                ["Retrovisores", "Espejos exteriores dobles panorámicos de gran cobertura"]
            ],
            "eje_del": [
                ["Tipo de eje", "Viga rígida forjada en sección I (Reverse Elliott)"],
                ["Suspensión", "Ballestas semielípticas de 6 hojas con amortiguadores hidráulicos de doble acción"],
                ["Capacidad de carga", "1.600 kg"],
                ["Rines", "Acero estampado reforzado 15 pulgadas"],
                ["Neumáticos", "185 R15 LT (8PR / Carga pesada)"]
            ],
            "eje_tras": [
                ["Tipo de eje", "Eje rígido de servicio pesado con reducción simple cónica hipoide"],
                ["Configuración de rodado", "Doble rodado trasero (4 ruedas posteriores)"],
                ["Suspensión", "Ballestas semielípticas principales (6 hojas) + auxiliares (5 hojas)"],
                ["Capacidad de carga", "2.800 kg"],
                ["Rines", "Acero reforzado 15 pulgadas"],
                ["Neumáticos", "185 R15 LT (doble rodado)"]
            ],
            "chasis": [
                ["Bastidor", "Largueros de acero de perfil C reforzado de alta rigidez torsional"],
                ["Plataforma de carga", "Tolva metálica de 2.60 metros con piso acanalado de alta fricción"],
                ["Compuertas de tolva", "Abatibles en 3 lados (laterales y trasera) con cerraduras seguras"],
                ["Protección", "Barra anti-empotramiento trasera y defensas laterales"]
            ],
            "interior": [
                ["Climatización", "Aire acondicionado de alto poder para habitáculo doble cabina"],
                ["Vidrios y seguros", "Alzacristales eléctricos en las 4 puertas y cierre centralizado"],
                ["Audio e info-entretenimiento", "Radio AM/FM con puerto USB, entrada auxiliar y 4 parlantes"],
                ["Instrumentación", "Tablero integral con velocímetro, tacómetro y medidores de aguja de temperatura y combustible"],
                ["Asientos", "Asientos ergonómicos con tapicería de tela vinílica lavable y duradera"]
            ]
        }
    }
]
