# -*- coding: utf-8 -*-
"""Generador final de fichas_tecnicas.html modular y limpio."""

import json
from render_sheet1 import render_sheet1
from render_sheet2 import render_sheet2

def generate_html():
    with open('fichas_ready.json', 'r', encoding='utf-8') as f:
        models = json.load(f)

    # Tabs generation
    tabs_html_parts = []
    for idx, m in enumerate(models):
        cid = m["id"]
        tab = m["tab"]
        active_class = "active bg-red-600 text-white shadow-xs font-bold" if idx == 0 else "bg-white text-slate-700 hover:bg-slate-100 hover:text-slate-900 border border-slate-200"
        tabs_html_parts.append(f'''
        <button id="tab-btn-{cid}" onclick="selectModel('{cid}')" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold transition whitespace-nowrap flex items-center gap-1.5 {active_class}">
          <span>{tab}</span>
        </button>
        ''')
    tabs_html = "\n".join(tabs_html_parts)

    # Vehicles containers generation
    vehicles_html_parts = []
    for idx, m in enumerate(models):
        cid = m["id"]
        h1 = render_sheet1(m)
        h2 = render_sheet2(m)
        hidden_class = "" if idx == 0 else "hidden"
        vehicles_html_parts.append(f'''
        <div id="model-wrapper-{cid}" class="model-wrapper {hidden_class}" data-model-id="{cid}">
          {h1}
          {h2}
        </div>
        ''')
    vehicles_html = "\n".join(vehicles_html_parts)

    html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fichas Técnicas Oficiales | PLANCHART GLOBAL</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            brand: {{
              red: '#d32f2f',
              dark: '#0f172a',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    /* ESTILOS EXACTOS DE PANTALLA E IMPRESIÓN */
    @page {{
      size: letter;
      margin: 8mm 10mm;
    }}

    body {{
      background-color: #f1f5f9;
      color: #0f172a;
      -webkit-font-smoothing: antialiased;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    }}

    /* Hoja física en pantalla con proporciones Letter */
    .sheet-page {{
      width: 215.9mm;
      min-height: 279.4mm;
      max-height: 279.4mm;
      box-sizing: border-box;
      padding: 8mm 12mm;
      margin: 20px auto;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      page-break-inside: avoid;
      break-inside: avoid;
      overflow: hidden;
    }}

    .page-1 {{
      page-break-after: always;
      break-after: page;
    }}

    .page-2 {{
      page-break-after: auto;
      break-after: auto;
    }}

    /* COMPORTAMIENTO ESTRICTO DE IMPRESIÓN */
    @media print {{
      @page {{
        size: letter;
        margin: 8mm 10mm;
      }}

      html, body {{
        background: #ffffff !important;
        margin: 0 !important;
        padding: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      main {{
        padding: 0 !important;
        margin: 0 !important;
      }}

      .no-print {{
        display: none !important;
      }}

      /* En impresión, solo se imprime el wrapper activo */
      .model-wrapper.hidden {{
        display: none !important;
      }}

      .model-wrapper:not(.hidden) {{
        display: block !important;
      }}

      .sheet-page {{
        width: 100% !important;
        height: 263.4mm !important;
        min-height: 263.4mm !important;
        max-height: 263.4mm !important;
        margin: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        overflow: hidden !important;
      }}

      .page-1 {{
        page-break-after: always !important;
        break-after: page !important;
      }}

      .page-2 {{
        page-break-after: avoid !important;
        break-after: avoid !important;
      }}
    }}

    /* Barra scroll suave para navegación horizontal */
    .custom-scrollbar::-webkit-scrollbar {{
      height: 5px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #f1f5f9;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 4px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
  </style>
</head>
<body class="min-h-screen">

  <!-- BARRA DE NAVEGACIÓN Y ACCIONES (NO IMPRIMIBLE) -->
  <header class="no-print bg-slate-900 text-white sticky top-0 z-50 shadow-md border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
        <!-- Logo y Título -->
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-lg bg-red-600 flex items-center justify-center font-black text-white text-base shadow-sm">
            PG
          </div>
          <div>
            <h1 class="text-sm font-black tracking-tight flex items-center gap-2">
              <span>PLANCHART GLOBAL</span>
              <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-red-500/20 text-red-300 border border-red-500/30">Fichas Técnicas Oficiales</span>
            </h1>
            <p class="text-[11px] text-slate-400">17 Modelos Homologados (Incluye Minivan M09, Mini Trucks 2T y VR210 12 TON) · Formato 2 Páginas por Modelo (Carta / Letter)</p>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="flex items-center gap-2.5">
          <button onclick="window.print()" class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-2 shadow-sm hover:shadow active:scale-95">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
            <span>🖨️ Imprimir Ficha Técnica (PDF)</span>
          </button>
        </div>
      </div>

      <!-- Barra de Pestañas / Tabs por Modelo -->
      <div class="mt-2.5 pt-2.5 border-t border-slate-800 flex items-center gap-1.5 overflow-x-auto pb-1.5 custom-scrollbar text-xs">
        {tabs_html}
      </div>
    </div>
  </header>

  <!-- CONTENEDOR PRINCIPAL DE FICHAS -->
  <main class="py-4 sm:py-6 px-2">
    {vehicles_html}
  </main>

  <!-- SCRIPT INTERACTIVO -->
  <script>
    // Seleccionar modelo activo
    function selectModel(modelId) {{
      // Actualizar wrappers
      document.querySelectorAll('.model-wrapper').forEach(el => {{
        el.classList.add('hidden');
      }});
      const targetWrapper = document.getElementById('model-wrapper-' + modelId);
      if (targetWrapper) {{
        targetWrapper.classList.remove('hidden');
      }}

      // Actualizar estilo botones tabs
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.classList.remove('active', 'bg-red-600', 'text-white', 'font-bold');
        btn.classList.add('bg-white', 'text-slate-700', 'border', 'border-slate-200');
      }});
      const activeBtn = document.getElementById('tab-btn-' + modelId);
      if (activeBtn) {{
        activeBtn.classList.remove('bg-white', 'text-slate-700', 'border', 'border-slate-200');
        activeBtn.classList.add('active', 'bg-red-600', 'text-white', 'font-bold');
      }}

      // Scroll suave arriba
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Manejo de carga de imagen en placeholder
    function triggerImgUpload(targetId) {{
      const input = document.getElementById('file_' + targetId);
      if (input) input.click();
    }}

    function handleImgFile(e, targetId) {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) {{
        const img = document.getElementById('img_' + targetId);
        const ph = document.getElementById('ph_' + targetId);
        if (img && ph) {{
          img.src = evt.target.result;
          img.classList.remove('hidden');
          ph.classList.add('hidden');
        }}
      }};
      reader.readAsDataURL(file);
    }}
  </script>
</body>
</html>
'''

    with open('fichas_tecnicas.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("fichas_tecnicas.html generado con éxito.")

if __name__ == '__main__':
    generate_html()
