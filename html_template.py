"""
Plantilla HTML y estructura de presentación bilingüe (ES / EN).
Incluye selector de idioma reactivo y estructura modular (< 500 líneas).
"""

def get_html_head():
    return """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="page-title">Especificaciones Técnicas por Modelo | Catálogo Oficial</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #f8fafc;
      color: #0f172a;
      -webkit-font-smoothing: antialiased;
    }
    .custom-scrollbar::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
      background: #f1f5f9;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {
      background: #94a3b8;
    }
  </style>
</head>
<body class="min-h-screen bg-slate-50 text-slate-800">
"""

def get_html_body_header():
    return """
  <!-- Header Principal -->
  <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <!-- Logo / Titulo -->
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white shadow-md shadow-emerald-500/20 shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"></path>
            </svg>
          </div>
          <div>
            <h1 id="ui-header-title" class="text-lg font-bold text-slate-900 tracking-tight flex items-center gap-2 flex-wrap">
              <span>Especificaciones Técnicas por Modelo</span>
              <span id="ui-badge-official" class="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200">100% Excel Oficial</span>
            </h1>
            <p id="ui-header-subtitle" class="text-xs text-slate-500">8 Modelos · 15 Versiones · 1,213 especificaciones técnicas extraídas fila por fila</p>
          </div>
        </div>

        <!-- Selector de Idioma, Buscador y Acciones -->
        <div class="flex flex-wrap items-center gap-2.5">
          <!-- SELECTOR DE IDIOMA REACTIVO (ES / EN) -->
          <div class="inline-flex items-center p-0.5 bg-slate-100 border border-slate-200 rounded-lg text-xs font-semibold shadow-xs">
            <button id="lang-btn-es" onclick="setLanguage('es')" class="px-2.5 py-1 rounded-md transition flex items-center gap-1.5 bg-white text-emerald-800 shadow-xs font-bold">
              <span>🇪🇸</span>
              <span>Español</span>
            </button>
            <button id="lang-btn-en" onclick="setLanguage('en')" class="px-2.5 py-1 rounded-md transition flex items-center gap-1.5 text-slate-600 hover:text-slate-900">
              <span>🇺🇸</span>
              <span>English</span>
            </button>
          </div>

          <!-- Buscador Reactivo -->
          <div class="relative w-full sm:w-64">
            <svg class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
            <input type="text" id="search-input" placeholder="Buscar motor, versión, tracción, código..." class="w-full pl-9 pr-3 py-1.5 text-xs bg-slate-100 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition-all">
          </div>

          <!-- Boton Expandir / Colapsar Todo -->
          <button id="btn-toggle-all" class="px-3 py-1.5 text-xs font-medium text-slate-700 bg-white border border-slate-300 rounded-lg hover:bg-slate-50 transition shadow-xs whitespace-nowrap">
            Expandir Todo
          </button>
        </div>
      </div>

      <!-- Selector de Pestañas por Modelo (8 modelos) -->
      <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center gap-1.5 overflow-x-auto pb-1 custom-scrollbar text-xs font-medium" id="tabs-container">
      </div>
    </div>
  </header>

  <!-- Contenedor Principal -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <!-- Barra de Estado / Filtros Activos -->
    <div class="mb-5 flex flex-wrap items-center justify-between gap-3 text-xs text-slate-600 bg-white px-4 py-2.5 rounded-xl border border-slate-200 shadow-xs">
      <div class="flex items-center gap-2">
        <span id="ui-label-showing" class="font-semibold text-slate-800">Mostrando:</span>
        <span id="results-count" class="font-mono bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded border border-emerald-200 font-bold">15</span>
        <span id="ui-label-cards">tarjetas de especificación técnica</span>
      </div>
      <div class="flex items-center gap-2">
        <span id="ui-label-legend" class="text-slate-400">Simbología:</span>
        <span id="ui-sym-standard" class="inline-flex items-center gap-1 font-mono text-emerald-700 font-bold">● De serie</span>
        <span id="ui-sym-optional" class="inline-flex items-center gap-1 font-mono text-blue-700 font-bold">○ Opcional</span>
        <span id="ui-sym-na" class="inline-flex items-center gap-1 font-mono text-slate-400">- No disponible</span>
      </div>
    </div>

    <!-- Grid de Tarjetas de Especificaciones -->
    <div id="cards-container" class="space-y-6"></div>
  </main>

  <!-- Modal para ver el 100% de filas en bruto del Excel -->
  <div id="raw-modal" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs hidden flex items-center justify-center p-3 sm:p-6">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-5xl max-h-[92vh] flex flex-col border border-slate-200 overflow-hidden">
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
        <div>
          <h3 id="modal-title" class="text-base font-bold text-slate-900">Especificaciones Completas Excel</h3>
          <p id="modal-subtitle" class="text-xs text-slate-500">Recorrido íntegro de todas las filas sin filtros ni omisiones</p>
        </div>
        <button onclick="closeRawModal()" class="w-8 h-8 rounded-lg bg-white border border-slate-200 text-slate-500 hover:text-slate-800 hover:bg-slate-100 flex items-center justify-center transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <div class="px-6 py-2.5 bg-white border-b border-slate-100">
        <input type="text" id="modal-search" placeholder="Filtrar dentro de esta hoja..." class="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500">
      </div>

      <div class="flex-1 overflow-auto p-6 custom-scrollbar">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="bg-slate-100 text-slate-700 font-semibold border-b border-slate-200 sticky top-0">
              <th id="th-row" class="p-2.5 w-12 font-mono">Fila</th>
              <th id="th-cat" class="p-2.5 w-40">Categoría</th>
              <th id="th-spec" class="p-2.5">Especificación Técnica</th>
              <th id="th-sub" class="p-2.5 w-40">Subparámetro</th>
              <th id="th-val" class="p-2.5 w-36 text-emerald-800 bg-emerald-50/70">Valor Versión</th>
            </tr>
          </thead>
          <tbody id="modal-table-body" class="divide-y divide-slate-100 font-sans"></tbody>
        </table>
      </div>

      <div class="px-6 py-3 border-t border-slate-200 bg-slate-50 flex items-center justify-between text-xs text-slate-500">
        <span id="modal-count">Total filas</span>
        <button id="btn-modal-close" onclick="closeRawModal()" class="px-4 py-1.5 bg-slate-800 text-white rounded-lg hover:bg-slate-900 transition font-medium">Cerrar</button>
      </div>
    </div>
  </div>
"""
