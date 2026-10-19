"""
Componente de tarjeta para el visualizador de especificaciones técnicas.
Encapsula la representación visual de cada tarjeta de modelo (resumen y desglose exhaustivo).
Módulo desacoplado (< 500 líneas).
"""

def get_card_template_js():
    return """
    function renderSingleCard(c, isExpanded, t) {
      const title = c.title[currentLang] || c.title.es;
      const subtitle = c.subtitle[currentLang] || c.subtitle.es;
      const tag = c.tag[currentLang] || c.tag.es;
      const fuelBadge = c.fuel_badge[currentLang] || c.fuel_badge.es;
      const category = c.category[currentLang] || c.category.es;
      const highlights = c.highlights[currentLang] || c.highlights.es;

      return `
      <article class="bg-white rounded-2xl border border-slate-200 border-l-[6px] border-l-amber-500 shadow-xs hover:shadow-md transition-all overflow-hidden">
        
        <!-- CABECERA DE LA TARJETA -->
        <div class="p-5 sm:p-6 pb-4">
          <div class="flex items-center justify-between gap-3">
            <div class="flex flex-wrap items-center gap-2">
              <!-- Badge ID Verde Esmeralda -->
              <span class="inline-flex items-center px-2.5 py-0.5 rounded text-xs font-mono font-bold border border-emerald-500 bg-emerald-50/70 text-emerald-800 tracking-wider">
                ${c.badge_id}
              </span>

              <!-- Badge Punto Ambar -->
              <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-50 text-amber-800 border border-amber-200">
                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                ${fuelBadge}
              </span>

              <!-- Badge Gris Suave -->
              <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-slate-100 text-slate-700 border border-slate-200">
                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                ${category} · ${tag}
              </span>
            </div>

            <!-- Flecha de despliegue v -->
            <button 
              onclick="toggleCard('${c.id}')" 
              class="w-8 h-8 rounded-full bg-slate-50 hover:bg-slate-100 border border-slate-200 flex items-center justify-center text-slate-500 hover:text-slate-800 transition" 
              title="Expandir / Contraer tarjeta">
              <svg class="w-4 h-4 transform transition-transform duration-200 ${isExpanded ? 'rotate-180' : ''}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
          </div>

          <!-- Titulo Grande en Negrita -->
          <h2 class="text-lg sm:text-xl font-bold text-slate-900 mt-3 tracking-tight leading-snug">
            ${title}
          </h2>

          <!-- Subtitulo en gris -->
          <p class="text-xs sm:text-sm text-slate-600 font-medium mt-1">
            ${subtitle}
          </p>

          <!-- Linea divisoria horizontal verde esmeralda suave -->
          <div class="border-b border-emerald-400 mt-4"></div>
        </div>

        <!-- BLOQUES DE CONTENIDO -->
        <div class="px-5 sm:px-6 pb-6 space-y-4">
          
          <!-- Resumen Superior de 4 Bloques Clave -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <!-- 1. Dimensiones -->
            <div class="bg-slate-50/80 rounded-xl p-3.5 border border-slate-200/80 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-slate-200 text-xs font-bold text-slate-800">
                  <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
                  ${t.blockDimensions}
                </div>
                <ul class="space-y-1.5 text-xs">
                  ${c.summary_blocks.dimensions.map(item => `
                    <li class="flex justify-between items-baseline gap-2">
                      <span class="text-slate-500 truncate" title="${item.label[currentLang]}">${item.label[currentLang]}</span>
                      <span class="font-semibold text-slate-900 font-mono text-right shrink-0">${item.value[currentLang]}</span>
                    </li>
                  `).join('')}
                </ul>
              </div>
            </div>

            <!-- 2. Tren Motriz -->
            <div class="bg-slate-50/80 rounded-xl p-3.5 border border-slate-200/80 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-slate-200 text-xs font-bold text-slate-800">
                  <svg class="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                  ${t.blockPowertrain}
                </div>
                <ul class="space-y-1.5 text-xs">
                  ${c.summary_blocks.powertrain.map(item => `
                    <li class="flex justify-between items-baseline gap-2">
                      <span class="text-slate-500 truncate" title="${item.label[currentLang]}">${item.label[currentLang]}</span>
                      <span class="font-semibold text-slate-900 font-mono text-right shrink-0">${item.value[currentLang]}</span>
                    </li>
                  `).join('')}
                </ul>
              </div>
            </div>

            <!-- 3. Chasis y Seguridad -->
            <div class="bg-slate-50/80 rounded-xl p-3.5 border border-slate-200/80 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-slate-200 text-xs font-bold text-slate-800">
                  <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                  ${t.blockChassis}
                </div>
                <ul class="space-y-1.5 text-xs">
                  ${c.summary_blocks.chassis_safety.map(item => `
                    <li class="flex justify-between items-baseline gap-2">
                      <span class="text-slate-500 truncate" title="${item.label[currentLang]}">${item.label[currentLang]}</span>
                      <span class="font-semibold text-slate-900 font-mono text-right shrink-0">${item.value[currentLang]}</span>
                    </li>
                  `).join('')}
                </ul>
              </div>
            </div>

            <!-- 4. Equipamiento -->
            <div class="bg-slate-50/80 rounded-xl p-3.5 border border-slate-200/80 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-slate-200 text-xs font-bold text-slate-800">
                  <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                  ${t.blockEquipment}
                </div>
                <ul class="space-y-1.5 text-xs">
                  ${c.summary_blocks.equipment.map(item => `
                    <li class="flex justify-between items-baseline gap-2">
                      <span class="text-slate-500 truncate" title="${item.label[currentLang]}">${item.label[currentLang]}</span>
                      <span class="font-semibold text-slate-900 font-mono text-right shrink-0">${item.value[currentLang]}</span>
                    </li>
                  `).join('')}
                </ul>
              </div>
            </div>
          </div>

          <!-- VISTA EXPANDIDA: TODAS LAS CATEGORÍAS Y ESPECIFICACIONES (100% EXCEL) -->
          ${isExpanded ? `
          <div class="mt-4 pt-4 border-t border-slate-200 space-y-4">
            <div class="flex items-center justify-between pb-2 border-b border-slate-200">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <h3 class="text-sm font-bold text-slate-900">${t.fullSpecsHeading}</h3>
                <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-200">
                  ${c.total_specs_count} ${t.specsCountBadge}
                </span>
              </div>
              <span class="text-xs text-slate-500 font-medium hidden sm:inline">
                ${t.fullSpecsBadge}
              </span>
            </div>

            <!-- Lista exhaustiva por todas las categorías sin omitir ninguna fila -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              ${c.all_categories.map(cat => `
                <div class="bg-white rounded-xl border border-slate-200 shadow-xs overflow-hidden">
                  <div class="px-3.5 py-2 bg-slate-100/90 border-b border-slate-200 flex items-center justify-between">
                    <span class="font-bold text-xs text-slate-800 tracking-tight">
                      ${cat.category_name[currentLang] || cat.category_name.es}
                    </span>
                    <span class="text-[11px] font-mono font-semibold px-1.5 py-0.5 rounded bg-white text-slate-600 border border-slate-200">
                      ${cat.specs.length}
                    </span>
                  </div>
                  <ul class="divide-y divide-slate-100 text-xs">
                    ${cat.specs.map(spec => `
                      <li class="px-3.5 py-2 flex justify-between items-baseline gap-3 hover:bg-slate-50 transition">
                        <span class="text-slate-600 font-medium">
                          ${spec.label[currentLang] || spec.label.es}
                        </span>
                        <span class="font-mono font-bold text-right shrink-0 ${
                          spec.value[currentLang] === '●' 
                            ? 'text-emerald-700 font-black' 
                            : spec.value[currentLang] === '○'
                              ? 'text-blue-700 font-black'
                              : spec.value[currentLang] === '-'
                                ? 'text-slate-400 font-normal'
                                : 'text-slate-900'
                        }">
                          ${spec.value[currentLang] || spec.value.es}
                        </span>
                      </li>
                    `).join('')}
                  </ul>
                </div>
              `).join('')}
            </div>
          </div>
          ` : ''}

          <!-- CAJA DESTACADA INFERIOR (Arreglo verde) -->
          <div class="border border-emerald-300 bg-emerald-50 text-emerald-950 rounded-xl p-3.5 flex items-start gap-3 shadow-xs">
            <div class="w-7 h-7 rounded-lg bg-emerald-200/70 text-emerald-800 flex items-center justify-center shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path>
              </svg>
            </div>
            <div class="flex-1 text-xs">
              <h4 class="font-bold text-emerald-900 mb-0.5 flex items-center gap-1.5">
                ${t.keyHighlights}
              </h4>
              <p class="leading-relaxed text-emerald-950 font-medium">
                ${highlights}
              </p>
            </div>
          </div>

          <!-- BOTON PARA ABRIR LAS 100% FILAS DEL EXCEL -->
          <div class="flex items-center justify-between pt-2">
            <span class="text-xs text-slate-500">
              ${t.sourceFile} <span class="font-mono font-medium">${c.model_key}</span> · ${t.officialSheet}
            </span>
            <button 
              onclick="openRawModal('${c.model_key}', '${c.id}')"
              class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 rounded-lg transition shadow-xs">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path></svg>
              ${t.viewAllBtn}
            </button>
          </div>

        </div>
      </article>
      `;
    }
    """
