# <PROYECTO> — Reglas del proyecto

> **Contexto MODULAR.** Este archivo es solo un **índice delgado**; el detalle vive en `docs/contexto/`.
> Carga solo el módulo que necesites + `00-global.md` (máx 3). NO cargues el anexo salvo petición.

## Stack (3 líneas)

- <Framework/stack principal, ej. Astro 7 + @astrojs/node, PostgreSQL, etc.>
- <Lenguaje/tipado, ej. TypeScript strict>
- <Otros: ORM, auth, deploy>

## Reglas duras

- <Regla 1 — obligatoria y concreta>
- <Regla 2>
- <Regla 3>

## Verificación (antes de decir "listo")

- <Comando de typecheck/build> · <tests> · <linter>
- Revisar el diff.

## Índice de contexto

| Módulo | Archivo | Cuándo usarlo |
| --- | --- | --- |
| Global | `docs/contexto/00-global.md` | Siempre |
| <Dominio A> | `docs/contexto/01-<a>.md` | <casos> |
| <Dominio B> | `docs/contexto/02-<b>.md` | <casos> |
| Historial | `docs/contexto/99-historial.md` | Cambios recientes |

## Arquitectura

- Mapa de capas y flujos: `docs/ARQUITECTURA.md`.
- Convenciones de mantenimiento del contexto: `docs/MANUAL_CONTEXTO.md`.

## Cierre de tarea (obligatorio)

1. Actualizar el/los módulos afectados (fecha en el header).
2. Añadir entrada al `docs/contexto/99-historial.md`.
