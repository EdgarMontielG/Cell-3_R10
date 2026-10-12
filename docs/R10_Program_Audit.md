# R10 — Program Audit (BMW-03-10-R1)

Proyecto 250216 – Gestamp BMW G65 Nut Cell #3, Union SC. Insumo para el Gestamp Assembly Equipment Buy-Off
Workbook NA-FM-71-070 (pestañas "Robotics Approval" y "Controls Approval").

Alcance: revisión del **programa** del robot a partir de los respaldos completos del controlador (KRL `.src` /
`.dat`, `$config.dat`, `sps.sub`, machine data, `am.ini`). No hubo inspección física de la celda: todo lo físico
(dress pack, gabinete, cableado, red, relevadores de seguridad) queda **NO REVISADO**. Estado al respaldo del
2026-10-11 22:32. Lista maestra de puntos: `docs/open_items.json` (G = revisión de Gestamp, F/C = revisión de
Ethos); detalle técnico: `docs/FINDINGS.md`.

Origen del código:

- **Estándar Gestamp / KUKA (existente, reutilizado):** paquetes de KUKA instalados en el controlador
  (AutomationCore 1.0.5 con su estructura `cell.src` / Style / Pick / App / Drop y rutinas de background, NutWeld
  1.0.4, GripperSpotTech 4.0.4, SafeOperation 3.2.4, LoadDataDetermination 6.2.6, `KRC/R1/TP/**`). Como referencia
  de estándar se usó el respaldo de Gestamp `nut07_10r1.zip` (robot NUT07_10R1, serie 658415, KSS 8.3.29,
  2026-08-18), revisado en la conversación de R20; el programador se basó en ese respaldo.
- **Programa del integrador (programador de robot):** módulos de la celda (`Program/Centerline/*`: PRELOAD,
  CENTERLINE_WELD, CENTERLINE_HOME, GUN_OPEN_CHECK, Request_next_nut; `Program/StylePicks|StyleApps|StyleDrops/*`;
  `Program/Utilities/rejectge4`; partes de usuario de `sps.sub` y `$config.dat`) y ediciones dentro de archivos de
  KUKA (C28): `automationcoreroutines.src` (EndOfCycle sin Work Complete), `ir_stopm.src`, `tm_bib.dat`,
  `nutweldroutines.src/.dat` (2026-10-11), `grp_func.src`, `grp_user.src`, `bas.src`. Respaldo de partida: el del
  2026-10-02, tal como se recibió; corrió en producción y Gestamp no lo aceptó. La empresa del programador (Ethos o
  SGA) no se establece en esta revisión.
- **Ethos:** revisión de hallazgos y una versión de oficina (2026-10-03 a 2026-10-07: depuración de comentarios en
  inglés, encabezados Gestamp, nombres de señal, correcciones de la revisión de Gestamp, integración). El programador
  cargó la versión de oficina del 2026-10-05 antes de su respaldo del 2026-10-10 y trabajó encima del 06 al 11/10.
  Entrega pendiente de cargar: `entregas/2026-10-11_F52_esperas_PLC` (solo medición de tiempos).

## 1. Identificación

| Dato | Valor | Evidencia |
|---|---|---|
| Robot | KUKA KR 210 R2700 extra (C4, piso) | `KRC/R1/Mada/$machine.dat:431` `$TRAFONAME[]="#KR210R2700 EXTRA C4 FLR"` |
| Controlador | KUKA KR C4 | `am.ini`, estructura del respaldo |
| Software | KSS V8.3.29 (igual que la referencia de Gestamp NUT07_10R1) | `am.ini` `[Version] Version=V8.3.29` |
| Tech packages | AutomationCore 1.0.5, DeviceConnector 2.4.10, DiagnoseSafety 2.1.0, GlueTech 4.2.3, GripperSpotTech 4.0.4, KRC4 EthernetIP 2.0.3, LoadDataDetermination 6.2.6, NutWeld 1.0.4, RemoteService 1.2.0, SafeOperation 3.2.4, OrangeApps.UserLogonUSB 1.0.5 | `am.ini` `[TechPacks]` |
| Nombre del robot | `BMW_03_10_R1` (Gestamp pide cambiarlo, G01) | `am.ini` `RobName` |
| Número de serie | 658424 (F#: no aplica, es KUKA) | `am.ini` `IRSerialNr=658424`; `C/KRC/Roboter/Rdc/658424.cal` |
| Estación | 03-10 (BMW-03-10-R1) | encabezados de los módulos; revisión de Gestamp sección BMW-03-10R1 |
| Función en la celda | Material handler: toma la pieza en pickup 1 o 2 con EOAT 1 (gripper 1), la presenta al pedestal CenterLine de soldadura de tuercas por proyección (3 tuercas, alimentador QFP, timer Bosch), revisa tuercas con sensor y cámara, deja en conveyor o en rechazo; ciclo red rabbit (option 12). El programa del robot también controla el pedestal (CENTERLINE_WELD y PRELOAD en el submit). | `Program/Styles/optiones/style1opt1.src`, `Program/Centerline/*`, `Program/StyleApps/Options/style1app2opt1.src` (sensor), `style1app2opt2.src` (cámara) |
| Respaldo auditado | `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip`, `am.ini` `Date=2026-10-11_22-32-16`, Archive All, sha256 `0f71260b…`; sacado por el programador de robot y entregado por Edgar Montiel para esta revisión | `audits/2026-10-11_22-32-16/AUDIT.md`; commit `8cb5c7a` |

## 2. Resumen del audit

- Revisión de Gestamp del 2026-10-02 (22 puntos): 13 cerrados o aceptados y 9 abiertos (G01, G02, G03, G05, G06,
  G07, G19, G21, G22). El buy-off depende de cerrar esos 9 y 6 puntos de Ethos que sus criterios piden (C02, F43,
  F21, F31, F14, F38).
- **Seguridad, crítico:** PRELOAD corre en el submit y mueve el pedestal (QFP, pines, soplado) en cualquier modo,
  sin dueño de las salidas (F11, requiere revisión de seguridad con Gestamp).
- **Request to enter no se reporta:** desde el respaldo del 10/10 el background de AutomationCore está apagado;
  `doCriticalWZ` queda en FALSE y el PLC ve la entrada permitida aunque el pedestal esté en proceso (C19, C01).
  Tampoco se reportan brake test pendiente, Ethernet OK de periféricos ni mastering pendiente.
- **Detección de colisión apagada** en todo el programa (C09) y herramienta de seguridad distinta al TCP de la
  herramienta 1 (G02).
- Datos de carga de la herramienta 1 ya determinados (67.28 kg con centro de masa), falta el protocolo de Load Data
  Determination como evidencia (G03/C08).
- Entrada al pedestal resuelta: PEDESTAL_CLEAR_CHECK confirma pistola abierta, clamp abierto y pin retraído antes de
  entrar y al salir, con vigilancia por interrupciones (F01 cerrado).
- Verificación de tuercas: ventana de pistola cerrada (sin tuerca / doble tuerca), sensor de tuerca por tuerca y
  cámara. Pendientes: la cámara puede tomar el resultado anterior (F54), ventana de 150 ms contra 200 ms de Gestamp
  (F07/F53), red rabbit con lógica AND y resultado borrado en el drop (G21/F19).
- Tiempo ciclo: meta de R10 38 s pieza a pieza. Medido: 17.2 s de la tuerca 1 al fin de la tuerca 3; último ciclo
  de AutomationCore 39 s el 10/10 (probablemente producción, sin confirmar). Falta medir 10 piezas seguidas.
- Programa con módulos sobrantes y código comentado (G05), ediciones en archivos de KUKA sin lista de entrega (C28).
- Lo físico (dress pack, gabinete, E-stop, red, IP) no se revisó.

## 3. Tabla de ítems Robotics Approval

| # | Ítem (texto corto) | Resultado | Evidencia o comentario |
|---|---|---|---|
| 1 | F# controller vs base | NO REVISADO | Placa física no revisada. En el respaldo la serie es 658424 (`am.ini`, `Rdc/658424.cal`). KUKA no usa F#. |
| 2–9 | Dress pack | NO REVISADO | Físico. |
| 10–11 | Enclosure outside | NO REVISADO | Físico. |
| 12 | ESTOP board / jumpers | NO REVISADO | Físico. |
| 13 | PLC Ethernet Port 1 / switch Port 2 | NO REVISADO | Físico. |
| 14 | Master / zero marks | NO REVISADO | Marcas físicas no revisadas. No existe programa de mastering `ZERO_G1` (C10); sí el mastering reference (`masref_main`, `cell.src:93`); `XREFSWITCH` re-enseñado ~1 mm el 10/10 (F35). |
| 15 | EOAT mounted per RDS | NO REVISADO | Físico; RDS no revisado. |
| 18 | Software version | OK | KSS V8.3.29, igual que el respaldo de referencia de Gestamp NUT07_10R1. Versión exigida por Gestamp no revisada. |
| 19 | Master counts (Fanuc) | N/A | Robot KUKA. Datos de mastering en `C/KRC/Roboter/Rdc/658424.mam`, no revisados. |
| 21 | TCP setup | Not OK | `TOOL_DATA[1]={X 0,Y 0,Z 380.79,A -90,B -90,C -90}` (`$config.dat:234`). La herramienta de seguridad no es igual al TCP (G02, abierto). Herramientas y bases con nombres de otro proyecto (C06). Medición del TCP no revisada. |
| 22 | RTCP (pedestal welder) | Not OK | `BASE_DATA[3]` "NUT WELDER" `{X 21.84,Y 1866.09,Z 658.47,A 90,B 0,C 180}` (`$config.dat:314`) sin medir contra el electrodo fijo (C05). Movimientos del pedestal mezclan base y external TCP (F22, C04: requiere decisión). |
| 23 | Latest Gestamp programming updates / standard | Not OK | 9 de 22 puntos de la revisión de Gestamp abiertos (sección 6). Comparado con NUT07_10R1; AutomationCore_BKG apagado (Gestamp lo tiene activo, C01). |
| 24 | Payloads correct / within spec | Not OK | `LOAD_DATA[1]` 67.28 kg con centro de masa e inercias (`$config.dat:271`), ya no los 210 kg tecleados; falta el protocolo de Load Data Determination (G03/C08, en proceso). `LOAD_A3_DATA` 50 kg (`$config.dat:308`). Capacidad contra carga no revisada. |
| 25 | No unused / commented code | Not OK | Módulos sobrantes: `capchange`, `electrodechange`, `redrabbit` (no compila: usa `REDRABBIT`, quitado de `$config.dat`), `pounce`, `safetest`; GlueTech instalado sin uso (`movetopurge`) (G05). Código comentado: 17 líneas en `sps.sub` (audit 11/10), TRIGGER comentado en `style1app1opt1a/b`, `opt2a/b` (audit 10/10). |
| 26 | Slave devices unicast | NO REVISADO | Configuración EtherNet/IP no revisada. |
| 27 | I/O bitmap per standard | Not OK | No se comparó contra el bitmap de Gestamp. El código usa nombres de señal (G12 cerrado), pero `KRC_IO.xml` mapea `$OUT[820..979]` e `$IN[820..930]` sobre los mismos bytes del adapter que `$OUT[1..160]` / `$IN[1..111]` (F18, requiere decisión) y hay declaraciones traslapadas de pistolas 2/3 (F17). |
| 28 | No unlabeled spare I/O used | Not OK | `$OUT[470]` declarado `do470Spare` (`automationcoreroutines.dat:1305`) y escrito por NutWeld_Bkg como `dopw1_Hidraulyc_Valve = $PERI_RDY` (`nutweldroutines.src:33`) desde el 11/10: confirmar que no tiene nada conectado. Nombres Spare dobles en `$IN[466/467/470]` (F17). |
| 29 | IP addresses per Gestamp list | NO REVISADO | No revisado. |
| 32 | Collision detection active / sensitive | Not OK | `TQ_STATE FALSE` en los 149 FDAT de movimiento, `BTQM_ACTIVE=FALSE` (`$config.dat:83`), `TQM_ACT` T21..T26 = 100000 (`tm_bib.dat:73`); reacción HALT (C09, F39). |
| 34 | E-stop / gate relays | NO REVISADO | Físico. |
| 35 | Robot Zone Assignment (NA-FM-71-138) | Not OK | El programa no pide ninguna zona (producción, repair, pounce); falta la forma NA-FM-71-138.1 (C11, requiere decisión). |
| 36 | Safety zones (SafeOperation) and recovery | Not OK | SafeOperation 3.2.4 con espacio de monitoreo "Nest Workspace" (F42). Herramienta de seguridad distinta al TCP (G02). `$AXWORKSPACE[1..8]` en `#OFF` (`$machine.dat:378`); los espacios cartesianos solo señalan (F42). Configuración de seguridad y recuperación no revisadas en el controlador. |
| 37 | Aux 24 V off with motors off | NO REVISADO | Físico / eléctrico. |
| 38 | Hard / soft stops | NO REVISADO | Topes mecánicos y límites de software de ejes no revisados. |
| 39 | Adjacent robots not in teach at same time | NO REVISADO | Lógica de celda / PLC no revisada. |
| 40 | Safety settings locked + signature recorded | NO REVISADO | Checksum y checklist de aceptación no visibles en el respaldo; G02 los pide al corregir la herramienta de seguridad. |
| 41 | Repair / maintenance positions | OK | `XREPAIR` (`automationglobalpos.dat:17`); `HomeToRepair` / `RepairToHome` con `di009GoToRepair` (`cell.src:83`, `:88`); `do009RobotAtRepair` calculado en `sps.sub:248-257` desde el 11/10. Prueba en celda no vista. |
| 42 | Interference with peripheral tooling monitored | Not OK | Entrada al pedestal confirmada (F01 cerrado). Pero PRELOAD mueve el pedestal en cualquier modo (F11, crítico) y los permisos de drop-off y de application se revisan después de llegar al punto (`style1drop1opt1.src:38→49`, F48; `style1app2opt1.src:46→56`, F50). |
| 43 | Cannot run auto with simulated I/O | NO REVISADO | No revisado. |
| 44 | Peripheral Ethernet status to PLC | Not OK | `do048RPWCtrlrEnetOK`, `do052EOATVlvMnfldEnetOK` y similares fijos en FALSE al arrancar (`sps.sub:56-59`): AutomationCore_BKG apagado desde el 10/10 (C01). |
| 45 | Clear-of-index / zone signals (conveyor) | Not OK | Pickup clear y drop-off clear por AutomationCore (`do065PickupClear1`, `do075DropOffClear1`). El permiso de drop-off al conveyor se pide después de `PTP P5` (F48). |
| 46 | Request-to-enter finishes cycle before stop | Not OK | `doCriticalWZ=FALSE` al arrancar (`sps.sub:44`) y nadie lo escribe: el PLC ve entrada permitida con el pedestal en proceso (C19, reabierto el 12/10). |
| 52 | Air / gas restriction stops robot | NO REVISADO | En código: antes de entrar al pedestal GUN_OPEN_CHECK espera `$IN[3132] dipw1_AirOK` con mensaje (`gun_open_check.src:61-62`, `bGunAirCheck=TRUE`); `do094AirOK` al PLC. Comportamiento en el resto del ciclo y corte de aire de la celda no revisados. |
| — | Spot weld | N/A | El robot no lleva pistola. La soldadura de tuercas la hace el pedestal CenterLine fijo (timer Bosch); el robot presenta la pieza y el programa del robot comanda el pedestal. GripperSpotTech se usa solo para el gripper. |
| — | MIG | N/A | No hay proceso MIG. |
| — | Sealer | N/A | GlueTech instalado sin uso (debe desinstalarse, G05); base "PED SEALER" de otro proyecto (C06). |
| — | SPR | N/A | No hay proceso SPR. |
| — | Flow drill | N/A | No hay proceso flow drill. |
| — | Laser | N/A | No hay proceso láser. |
| — | TOX | N/A | No aparece TOX en el programa de este robot. |

## 4. Ítems de Controls relacionados

| # | Ítem (texto corto) | Resultado | Evidencia o comentario |
|---|---|---|---|
| C-1 | E-stop / program reset recovery | Not OK | Sin estado seguro del pedestal al cancelar o resetear (F10); desde el 11/10 NutWeld_ProcessReset apaga weld init, programa Bosch, intensify y blow-off (avance parcial). Estado de la tuerca no se reinicializa tras reset o reinicio (F38, G19). |
| C-2 | Request-to-enter | Not OK | Ver ítem 46 (C19). |
| C-3 | Crash conditions robot / tooling | Not OK | Entrada al pedestal con PEDESTAL_CLEAR_CHECK e interrupciones 20-24 (F01 cerrado). Detección de colisión apagada (C09); PRELOAD en cualquier modo (F11); permisos después de llegar (F48, F50). |
| C-4 | Home = initial load position | NO REVISADO | `HomeCheck` antes de cada ciclo (`cell.src:52`); si HOME es la posición de carga inicial no se revisó. |
| C-5 | Poka-yoke / 300 % fastener check | Not OK | Tres chequeos en código: ventana de pistola cerrada (sin tuerca / doble tuerca, `CL_GUN_IN_WINDOW_TIME=150`, `$config.dat:846`; Gestamp pide 200 ms), sensor de tuerca por tuerca (`style1app2opt1.src`, WAIT SEC 0.2 antes de leer) y cámara OK/NG (`style1app2opt2.src:63-68`). Pendientes: resultado de cámara de la pieza anterior (F54), banderas sin reset al inicio (F03), HALT tras el reintento (F07). |
| C-6 | Red rabbit | Not OK | FAILED solo con las 3 tuercas (AND) y el drop red rabbit borra el resultado (G21, F19). Ciclo red rabbit propio aceptado (G08). |
| C-7 | LVDT / TOX interlock | OK | LPT de la pistola: rango abierto 137000..142000 vigilado por interrupciones 20-21 al entrar y salir del pedestal (`style1app1opt1a.src`, GUN_OPEN_CHECK). TOX: no aplica en R10. |
| C-8 | HMI pantallas de robot | NO REVISADO | Pantallas del PLC/HMI no revisadas. `GripperConfig.xml` del smartHMI desincronizado con `grp_data.dat` (F33). |
| C-9 | Work Complete / fin de ciclo al PLC | Not OK | EndOfCycle de AutomationCore editado: Work Complete comentado (`automationcoreroutines.src:381-389`, F46). |
| C-10 | Brake test due al PLC | Not OK | `do021BrakeTestReqd` fijo en FALSE (`sps.sub:53`); camino del brake test enseñado con tool/base de otro robot (C14, F47). |

## 5. Cycle time y desempeño

| Medición | Valor | Fuente |
|---|---|---|
| Meta de R10 (Edgar, 2026-10-11) | 38 s pieza a pieza | — |
| Dentro de la pistola por tuerca (CENTERLINE_WELD) | 4.03 / 3.92 / 3.91 s | timers del programador `nCtInWelder`, `gun_open_check.dat:76-78` (10/10) |
| Tuerca a tuerca | 6.71 / 6.61 s | `nCtNutToNut[2..3]` |
| Espera de tuerca | 0 / 0.24 / 0.32 s (0.56 s por pieza; ~4 s antes de las tuercas 2 y 3 en el video del 05/10) | `nCtNutWait` |
| Tuerca 1 en posición → fin de tuerca 3 | 17.2 s | `nCtPart` |
| Último ciclo de AutomationCore (arranque → fin, sin espera en HOME) | 50 s (05/10), 39 s (10/10), 26 s (11/10, ciclo sin soldar) | `nCycleTime`, `automationcoredata.dat` |

- El ciclo completo no se ha medido con varias piezas seguidas; `nCtCycle` = 276.8 s del 10/10 incluye un paro.
  Falta la medición de 10 piezas y de las esperas del PLC (entrega `2026-10-11_F52_esperas_PLC`, no cargada).
- Cuellos de botella identificados: la soldadura de las 3 tuercas ocupa 45 % de la meta; la espera fija de la
  cámara (0.2 s → 2.0 s el 10/10 → espera del resultado el 11/10); WAIT SEC 0.2 al abrir la pistola, regresado el
  11/10 (+0.6 s por pieza); permisos del PLC pedidos después de llegar (F48, F50). Palancas pendientes estimadas en
  ~2-6 s por pieza sin medir (`audits/2026-10-11_tiempo_ciclo/PALANCAS.es.md`).
- Fallas recurrentes: tuercas faltantes, 8 reintentos acumulados (`nNutRetryTotal=8`, `gun_open_check.dat:53`). El
  programador subió la alimentación a 5 s el 10/10 ("el alimentador sopla hasta 5 s") y la regresó a 2 s el 11/10;
  la alimentación no se confirma con `$IN[481] dipw1_FeedComplt` (F13). Atribución (alimentador de Gestamp,
  programa o hardware): no determinada.

## 6. Pendientes / Open issues

\*Programador = programador de robot del integrador; la empresa (Ethos o SGA) no se establece en esta revisión.
"Bloquea buy-off": Sí para los puntos de Gestamp y los que su criterio pide; para los demás, Sí cuando el ítem del
workbook queda Not OK por ese punto.

| # | Descripción | Responsable | Bloquea buy-off |
|---|---|---|---|
| G01 / C02 | Cambiar el nombre del robot (por analogía NUT03_10R1) y la designación en encabezados; formato a confirmar | Gestamp (formato) / Programador\* | Sí |
| G02 | Herramienta de seguridad igual al TCP de la herramienta 1; checksum y checklist de aceptación | Programador\* | Sí |
| G03 | Protocolo de Load Data Determination de la herramienta 1 | Programador\* | Sí |
| G05 | Borrar módulos sobrantes, decidir `safetest`, desinstalar GlueTech; `redrabbit` no compila | Programador\* / Gestamp (safetest) | Sí |
| G06 / F43 | Cambio de electrodo: forma de pedirlo y reset del stepper confirmado | Gestamp / Programador\* | Sí |
| G07 / F21 / F31 | Options 1, 2, 7 y 8 llaman el mismo programa; forms AutomationCore y GripperTech con parámetros ocultos distintos | Gestamp (decisión) / Programador\* | Sí |
| G19 / F14 / F38 | Handshake de la tuerca ante selección de bloque, reset y reinicio | Programador\* | Sí |
| G21 | Red rabbit con lógica OR y resultado sin borrar en el drop | Programador\* | Sí |
| G22 | Uso de AutomationCore: Gestamp no ha mandado su lista | Gestamp | Sí |
| F11 | PRELOAD en el submit mueve el pedestal en cualquier modo (crítico) | Gestamp (seguridad) / Programador\* | Sí (ítem 42) |
| C19 / C01 | Request to enter y estado al PLC: reactivar AutomationCore_BKG como en R20 | Programador\* | Sí (ítems 44, 46) |
| C14 | Brake test pendiente al PLC; camino con tool/base de otro robot | Programador\* | Sí (C-10) |
| C09 | Detección de colisión apagada | Programador\* / Gestamp (si se dispensa) | Sí (ítem 32) |
| C11 | Zonas y forma NA-FM-71-138.1 | Gestamp / Ethos | Sí (ítem 35) |
| C05 | Medir el TCP remoto del pedestal | Programador\* | Sí (ítem 22) |
| F48 / F50 | Permisos de drop-off y application antes de llegar | Programador\* | Sí (ítems 42, 45) |
| F10 | Estado seguro del pedestal al cancelar o resetear | Programador\* | Sí (C-1) |
| F54 | Confirmar que la cámara no da el resultado de la pieza anterior | Programador\* / PLC | Sí (C-5) |
| F52 | Tiempo ciclo: medir 10 piezas y llegar a 38 s | Programador\* / Ethos | No (meta interna) |
| C28 | Lista de ediciones en archivos de KUKA para la entrega | Programador\* / Ethos | No |
| — | Todo lo marcado NO REVISADO en las secciones 3 y 4 | Ethos (en sitio) | Por revisar |

## 7. Backups y entregables

| Respaldo | Fecha (`am.ini`) | Dónde está | Nota |
|---|---|---|---|
| `v431_03_10_r1.zip` | 2026-10-02 | Repositorio `EdgarMontielG/Cell-3_R10`, commit `22a98cc` | Programa original del integrador, tal como se recibió |
| `bmw_03_10_r1.zip` | 2026-10-05 09:43 y 14:46 | Mismo repositorio (`audits/2026-10-05_*`; 14:46 en commit `468e29f`) | Base del cambio de base del 11/10 |
| `V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-10 21:20 | Commit `cd17b34` | Versión de oficina del 05/10 cargada + cambios del programador |
| `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-11 22:32 | Commit `8cb5c7a`, rama `claude/hopeful-mendel-mo6t3h` | **Último auditado (base actual)** |

- Cada respaldo se importó byte por byte al repositorio y se auditó contra el anterior
  (`audits/<fecha>/AUDIT.md`, `REVISION.es.md`).
- Entregables vigentes (2026-10-12 06:25): `dist/R10_Gestamp_Puntos_*.xlsx`, `dist/R10_Gestamp_reporte_*.pdf`
  (puntos de Gestamp para el buy-off) y `dist/R10_Mejora_Puntos_*.xlsx`, `dist/R10_Mejora_reporte_*.pdf`.
- Entrega de código pendiente de cargar: `entregas/2026-10-11_F52_esperas_PLC` (medición de esperas del PLC).
- Entrega del respaldo a Gestamp: no consta en esta revisión (NO REVISADO).
