# Auditoría del respaldo del 2026-10-10 21:20 (R10, BMW-03-10-R1)

- Respaldo: `V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `5bbd1a59c40285b9…`), am.ini
  `2026-10-10_21-20-39`, robot `BMW_03_10_R1`, serie 658424, KSS 8.3.29, archivo completo (All).
- Comparado contra su respaldo anterior, el del 2026-10-05 14:46 (base auditada desde el 11/10). Reporte del
  auditor: `AUDIT.md` y `summary.json` en esta carpeta; contra la versión de oficina del 05/10: `contra_oficina_1b28a7e/`.
- Importado byte por byte: commit `cd17b34`. Es la nueva base.
- Criterio: no se le exige más de lo que hace el respaldo de Gestamp NUT07_10R1; lo que se resolvió así en R20 se
  aplica igual.

## Qué es este respaldo

Cargó la versión de oficina del 05/10 (la entrega integrada) y sobre ella trabajó del 06 al 10/10. Contra su
respaldo del 05/10: 90 archivos cambiados, 3 agregados, 19 faltantes (14 de los 8 módulos sobrantes que borró y 5
de proyectos WorkVisual), 51 KRL con cambios de código. Lo suyo, en resumen:

- Tiempo ciclo (igual que hizo en R20): pre-alimenta la siguiente tuerca al QFP (PRELOAD paso 30), pide la tuerca
  justo después de soldar, Bosch habilitado fuera de dry cycle, un solo Ready por tuerca, sin los WAIT SEC 0.2 de la
  pistola, CONT y PTP en los traslados, ventana de pistola cerrada de 150 ms (era 300). Timers CT_* para medir.
- Pedestal: PEDESTAL_CLEAR_CHECK (pistola abierta, clamp abierto, pin superior retraído) antes de entrar y al
  salir, interrupciones 23 y 24 para clamp y pin, PIN_WELD_CHECK y PIN_SETTLE_WAIT.
- Soldadura: WELD_COMPLETE_WAIT con timeout y falla del Bosch; GUN_CLOSE_FAULT con mensaje y luz roja; reintento
  de tuerca en la pose de soldadura (una vez, `nNutRetryMax`). En el respaldo lleva 8 reintentos acumulados.
- Señales del soldador al PLC en sps.sub "como NUT07" (F12), cambio de electrodo con do111 (G06).
- Limpieza: borró 8 módulos sobrantes; nombres corregidos; sin GOTO; sin $IN/$OUT con número fuera de los forms.
- Carga de la herramienta 1: 67.28 kg con centro de masa e inercias (antes 210 kg tecleados).
- Archivos de KUKA editados: `ir_stopm.src` sin las llamadas de GlueTech y `tm_bib.dat` con TQM_ACT T21..T26 de
  100000 a 1000 (C28, C09).
- La espera antes de leer la cámara pasó de 0.2 a **2.0 s** (style1app2opt2.src:60); el comentario sigue diciendo
  0.2 s.

## Verificaciones mecánicas

12 FAIL, revisados uno por uno:

- 10 forms OUT 18 / 106 / 249 / 250 "sin asignación": el cuerpo escribe la misma salida con su nombre
  (`do018Part1InGripper=TRUE` en lugar de `$OUT[18]=TRUE`). Falsa alarma del auditor: reabrir el form regenera
  la misma salida.
- `NUT_WELD_RETRY` ya no está en $config.dat: falsa alarma, ahora se declara en gun_open_check.dat.
- `REDRABBIT` ya no está en $config.dat y lo usa `redrabbit.dat`: real. El módulo sobrante ya no compila; nadie lo
  llama. Se sigue en G05.

WARN: 40 de E/S sin comentario que las nombre (usa los nombres de señal, estilo), 10 líneas escritas dentro de forms
(las mismas 10 de arriba), 5 TRIGGER/movimientos comentados (el TRIGGER de Request_next_nut que reemplazó, en las
apps 1 y 2, y un LIN en el drop red rabbit), y el cambio en `ir_stopm.src`.

## Puntos

| Punto | Resultado | Evidencia |
|---|---|---|
| G12, G13, G14, G15, G16, G17, G20 | Cerrados | Ver nota de cada punto; G17: retry con tope, como el REPEAT UNTIL de Gestamp |
| F01 | Cerrado (era el crítico de entrada al pedestal) | PEDESTAL_CLEAR_CHECK antes de entrar y al salir; interrupciones 20-24; igual que R20 |
| F20, F36 | Cerrados | Reject libera Application 1 por TRIGGER; $IN[227] una sola declaración |
| G03 / C08 | En proceso | Carga real de 67.28 kg; falta la evidencia de Load Data Determination |
| F12 | En proceso | Señales del soldador en sps.sub; falta que el PLC confirme |
| F53 (nuevo) | Aceptado sin cambio | Pre-alimentación y tuerca pedida con la pieza en la pistola: igual que R20 F51 |
| F03, F07, F13, F14 | Abiertos con avance | Ver riesgos |
| G21 / F19, F21, F46, F48, F50 | Sin cambio | Red rabbit con AND; 4 forms AutomationCore con número oculto distinto; Work Complete comentado; permisos después de llegar |
| F11 | Requiere decisión (crítico) | PRELOAD en el submit mueve el pedestal en cualquier modo; pendiente la decisión como en R20 |

## Tiempo ciclo

Sus timers CT_* (un ciclo): 4.03 / 3.92 / 3.91 s dentro de la pistola, 6.71 / 6.61 s tuerca a tuerca, 0 / 0.24 /
0.32 s de espera de tuerca (0.56 s por pieza; en el video del 05/10 eran ~4 s antes de las tuercas 2 y 3), 17.2 s de
la tuerca 1 al fin de la tuerca 3. `nCtCycle` = 276.8 s no sirve (la pieza vino después de un paro). Falta medir 10
piezas seguidas y las esperas del PLC.

La entrega de medición de Ethos sobre el 05/10 (`entregas/2026-10-11_F52_medicion`) quedó obsoleta: él ya mide con
sus CT_*. Se retiró del repositorio y se reemplazó por `entregas/2026-10-11_F52_esperas_PLC` (sobre este respaldo,
7 archivos, solo agrega `nCtHomeWait` y `nCtPlcWait[1..3]` con `$TIMER[24]`; mismo comportamiento).

Meta de R10 (Edgar, 2026-10-11): 38 s pieza a pieza. La soldadura de las 3 tuercas ya ocupa 17.2 s; quedan 20.8 s
para el resto del ciclo (3.4 s de esperas fijas), sin medir todavía.

Palancas que quedan, con rangos y líneas: `audits/2026-10-11_tiempo_ciclo/PALANCAS.es.md` (~3.5-7 s por pieza sin
medir; la mayor y más barata, la espera de 2.0 s de la cámara).

## Riesgos

1. Ventana de pistola cerrada de 150 ms (Gestamp: 200 ms estables): más riesgo de soldar sin tuerca o con doble
   tuerca si la pistola rebota. Pedir prueba sin tuerca y con doble tuerca, o volver a 200 ms (F07, F53).
2. Tuercas faltantes: 8 reintentos acumulados; la alimentación se confirma por tiempo (2 s + 3 s) sin leer
   `$IN[481] dipw1_FeedComplt` (F13).
3. NUT_READY no se borra al soldar: con la pre-alimentación de 5 s el margen para que el robot no entre con el
   NUT_READY anterior es de ~1.5 s (F14).
4. Drop y nut check piden permiso al PLC después de llegar al punto (F48, F50).
5. Red rabbit: FAILED solo con las 3 tuercas y el drop borra el resultado (G21, F19); Work Complete comentado (F46).
6. Archivos de KUKA editados (ir_stopm, tm_bib): se pierden si se actualiza GlueTech o TorqueMonitoring (C28, C09).
