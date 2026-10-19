# -*- coding: utf-8 -*-
"""Plantillas y lógica de renderizado HTML de la Hoja 1 y Hoja 2."""

def render_logo_header():
    return '''
    <div class="text-right select-none flex flex-col items-end">
      <img src="assets/logo_planchart.png" alt="PLANCHART GLOBAL" class="h-7 sm:h-8 object-contain mb-0.5" />
      <div class="text-[8.5px] font-semibold text-slate-500 tracking-wider">RIF: J-507655245</div>
    </div>
    '''

def render_spec_row(label, val):
    return f'''
    <div class="spec-row leading-tight mb-0.5 text-[10px] text-slate-800">
      <span class="font-semibold text-slate-900">{label}</span>: 
      <span class="text-slate-700">{val}</span>
    </div>
    '''

def render_sec_block(title, rows):
    rows_html = "".join([render_spec_row(l, v) for l, v in rows])
    return f'''
    <div class="spec-section mb-2">
      <h3 class="text-[11px] font-black tracking-wider text-black uppercase mb-1 border-b border-slate-200 pb-0.5">{title}</h3>
      <div class="space-y-0.5">
        {rows_html}
      </div>
    </div>
    '''

def render_sheet1(m):
    cid = m["id"]
    s1 = m["s1"]
    
    # Left col sections: Image placeholder + TRANSMISION + EMBRAGUE + SISTEMA ELECTRICO
    left_sections = (
        render_sec_block("TRANSMISIÓN", s1["trans"]) +
        render_sec_block("EMBRAGUE", s1["embrague"]) +
        render_sec_block("SISTEMA ELÉCTRICO", s1["electrico"])
    )
    
    # Right col sections: MOTOR + PESOS + SISTEMA COMBUSTIBLE + SISTEMA DE FRENOS + VOLUMEN DE FLUIDOS
    right_sections = (
        render_sec_block("MOTOR", s1["motor"]) +
        render_sec_block("PESOS", s1["pesos"]) +
        render_sec_block("SISTEMA COMBUSTIBLE", s1["comb"]) +
        render_sec_block("SISTEMA DE FRENOS", s1["frenos"]) +
        render_sec_block("VOLUMEN DE FLUIDOS / CAPACIDADES", s1["fluidos"])
    )

    hero_img = m.get("hero_image", "")
    has_hero = bool(hero_img)
    img_hidden = "" if has_hero else "hidden"
    ph_hidden = "hidden" if has_hero else ""

    return f'''
    <!-- HOJA 1: {cid} -->
    <div class="sheet-page page-1 bg-white shadow-xl rounded-sm mx-auto flex flex-col justify-between" id="sheet1-{cid}">
      <!-- Encabezado Hoja 1 -->
      <div>
        <div class="flex items-start justify-between border-b border-slate-200 pb-2 mb-2">
          <div>
            <h1 class="text-[18px] font-black text-slate-950 tracking-tight leading-none mb-1">{m["title_h1"]}</h1>
            <div class="text-[9.5px] font-medium text-slate-600 flex flex-wrap gap-x-2.5 gap-y-0.5">
              <span><strong class="text-slate-900 font-bold">FICHA TÉCNICA</strong></span>
              <span><span class="font-semibold text-slate-800">Vehículo</span>: {m["vehiculo"]}</span>
              <span><span class="font-semibold text-slate-800">Marca</span>: {m["marca"]}</span>
              <span><span class="font-semibold text-slate-800">Modelo</span>: {m["modelo"]}</span>
              <span><span class="font-semibold text-slate-800">Versión</span>: {m["version"]}</span>
              <span><span class="font-semibold text-slate-800">Tracción</span>: {m["traccion"]}</span>
            </div>
          </div>
          {render_logo_header()}
        </div>

        <!-- Grid 2 Columnas Hoja 1 -->
        <div class="grid grid-cols-12 gap-4 items-start">
          <!-- Columna Izquierda (5 columnas) -->
          <div class="col-span-5 flex flex-col">
            <!-- Contenedor Imagen Principal con Placeholder interactivo -->
            <div class="relative w-full h-[140px] bg-slate-50 border border-slate-200 rounded-lg overflow-hidden flex flex-col items-center justify-center p-1.5 mb-2 group cursor-pointer hover:border-slate-400 transition" onclick="triggerImgUpload('{cid}_hero')">
              <img id="img_{cid}_hero" src="{hero_img}" class="{img_hidden} w-full h-full object-contain z-0" alt="{m['title_h1']}" />
              <div id="ph_{cid}_hero" class="{ph_hidden} text-center z-1 flex flex-col items-center justify-center p-2">
                <svg class="w-8 h-8 text-slate-300 group-hover:text-slate-700 transition mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                <span class="text-[9.5px] font-bold text-slate-500 group-hover:text-slate-900 transition">Clic para cargar imagen del vehículo</span>
                <span class="text-[8px] text-slate-400">PNG, JPG, WebP (o arrastrar aquí)</span>
              </div>
              <input type="file" id="file_{cid}_hero" class="hidden" accept="image/*" onchange="handleImgFile(event, '{cid}_hero')" />
            </div>

            <!-- Secciones Izquierda -->
            {left_sections}
          </div>

          <!-- Columna Derecha (7 columnas) -->
          <div class="col-span-7">
            {right_sections}
          </div>
        </div>
      </div>

      <!-- Pie de página Hoja 1 -->
      <div class="pt-2 border-t border-slate-200 flex justify-between items-center text-[10px] text-slate-400">
        <span class="text-[9px] text-slate-400 font-mono tracking-wider">PLANCHART GLOBAL · ESPECIFICACIÓN OFICIAL VENEZUELA</span>
        <span class="font-bold text-slate-500">1 / 2</span>
      </div>
    </div>
    '''

