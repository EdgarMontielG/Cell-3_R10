# Auditoría del respaldo del 2026-11-10 08:31 y del reporte de seguridad (R10, BMW-03-10-R1)

- Respaldo: `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424_1.zip` (sha256 `1567fd5c63c86e01…`), am.ini
  `2026-11-10_08-31-30` (hora del controlador), robot `BMW_03_10_R1`, serie 658424, KSS 8.3.29, Archive All.
- Comparado contra su respaldo del 2026-10-14 15:05. Reporte del auditor: `AUDIT.md` y `summary.json`.
- Importado byte por byte: commit `51c56fa` (con los 2 archivos de movetopurge que borró). Es la nueva base.
- Reporte de seguridad: `Safety_Report_R10-11_10_2026.pdf`, impreso de WorkVisual (proyecto BMW-03-10R1_v8) el
  10/11/2026 10:33, 10 páginas. No se guardó en el repositorio.

## Qué cambió

44 archivos cambiados, 2 borrados, 18 KRL con cambios de código (-45/+54). Verificaciones: 0 FAIL, 5 WARN (señales
sin comentario en las líneas nuevas).

| Cambio | Dónde | Revisión |
|---|---|---|
| En dry cycle GUN_OPEN_CHECK ya no revisa el agua, con `GOTO Jump` | gun_open_check.src:66-68, :81 | Sin soldadura no hace falta el agua; el GOTO reabre G11. Sin GOTO: `IF bGunWaterCheck AND NOT di004UseDryCycle THEN` |
| Mínimo de flujo de agua 15.0 → 13.0 l/min (`nWaterFlowMin` 150 → 130) | gun_open_check.dat:18 | El valor original del programa era ~30.8 l/min; sigue sin el límite por escrito de CenterLine (F09) |
| `$OUT[18] do018Part1InGripper` = di253 AND di254 en cada ciclo del submit; quitó los OUT 18 de picks y drops | sps.sub:189-199 | Es lo que pide G09 (En proceso). Queda el OUT 18 FALSE de RejectGE4 (rejectge4.src:68), sin efecto; falta la prueba en T1 |
| Quitó `GRPg_ChkSetStatePLC()` del submit | sps.sub (antes de NutWeld_BKG) | Las teclas de estado / peticiones del PLC del gripper ya no se ejecutan; hay una pendiente (`ReqState 2`, grp_func.dat:15). R20 la conserva. F55 (nuevo) |
| Drop al conveyor re-enseñado: AtDrop3 (877 mm), P5, puntos nuevos P4, P6, P8; liberación `AC_DropOff` después de P7 en lugar de después de P3 | style1drop1opt1.src/.dat | Bien: P7 está a 2.5 m, fuera del conveyor. `AC_DropOffCheck` sigue después de PTP P5 (F48) |
| Pick 1: P40 y P30AbovePick re-enseñados, P13 nuevo (CONT) en lugar de P9; pick 2: P30AbovePick re-enseñado | style1pick1opt1, style1pick1opt2 | Probar el camino |
| RejectGE4: P23 70 mm más arriba, espera del gripper 0.2 → 0.4 s | rejectge4.src/.dat | Bien |
| Style_1: CASE 1,2,7,8 en una línea | style_1.src:24 | Sin efecto (G07 sigue en decisión) |
| Borró movetopurge y su llamada en glue.src (GlueTech) | glue.src:127 | G05 con avance; edición de archivo de KUKA (C28) |
| Incrementos de jog: ejes 1 → 3°, cartesiano 50 → 10 mm / 3° | $machine.dat:464-483 | Sin efecto en el programa; listar en la entrega (C28) |
| Configuración de seguridad: cell area cambiada y guardada el 10/11 06:41 (versión 56, WorksheetCrc 2441542264, ParameterCrc 8DA361E6 → 78FA8691) | SafetyConfigData.xml, SCTLCRC.XML | Ver abajo |

## Reporte de seguridad

SafeOperation habilitado, suma de verificación **78FA8691**, igual a la del respaldo (SCTLCRC.XML). El reporte dice
versión 57 y el respaldo 56: la suma es la misma, así que los parámetros son los mismos.

- Herramienta 1 "EOAT 1 GE4-001": TCP 0 / 0 / 380.8 mm, igual a `TOOL_DATA[1]` y `[2]` ($config.dat:234-235); una esfera
  de 350 mm de radio en Z 150 mm. G02 sigue cerrado.
- Cell area de 5 esquinas: (-2000, -2700), (1000, -2700), (3510, 0), (1000, 1800), (-2000, 1800); Z ±30000.
  Con la esfera de la herramienta, los puntos del programa en base 0 quedan a 189 mm o más del límite (cálculo
  nuestro con las posiciones del respaldo; el más cercano, AtDrop3).
- Espacio 1 "Nest Workspace": protegido, siempre activo, sin paro en el límite (solo señala), X 1000 a 4000,
  Y -1400 a 0, Z -800 a 1800 en $WORLD; el pick queda dentro. Espacios 2-16 apagados. Qué hace el PLC con esa señal
  no está documentado (F42).
- Velocidad cartesiana T1 250 mm/s; ejes en T1 30 °/s; paro operacional seguro 0.01°; posición de referencia y
  prueba de mastering configuradas.
- La declaración de aceptación (página 10) está **sin firmas**, sin número de serie y sin código de activación. No es
  el checklist de aceptación de SafeOperation.

## Puntos

| Punto | Resultado |
|---|---|
| G11 | Reabierto: GOTO nuevo en gun_open_check.src |
| G09 | En proceso: `$OUT[18]` desde los sensores; falta la prueba en T1 |
| F55 (nuevo) | Abierto: `GRPg_ChkSetStatePLC` quitado del submit |
| G02 | Sigue cerrado; confirmado con el reporte |
| G05, F09, F42, F48, C28 | Notas |

## Riesgos

1. Configuración de seguridad cambiada otra vez (cell area, CRC 78FA8691) y el reporte sin firmar: falta el checklist
   de aceptación de esta versión (ítem 40 del workbook).
2. Si se vuelve a poner `GRPg_ChkSetStatePLC` sin limpiar la petición pendiente, el gripper cambia de estado al
   arrancar el submit (F55).
3. Mínimo de agua bajado a 13 l/min sin el valor de CenterLine por escrito (F09).
