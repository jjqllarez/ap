# Arquitectura — <PROYECTO>

> Mapa de la arquitectura. Se consulta cuando la tarea toca diseño/estructura.
> Mantener conciso y actualizado; el detalle técnico por dominio vive en `docs/contexto/`.

## Visión general

<2–4 líneas: qué hace el sistema y su forma.>

## Capas

| Capa | Responsabilidad | Carpeta |
| --- | --- | --- |
| UI / presentación | <...> | `<src/...>` |
| Lógica / casos de uso | <...> | `<src/...>` |
| Datos / acceso | <...> | `<src/...>` |
| Utilidades / compartido | <...> | `<src/...>` |

## Flujo principal

<Diagrama o pasos: entrada → capas → salida.>

## Módulos / dominios

| Módulo | Responsabilidad | Contexto |
| --- | --- | --- |
| <A> | <...> | `docs/contexto/01-<a>.md` |

## Decisiones de arquitectura (ADR)

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| AAAA-MM-DD | <...> | <...> |

## Reglas estructurales

- 0 monolitos: una responsabilidad por unidad (archivo/componente/función).
- Modular, desacoplado, reutilizable y escalable.
- Evaluar el mejor patrón de diseño antes de codificar.
- Dependencias en una sola dirección; sin acoplamiento oculto ni estado global mutable.
