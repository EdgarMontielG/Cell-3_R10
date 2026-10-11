# R10 — palancas de tiempo ciclo sobre el programa del programador (actualizado con su respaldo del 10/10)

Base: su respaldo del 2026-10-10 21:20 (commit `cd17b34`). **Meta de R10: 38 s pieza a pieza** (Edgar, 2026-10-11;
R20: 57.3 s hoy, meta 53 s). Las líneas son de la variante A; las B (estación 2) son iguales salvo donde se indica.

No se tocan: el tiempo de soldadura, los chequeos de calidad (nut check con su WAIT SEC 0.2 por sensor, cámara,
ventana de pistola cerrada) ni los interlocks de seguridad (PEDESTAL_CLEAR_CHECK antes de entrar y al salir,
vigilancia con las interrupciones 20-24 y su paro al salir del pedestal).

## Lo que ya midió (sus timers CT_*, gun_open_check.dat:57-81)

| Tramo | Tuerca 1 | Tuerca 2 | Tuerca 3 |
|---|---:|---:|---:|
| Dentro de la pistola (CENTERLINE_WELD) | 4.03 s | 3.92 s | 3.91 s |
| Tuerca a tuerca (pose de soldadura a pose de soldadura) | — | 6.71 s | 6.61 s |
| Espera de tuerca en la aproximación | 0 | 0.24 s | 0.32 s |

Tuerca 1 → fin de tuerca 3: 17.2 s; espera de tuerca por pieza: 0.56 s (en el video del 05/10 eran ~4 s antes de
las tuercas 2 y 3). Es un solo ciclo: `nCtCycle` = 276.8 s no sirve (la pieza vino después de un paro). Falta medir
10 piezas seguidas y las esperas del PLC (`entregas/2026-10-11_F52_esperas_PLC`: `nCtHomeWait`, `nCtPlcWait[1..3]`).

## Presupuesto contra los 38 s

| Tramo | Tiempo | Fuente |
|---|---:|---|
| Tuerca 1 en posición → fin de tuerca 3 (3 × ~4.0 s en la pistola + 2 × ~2.7 s de salir y entrar) | 17.2 s medido | nCtPart, nCtInWelder, nCtNutToNut |
| Todo lo demás: salida tras la tuerca 3, nut check, cámara, drop, HOME, esperas del PLC, pick, traslado y entrada a la tuerca 1 | 20.8 s disponibles | sin medir |
| de eso, esperas fijas: cámara 2.0 s, nut check 4 × 0.2 s, gripper 3 × 0.2 s | 3.4 s | style1app2opt2.src:60; style1app2opt1.src:72, :98, :124, :145; style1pick1opt1.src:46, :102; style1drop1opt1.src:67 |

Dentro de la pistola (12 s por pieza) no se toca el tiempo de soldadura; un recorte ahí (secuencia de clamp, pines,
pistola y presión) necesita el desglose por paso y el OK de CenterLine/Bosch. Si con la medición de 10 piezas el resto
del ciclo no cabe en 20.8 s, las palancas de abajo dan ~3.5-7 s.

## Lo que ya hizo (del 06 al 10/10)

- Palanca d): pre-alimenta la siguiente tuerca al QFP en cuanto la anterior queda en el pin (PRELOAD paso 30) y pide
  la tuerca justo después de CENTERLINE_WELD (style1app1opt1a.src:119). Aceptado como R20 F51 (F53).
- Palanca c): quitó los WAIT SEC 0.2 al cerrar y abrir la pistola y después de GUN_OPEN_CHECK
  (centerline_weld.src:181, :313, :323); un solo `dipw1_Ready` por tuerca; el Bosch queda habilitado fuera de dry
  cycle; la ventana de pistola cerrada bajó de 300 a 150 ms (`CL_GUN_IN_WINDOW_TIME`, $config.dat:846; Gestamp pide
  200 ms estables, ver F07/F53).
- Palanca a): CONT en las salidas de las apps (P0, P8, P20), en P22 del nut check y en P6 de la cámara.

## Lo que queda

| # | Palanca | Evidencia (respaldo 10/10) | Estimado por pieza | Condición |
|---|---|---|---|---|
| c | Espera fija de **2.0 s** antes de leer la cámara: el 05/10 era 0.2 s; el comentario sigue diciendo 0.2 s | style1app2opt2.src:60 | hasta 1.8 s | Preguntar por qué la subió. Si el resultado de la cámara tarda, esperar `di100` o `di101` con timeout en lugar del tiempo fijo; el chequeo se queda |
| b | Dry cycle leído justo después de la aproximación: el `IF di004UseDryCycle` lee una entrada y quita el CONT (paro exacto antes de bajar a soldar) | style1app1opt1a.src:83→89 (P20), style1app1opt2a.src:72→78 (P6, ya sin CONT), style1app1opt3a.src:73→79 (P13); igual en las B | 0.6–1.2 s | Leerlo una vez durante la espera de tuerca (el robot ya está parado) y usar la variable; también resuelve F05 |
| b | Permisos de AutomationCore después de llegar: el robot se detiene en P22 (el CONT nuevo se pierde) y en P5 del drop | style1app2opt1.src:46→56 (F50), style1drop1opt1.src:38→49 (F48) | 0.3–0.8 s (más la espera real del PLC) | Pedirlos antes del primer movimiento, como Gestamp; cierra F48 y F50 |
| b | Petición de la cámara hasta llegar a P3 | style1app2opt2.src:44→50-53 (`do080`, `WAIT FOR di080`) | 0.2–1.0 s | Mandarla por TRIGGER en la aproximación; confirmar con PLC que puede preparar la inspección mientras el robot llega |
| d | Tuerca confirmada por tiempo: el paso 30 dura 2000 ms + `nFeedSettleMs` 3000 ms; quedan 0.24–0.32 s de espera en las tuercas 2 y 3 | preload.src:276-281, preload.dat:28 | 0–0.6 s | Confirmar la tuerca con `$IN[481] dipw1_FeedComplt` (F13, F25) en lugar de 5 s fijos; además da la falla de tuerca faltante |
| a | Paradas exactas en espacio libre en el pick 1 | style1pick1opt1.src:63 (P12), :127 (P40), :134 (P9); P8 (:141) lo detiene la liberación que sigue | 0.3–0.9 s | CONT donde no haya obstáculo; revisar el TRIGGER de NUT_START antes de P12 (DISTANCE=0 dispara al empezar el movimiento) |
| c | `GRPg_SetStateAndCheck(…, 0.2, 1)`: espera fija de 0.2 s y luego revisa los sensores con timeout | style1pick1opt1.src:46, :102; style1pick1opt2.src:48, :97; style1drop1opt1.src:67 | 0.4–0.6 s | Tiempo de espera 0 en el form: el chequeo con timeout ya confirma el estado |
| c | WAIT SEC 0.2 después del último sensor del nut check, antes de evaluar (no hay lectura después) | style1app2opt1.src:145 | 0.2 s | Las tres esperas por sensor se quedan (estándar Gestamp) |
| e | Esperas del PLC (HOME, pickup, application, drop-off) y liberaciones con paro exacto antes (`AC_pickUP` después de P8, `AC_DropOff` después de P3) | cell.src; style1pick1opt1.src:141→149; style1drop1opt1.src:108 | por medir (`nCtHomeWait`, `nCtPlcWait`) | Solo con OK de Gestamp |

Suma de rangos, sin medir el ciclo completo: ~3.5–7 s por pieza; la espera de la cámara es la mayor y la más
barata. Ningún número se promete antes de tener 10 piezas seguidas medidas.
