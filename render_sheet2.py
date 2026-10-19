# -*- coding: utf-8 -*-
"""Plantillas y lógica de renderizado HTML de la Hoja 2."""

from render_sheet1 import render_logo_header, render_spec_row, render_sec_block

def render_svg_chassis_diagram(label, cotas):
    """Genera un diagrama técnico dimensional estilizado con cotas acotadas A-I en SVG nítido vectorial."""
    return f'''
    <div class="relative w-full bg-white flex flex-col justify-between overflow-hidden">
      <div class="flex justify-between items-center mb-1">
        <span class="text-[10px] font-black text-black tracking-wider font-mono uppercase">{label}</span>
        <span class="text-[8.5px] font-bold text-slate-500 tracking-wide">PLANO TÉCNICO DIMENSIONAL · COTAS A-I (MM)</span>
      </div>
      
      <!-- SVG Vectorial de Chasis Acotado ocupando prácticamente todo el ancho -->
      <div class="w-full h-[145px] flex items-center justify-center bg-white">
        <svg class="w-full h-full" viewBox="0 0 760 135" fill="none" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <!-- Rejilla tenue de fondo -->
          <line x1="20" y1="20" x2="740" y2="20" stroke="#f1f5f9" stroke-dasharray="3 3"/>
          <line x1="20" y1="60" x2="740" y2="60" stroke="#f1f5f9" stroke-dasharray="3 3"/>
          <line x1="20" y1="100" x2="740" y2="100" stroke="#f1f5f9" stroke-dasharray="3 3"/>

          <!-- Silueta Frontal de Cabina (Izquierda) -->
          <g stroke="#334155" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="#f8fafc">
            <!-- Cabina frontal -->
            <path d="M 60 40 L 70 20 L 150 20 L 160 40 L 165 95 L 55 95 Z" />
            <!-- Parabrisas -->
            <path d="M 72 24 L 148 24 L 156 46 L 64 46 Z" fill="#e2e8f0" stroke="#64748b" stroke-width="1.2"/>
            <!-- Parrilla y faros -->
            <rect x="75" y="55" width="70" height="22" rx="3" fill="#cbd5e1" stroke="#475569" stroke-width="1.2"/>
            <line x1="75" y1="62" x2="145" y2="62" stroke="#64748b" stroke-width="1"/>
            <line x1="75" y1="70" x2="145" y2="70" stroke="#64748b" stroke-width="1"/>
            <!-- Ruedas frontales -->
            <circle cx="70" cy="98" r="14" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <circle cx="70" cy="98" r="6" fill="#94a3b8"/>
            <circle cx="150" cy="98" r="14" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <circle cx="150" cy="98" r="6" fill="#94a3b8"/>
          </g>

          <!-- Silueta Lateral del Chasis y Vehículo (Derecha) -->
          <g stroke="#334155" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <!-- Cabina lateral -->
            <path d="M 230 95 L 230 65 L 255 42 L 340 42 L 355 58 L 355 95 Z" fill="#f8fafc"/>
            <!-- Ventana lateral -->
            <path d="M 260 46 L 332 46 L 344 58 L 260 58 Z" fill="#e2e8f0" stroke="#64748b" stroke-width="1.2"/>
            <!-- Bastidor Chasis / Larguero principal -->
            <rect x="220" y="80" width="460" height="15" rx="2" fill="#334155" stroke="#1e293b" stroke-width="1.5"/>
            <!-- Compartimiento de carga / Tolva -->
            <path d="M 360 55 L 675 55 L 680 95 L 360 95 Z" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 2"/>
            <!-- Rueda delantera lateral -->
            <circle cx="280" cy="98" r="16" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <circle cx="280" cy="98" r="7" fill="#cbd5e1"/>
            <!-- Rueda trasera lateral -->
            <circle cx="580" cy="98" r="16" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <circle cx="580" cy="98" r="7" fill="#cbd5e1"/>
          </g>

          <!-- COTA A: Distancia entre ejes (280 -> 580) -->
          <g stroke="#0f172a" stroke-width="1.2">
            <line x1="280" y1="120" x2="580" y2="120" marker-start="url(#dot)" marker-end="url(#dot)"/>
            <line x1="280" y1="112" x2="280" y2="126"/>
            <line x1="580" y1="112" x2="580" y2="126"/>
          </g>
          <text x="430" y="129" fill="#0f172a" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">A: {cotas["A"].split(" ")[0]}</text>

          <!-- COTA C: Longitud total (220 -> 680) -->
          <g stroke="#0f172a" stroke-width="1.2">
            <line x1="220" y1="14" x2="680" y2="14"/>
            <line x1="220" y1="8" x2="220" y2="20"/>
            <line x1="680" y1="8" x2="680" y2="20"/>
          </g>
          <text x="450" y="11" fill="#0f172a" font-size="9.5" font-weight="bold" font-family="sans-serif" text-anchor="middle">C (Longitud total): {cotas["C"].split(" ")[0]}</text>

          <!-- COTA F: Voladizo delantero (220 -> 280) -->
          <g stroke="#64748b" stroke-width="1">
            <line x1="220" y1="120" x2="280" y2="120"/>
            <line x1="220" y1="115" x2="220" y2="125"/>
          </g>
          <text x="250" y="129" fill="#475569" font-size="8.5" font-weight="bold" font-family="sans-serif" text-anchor="middle">F</text>

          <!-- COTA B: Voladizo trasero (580 -> 680) -->
          <g stroke="#64748b" stroke-width="1">
            <line x1="580" y1="120" x2="680" y2="120"/>
            <line x1="680" y1="115" x2="680" y2="125"/>
          </g>
          <text x="630" y="129" fill="#475569" font-size="8.5" font-weight="bold" font-family="sans-serif" text-anchor="middle">B</text>

          <!-- COTA H: Altura total (Frontal) -->
          <g stroke="#2563eb" stroke-width="1.2">
            <line x1="38" y1="20" x2="38" y2="98"/>
            <line x1="32" y1="20" x2="44" y2="20"/>
            <line x1="32" y1="98" x2="44" y2="98"/>
          </g>
          <text x="32" y="60" fill="#2563eb" font-size="8.5" font-weight="bold" font-family="sans-serif" text-anchor="end">H: {cotas["H"].split(" ")[0]}</text>

          <!-- COTA G: Ancho de Vía Frontal (70 -> 150) -->
          <g stroke="#059669" stroke-width="1.2">
            <line x1="70" y1="120" x2="150" y2="120"/>
            <line x1="70" y1="115" x2="70" y2="125"/>
            <line x1="150" y1="115" x2="150" y2="125"/>
          </g>
          <text x="110" y="129" fill="#059669" font-size="8.5" font-weight="bold" font-family="sans-serif" text-anchor="middle">G</text>

          <!-- COTA I: Largo útil de carga (360 -> 675) -->
          <g stroke="#ea580c" stroke-width="1.2">
            <line x1="360" y1="32" x2="675" y2="32"/>
            <line x1="360" y1="26" x2="360" y2="38"/>
            <line x1="675" y1="26" x2="675" y2="38"/>
          </g>
          <text x="517" y="30" fill="#ea580c" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">I (Carga): {cotas["I"].split(" ")[0]}</text>
        </svg>
      </div>
    </div>
    '''

def render_chassis_area(m, cotas):
    chassis_img = m.get("chassis_image") or m.get("chassis_diagram_img")
    if chassis_img:
        return f'''
        <div class="relative w-full bg-white flex flex-col justify-between overflow-hidden">
          <div class="flex justify-between items-center mb-1">
            <span class="text-[10px] font-black text-black tracking-wider font-mono uppercase">{m["diagram_label"]}</span>
            <span class="text-[8.5px] font-bold text-slate-500 tracking-wide">PLANO TÉCNICO OFICIAL · COTAS A-I (MM)</span>
          </div>
          <div class="w-full h-[155px] flex items-center justify-center bg-white">
            <img src="{chassis_img}" class="w-full h-full max-w-full object-contain" alt="Plano Técnico Chasis {m['diagram_label']}" />
          </div>
        </div>
        '''
    else:
        return render_svg_chassis_diagram(m["diagram_label"], cotas)

def render_sheet2(m):
    cid = m["id"]
    s2 = m["s2"]
    cotas = m["cotas"]
    ed = m["extra_dim"]

    # Secciones Izquierda Hoja 2:
    # 1. DIMENSIONES
    dim_rows = [
        ("Longitud total", ed["longitud"]),
        ("Ancho total", ed["ancho"]),
        ("Altura total", ed["alto"]),
        ("Distancia entre ejes", ed["distancia_ejes"]),
        ("Voladizo delantero", ed["voladizo_del"]),
        ("Voladizo trasero", ed["voladizo_tras"]),
        ("Despeje libre al suelo", ed["despeje"]),
        ("Radio mínimo de giro", ed["radio_giro"])
    ]
    
    # 2. COTAS DEL CHASIS (mm) - Letras A a I
    custom_labels = m.get("cotas_labels", {})
    cotas_rows = [
        (custom_labels.get("A", "A · Distancia entre ejes"), cotas["A"]),
        (custom_labels.get("B", "B · Voladizo trasero"), cotas["B"]),
        (custom_labels.get("C", "C · Longitud total"), cotas["C"]),
        (custom_labels.get("D", "D · Eje delantero a cabina"), cotas["D"]),
        (custom_labels.get("E", "E · Altura piso de carga / maletero"), cotas["E"]),
        (custom_labels.get("F", "F · Voladizo delantero"), cotas["F"]),
        (custom_labels.get("G", "G · Ancho de vía (Trocha)"), cotas["G"]),
        (custom_labels.get("H", "H · Altura total"), cotas["H"]),
        (custom_labels.get("I", "I · Largo zona de carga / maletero"), cotas["I"])
    ]

    cotas_title = m.get("cotas_title", "COTAS DEL CHASIS (mm)")
    left_sections_h2 = (
        render_sec_block("DIMENSIONES", dim_rows) +
        render_sec_block(cotas_title, cotas_rows) +
        render_sec_block("CABINA Y DIRECCIÓN", s2["cabina_dir"])
    )

    # Secciones Derecha Hoja 2: EJE DELANTERO + EJE TRASERO + CHASIS + CARACTERISTICAS INTERIORES / CONFORT
    right_sections_h2 = (
        render_sec_block("EJE DELANTERO", s2["eje_del"]) +
        render_sec_block("EJE TRASERO", s2["eje_tras"]) +
        render_sec_block("CHASIS", s2["chasis"]) +
        render_sec_block("CARACTERÍSTICAS INTERIORES / CONFORT", s2["interior"])
    )

    return f'''
    <!-- HOJA 2: {cid} -->
    <div class="sheet-page page-2 bg-white shadow-xl rounded-sm mx-auto flex flex-col justify-between" id="sheet2-{cid}">
      <!-- Encabezado Hoja 2 -->
      <div>
        <div class="flex items-start justify-between border-b border-slate-200 pb-2 mb-2">
          <div>
            <h1 class="text-[18px] font-black text-slate-950 tracking-tight leading-none mb-1">{m["title_h2"]}</h1>
            <div class="text-[9.5px] font-bold text-slate-600 tracking-wider uppercase">
              CHASIS, DIMENSIONES Y CABINA · {m["badge_text"]}
            </div>
          </div>
          {render_logo_header()}
        </div>

        <!-- Zona Superior: Diagrama Acotado Chasis (A-I) -->
        <div class="mb-2.5">
          {render_chassis_area(m, cotas)}
        </div>

        <!-- Grid 2 Columnas Hoja 2 -->
        <div class="grid grid-cols-12 gap-4 items-start">
          <!-- Columna Izquierda (5 columnas) -->
          <div class="col-span-5">
            {left_sections_h2}
          </div>

          <!-- Columna Derecha (7 columnas) -->
          <div class="col-span-7">
            {right_sections_h2}
          </div>
        </div>
      </div>

      <!-- Pie de página Hoja 2 -->
      <div class="pt-2 border-t border-slate-200 flex justify-between items-center text-[10px] text-slate-500">
        <a href="https://www.planchartglobal.com" target="_blank" class="font-bold text-slate-700 hover:text-black transition tracking-wider">www.planchartglobal.com</a>
        <span class="font-bold text-slate-500">2 / 2</span>
      </div>
    </div>
    '''
