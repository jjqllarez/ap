# -*- coding: utf-8 -*-
"""Generador de secciones técnicas de la Hoja 2 para cada modelo."""

def get_sheet2_sections(cid, tab_name):
    # 1. EJE DELANTERO
    if cid in ["Z16A", "Z20A", "Z42A", "X21B"]:
        eje_del = [
            ("Tipo", "Semiejes de tracción con articulación homocinética"),
            ("Suspensión", "Doble horquilla independiente con barra estabilizadora transversal"),
            ("Amortiguación", "Amortiguadores telescópicos presurizados de doble acción"),
            ("Capacidad de carga", "1.650 kg de carga frontal"),
            ("Rin de acero / aleación", "Aleación de aluminio 18''"),
            ("Neumático", "265/60 R18 (Todo Terreno AT)")
        ]
    elif cid in ["Z11A", "Z22A", "Y38G", "Y38E"]:
        eje_del = [
            ("Tipo", "Rótulas forjadas de servicio pesado (Chasis Nissan)"),
            ("Suspensión", "Doble horquilla con barra estabilizadora y brazos reforzados"),
            ("Amortiguación", "Amortiguadores hidráulicos telescópicos"),
            ("Capacidad de carga", "1.300 kg"),
            ("Rin de acero / aleación", "Aleación de aluminio 16''"),
            ("Neumático", "255/70 R16")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        eje_del = [
            ("Tipo", "Eje independiente articulado para SUV todoterreno"),
            ("Suspensión", "Doble horquilla independiente con barra estabilizadora"),
            ("Amortiguación", "Amortiguadores de gas bitubo de largo recorrido"),
            ("Capacidad de carga", "1.450 kg"),
            ("Rin de acero / aleación", "Aleación de aluminio 18''"),
            ("Neumático", "265/60 R18 All-Terrain")
        ]
    else:  # T5 EVO
        eje_del = [
            ("Tipo", "Tracción delantera con diferencial integrado a la caja DCT"),
            ("Suspensión", "Independiente tipo MacPherson con barra estabilizadora"),
            ("Amortiguación", "Amortiguadores telescópicos progresivos deportivos"),
            ("Capacidad de carga", "1.100 kg"),
            ("Rin de acero / aleación", "Aleación ligera deportiva de 19'' en acabado negro"),
            ("Neumático", "235/55 R19 de ultra alto agarre")
        ]

    # 2. EJE TRASERO
    if cid in ["Z16A", "Z20A"]:
        eje_tras = [
            ("Reducción", "Simple con piñón y corona hipoide reforzados"),
            ("Relación", "Optimizada para capacidad de arrastre y carga útil"),
            ("Suspensión", "Ballestas longitudinales semielípticas multi-hoja"),
            ("Diferencial", "Diferencial de servicio pesado / Bloqueo opcional"),
            ("Rin de acero / aleación", "Aleación 18'' · Medida 18x8.0J"),
            ("Neumático", "265/60 R18")
        ]
    elif cid in ["Z42A", "X21B"]:
        eje_tras = [
            ("Reducción", "Simple helicoidal / Motor eléctrico de tracción trasera (PHEV)"),
            ("Relación", "Ajustada electrónicamente para máxima eficiencia"),
            ("Suspensión", "Multilink independiente o ballestas parabólicas progresivas"),
            ("Diferencial", "Bloqueo electrónico de diferencial trasero (E-Locker)"),
            ("Rin de acero / aleación", "Aleación 18''"),
            ("Neumático", "265/60 R18")
        ]
    elif cid in ["Z11A", "Z22A", "Y38G", "Y38E"]:
        eje_tras = [
            ("Reducción", "Simple, tipo Banjo reforzado laminado a presión"),
            ("Relación", "Optimizada para fuerza motriz y economía de marcha"),
            ("Suspensión", "Paquete de ballestas semielípticas sobre eje"),
            ("Capacidad de carga", "1.800 kg de carga trasera"),
            ("Rin de acero / aleación", "Aleación de aluminio 16''"),
            ("Neumático", "255/70 R16")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        eje_tras = [
            ("Reducción", "Eje rígido guiado por 5 brazos articulados"),
            ("Relación", "4x4 reductora para trepada off-road"),
            ("Suspensión", "Multilink independiente con resortes helicoidales"),
            ("Diferencial", "Bloqueo de diferencial trasero al 100% (Rear Locker)"),
            ("Rin de acero / aleación", "Aleación 18''"),
            ("Neumático", "265/60 R18")
        ]
    else:  # T5 EVO
        eje_tras = [
            ("Reducción", "Eje trasero portante independiente"),
            ("Relación", "Alineada con control de estabilidad de viraje"),
            ("Suspensión", "Multi-link independiente multibrazo con estabilizadora"),
            ("Amortiguación", "Resortes espirales progresivos y amortiguador a gas"),
            ("Rin de acero / aleación", "Aleación deportiva 19''"),
            ("Neumático", "235/55 R19")
        ]

    # 3. CHASIS
    if cid in ["Z16A", "Z20A", "Z42A", "X21B", "Z11A", "Z22A", "Y38G", "Y38E", "W91A", "W92B", "W92C"]:
        chasis = [
            ("Estructura", "Escalera reforzada de doble perfil cajonado cerrado"),
            ("Material", "Acero de alta resistencia galvanizado de grado automotriz"),
            ("Protección inferior", "Cubre-cárter, protector de caja de cambios y tanque"),
            ("Puntos de anclaje", "Ganchos de remolque delantero y trasero para servicio pesado"),
            ("Tratamiento", "Protección anticorrosiva por electrodeposición cataforética")
        ]
    else:
        chasis = [
            ("Estructura", "Carrocería autoportante monocasco de ultra alta rigidez"),
            ("Acero avanzado", "76% de aceros de ultra-alta y alta resistencia estampados"),
            ("Seguridad pasiva", "Zonas de deformación programada frontal y posterior"),
            ("Refuerzos", "Barras de acero al boro anti-impacto en las 4 puertas"),
            ("Subchasis", "Subchasis aislante hidroformado de doble soporte")
        ]

    # 4. CABINA Y DIRECCION
    if cid in ["Z16A", "Z20A", "Z42A", "X21B"]:
        cabina_dir = [
            ("Configuración", "Doble cabina cuatro puertas / Capacidad 5 asientos confort"),
            ("Aislamiento", "Cabina acústica NVH con doble burlete y vidrios laminados"),
            ("Mecanismo conductor", "Asiento con ajuste en 6 direcciones y soporte lumbar"),
            ("Dirección", "Bosch, sistema hidráulico asistido / Asistencia electrónica"),
            ("Volante", "Columna de dirección colapsable y ajustable en altura y profundidad")
        ]
    elif cid in ["Z11A", "Z22A", "Y38G", "Y38E"]:
        cabina_dir = [
            ("Configuración", "Doble cabina utilitaria reforzada / 5 pasajeros"),
            ("Montaje de cabina", "Montada sobre 6 tacos elásticos de absorción de impactos"),
            ("Mecanismo conductor", "Asiento ergonómico con tapizado resistente de alto tráfico"),
            ("Dirección", "Dirección asistida hidráulica de cremallera y piñón"),
            ("Volante", "Volante de 3 radios colapsable con regulación de inclinación")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        cabina_dir = [
            ("Configuración", "SUV cerrado 5 puertas / 5 plazas de gran habitabilidad"),
            ("Insonorización", "Paquete acústico premium de absorción de ruidos y vibraciones"),
            ("Mecanismo conductor", "Butaca con regulación eléctrica de 8 posiciones"),
            ("Dirección", "Dirección electroasistida EPS regulable según velocidad"),
            ("Volante", "Volante multifunción forrado en cuero con mandos integrados")
        ]
    else:  # T5 EVO
        cabina_dir = [
            ("Configuración", "SUV crossover deportivo 5 puertas / 5 ocupantes"),
            ("Diseño interior", "Cockpit envolvente inspirado en aeronáutica deportiva"),
            ("Mecanismo conductor", "Butaca deportiva con ajuste eléctrico y memoria"),
            ("Dirección", "Dirección electroasistida con 3 modos de tacto (Sport/Comfort/Normal)"),
            ("Volante", "Volante deportivo achatado en base (D-Cut) forrado en microfibra")
        ]

    # 5. CARACTERISTICAS INTERIORES / CONFORT
    if cid in ["Z16A", "Z20A"]:
        interior = [
            ("Aire acondicionado", "Automático digital con ductos hacia plazas traseras"),
            ("Vidrios / Apertura", "Vidrios eléctricos en las 4 puertas / Cierre centralizado con llave"),
            ("Velocímetro y tacómetro", "Cuadro de mandos digital multifuncional en español"),
            ("Indicadores", "Presión de neumáticos TPMS, consumo y autonomía"),
            ("Equipo de sonido", "Pantalla de 12'' con conectividad smartphone / Parlantes HD"),
            ("Conductor y pasajero", "Airbags frontales y anclajes ISOFIX de serie"),
            ("Cámara de reversa", "Cámara de alta definición con sensores de proximidad")
        ]
    elif cid == "Z42A":
        interior = [
            ("Aire acondicionado", "Climatizador bizona automático con filtro PM2.5"),
            ("Pantalla multifuncional", "Pantalla flotante de 12.3 pulgadas con soporte táctil"),
            ("Equipo de sonido", "Sistema surround de audio de 6 parlantes"),
            ("Asientos", "Cuero microperforado, butacas delanteras calefaccionadas"),
            ("Cámara de reversa", "Cámara panorámica 360° / 540° con chasis transparente"),
            ("Acceso", "Apertura sin llave (Keyless) y botón de encendido Start/Stop"),
            ("Techo y luces", "Iluminación ambiental LED y tomas USB en plazas traseras")
        ]
    elif cid == "X21B":
        interior = [
            ("Aire acondicionado", "Climatizador inteligente de alto rendimiento con bomba de calor"),
            ("Pantalla multifuncional", "Pantalla táctil HD de 12.8 pulgadas con telemetría híbrida"),
            ("Instrumentación", "Panel de instrumentos completamente digital de 10.25 pulgadas"),
            ("Tomas auxiliares", "Salida externa V2L de 220 V / 6 kW para herramientas"),
            ("Seguridad activa", "8 Airbags, frenado autónomo y control de estabilidad ESC"),
            ("Cámara de visión", "Cámara 540° con visión de ángulo muerto y retrovisor digital"),
            ("Asientos", "Tapicería de cuero de alta costura con ajuste lumbar eléctrico")
        ]
    elif cid in ["Z11A", "Z22A"]:
        interior = [
            ("Aire acondicionado", "Manual de alto poder de refrigeración para climas cálidos"),
            ("Vidrios / Apertura", "Alzacristales eléctricos y bloqueo central remoto"),
            ("Equipo de sonido", "Radio AM/FM con conexión Bluetooth, puerto USB y AUX"),
            ("Indicadores", "Odómetro digital, tacómetro y alerta de cinturones"),
            ("Seguridad", "Doble airbag frontal de fábrica, ABS y anclajes infantiles"),
            ("Tapicería", "Tapicería de tela de alta durabilidad y fácil limpieza"),
            ("Cámara / Sensores", "Sensores de proximidad traseros con alarma sonora")
        ]
    elif cid in ["Y38G", "Y38E"]:
        interior = [
            ("Aire acondicionado", "Climatizador electrónico digital con display integrado"),
            ("Pantalla multifuncional", "Pantalla táctil multimedia con soporte para celular"),
            ("Vidrios / Alzacristales", "Vidrios eléctricos con función un toque para el conductor"),
            ("Volante", "Mandos de telefonía, control multimedia y control crucero"),
            ("Seguridad", "Control de estabilidad ESC, control de tracción y frenos ABS+EBD"),
            ("Cámara de reversa", "Cámara de reversa HD con guías dinámicas de estacionamiento"),
            ("Asientos", "Ecocuero ergonómico de fácil mantenimiento y apoyabrazos central")
        ]
    elif cid in ["W91A", "W92B", "W92C"]:
        interior = [
            ("Aire acondicionado", "Climatizador automático bizona con purificador de aire"),
            ("Pantalla multifuncional", "Pantalla vertical HD de 12 pulgadas con conectividad"),
            ("Instrumentación", "Panel de instrumentos a color de 7 pulgadas con pantalla off-road"),
            ("Asistencias ADAS", "Control crucero adaptativo, Frenado autónomo y Carril" if cid == "W92C" else "Control de crucero, Sensores perimétricos y cámara"),
            ("Cámara de visión", "Cámara panorámica 360° con vista cenital e inclinómetro digital"),
            ("Techo", "Techo solar panorámico con apertura eléctrica"),
            ("Asientos", "Butacas en cuero con regulación eléctrica de 8 posiciones")
        ]
    else:  # T5 EVO
        interior = [
            ("Aire acondicionado", "Climatizador automático inteligente con salidas traseras"),
            ("Doble pantalla", "Doble pantalla panorámica digital de 10.25'' + 10.25'' integrada"),
            ("Techo solar", "Techo panorámico corredizo de apertura total con cortina eléctrica"),
            ("Asientos", "Butacas deportivas ergonómicas envolventes en eco-cuero"),
            ("Asistencias ADAS", "Monitoreo punto ciego BSD, Aviso cambio carril LDW" if cid == "T5-EXC" else "Cámara de reversa, Control de descenso HDC y crucero"),
            ("Conectividad", "Apple CarPlay, Bluetooth manos libres y puertos rápidos de carga"),
            ("Audio", "Sistema de audio envolvente de 6 parlantes de alta fidelidad")
        ]

    return {
        "eje_del": eje_del,
        "eje_tras": eje_tras,
        "chasis": chasis,
        "cabina_dir": cabina_dir,
        "interior": interior
    }
