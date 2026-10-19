# Contexto LLM — <PROYECTO>

> **Sistema de contexto MODULAR.** NO cargues archivos completos: carga solo el módulo que necesitas.
> Regla de oro: el contexto es una **biblioteca**, no un system prompt.

## Cómo usar (ahorro de tokens)

1. Identifica el módulo (tabla abajo).
2. Carga SOLO ese archivo + `00-global.md` si necesitas reglas base.
3. NO cargues el anexo histórico salvo que sea estrictamente necesario.

## Índice de módulos

| # | Módulo | Archivo | Cuándo usarlo |
| --- | --- | --- | --- |
| 0 | Global / Stack | `00-global.md` | Siempre (reglas base, entorno, convenciones) |
| 1 | <Dominio A> | `01-<a>.md` | <casos> |
| 2 | <Dominio B> | `02-<b>.md` | <casos> |
| 99 | Historial reciente | `99-historial.md` | Cambios de los últimos ~30 días |

> Añadir un módulo: copia `_plantilla-modulo.md`, renómbralo `NN-<dominio>.md` y añádelo a esta tabla.

## Pendientes globales

| Pendiente | Módulo | Prioridad |
| --- | --- | --- |
| <pendiente> | `<modulo>` | Alta/Media/Baja |
