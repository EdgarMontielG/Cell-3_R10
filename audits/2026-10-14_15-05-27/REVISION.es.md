# Auditoría del respaldo del 2026-10-14 15:05 (R10, BMW-03-10-R1)

- Respaldo: `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `a6ac5a6e30df2f15…`), am.ini
  `2026-10-14_15-05-27` (hora del controlador), robot `BMW_03_10_R1`, serie 658424, KSS 8.3.29, Archive All.
- Comparado contra su respaldo del 2026-10-13 07:32. Reporte del auditor: `AUDIT.md` y `summary.json`.
- Importado byte por byte: commit `c401a76` (con los 8 archivos que borró en el controlador). Es la nueva base.
- El zip trae además `Ethos -  Purchase Order 263178.pdf` (fechado 2026-11-03), fuera de la estructura del respaldo.
  No es parte del robot, no se abrió ni se guardó en el repositorio.

## Qué cambió

75 archivos cambiados, 8 borrados, 26 KRL con cambios de código (-84/+112). Verificaciones: 0 FAIL, 9 WARN (señales
sin comentario en las líneas nuevas).

| Cambio | Dónde | Revisión |
|---|---|---|
| AutomationCore_BKG activo otra vez | sps.sub:102 | Como Gestamp y R20: escribe request to enter (`doCriticalWZ` por AC_Request_to_enter, automationcoreroutines.src:1411-1434), brake test pendiente, mastering, batería, velocidad, eje 1, Tool ID, posiciones y Ethernet de periféricos. C01 y C19 se cierran; C14 queda solo en F47. sps.sub sigue escribiendo sus copias de las mismas señales con la misma expresión. `do052EOATVlvMnfldEnetOK` fijo en TRUE (automationcoreroutines.src:178) |
| Work Complete al PLC: después de EndOfCycle, `do015WorkComplete` y espera de `di015WorkCompleteAckn` con mensaje | cell.src:65-72 | F46 en proceso (falta la prueba). El tiempo de AutomationCore ahora incluye la espera del acuse |
| Red rabbit con OR: FAILED con cualquier tuerca, PASSED sin ninguna; el drop red rabbit ya no borra el resultado; la cámara solo puede dar FAILED | style1app2opt1.src:144-145, style1app2opt2.src:63-68, style1drop1opt2autorr.src | G21 cumple en código; falta la prueba. F19 se cierra con G21 |
| Drop red rabbit con el gripper 1 (form con los mismos parámetros) y sin escribir `$OUT[249]`/`$OUT[250]` | style1drop1opt2autorr.src | F31 en proceso |
| Estado de la tuerca: `NUT_STATE_INIT` al arrancar (USER INIT de sps.sub y cell.src), `NUT_READY=FALSE` al terminar la soldadura, PRELOAD descarta una petición si ya hay tuerca lista, y antes de esperar la tuerca se pide si nadie la pidió | preload.src:20-22, :260-285; centerline_weld.src:234; gun_open_check.src:422-424; sps.sub; cell.src | G19, F14 y F38 en proceso. Riesgo: la inicialización deja `NUT_READY=FALSE` aunque haya una tuerca en el pin; la petición siguiente puede alimentar otra (doble tuerca, que la ventana de pistola detectaría). Falta la prueba en celda |
| Herramienta 2 "TOOL 1 WITH PART": mismo TCP que la 1 y carga 68.28 kg (la de la herramienta 1 + 1 kg); los movimientos con pieza usan la herramienta 2 | $config.dat:235, :253, :272; .dat de picks, apps, drops y reject | Bien: ya no hay movimientos con carga por defecto (C08). La masa de la pieza (1 kg) y el centro de masa sin cambio son estimados. La herramienta de seguridad sigue igual al TCP (G02) |
| Mastering reference: `do930MasterRefInProcess=FALSE` al terminar | masref_user.src:133 | F35 en proceso (falta prueba en T1) |
| Módulos borrados: capchange, electrodechange, redrabbit, safetest | controlador | G05: quedan pounce y GlueTech con movetopurge |
| `XATDROP3` re-enseñado 66.7 mm; `iSTOP_TYPE` de TorqueMonitoring otra vez 53 | style1drop1opt1.dat, tm_bib.dat | Notas |
| Configuración de seguridad: "Cell area" cambiada y guardada el 2026-10-13 18:58, versión 55, WorksheetCrc 3865158541, ParameterCrc 8DA361E6 | SafetyConfigData.xml, SCTLCRC.XML | Falta el checklist de aceptación de esta versión (ítem 40 del workbook) |

## Tiempo ciclo (última pieza, timers CT_*)

| Tramo | 14/10 | 10/10 |
|---|---:|---:|
| Dentro de la pistola, tuercas 1 / 2 / 3 | 4.10 / 4.01 / 4.00 s | 4.03 / 3.92 / 3.91 s |
| Tuerca a tuerca, 2 / 3 | 6.94 / 6.89 s | 6.71 / 6.61 s |
| Espera de tuerca, 2 / 3 (por pieza) | 0.44 / 0.52 s (0.96 s) | 0.24 / 0.32 s (0.56 s) |
| Tuerca 1 → fin de tuerca 3 | 17.8 s | 17.2 s |
| Último ciclo de AutomationCore (arranque → fin) | 42 s, con la espera de Work Complete | 39 s |

Meta 38 s. La soldadura subió 0.6 s por pieza: el WAIT SEC 0.2 al abrir la pistola (13/10) y la pre-alimentación de
2 s, que deja más espera de tuerca. Sigue sin medirse una serie de 10 piezas.

## Puntos

| Punto | Resultado |
|---|---|
| C01, C19 | Cerrados (AutomationCore_BKG activo, como R20) |
| C14, F19 | Se cierran con F47 y G21 |
| G19, F14, F38 | En proceso: código hecho; faltan pin vacío antes de alimentar y la prueba |
| G21 | En proceso: falta la prueba con la pieza red rabbit y con una pieza buena |
| F35, F46, F31 | En proceso: falta la prueba |
| G03 / C08 | En proceso: carga con pieza agregada; falta el protocolo de Load Data Determination |
| G05 | Abierto con avance |

## Riesgos

1. Doble tuerca después de un reset con tuerca en el pin (F38): probar antes de producción.
2. Configuración de seguridad cambiada sin checklist de aceptación (versión 55).
3. Tiempo ciclo: 42 s contra 38 s de meta.
4. El zip del respaldo incluye una orden de compra de Ethos: no reenviarlo tal cual a Gestamp.
