# R10 — palancas de tiempo ciclo sobre el programa del programador (2026-10-11)

Base: su respaldo del 2026-10-05 14:46 (commit `468e29f`). **Nada de esto está medido todavía**: los rangos son
estimados a partir del código y del video del 2026-10-05, y se confirman con la medición
(`entregas/2026-10-11_F52_medicion`, variables `nCt*`). Meta: R10 por debajo de R20 (57.3 s hoy, meta 53 s) con
margen; la meta exacta de R10 está por confirmar con Edgar. Las líneas son de la variante A; las B (estación 2) son
iguales salvo donde se indica.

Lo que ya se sabe: en el video del 05/10 las soldaduras de una pieza van cada ~9.5 s; antes de las tuercas 2 y 3
el robot espera ~4 s la tuerca. En R20, con sus timers CT_*, el programador midió 3.8–4.1 s dentro de la pistola
por tuerca y 57.3 s pieza a pieza.

No se tocan: el tiempo de soldadura, los chequeos de calidad (nut check con su WAIT SEC 0.2 por sensor, cámara,
ventana de pistola cerrada) ni los interlocks de seguridad (GUN_OPEN_CHECK antes de entrar, vigilancia de pistola
con las interrupciones 20-22 y su paro al salir).

| # | Palanca | Evidencia | Estimado por pieza | Condición |
|---|---|---|---|---|
| d | Pedir la tuerca con anticipación: hoy la precarga completa (alimentar 2 s, avanzar, soplar 0.8 s, 0.8 s fijos tras el regreso) arranca hasta la salida; el robot espera ~4 s antes de las tuercas 2 y 3 | `Request_next_nut` por TRIGGER al salir: style1app1opt1A.src:137, style1app1opt2A.src:133; espera: :69 / :68; PRELOAD.src:47, :126, :145 | 5–7 s | Diseño de oficina F52 etapa 1 (en el historial) o como R20 F51 (pedir la tuerca justo después de soldar; aceptado porque el spear de Gestamp alimenta con el robot en la pose). Con la medición se ve cuánto queda |
| b | Lectura de dry cycle justo después de la aproximación: el `IF di004UseDryCycle` lee una entrada y quita el CONT de P20/P6/P13 (paro exacto antes de bajar a soldar) | style1app1opt1A.src:80→83, style1app1opt2A.src:78→81, style1app1opt3A.src:72→75 | 0.6–1.2 s | Leerlo una vez en la espera de tuerca (el robot ya está parado) y usar la variable; también resuelve F05 |
| b | Permisos de AutomationCore después de llegar al punto: el robot se detiene en P22 y en P5 del drop | style1app2opt1.src:43→50 (F50), style1drop1opt1.src:24→30 (F48) | 0.3–0.8 s (más la espera real del PLC) | Pedirlos antes del primer movimiento, como en Gestamp (cada programa de revisión pide el suyo); cierra F48 y F50 |
| b | Petición de reposicionar la herramienta de la cámara hasta llegar a P3 | style1app2opt2.src:46→49-53 (`do080`, `WAIT FOR di080`, 0.2 s) | 0.2–1.0 s | Mandarla por TRIGGER en la aproximación; confirmar con PLC/mecánica que puede moverse mientras el robot llega |
| a | Paradas exactas en espacio libre (sin CONT y el siguiente movimiento sigue directo) | style1pick1opt1.src:60, :122, :129 (pick2: :116); style1app1opt1A.src:138; style1app1opt2A.src:126; style1app1opt3A.src:118; style1app2opt1.src:77, :105; style1app2opt2.src:37 | 1–3 s (≈0.1–0.3 s cada una) | CONT donde no haya obstáculo; revisar los TRIGGER de esos movimientos (DISTANCE=1 dispara al empezar el redondeo). LIN → PTP solo donde no haga falta línea recta (pedestal y pick no) |
| c | Esperas fijas de 0.2 s en la pistola después de acciones que el LPT ya confirma | centerline_weld.src:133 (cruce de válvulas al cerrar), :231 (al abrir), :237 (después de GUN_OPEN_CHECK, que ya confirmó la pistola abierta) | 0.6–1.8 s (3 tuercas) | :237 sale sin riesgo; :133 y :231 con el mínimo que confirme CenterLine |
| c | `GRPg_SetStateAndCheck(…, 0.2, 1)`: espera fija de 0.2 s y luego revisa los sensores con timeout | style1pick1opt1.src:40, :96; style1drop1opt1.src:44 (GripperTech Grp_Func.src: `WAIT SEC rWaitTime` antes de `GRPg_CheckWithTimeOut`) | 0.2–0.6 s | Tiempo de espera 0 en el form: el chequeo con timeout ya confirma el estado |
| c | WAIT SEC 0.2 después del último sensor, antes de evaluar (no hay lectura después) | style1app2opt1.src:139 | 0.2 s | Las tres esperas por sensor se quedan (estándar Gestamp) |
| e | Esperas del PLC (HOME, pickup, application, drop-off) y liberaciones con paro exacto antes (`AC_pickUP` después de P8, `AC_DropOff` después de P3) | cell.src; style1pick1opt1.src:136→143; style1drop1opt1.src:79→86 | por medir (`nCtHomeWait`, `nCtPlcWait`) | Solo con OK de Gestamp |

Suma de rangos, sin medir: ~8–15 s por pieza; la palanca d) es la mayor. El orden de trabajo sigue a–e, pero con la
medición se decide dónde está el tiempo. Ningún número se promete antes de medir.
