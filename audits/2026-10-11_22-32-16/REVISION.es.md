# Auditoría del respaldo del 2026-10-11 22:32 (R10, BMW-03-10-R1)

- Respaldo: `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `0f71260b2b08429d…`), am.ini
  `2026-10-11_22-32-16`, robot `BMW_03_10_R1`, serie 658424, KSS 8.3.29, archivo completo (All).
- Comparado contra su respaldo del 2026-10-10 21:20. Reporte del auditor: `AUDIT.md` y `summary.json` en esta carpeta.
- Importado byte por byte: commit `8cb5c7a`. Es la nueva base.

## Qué cambió

39 archivos cambiados, 1 agregado, 10 KRL con cambios de código (-38/+70). Verificaciones: 0 FAIL, 19 WARN (17 líneas
de código comentado en sps.sub, donde dejó la copia vieja de las luces de tolva y del stepper; 2 señales sin
comentario).

| Cambio | Dónde | Revisión |
|---|---|---|
| La cámara espera el resultado (exactamente uno de OK / NG, máximo 5 s con `$TIMER[17]`) y lo lee 0.1 s después, en lugar de 2.0 s fijos. Sin resultado: scrap | style1app2opt2.src:60-68 | Bien planteado; ahorra hasta 1.9 s. `$TIMER[17]` no lo usa nadie más. Falta confirmar que no lee el resultado de la pieza anterior (F54, nuevo) |
| Pre-alimentación de 2000 ms; quitó `nFeedSettleMs` (3000 ms) | preload.src:98, :267-275; preload.dat | Como R20. El 10/10 la había subido porque faltaban tuercas: si vuelven a faltar, la corrección es leer `$IN[481]` (F13) |
| WAIT SEC 0.2 entre GunWork OFF y GunHome ON al abrir la pistola (lo había quitado el 08/10) | centerline_weld.src:314-321 | Como R20. +0.6 s por pieza |
| NutWeld_BKG activo, como Gestamp; quitó de sps.sub su copia de las luces de tolva y del stepper | sps.sub:105, :164-221 | Ver abajo |
| Robot en repair al PLC (`do009RobotAtRepair`), mismo código que AutomationCore_BKG | sps.sub:248-257 | Bien; variables declaradas en AutomationCore |
| Pick red rabbit: sin NUT_START (no pide tuerca), salida nueva P8 → P2 → P1 a 100 % con CONT (antes P16 a 60 %), XAtPick3 +0.5 mm | style1pick1opt1autorr.src/.dat | Bien; probar el camino nuevo. El encabezado dice que es el pick de producción llamado por Style1Opt1: corregir el comentario |
| Archivos de NutWeld de KUKA editados: escrituras de pistolas 2/3 condicionadas a `nMaxGunNr` (=1) porque se traslapan con `CL_GunPressureCmd`; luces de la tolva 1 combinadas con `CL_WeldFault` y `dipw1_Fault`; el reset de NutWeld no apaga intensify ni blow-off mientras corre PRELOAD; `nNutWeldGunNrSTK` 3 → 1 | nutweldroutines.src/.dat | Bien resuelto; listarlo en la entrega (C28) |
| Atributos de cabecera (&ACCESS, &REL) en 15 archivos; valores de proceso en 6 `.dat`; `GRPg_SignVal` de GripperTech | varios | Sin efecto |

NutWeld_BKG activo: además de tolva y stepper, al cancelar o resetear el programa apaga weld init, el programa del
Bosch, intensify y blow-off (avance de F10), y en T1/T2 permite abrir/cerrar la pistola y el pin desde las teclas de
estado de NutWeld, como en Gestamp. Escribe `$OUT[470] dopw1_Hidraulyc_Valve = $PERI_RDY`; AutomationCore declara esa
salida como Spare: confirmar que no tiene nada conectado.

No cargó la entrega de esperas del PLC. Sigue válida sobre este respaldo: sus 7 archivos solo cambiaron aquí en
atributos de cabecera y un valor de proceso.

## Corrección de la auditoría del 10/10

Al cargar la versión de oficina del 05/10, **AutomationCore_BKG quedó apagado** (el fold está vacío y el submit pone
sus salidas en OFF al arrancar). Su respaldo del 05/10 y R20 lo tienen activo, y C01 y C19 se habían cerrado el 11/10 con
ese supuesto. En la auditoría del 10/10 no lo detecté. El programador copia en sps.sub parte de sus señales (weld enable
y weld mode, aire, agua, tolva, nut ready/fault, cambio de electrodo y ahora robot en repair), pero faltan:

- `doCriticalWZ` (request to enter): FALSE fijo, el PLC ve entrada permitida (C19).
- `do021BrakeTestReqd` (brake test pendiente): FALSE fijo (C14).
- Mastering pendiente, batería, velocidad distinta de 100 %, posición del eje 1, Tool ID, robot en pounce / tip
  dress / switch de referencia y el arranque automático del programa CELL en EXT (C01).

C01, C19 y C14 quedan **Reabiertos**. Lo más simple es reactivar AutomationCore_BKG como en R20 (mismo código) y quitar
de sps.sub las copias, para que cada salida tenga un solo escritor.

## Tiempo ciclo

AutomationCore guarda el último ciclo de arranque a fin, sin la espera en HOME (`nCycleTime`, segundos enteros):
50 s el 05/10, 39 s el 10/10 y 26 s el 11/10. El de 26 s no soldó (sus timers CT_* no cambiaron desde el 10/10): por
los cambios del día, probablemente un ciclo red rabbit. El de 39 s es probablemente la pieza que midió el 10/10, sin
confirmar. Contra la meta de 38 s: el cambio de la cámara ahorra hasta 1.9 s y la espera de la pistola agrega 0.6 s.
Hace falta la medición de 10 piezas seguidas.

## Puntos

| Punto | Resultado |
|---|---|
| C01, C19, C14 | Reabiertos (AutomationCore_BKG apagado desde el 10/10) |
| F54 (nuevo) | Abierto: confirmar con el PLC que la cámara no deja el resultado de la pieza anterior |
| F12 | En proceso: NutWeld_BKG activo; AutomationCore_BKG apagado |
| F10, F13, F14, F15, F17 | Abiertos con avance |
| F52, F53, F29, G08, C28, F49, G22 | Notas |

## Riesgos

1. Request to enter sin escribir: el PLC ve entrada permitida aunque el pedestal esté en proceso (C19).
2. Cámara: si el PLC deja el resultado anterior, una pieza NG después de una OK sale como buena (F54).
3. Tuercas faltantes: la alimentación volvió a 2 s por tiempo, sin `$IN[481]` (F13).
4. Brake test pendiente sin reportar al PLC (C14).
