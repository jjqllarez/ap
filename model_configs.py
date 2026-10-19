"""
Configuración de modelos, versiones y metadatos bilingües (ES / EN).
Módulo de configuración desacoplado (Separación de responsabilidades).
"""

SHEET_CONFIGS = {
    "Z9": {
        "model_key": "Z9",
        "model_name": {"es": "Z9 Comercial", "en": "Z9 Commercial"},
        "category": {"es": "Pick-up Mediana 4WD", "en": "Mid-size Pickup 4WD"},
        "vehicle_type": {"es": "Pick-up", "en": "Pickup"},
        "fuel_badge": {"es": "Gasolina Turbo", "en": "Turbo Gasoline"},
        "versions": [
            {
                "id": "Z16A",
                "col_idx": 3,
                "badge_id": "Z16A",
                "tag": {"es": "4WD 6MT", "en": "4WD 6MT"},
                "fuel_badge": {"es": "Gasolina Turbo", "en": "Turbo Gasoline"},
                "title": {
                    "es": "Z9 Comercial 4WD MT: Motor 4K31 2.0T con 1,175 kg de capacidad de carga útil",
                    "en": "Z9 Commercial 4WD MT: 4K31 2.0T Engine with 1,175 kg Payload Capacity"
                },
                "subtitle": {
                    "es": "Motor 2.0T Gasolina · 190 kW (255 HP) · 400 Nm · Transmisión 6MT",
                    "en": "2.0T Gasoline Engine · 190 kW (255 HP) · 400 Nm · 6MT Transmission"
                },
                "highlights": {
                    "es": "Capacidad récord de carga útil de 1,175 kg con suspensión reforzada de ballestas. Motor Mitsubishi 4K31 2.0T de 190 kW (255 HP) y 400 Nm de torque acoplado a caja manual de 6 velocidades. Frenos de disco ventilados en las 4 ruedas y tracción 4WD con caja reductora.",
                    "en": "Record payload capacity of 1,175 kg with heavy-duty leaf spring rear suspension. Mitsubishi 4K31 2.0T engine producing 190 kW (255 HP) and 400 Nm of torque paired with a 6-speed manual gearbox. Ventilated 4-wheel disc brakes and electronic 4WD with low-range transfer case."
                },
            },
            {
                "id": "Z20A",
                "col_idx": 4,
                "badge_id": "Z20A",
                "tag": {"es": "4WD 8AT", "en": "4WD 8AT"},
                "fuel_badge": {"es": "Gasolina Turbo", "en": "Turbo Gasoline"},
                "title": {
                    "es": "Z9 Comercial 4WD AT: Motor 4K31 2.0T con Transmisión Automática 8AT y 865 kg de carga",
                    "en": "Z9 Commercial 4WD AT: 4K31 2.0T Engine with 8AT Automatic Transmission and 865 kg Payload"
                },
                "subtitle": {
                    "es": "Motor 2.0T Gasolina · 190 kW (255 HP) · 400 Nm · Transmisión 8AT",
                    "en": "2.0T Gasoline Engine · 190 kW (255 HP) · 400 Nm · 8AT Transmission"
                },
                "highlights": {
                    "es": "Transmisión automática de 8 velocidades 8AT combinada con el motor 2.0T 4K31 de alto torque (400 Nm). Capacidad de carga de 865 kg, tracción 4x4 electrónica, interior refinado con confort para faenas exigentes y trayectos interurbanos.",
                    "en": "8-speed automatic transmission (8AT) paired with high-torque 2.0T 4K31 engine (400 Nm). 865 kg payload capacity, electronic 4x4 drivetrain, refined cabin comfort tailored for demanding fleet tasks and intercity driving."
                },
            },
        ],
    },
    "Z9 PASSENGER": {
        "model_key": "Z9 PASSENGER",
        "model_name": {"es": "Z9 Passenger", "en": "Z9 Passenger"},
        "category": {"es": "Pick-up Pasajeros / Confort", "en": "Passenger Pickup / Comfort"},
        "vehicle_type": {"es": "Pick-up Pasajeros", "en": "Passenger Pickup"},
        "fuel_badge": {"es": "Gasolina Turbo Euro 6", "en": "Euro 6 Turbo Gasoline"},
        "versions": [
            {
                "id": "Z42A",
                "col_idx": 3,
                "badge_id": "Z42A",
                "tag": {"es": "4WD 8AT Confort", "en": "4WD 8AT Comfort"},
                "fuel_badge": {"es": "Gasolina Turbo Euro 6", "en": "Euro 6 Turbo Gasoline"},
                "title": {
                    "es": "Z9 Passenger 4WD 8AT: Pick-up Premium de Pasajeros Euro 6 con Suspensión Confort",
                    "en": "Z9 Passenger 4WD 8AT: Premium Euro 6 Passenger Pickup with Comfort Suspension"
                },
                "subtitle": {
                    "es": "Motor 2.0T Gasolina Euro 6 · 190 kW (255 HP) · 400 Nm · Transmisión 8AT",
                    "en": "2.0T Euro 6 Gasoline Engine · 190 kW (255 HP) · 400 Nm · 8AT Transmission"
                },
                "highlights": {
                    "es": "Versión orientada al transporte de pasajeros y uso personal con nivel de emisiones Euro 6 (código ZN1039UCB6A). Equipada con transmisión automática 8AT, suspensión optimizada para marcha suave, cabina insonorizada y acabados de alta gama.",
                    "en": "Passenger and personal luxury orientation with Euro 6 emission certification (Code ZN1039UCB6A). Features 8AT automatic transmission, comfort-tuned suspension, soundproofed cabin, and executive interior styling."
                },
            }
        ],
    },
    "Z9 HYBRID ": {
        "model_key": "Z9 HYBRID",
        "model_name": {"es": "Z9 Hybrid PHEV", "en": "Z9 Hybrid PHEV"},
        "category": {"es": "Pick-up Híbrida Enchufable 4WD", "en": "Plug-in Hybrid Pickup 4WD"},
        "vehicle_type": {"es": "Pick-up PHEV", "en": "PHEV Pickup"},
        "fuel_badge": {"es": "Híbrido Enchufable PHEV", "en": "Plug-in Hybrid PHEV"},
        "versions": [
            {
                "id": "X21B",
                "col_idx": 3,
                "badge_id": "X21B",
                "tag": {"es": "PHEV 4WD 4DHT", "en": "PHEV 4WD 4DHT"},
                "fuel_badge": {"es": "Híbrido Enchufable PHEV", "en": "Plug-in Hybrid PHEV"},
                "title": {
                    "es": "Z9 P20 PHEV 4WD 135KM UPR: Pick-up Híbrida Enchufable con Transmisión 4DHT",
                    "en": "Z9 P20 PHEV 4WD 135KM UPR: Plug-in Hybrid Pickup with 4DHT Dedicated Hybrid Transmission"
                },
                "subtitle": {
                    "es": "Sistema Híbrido PHEV · 135 km Rango EV · Tracción 4WD · Transmisión 4DHT",
                    "en": "PHEV Hybrid System · 135 km EV Range · 4WD Drivetrain · 4DHT Transmission"
                },
                "highlights": {
                    "es": "Tecnología híbrida enchufable de vanguardia con 135 km de autonomía en modo 100% eléctrico (código ZN1030UCEPHEVB / P20 PHEV). Transmisión híbrida multimodo 4DHT, tracción integral 4WD inteligente, homologación de emisiones China 6b+RDE+FE4 y eficiencia energética excepcional.",
                    "en": "Cutting-edge plug-in hybrid technology with 135 km 100% electric range (Code ZN1030UCEPHEVB / P20 PHEV). Multimode 4DHT hybrid transmission, intelligent 4WD system, China 6b+RDE+FE4 homologation, and exceptional energy efficiency."
                },
            }
        ],
    },
    "RICH 6 ": {
        "model_key": "RICH 6",
        "model_name": {"es": "Rich 6", "en": "Rich 6"},
        "category": {"es": "Pick-up Utilitaria Trabajo", "en": "Commercial Work Pickup"},
        "vehicle_type": {"es": "Pick-up Trabajo", "en": "Work Pickup"},
        "fuel_badge": {"es": "Gasolina 2.4L", "en": "2.4L Gasoline"},
        "versions": [
            {
                "id": "Z11A",
                "col_idx": 3,
                "badge_id": "Z11A",
                "tag": {"es": "2WD 5MT", "en": "2WD 5MT"},
                "fuel_badge": {"es": "Gasolina 2.4L", "en": "2.4L Gasoline"},
                "title": {
                    "es": "Rich 6 Doble Cabina 2WD 5MT: Confiabilidad probada con motor 2.4L y chasis Nissan",
                    "en": "Rich 6 Double Cab 2WD 5MT: Proven Reliability with 2.4L Engine and Nissan Chassis Platform"
                },
                "subtitle": {
                    "es": "Motor 2.4L 2TZD · 116 kW (156 HP) · 230 Nm · Transmisión 5MT",
                    "en": "2.4L 2TZD Engine · 116 kW (156 HP) · 230 Nm · 5MT Transmission"
                },
                "highlights": {
                    "es": "Plataforma heredada de Nissan con motor 2TZD 2.4L de inyección multipunto, 116 kW y 230 Nm. Tracción trasera 2WD, caja manual de 5 velocidades, capacidad de carga de 500 kg y despeje al suelo de 207 mm. Solución de alta rentabilidad para flotas de trabajo.",
                    "en": "Nissan-heritage chassis platform powered by 2TZD 2.4L multi-point injection engine (116 kW / 230 Nm). Rear-wheel drive 2WD, 5-speed manual transmission, 500 kg payload, and 207 mm ground clearance. Cost-effective fleet solution."
                },
            },
            {
                "id": "Z22A",
                "col_idx": 4,
                "badge_id": "Z22A",
                "tag": {"es": "4WD 5MT", "en": "4WD 5MT"},
                "fuel_badge": {"es": "Gasolina 2.4L", "en": "2.4L Gasoline"},
                "title": {
                    "es": "Rich 6 Doble Cabina 4WD 5MT: Tracción 4x4 reforzada con tolva protegida y barras antivuelco",
                    "en": "Rich 6 Double Cab 4WD 5MT: Reinforced 4x4 Off-Road Utility with Bedliner and Roll Bar"
                },
                "subtitle": {
                    "es": "Motor 2.4L 2TZD · 116 kW (156 HP) · 230 Nm · Transmisión 5MT · Tracción 4WD",
                    "en": "2.4L 2TZD Engine · 116 kW (156 HP) · 230 Nm · 5MT Transmission · 4WD Drivetrain"
                },
                "highlights": {
                    "es": "Versión 4WD con caja de transferencia y reductora para caminos difíciles. Equipada de serie con recubrimiento protector de tolva (bedliner), estribos laterales, barra protectora trasera y pantalla táctil con conectividad multimedia.",
                    "en": "Heavy-duty 4WD utility with transfer case and low range for harsh terrains. Factory equipped with spray-on bedliner, side steps, rear safety roll bar, and multimedia touchscreen display."
                },
            },
        ],
    },
    "RICH 6 PRO ": {
        "model_key": "RICH 6 PRO",
        "model_name": {"es": "Rich 6 PRO", "en": "Rich 6 PRO"},
        "category": {"es": "Pick-up Mediana Reforzada", "en": "Reinforced Mid-size Pickup"},
        "vehicle_type": {"es": "Pick-up PRO", "en": "PRO Pickup"},
        "fuel_badge": {"es": "Gasolina Euro III", "en": "Euro III Gasoline"},
        "versions": [
            {
                "id": "Y31E",
                "col_idx": 3,
                "badge_id": "Y31E",
                "tag": {"es": "STD 2WD 6MT", "en": "STD 2WD 6MT"},
                "fuel_badge": {"es": "Gasolina Euro III", "en": "Euro III Gasoline"},
                "title": {
                    "es": "Rich 6 PRO STD 2WD 6MT: Evolución con transmisión manual de 6 velocidades",
                    "en": "Rich 6 PRO STD 2WD 6MT: Modernized Utility with 6-Speed Manual Gearbox"
                },
                "subtitle": {
                    "es": "Motor 2.4L 2TZD · 116 kW (156 HP) · 230 Nm · Transmisión 6MT Euro III",
                    "en": "2.4L 2TZD Engine · 116 kW (156 HP) · 230 Nm · 6MT Euro III Transmission"
                },
                "highlights": {
                    "es": "Actualización PRO con nueva caja manual de 6 cambios que reduce el régimen del motor en autopista mejorando el consumo. Frenos de disco en las 4 ruedas, pantalla de control central, chasis cerrado de alta rigidez torsional y capacidad de carga de 490 kg.",
                    "en": "PRO upgrade featuring a 6-speed manual transmission for reduced highway RPM and improved fuel economy. 4-wheel disc brakes, central touchscreen display, high-rigidity closed-section frame, and 490 kg payload."
                },
            },
            {
                "id": "Y32E",
                "col_idx": 4,
                "badge_id": "Y32E",
                "tag": {"es": "STD 4WD 6MT", "en": "STD 4WD 6MT"},
                "fuel_badge": {"es": "Gasolina Euro III", "en": "Euro III Gasoline"},
                "title": {
                    "es": "Rich 6 PRO STD 4WD 6MT: Capacidad todoterreno reforzada con 6MT y tracción 4x4",
                    "en": "Rich 6 PRO STD 4WD 6MT: Reinforced 4x4 Off-Road Capability with 6MT Gearbox"
                },
                "subtitle": {
                    "es": "Motor 2.4L 2TZD · 116 kW (156 HP) · 230 Nm · Transmisión 6MT · Tracción 4WD",
                    "en": "2.4L 2TZD Engine · 116 kW (156 HP) · 230 Nm · 6MT Transmission · 4WD Drivetrain"
                },
                "highlights": {
                    "es": "Configuración 4WD con transmisión manual de 6 velocidades, caja de transferencia para acople de doble tracción, suspensión delantera de doble horquilla y posterior de muelles reforzados para soportar caminos mineros y rurales.",
                    "en": "4WD configuration with 6-speed manual transmission, dual-traction transfer case, double-wishbone front suspension, and reinforced rear leaf springs for mining and rural applications."
                },
            },
        ],
    },
    "rich 6 pro nuevo ": {
        "model_key": "RICH 6 PRO NUEVO",
        "model_name": {"es": "Rich 6 PRO Nuevo (Turbo)", "en": "Rich 6 PRO New (Turbo)"},
        "category": {"es": "Pick-up Turbo Potenciada", "en": "High-Power Turbo Pickup"},
        "vehicle_type": {"es": "Pick-up Turbo", "en": "Turbo Pickup"},
        "fuel_badge": {"es": "Gasolina Turbo 4K31", "en": "Mitsubishi 4K31 Turbo Gasoline"},
        "versions": [
            {
                "id": "Y38E",
                "col_idx": 3,
                "badge_id": "Y38E",
                "tag": {"es": "Turbo 4WD 6MT", "en": "Turbo 4WD 6MT"},
                "fuel_badge": {"es": "Gasolina Turbo 4K31", "en": "Mitsubishi 4K31 Turbo Gasoline"},
                "title": {
                    "es": "Rich 6 PRO Nuevo 4WD 6MT: Motor Turbo Mitsubishi 4K31TD con 168 kW y 360 Nm",
                    "en": "Rich 6 PRO New 4WD 6MT: Mitsubishi 4K31TD Turbo Engine with 168 kW and 360 Nm Torque"
                },
                "subtitle": {
                    "es": "Motor Mitsubishi 2.0T · 168 kW (225 HP) · 360 Nm · Transmisión 6MT · FOB $13,100",
                    "en": "Mitsubishi 2.0T Engine · 168 kW (225 HP) · 360 Nm · 6MT Transmission · FOB $13,100"
                },
                "highlights": {
                    "es": "Salto generacional con motor Mitsubishi 4K31TD 2.0L Turbo que entrega 168 kW (225 HP) y un torque contundente de 360 Nm. Caja manual de 6 velocidades, tracción 4WD con reductora, pantalla central de 10 pulgadas y excelente relación costo/rendimiento (FOB $13,100).",
                    "en": "Generational leap with Mitsubishi 4K31TD 2.0L Turbo engine delivering 168 kW (225 HP) and 360 Nm torque. 6-speed manual gearbox, 4WD with low range, 10-inch center screen, and competitive value ratio (FOB $13,100)."
                },
            },
            {
                "id": "Y38G",
                "col_idx": 4,
                "badge_id": "Y38G",
                "tag": {"es": "Turbo 4WD 8AT", "en": "Turbo 4WD 8AT"},
                "fuel_badge": {"es": "Gasolina Turbo 4K31", "en": "Mitsubishi 4K31 Turbo Gasoline"},
                "title": {
                    "es": "Rich 6 PRO Nuevo 4WD 8AT: Potencia Turbo acoplada a transmisión automática de 8 marchas",
                    "en": "Rich 6 PRO New 4WD 8AT: Turbo Power Mated to 8-Speed Automatic Transmission"
                },
                "subtitle": {
                    "es": "Motor Mitsubishi 2.0T · 168 kW (225 HP) · 360 Nm · Transmisión 8AT · FOB $14,600",
                    "en": "Mitsubishi 2.0T Engine · 168 kW (225 HP) · 360 Nm · 8AT Transmission · FOB $14,600"
                },
                "highlights": {
                    "es": "Combinación del motor Turbo 4K31TD con caja automática ZF de 8 marchas 8AT para suavidad y empuje continuo. Incluye pantalla táctil multimedia de 10 pulgadas, tracción integral 4WD seleccionable y máxima comodidad de manejo (FOB $14,600).",
                    "en": "Smooth continuous surge pairing the 4K31TD Turbo engine with ZF 8-speed automatic (8AT). Includes 10-inch multimedia display, selectable 4WD, and maximum driving comfort (FOB $14,600)."
                },
            },
        ],
    },
    "PALADIN": {
        "model_key": "PALADIN",
        "model_name": {"es": "Paladin SUV", "en": "Paladin SUV"},
        "category": {"es": "SUV Todoterreno Chasis", "en": "Body-on-Frame 4x4 SUV"},
        "vehicle_type": {"es": "SUV 4x4", "en": "4x4 SUV"},
        "fuel_badge": {"es": "Gasolina Turbo 2.0T", "en": "2.0T Turbo Gasoline"},
        "versions": [
            {
                "id": "W92C",
                "col_idx": 3,
                "badge_id": "W92C",
                "tag": {"es": "UPR 4WD 8AT", "en": "UPR 4WD 8AT"},
                "fuel_badge": {"es": "Gasolina Turbo 2.0T", "en": "2.0T Turbo Gasoline"},
                "title": {
                    "es": "Paladin SUV UPR 4WD 8AT: Todoterreno tope de gama con modos de terreno y pantalla de 12 pulgadas",
                    "en": "Paladin SUV UPR 4WD 8AT: Flagship Body-on-Frame SUV with Terrain Modes and 12-inch Screen"
                },
                "subtitle": {
                    "es": "Motor 2.0T 4K31 · 168 kW (225 HP) · 360 Nm · Transmisión 8AT · Tracción 4WD",
                    "en": "2.0T 4K31 Engine · 168 kW (225 HP) · 360 Nm · 8AT Transmission · 4WD Drivetrain"
                },
                "highlights": {
                    "es": "Versión tope de gama UPR con chasis de largueros independiente, tracción 4x4 con reductora y modos todoterreno (Arena, Nieve, Barro, ECO, Sport). Pantalla central gigante de 12 pulgadas, sistema de audio de 6 parlantes, rieles de techo, estribos y máximo confort.",
                    "en": "Flagship UPR grade built on a rigid ladder chassis, low-range 4x4, and multi-terrain drive modes (Sand, Snow, Mud, ECO, Sport). Massive 12-inch center screen, 6-speaker audio, roof rails, side steps, and executive comfort."
                },
            },
            {
                "id": "W92B",
                "col_idx": 4,
                "badge_id": "W92B",
                "tag": {"es": "MID 4WD 8AT", "en": "MID 4WD 8AT"},
                "fuel_badge": {"es": "Gasolina Turbo 2.0T", "en": "2.0T Turbo Gasoline"},
                "title": {
                    "es": "Paladin SUV MID 4WD 8AT: Equilibrio óptimo entre capacidad 4x4 y equipamiento de confort",
                    "en": "Paladin SUV MID 4WD 8AT: Balanced 4x4 Capability and Comfort Technology"
                },
                "subtitle": {
                    "es": "Motor 2.0T 4K31 · 168 kW (225 HP) · 360 Nm · Transmisión 8AT · Tracción 4WD",
                    "en": "2.0T 4K31 Engine · 168 kW (225 HP) · 360 Nm · 8AT Transmission · 4WD Drivetrain"
                },
                "highlights": {
                    "es": "Versión intermedia MID con la misma arquitectura mecánica 4WD y transmisión 8AT. Incorpora pantalla de 10 pulgadas, 4 parlantes, control electrónico de estabilidad ESC, cámara de retroceso y despeje al suelo de 215 mm para superar cualquier obstáculo.",
                    "en": "Mid-tier grade sharing the robust 4WD architecture and 8AT gearbox. Features 10-inch display, 4 speakers, ESC electronic stability control, reverse camera, and 215 mm ground clearance to conquer any terrain."
                },
            },
            {
                "id": "W91A",
                "col_idx": 5,
                "badge_id": "W91A",
                "tag": {"es": "STD 2WD 8AT", "en": "STD 2WD 8AT"},
                "fuel_badge": {"es": "Gasolina Turbo 2.0T", "en": "2.0T Turbo Gasoline"},
                "title": {
                    "es": "Paladin SUV STD 2WD 8AT: Espacio, robustez y transmisión automática para uso urbano e interurbano",
                    "en": "Paladin SUV STD 2WD 8AT: Spacious, Rugged Urban/Intercity SUV with 8AT Transmission"
                },
                "subtitle": {
                    "es": "Motor 2.0T 4K31 · 168 kW (225 HP) · 360 Nm · Transmisión 8AT · Tracción 2WD",
                    "en": "2.0T 4K31 Engine · 168 kW (225 HP) · 360 Nm · 8AT Transmission · 2WD Drivetrain"
                },
                "highlights": {
                    "es": "Versión de entrada STD con tracción trasera 2WD y caja automática de 8 velocidades. Peso reducido (1,890 kg) que optimiza el consumo de combustible manteniendo la imponente presencia y habitabilidad de un SUV con carrocería sobre chasis.",
                    "en": "Entry STD model with 2WD rear-wheel drive and 8-speed automatic gearbox. Reduced curb weight (1,890 kg) optimizing fuel economy while preserving the commanding stance and spaciousness of a true body-on-frame SUV."
                },
            },
        ],
    },
    "T5 EVO ": {
        "model_key": "T5 EVO",
        "model_name": {"es": "Forthing T5 EVO", "en": "Forthing T5 EVO"},
        "category": {"es": "SUV Compacto Deportivo", "en": "Sport Compact SUV"},
        "vehicle_type": {"es": "SUV Crossover", "en": "Crossover SUV"},
        "fuel_badge": {"es": "Gasolina Turbo DVVT+GDI", "en": "DVVT+GDI Turbo Gasoline"},
        "versions": [
            {
                "id": "T5-LUX",
                "col_idx": 3,
                "badge_id": "T5-LUX",
                "tag": {"es": "Luxury 7DCT", "en": "Luxury 7DCT"},
                "fuel_badge": {"es": "Gasolina Turbo DVVT+GDI", "en": "DVVT+GDI Turbo Gasoline"},
                "title": {
                    "es": "T5 EVO 1.5TD Luxury 7DCT: SUV Deportivo con motor Mitsubishi de 195 HP y caja doble embrague",
                    "en": "T5 EVO 1.5TD Luxury 7DCT: Sporty Compact SUV with 195 HP Mitsubishi Engine & 7DCT Dual-Clutch"
                },
                "subtitle": {
                    "es": "Motor 1.5T 4A95TD · 145 kW (195 HP) · 285 Nm · Transmisión Magna 7DCT",
                    "en": "1.5T 4A95TD Engine · 145 kW (195 HP) · 285 Nm · Magna 7DCT Transmission"
                },
                "highlights": {
                    "es": "Diseño aerodinámico vanguardista con motor Shenyang Mitsubishi 1.5T con inyección directa GDI y doble distribución variable DVVT (145 kW / 195 HP y 285 Nm). Transmisión de doble embrague húmedo de 7 marchas, techo panorámico corredizo y habitáculo tecnológico.",
                    "en": "Aerodynamic avant-garde styling with Shenyang Mitsubishi 1.5T engine featuring GDI direct injection and DVVT (145 kW / 195 HP, 285 Nm). Magna 7-speed wet dual-clutch transmission, panoramic sunroof, and high-tech cabin."
                },
            },
            {
                "id": "T5-EXC",
                "col_idx": 4,
                "badge_id": "T5-EXC",
                "tag": {"es": "Exclusive 7DCT", "en": "Exclusive 7DCT"},
                "fuel_badge": {"es": "Gasolina Turbo DVVT+GDI", "en": "DVVT+GDI Turbo Gasoline"},
                "title": {
                    "es": "T5 EVO 1.5TD Exclusive 7DCT: Máximo nivel de tecnología, asistencias avanzadas y confort",
                    "en": "T5 EVO 1.5TD Exclusive 7DCT: Peak Technology, Advanced ADAS Driver Assist & Luxury Comfort"
                },
                "subtitle": {
                    "es": "Motor 1.5T 4A95TD · 145 kW (195 HP) · 285 Nm · Transmisión Magna 7DCT",
                    "en": "1.5T 4A95TD Engine · 145 kW (195 HP) · 285 Nm · Magna 7DCT Transmission"
                },
                "highlights": {
                    "es": "Versión Exclusive con paquete integral de asistencias a la conducción ADAS, asientos de cuero con calefacción/ventilación, panel digital envolvente con doble pantalla, climatizador bi-zona automático y portón trasero eléctrico.",
                    "en": "Top Exclusive grade with full L2+ ADAS driver assistance suite, heated/ventilated leather seating, dual widescreen digital cockpit, dual-zone automatic climate control, and smart electric liftgate."
                },
            },
        ],
    },
}
