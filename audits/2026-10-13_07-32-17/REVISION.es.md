# Auditoría del respaldo del 2026-10-13 07:32 (R10, BMW-03-10-R1)

- Respaldo: `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `6819763dc1b260dd…`), am.ini
  `2026-10-13_07-32-17`, robot `BMW_03_10_R1`, serie 658424, KSS 8.3.29, archivo completo (All). Edgar lo
  entregó como el respaldo del 12/10.
- Comparado contra su respaldo del 2026-10-11 22:32. Reporte del auditor: `AUDIT.md` y `summary.json`.
- Importado byte por byte: commit `6e70821`. Es la nueva base.

## Qué cambió

54 archivos cambiados, ninguno agregado ni faltante. 3 KRL con cambios de código (-6/+28) y 40 con cambios solo de
comentarios. Verificaciones: 0 FAIL, 1 WARN (`$IN[466]` en el texto de un mensaje).

| Cambio | Dónde | Revisión |
|---|---|---|
| GUN_OPEN_LOST (interrupciones 20-24) regresa sin frenar si al atenderla ya está todo bien; si no, frena como antes. El mensaje dice qué falta: submit, pistola (con su posición), clamp o pin (con su posición) | gun_open_check.src:116-188 | Filtro de caídas cortas de señal. Un evento real que dure menos que la atención de la interrupción ya no detiene el robot; uno que siga, sí. Preguntar si hubo paros en falso (F01) |
| Comentarios simplificados en 40 módulos: quitó las notas NOTE/CHECK/WARNING de la versión de oficina y los comentarios largos de señal; dejó comentarios cortos en inglés | Program/**, cell.src, sps.sub, $config.dat | Sin cambio de código. Quitó también el código comentado de sps.sub y los TRIGGER comentados (G05) |
| `iSTOP_TYPE` de TorqueMonitoring de 53 a 20 | tm_bib.dat:47 | La detección de colisión sigue apagada (C09) |
| `XPOUNCE` re-enseñado 100.7 mm más arriba | automationglobalpos.dat:13 | El ciclo no pasa por pounce (C12) |
| ir_stopm.src (solo comentarios), BrakeTest (solo `&ACCESS`) | archivos de KUKA | C28 |

Valores de proceso: último ciclo de AutomationCore 67 s; los timers CT_* no cambiaron desde el 10/10, así que en
los respaldos del 11 y 13/10 no hay ninguna soldadura registrada.

## Puntos

| Punto | Resultado | Evidencia |
|---|---|---|
| G01 | Aceptado sin cambio (decisión de Edgar, 13/10) | El robot sigue llamándose BMW_03_10_R1 (am.ini, captura del 12/10) |
| C02 | Se cierra con G01 | La designación de los encabezados queda como está |
| G02 | Cerrado | Captura del 12/10 09:03: herramienta de seguridad "EOAT 1 GE4-001" activada, TCP 0 / 0 / 380.8 mm; TOOL 1 en Datos de carga 0 / 0 / 380.790, -90 / -90 / -90 = `TOOL_DATA[1]` ($config.dat:234). SafetyConfigData.xml: herramienta cambiada y guardada el 10/10 11:12, versión 54, WorksheetCrc 2258919054. Falta el checklist de aceptación firmado (ítem 40 del workbook) |
| G05 | Abierto con avance | Ya no hay código comentado; siguen los módulos sobrantes y GlueTech |
| F01, C09, C12, C24, C28, F52 | Notas | Ver arriba |

## Entrega de esperas del PLC

`entregas/2026-10-11_F52_esperas_PLC` queda obsoleta (`OBSOLETO.txt`): se hizo sobre el respaldo del 10/10 y sus 7
archivos cambiaron en este respaldo. Cargarla desharía la limpieza de comentarios y el cambio de GUN_OPEN_LOST.

## Riesgos

1. Request to enter sin escribir (C19, C01): sin cambio.
2. GUN_OPEN_LOST ignora caídas cortas: aceptable como filtro; confirmar la razón.
3. Sin soldaduras registradas desde el 10/10: los cambios de tiempo ciclo del 10 al 13/10 (cámara, pistola,
   alimentación) no tienen medición.
