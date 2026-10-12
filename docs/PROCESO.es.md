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

## Base: el programa del programador (desde el 2026-10-11)

Decisión de Edgar (igual que en R20): ya no se le exige al programador cargar
la versión de oficina. **Su último respaldo es la base auditada**: el árbol del
programa del repositorio es su último respaldo byte por byte: hoy el del
2026-10-11 22:32 (commit `8cb5c7a`); el cambio de base fue sobre su respaldo
del 2026-10-05 14:46 (commit `468e29f`). La versión de oficina (depuración, correcciones de la
revisión de Gestamp, integraciones y la etapa 1 de tiempo ciclo) queda en el
historial en `84442ac`, solo como referencia. Los dos commits están en
`tools/audit_base.json`.

- Cada respaldo nuevo se audita contra su respaldo anterior
  (`tools/audit_backup.py`) y se importa. La auditoría ya no marca los
  módulos que borró la oficina ni las reglas de la depuración.
- Los módulos sobrantes se siguen solo en G05 y no se evalúan hasta que la
  celda esté probada al 100 %.
- El estado *Corregido en oficina - probar en celda* ya no se usa: esos puntos
  se revisaron contra su programa (cerrados si ya cumple; si no, abiertos, en
  proceso o requiere decisión) y la nota de cada uno dice cómo lo resolvió la
  oficina.
- `build_archive.py`, `make_package.py`, `check_cleanup.py` y
  `check_equivalence.py` son herramientas de la etapa anterior.
- Las anotaciones de Edgar con el programador van en la columna "Qué cambió
  el programador" del Excel.

## Estándar de referencia: el respaldo de Gestamp NUT07_10R1

El programador se basó en un respaldo de otra celda que dio Gestamp
(`nut07_10r1.zip`, robot `NUT07_10R1`, serie 658415, KSS 8.3.29,
2026-08-18). **No se le exige más de lo que hace ese respaldo**: si un punto
queda igual o mejor, o el respaldo de Gestamp tampoco lo hace, se cierra o se
acepta sin cambio. En los puntos G el argumento es "igual que su propio
respaldo", pero el cierre final lo acepta Gestamp. Esa celda usa el paquete
NutWeld de KUKA con alimentador spear, sin CenterLine ni PRELOAD: los puntos
del pedestal se comparan por analogía. El respaldo se revisó en la conversación
de R20; la aplicación a R10 está en
`audits/2026-10-11_estandar_gestamp/REVISION.es.md`.

## Tiempo ciclo: prioridad

Meta de R10: **38 s pieza a pieza** (Edgar, 2026-10-11; R20: 57.3 s hoy,
meta 53 s). Antes de prometer números se mide en el robot (pieza a pieza,
tuerca a tuerca, dentro de la pistola, espera de tuerca, esperas del PLC en
HOME y en permisos). Palancas, en este orden: (a) paradas exactas en espacio libre (CONT,
PTP en lugar de LIN donde no hace falta línea recta); (b) lo que detiene el
avance entre movimientos (salidas por TRIGGER o con CONTINUE, chequeos juntos
en una parada planeada antes del pedestal); (c) esperas fijas después de
acciones que ya confirma un sensor o un handshake; (d) pedir la tuerca con
anticipación, escondida en el traslado; (e) handshakes de AutomationCore, solo
con OK de Gestamp. No se tocan el tiempo de soldadura, los chequeos de calidad
ni los interlocks de seguridad, y el chequeo de pedestal no se mueve a después
de entrar. Los estimados van en rangos y con evidencia (archivo:línea).

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

* Primero las herramientas mecánicas: `audit_backup.py` contra el respaldo
  anterior (y, como referencia, contra la versión de oficina) y, si se tocó
  el auditor, `test_audit_backup.py`. Son deterministas y cubren lo
  repetitivo.
* El auditor lee él mismo el diff solo de código (sin comentarios ni
  renombres) contra el respaldo anterior. No se
  reparte la revisión en un agente por módulo ni por tema.
* Revisión independiente con agentes solo si Edgar lo pide (uno o dos, con el
  alcance acotado a los archivos y las preguntas concretas), en dos casos: cuando el cambio
  toca seguridad o interlocks (entrada al pedestal, interrupts, PRELOAD,
  rutinas del proveedor, inline forms), y antes de entregar un zip para
  cargar. El revisor confirma o refuta hallazgos concretos; no vuelve a
  auditar todo.
* Si Edgar lo pide: revisión independiente de PEDESTAL_CLEAR_CHECK y las
  interrupciones 20-24 (apps 1-3) y del background de AutomationCore con sus
  ediciones del proveedor, sobre el respaldo del 10/10.

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
| En proceso | Programador | Trabajo empezado (o cumple en código y falta la prueba en celda). |
| Corregido - por auditar | Programador | Cambio hecho y probado en celda, con evidencia. |
| Cerrado - auditado | Auditoría | Cumple el criterio de cierre en el respaldo. |
| Reabierto | Auditoría | No se encontró el cambio o no cumple. |
| Aceptado sin cambio | Ethos / Gestamp | Se decidió no corregir; queda la razón. |
| Cerrado - depuración / No aplica / Sin acción / Se cierra con otro punto | Auditoría | Resuelto por la depuración, ya cumple, documentado, o duplica otro punto. |

## Cambios que hace Ethos

Solo cuando Edgar lo pide, y siempre sobre el último respaldo del
programador. Se entregan en `entregas/<fecha>_<puntos>/`: solo los archivos
que cambian, `cambios.diff`, `LEEME.txt` y un PDF de instrucciones (orden de
carga, tabla de archivos con casillas, qué cambia en cada punto y pruebas con
resultado esperado). `$config.dat` nunca va completo: el LEEME dice qué líneas
agregar o quitar. El árbol KRC del repositorio no se toca hasta que el cambio
llega en un respaldo del programador. Mismo comportamiento salvo lo que el
punto pide cambiar; se conservan los fines de línea originales y texto ASCII.
