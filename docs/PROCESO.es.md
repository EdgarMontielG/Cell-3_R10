# Proceso de cierre de puntos abiertos y auditoría diaria

Robot R10 (BMW-03-10-R1). El programador cierra los puntos abiertos modificando
el programa; cada respaldo diario se audita contra el criterio de cierre de
cada punto. La lista maestra es [`docs/open_items.json`](open_items.json)
(vista legible en [OPEN_ITEMS.es.md](OPEN_ITEMS.es.md)); el programador
trabaja sobre la copia en Excel `dist/R10_Puntos_Abiertos_AAAA-MM-DD_HHMM.xlsx`.

Los archivos que se entregan llevan fecha y hora (centro de México) en el
nombre: el respaldo del robot `658424_R10_AAAA-MM-DD_HHMM.zip`, el Excel
`R10_Puntos_Abiertos_AAAA-MM-DD_HHMM.xlsx` y el reporte
`R10_reporte_AAAA-MM-DD_HHMM.pdf`.

## Día 0 — punto de partida

1. Cargar en el robot la versión de oficina: el zip que genera
   `tools/build_archive.py` sobre el último respaldo auditado (depuración,
   correcciones de la revisión de Gestamp y cambios del programador ya
   integrados), o los archivos modificados (modo experto, navegador, USB).
   No hacer deploy desde WorkVisual: los proyectos guardados traen el
   programa viejo (así se perdió la depuración el 2026-10-05).
2. Borrar en el controlador los 22 archivos de módulos eliminados: 21 de la
   depuración (`tools/cleanup_allowlist.json`) y 1 de las correcciones
   (`centerline_loop.src`, `tools/code_changes.json`), y la carpeta vieja
   `Program/Styles/optiones` (sus dos archivos ahora están en
   `Program/Styles/Options`). Un restore no borra archivos. Las copias
   AutoRR pueden aparecer en minúsculas (`style1app2opt1autorr.src`): son
   las mismas.
3. Actualizar el proyecto WorkVisual desde el controlador y guardarlo antes
   de cualquier deploy; si no, el deploy regresa el programa viejo.
4. Un ciclo en T1 con override reducido y uno en automático; después, las
   pruebas en celda de los puntos en *Corregido en oficina - probar en
   celda* (criterio de cierre de cada uno; resumen en la sección 3.3 del
   PDF). Cada prueba que sale bien pasa el punto a *Corregido - por
   auditar* con la evidencia; si falla, a *En proceso* con lo que pasó.
5. Respaldo completo (Archive → All). La primera auditoría lo compara contra
   el estado del repositorio; tiene que salir sin cambios de código
   (salvo lo que el programador haya corregido y anotado).

El programador trabaja siempre sobre la versión cargada del zip, nunca sobre
un proyecto WorkVisual viejo ni sobre una copia anterior: cada cambio hecho
sobre el original hay que integrarlo a mano.

## Cada día

**Programador**

1. Modifica el programa para cerrar puntos. Reglas de
   [CONVENTIONS.md](CONVENTIONS.md) para lo que escriba: comentarios en
   inglés, cada acción de I/O con la señal nombrada (`$OUT[n] nombre`), sin
   código comentado, sin reabrir inline forms que tengan líneas escritas a
   mano (F32), sin abrir los forms AutomationCore con parámetros ocultos
   (F21).
2. Al cerrar un punto quita o actualiza el `;CHECK:` / `;WARNING:` del código
   que cita ese punto.
3. En el Excel, solo columnas amarillas de los puntos trabajados: Estado
   (`En proceso` o `Corregido - por auditar`), qué cambió, módulos
   modificados, evidencia (prueba en celda con fecha y resultado) y fecha.
   No pone `Cerrado`. Los puntos de Gestamp son G01–G22 (columna Origen
   "Gestamp #n"); se trabajan igual que los demás.
4. Al final del día: respaldo completo del robot y el Excel, a Edgar.

**Edgar**

5. Sube el respaldo y el Excel a esta sesión y pide la auditoría.

**Auditoría**

6. `python3 tools/audit_backup.py RESPALDO.zip --items EXCEL.xlsx` compara el
   respaldo contra el último estado auditado (`HEAD`) y escribe
   `audits/<fecha>/AUDIT.md`: archivos cambiados, diff del código sin
   comentarios, verificaciones mecánicas (folds, fines de línea, señales en
   comentarios, consistencia de inline forms, líneas escritas dentro de
   forms, código comentado nuevo, español, I/O sin comentario, módulos sin
   encabezado) y los puntos marcados como corregidos con los módulos que sí
   y no cambiaron.
7. Revisión de cada cambio de código y de cada punto marcado contra su
   criterio de cierre: **Cerrado - auditado** si cumple todo, **Reabierto**
   con la razón si no.
8. Si el respaldo parte de la versión entregada, se importa al repositorio
   (`--import`). Si trae archivos previos a la depuración o editados encima
   del original (como el 2026-10-05), no se importa: los cambios del
   programador se integran a mano en la versión depurada y se prueba con un
   diff solo de código contra su versión que hacen lo mismo. Después se
   actualiza `docs/open_items.json` (estado e historial de cada punto), se
   regeneran el Excel y el PDF (`tools/make_items_xlsx.py`,
   `tools/make_report.py`) y se hace commit con la fecha. El programador
   recibe el Excel nuevo para el día siguiente.

### Cómo se revisa, sin multiplicar agentes

* Primero las herramientas mecánicas: `audit_backup.py`,
  `check_cleanup.py --head <base>`, `check_equivalence.py` y, si se tocó el
  auditor, `test_audit_backup.py`. Son deterministas y cubren lo repetitivo.
* El auditor lee él mismo el diff solo de código (sin comentarios ni
  renombres) contra el último estado auditado y contra el original. No se
  reparte la revisión en un agente por módulo ni por tema.
* Revisión independiente (uno o dos agentes, con el alcance acotado a los
  archivos y las preguntas concretas) solo en dos casos: cuando el cambio
  toca seguridad o interlocks (entrada al pedestal, interrupts, PRELOAD,
  rutinas del proveedor, inline forms), y antes de entregar un zip para
  cargar. El revisor confirma o refuta hallazgos concretos; no vuelve a
  auditar todo.
* Pendiente para el próximo respaldo del R10: revisión independiente de
  GUN_OPEN_CHECK y los interrupts 20-22 (apps 1-3), del background de
  AutomationCore con sus ediciones del proveedor y de la integración hecha a
  mano el 2026-10-05.

## Qué hace reabrir un punto

* El criterio de cierre no se cumple en el respaldo, o falta la evidencia que
  pide.
* El punto dice "corregido" pero ninguno de sus módulos cambió.
* El cambio rompe otra cosa: una verificación mecánica en FAIL, o un cambio
  de código que no corresponde a ningún punto y nadie explicó.
* El `;CHECK:` / `;WARNING:` del punto sigue en el código diciendo que el
  problema existe.

## Cambios que no son de ningún punto

Se aceptan, pero el programador los anota en la columna "Qué cambió" de un
punto relacionado o al final del Excel. Un cambio de código sin explicación
se reporta en la auditoría como hallazgo nuevo.

## Respaldos

* Siempre respaldo completo (Archive → All), no solo `KRC:\R1`.
* Nombre del respaldo: `658424_AAAA-MM-DD_HHMM.zip`, con la hora en que se
  sacó. El Excel que regresa el programador, con su fecha y hora:
  `R10_Puntos_Abiertos_AAAA-MM-DD_HHMM.xlsx`.
* Si el respaldo trae el programa previo a la depuración (por ejemplo porque
  alguien cargó un respaldo viejo), la auditoría lo detecta y lo marca antes
  que nada.

## Estados

| Estado | Quién lo pone | Significa |
|---|---|---|
| Abierto | Auditoría | Pendiente de trabajar. |
| Requiere decisión | Auditoría | Falta información o decisión (Gestamp, seguridad, Ethos) antes de programar. |
| Corregido en oficina - probar en celda | Auditoría | Ethos lo corrigió en la versión entregada; falta la prueba en celda del programador. |
| En proceso | Programador | Trabajo empezado, o prueba de oficina que falló. |
| Corregido - por auditar | Programador | Cambio hecho (o corrección de oficina) y probado en celda, con evidencia. |
| Cerrado - auditado | Auditoría | Cumple el criterio de cierre en el respaldo. |
| Reabierto | Auditoría | No se encontró el cambio o no cumple. |
| Aceptado sin cambio | Ethos / Gestamp | Se decidió no corregir; queda la razón. |
| Cerrado - depuración / No aplica / Sin acción / Se cierra con otro punto | Auditoría | Resuelto por la depuración, ya cumple, documentado, o duplica otro punto. |

## Cambios de código de la oficina

Cuando Ethos cambia código (como con la revisión de Gestamp), cada cambio se
declara en `tools/code_changes.json` con sus puntos, y
`tools/check_equivalence.py` prueba que lo demás no cambió (compara señales
por dirección y constantes por valor). La auditoría diaria usa el mismo
`audit_backup.py`: el programador recibe la versión de oficina como nueva
base.
