# Manual del contexto modular

Cómo mantener el contexto del proyecto sin inflar el `AGENTS.md`.

## Regla de oro

El `AGENTS.md` de la raíz se envía **completo en cada request**. Por eso contiene
**solo** el índice de módulos y las reglas duras (< ~80 líneas). Todo lo demás
vive en `docs/contexto/` y se carga **bajo demanda**.

## Estructura

```
AGENTS.md                      índice delgado + reglas duras
docs/
  ARQUITECTURA.md              mapa de capas, flujos y decisiones
  MANUAL_CONTEXTO.md           este archivo
  contexto/
    README.md                  índice de módulos
    00-global.md               stack, entorno, convenciones (base)
    NN-<dominio>.md            un dominio por archivo
    _plantilla-modulo.md       plantilla para nuevos módulos
    99-historial.md            historial reciente
    anexo/historial-completo.md detalle extenso (no cargar salvo petición)
```

## Al iniciar una tarea

1. Mira el índice de `docs/contexto/README.md`.
2. Carga **solo** el módulo afectado + `00-global.md` (máx 3 módulos).
3. No cargues el anexo salvo petición explícita.

## Al terminar una tarea

1. Actualiza el/los módulos afectados y su fecha en el header.
2. Añade una línea a `99-historial.md`:
   `- **AAAA-MM-DD — Título:** qué, por qué, verificación`.
3. Si hay detalle extenso, muévelo al anexo.

## Qué va a cada sitio

| Contenido | Dónde |
| --- | --- |
| Regla que aplica a todo | `00-global.md` |
| Regla de un dominio | `NN-<dominio>.md` |
| Dato verificado (ID, valor) | `00-global.md` o su módulo |
| Decisión de arquitectura | `docs/ARQUITECTURA.md` |
| Bug resuelto relevante | módulo + historial |
| Volcado/diagnóstico largo | anexo |

## Cuándo dividir

- Si `AGENTS.md` > ~80 líneas → mueve detalle a módulos.
- Si un módulo > ~200 líneas → divídelo.
- **Nunca dupliques:** cada dato vive en un solo archivo.
