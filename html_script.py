"""
Lógica JavaScript del cliente para el visualizador bilingüe (ES / EN).
Coordina interactividad, traducción en caliente, búsqueda y modales (< 500 líneas).
"""

from html_card_component import get_card_template_js

def get_client_script(json_data_str):
    card_template_js = get_card_template_js()

    return f"""
  <script id="specs-data-json" type="application/json">
{json_data_str}
  </script>

  <script>
    const SPECS_DATA = JSON.parse(document.getElementById('specs-data-json').textContent);
    let currentLang = localStorage.getItem('ep_specs_lang') || 'es';
    let activeTab = 'ALL';
    let searchQuery = '';
    let expandedCards = new Set();
    let modalRowsData = [];
    let modalVersionId = '';
    let modalSheetName = '';

    const I18N = {{
      es: {{
        headerTitle: 'Especificaciones Técnicas por Modelo',
        officialBadge: '100% Excel Oficial',
        headerSubtitle: '8 Modelos · 15 Versiones · 1,213 especificaciones técnicas extraídas fila por fila',
        searchPlaceholder: 'Buscar motor, versión, tracción, código...',
        expandAll: 'Expandir Todo',
        collapseAll: 'Colapsar Todo',
        showing: 'Mostrando:',
        cardsCount: 'tarjetas de especificación técnica',
        legend: 'Simbología:',
        symStandard: '● De serie',
        symOptional: '○ Opcional',
        symNA: '- No disponible',
        tabAll: 'Todos los Modelos (15)',
        noResultsTitle: 'No se encontraron especificaciones',
        noResultsDesc: 'Prueba cambiando los términos de búsqueda o seleccionando otra pestaña.',
        blockDimensions: 'Dimensiones y Capacidades',
        blockPowertrain: 'Tren Motriz y Rendimiento',
        blockChassis: 'Chasis, Frenos y Seguridad',
        blockEquipment: 'Equipamiento y Tecnología',
        keyHighlights: 'Arreglo / Configuración Técnica Clave:',
        sourceFile: 'Archivo origen:',
        officialSheet: 'Hoja oficial',
        viewAllBtn: 'Ver Hoja Completa (100% Excel)',
        modalTitle: 'Especificaciones Completas Excel',
        modalSubtitle: 'Recorrido íntegro de todas las filas sin filtros ni omisiones',
        modalSearch: 'Filtrar dentro de esta hoja...',
        thRow: 'Fila',
        thCat: 'Categoría',
        thSpec: 'Especificación Técnica',
        thSub: 'Subparámetro',
        thVal: 'Valor Versión',
        modalRowsExtracted: 'filas extraídas',
        modalClose: 'Cerrar',
        fullSpecsHeading: 'Desglose Completo de Especificaciones de la Versión',
        fullSpecsBadge: '100% Especificaciones de la Hoja',
        specsCountBadge: 'especificaciones técnicas',
      }},
      en: {{
        headerTitle: 'Technical Specifications by Model',
        officialBadge: '100% Official Excel',
        headerSubtitle: '8 Models · 15 Versions · 1,213 technical specifications extracted row-by-row',
        searchPlaceholder: 'Search engine, version, drivetrain, code...',
        expandAll: 'Expand All',
        collapseAll: 'Collapse All',
        showing: 'Showing:',
        cardsCount: 'technical specification cards',
        legend: 'Legend:',
        symStandard: '● Standard',
        symOptional: '○ Optional',
        symNA: '- Not available',
        tabAll: 'All Models (15)',
        noResultsTitle: 'No specifications found',
        noResultsDesc: 'Try adjusting your search terms or selecting another model tab.',
        blockDimensions: 'Dimensions & Capacities',
        blockPowertrain: 'Powertrain & Performance',
        blockChassis: 'Chassis, Brakes & Safety',
        blockEquipment: 'Equipment & Technology',
        keyHighlights: 'Key Technical Configuration / Highlights:',
        sourceFile: 'Source file:',
        officialSheet: 'Official sheet',
        viewAllBtn: 'View Full Sheet (100% Excel)',
        modalTitle: 'Complete Excel Specifications',
        modalSubtitle: 'Exhaustive review of all rows without filters or omissions',
        modalSearch: 'Filter within this sheet...',
        thRow: 'Row',
        thCat: 'Category',
        thSpec: 'Technical Specification',
        thSub: 'Subparameter',
        thVal: 'Version Value',
        modalRowsExtracted: 'rows extracted',
        modalClose: 'Close',
        fullSpecsHeading: 'Complete Technical Breakdown for Version',
        fullSpecsBadge: '100% Sheet Specifications',
        specsCountBadge: 'technical specifications',
      }}
    }};

    function setLanguage(lang) {{
      currentLang = lang;
      try {{
        localStorage.setItem('ep_specs_lang', lang);
      }} catch (e) {{}}

      const btnEs = document.getElementById('lang-btn-es');
      const btnEn = document.getElementById('lang-btn-en');
      if (lang === 'es') {{
        btnEs.className = 'px-2.5 py-1 rounded-md transition flex items-center gap-1.5 bg-white text-emerald-800 shadow-xs font-bold';
        btnEn.className = 'px-2.5 py-1 rounded-md transition flex items-center gap-1.5 text-slate-600 hover:text-slate-900';
      }} else {{
        btnEn.className = 'px-2.5 py-1 rounded-md transition flex items-center gap-1.5 bg-white text-emerald-800 shadow-xs font-bold';
        btnEs.className = 'px-2.5 py-1 rounded-md transition flex items-center gap-1.5 text-slate-600 hover:text-slate-900';
      }}

      const t = I18N[currentLang];
      document.getElementById('page-title').textContent = `${{t.headerTitle}} | Catálogo Oficial`;
      document.getElementById('ui-header-title').firstElementChild.textContent = t.headerTitle;
      document.getElementById('ui-badge-official').textContent = t.officialBadge;
      document.getElementById('ui-header-subtitle').textContent = t.headerSubtitle;
      document.getElementById('search-input').placeholder = t.searchPlaceholder;
      document.getElementById('ui-label-showing').textContent = t.showing;
      document.getElementById('ui-label-cards').textContent = t.cardsCount;
      document.getElementById('ui-label-legend').textContent = t.legend;
      document.getElementById('ui-sym-standard').textContent = t.symStandard;
      document.getElementById('ui-sym-optional').textContent = t.symOptional;
      document.getElementById('ui-sym-na').textContent = t.symNA;

      document.getElementById('modal-title').textContent = t.modalTitle;
      document.getElementById('modal-subtitle').textContent = t.modalSubtitle;
      document.getElementById('modal-search').placeholder = t.modalSearch;
      document.getElementById('th-row').textContent = t.thRow;
      document.getElementById('th-cat').textContent = t.thCat;
      document.getElementById('th-spec').textContent = t.thSpec;
      document.getElementById('th-sub').textContent = t.thSub;
      document.getElementById('th-val').textContent = t.thVal;
      document.getElementById('btn-modal-close').textContent = t.modalClose;

      updateToggleAllBtn();
      renderTabs();
      renderCards();

      if (!document.getElementById('raw-modal').classList.contains('hidden')) {{
        renderModalTable(modalRowsData, modalVersionId);
      }}
    }}

    function updateToggleAllBtn() {{
      const t = I18N[currentLang];
      const allIds = [];
      SPECS_DATA.models.forEach(m => m.cards.forEach(c => allIds.push(c.id)));
      const isAll = expandedCards.size === allIds.length && allIds.length > 0;
      document.getElementById('btn-toggle-all').textContent = isAll ? t.collapseAll : t.expandAll;
    }}

    function getTabModels() {{
      const t = I18N[currentLang];
      const tabs = [{{ id: 'ALL', label: t.tabAll }}];
      SPECS_DATA.models.forEach(m => {{
        tabs.push({{ id: m.key, label: m.name[currentLang] || m.key }});
      }});
      return tabs;
    }}

    function renderTabs() {{
      const container = document.getElementById('tabs-container');
      const tabs = getTabModels();
      container.innerHTML = tabs.map(tab => {{
        const isActive = activeTab === tab.id;
        return `
          <button 
            onclick="setTab('${{tab.id}}')" 
            class="px-3 py-1.5 rounded-lg transition-all font-semibold whitespace-nowrap ${{
              isActive 
                ? 'bg-emerald-600 text-white shadow-xs' 
                : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100 hover:text-slate-900'
            }}">
            ${{tab.label}}
          </button>
        `;
      }}).join('');
    }}

    function setTab(tabId) {{
      activeTab = tabId;
      renderTabs();
      renderCards();
    }}

    function toggleCard(cardId) {{
      if (expandedCards.has(cardId)) {{
        expandedCards.delete(cardId);
      }} else {{
        expandedCards.add(cardId);
      }}
      updateToggleAllBtn();
      renderCards();
    }}

    {card_template_js}

    function renderCards() {{
      const container = document.getElementById('cards-container');
      const t = I18N[currentLang];
      let cards = [];

      SPECS_DATA.models.forEach(model => {{
        if (activeTab === 'ALL' || model.key === activeTab) {{
          cards.push(...model.cards);
        }}
      }});

      if (searchQuery.trim() !== '') {{
        const q = searchQuery.toLowerCase().trim();
        cards = cards.filter(c => {{
          const title = (c.title[currentLang] || '').toLowerCase();
          const subtitle = (c.subtitle[currentLang] || '').toLowerCase();
          const tag = (c.tag[currentLang] || '').toLowerCase();
          const highlights = (c.highlights[currentLang] || '').toLowerCase();
          const modelName = (c.model_name[currentLang] || '').toLowerCase();
          const badgeId = (c.badge_id || '').toLowerCase();
          return (
            title.includes(q) ||
            subtitle.includes(q) ||
            badgeId.includes(q) ||
            tag.includes(q) ||
            highlights.includes(q) ||
            modelName.includes(q)
          );
        }});
      }}

      document.getElementById('results-count').textContent = cards.length;

      if (cards.length === 0) {{
        container.innerHTML = `
          <div class="bg-white rounded-2xl p-12 text-center border border-slate-200">
            <h4 class="text-sm font-bold text-slate-700">${{t.noResultsTitle}}</h4>
            <p class="text-xs text-slate-500 mt-1">${{t.noResultsDesc}}</p>
          </div>
        `;
        return;
      }}

      container.innerHTML = cards.map(c => {{
        const isExpanded = expandedCards.has(c.id);
        return renderSingleCard(c, isExpanded, t);
      }}).join('');
    }}

    function openRawModal(modelKey, versionId) {{
      const model = SPECS_DATA.models.find(m => m.key === modelKey);
      if (!model) return;

      const card = model.cards.find(c => c.id === versionId);
      const title = card ? (card.title[currentLang] || card.title.es) : model.name[currentLang];

      modalRowsData = model.rows;
      modalVersionId = versionId;
      modalSheetName = model.sheet_name;

      const t = I18N[currentLang];
      document.getElementById('modal-title').textContent = title;
      document.getElementById('modal-subtitle').textContent = `${{t.sourceFile}} ${{model.sheet_name}} · Total: ${{model.rows.length}} ${{t.modalRowsExtracted}}`;
      document.getElementById('modal-count').textContent = `${{model.rows.length}} ${{t.modalRowsExtracted}}`;

      document.getElementById('modal-search').value = '';
      renderModalTable(model.rows, versionId);

      document.getElementById('raw-modal').classList.remove('hidden');
    }}

    function closeRawModal() {{
      document.getElementById('raw-modal').classList.add('hidden');
    }}

    function renderModalTable(rows, versionId) {{
      const tbody = document.getElementById('modal-table-body');
      const q = document.getElementById('modal-search').value.toLowerCase().trim();

      const filtered = rows.filter(r => {{
        if (!q) return true;
        const cat = (r.category[currentLang] || r.category.es).toLowerCase();
        const param = (r.param_name[currentLang] || r.param_name.es).toLowerCase();
        const subparam = (r.subparam_name[currentLang] || r.subparam_name.es).toLowerCase();
        const val = (r.values[currentLang][versionId] || '').toLowerCase();
        return (
          cat.includes(q) ||
          param.includes(q) ||
          subparam.includes(q) ||
          val.includes(q)
        );
      }});

      tbody.innerHTML = filtered.map(r => {{
        const val = r.values[currentLang][versionId] || '-';
        return `
          <tr class="hover:bg-slate-50 transition">
            <td class="p-2 font-mono text-slate-400">${{r.row_num}}</td>
            <td class="p-2 text-slate-600 font-medium">${{r.category[currentLang] || r.category.es}}</td>
            <td class="p-2 text-slate-900 font-medium">${{r.param_name[currentLang] || r.param_name.es}}</td>
            <td class="p-2 text-slate-500">${{r.subparam_name[currentLang] || r.subparam_name.es || '-'}}</td>
            <td class="p-2 font-mono font-bold text-emerald-700 bg-emerald-50/50">${{val}}</td>
          </tr>
        `;
      }}).join('');
    }}

    document.getElementById('search-input').addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      renderCards();
    }});

    document.getElementById('modal-search').addEventListener('input', () => {{
      renderModalTable(modalRowsData, modalVersionId);
    }});

    document.getElementById('btn-toggle-all').addEventListener('click', () => {{
      const allIds = [];
      SPECS_DATA.models.forEach(m => m.cards.forEach(c => allIds.push(c.id)));
      if (expandedCards.size === allIds.length) {{
        expandedCards.clear();
      }} else {{
        allIds.forEach(id => expandedCards.add(id));
      }}
      updateToggleAllBtn();
      renderCards();
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeRawModal();
    }});

    document.getElementById('raw-modal').addEventListener('click', (e) => {{
      if (e.target.id === 'raw-modal') closeRawModal();
    }});

    setLanguage(currentLang);
  </script>
</body>
</html>
"""
