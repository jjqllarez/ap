# -*- coding: utf-8 -*-
import re

with open('fichas_tecnicas.html', 'r', encoding='utf-8') as f:
    html = f.read()

underline_matches = re.findall(r'underline', html)
decoration_matches = re.findall(r'decoration-red', html)
logo_count = len(re.findall(r'assets/logo_planchart\.png', html))
vr210_vehiculo_count = len(re.findall(r'assets/vr210_vehiculo\.png', html))
vr210_plano_count = len(re.findall(r'assets/vr210_plano\.png', html))
z9_count = len(re.findall(r'assets/z9_hero\.jpg', html))
rich6_count = len(re.findall(r'assets/rich6_hero\.webp', html))
paladin_count = len(re.findall(r'assets/paladin_hero\.jpg', html))
t5_count = len(re.findall(r'assets/t5_hero\.jpg', html))
m09_hero_count = len(re.findall(r'assets/minivan_m09_hero\.jpg', html))
m09_plano_count = len(re.findall(r'assets/minivan_m09_plano\.jpg', html))
cs_count = len(re.findall(r'assets/minitruck_cs\.jpg', html))
cd_count = len(re.findall(r'assets/minitruck_cd\.webp', html))
cs_placeholder = bool(re.search(r'id="ph_MINI-CS_hero"', html))
cd_placeholder = bool(re.search(r'id="ph_MINI-CD_hero"', html))
total_models = len(re.findall(r'id="model-wrapper-', html))
total_sheets = len(re.findall(r'class="[^"]*sheet-page', html))

print('=== REPORTE DE VERIFICACIÓN ===')
print(f'1. Underlines encontrados: {len(underline_matches)}')
print(f'2. Decoration-red encontrados: {len(decoration_matches)}')
print(f'3. Referencias a logo_planchart.png (Hoja 1 y 2): {logo_count}')
print(f'4. Minivan M09 Hero imagen: {m09_hero_count}')
print(f'5. Minivan M09 Plano técnico: {m09_plano_count}')
print(f'6. Mini Truck CS imagen estática: {cs_count} (Placeholder interactivo activo: {cs_placeholder})')
print(f'7. Mini Truck CD imagen estática: {cd_count} (Placeholder interactivo activo: {cd_placeholder})')
print(f'8. VR210 Vehículo imagen: {vr210_vehiculo_count}')
print(f'9. VR210 Plano técnico chasis: {vr210_plano_count}')
print(f'10. Total Modelos configurados: {total_models}')
print(f'11. Total Hojas (2 por modelo): {total_sheets}')

# Verificaciones específicas de encabezados H3 y color de texto en fichas técnicas
h3_tags = re.findall(r'<h3[^>]*>.*?</h3>', html)
h3_red = [h for h in h3_tags if 'red' in h.lower()]
h3_black = [h for h in h3_tags if 'text-black' in h and 'font-black' in h]
print(f'12. Total encabezados H3 de sección: {len(h3_tags)}')
print(f'13. Encabezados H3 con "red": {len(h3_red)}')
print(f'14. Encabezados H3 en "text-black font-black": {len(h3_black)}')

# Comprobar si hay clases de texto rojo dentro del contenedor imprimible de fichas
sheet_sections = re.findall(r'<div class="sheet-page.*?(?=<div class="sheet-page|<!-- HOJA|\Z)', html, re.DOTALL)
red_in_sheets = []
for s in sheet_sections:
    matches = re.findall(r'text-red-[0-9]+', s)
    if matches:
        red_in_sheets.extend(matches)
print(f'15. Ocurrencias de text-red dentro de las fichas: {len(red_in_sheets)}')


