# R10 — Program Audit (BMW-03-10-R1)

Proyecto 250216 – Gestamp BMW G65 Nut Cell #3, Union SC. Insumo para el Gestamp Assembly Equipment Buy-Off
Workbook NA-FM-71-070 (pestañas "Robotics Approval" y "Controls Approval").

Alcance: revisión del **programa** del robot a partir de los respaldos completos del controlador (KRL `.src` /
`.dat`, `$config.dat`, `sps.sub`, machine data, `am.ini`). No hubo inspección física de la celda: todo lo físico
(dress pack, gabinete, cableado, red, relevadores de seguridad) queda **NO REVISADO**. Estado al respaldo del
2026-11-10 08:31 y reporte de seguridad del mismo día (actualizado el 2026-11-10). Lista maestra de puntos: `docs/open_items.json` (G = revisión de Gestamp, F/C = revisión de
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

## 1. Identificación

| Dato | Valor | Evidencia |
|---|---|---|
| Robot | KUKA KR 210 R2700 extra (C4, piso) | `KRC/R1/Mada/$machine.dat:431` `$TRAFONAME[]="#KR210R2700 EXTRA C4 FLR"` |
| Controlador | KUKA KR C4 | `am.ini`, estructura del respaldo |
| Software | KSS V8.3.29 (igual que la referencia de Gestamp NUT07_10R1) | `am.ini` `[Version] Version=V8.3.29` |
| Tech packages | AutomationCore 1.0.5, DeviceConnector 2.4.10, DiagnoseSafety 2.1.0, GlueTech 4.2.3, GripperSpotTech 4.0.4, KRC4 EthernetIP 2.0.3, LoadDataDetermination 6.2.6, NutWeld 1.0.4, RemoteService 1.2.0, SafeOperation 3.2.4, OrangeApps.UserLogonUSB 1.0.5 | `am.ini` `[TechPacks]` |
| Nombre del robot | `BMW_03_10_R1` (G01 cerrado por decisión de Edgar el 13/10: el nombre queda) | `am.ini` `RobName` |
| Número de serie | 658424 (F#: no aplica, es KUKA) | `am.ini` `IRSerialNr=658424`; `C/KRC/Roboter/Rdc/658424.cal` |
| Estación | 03-10 (BMW-03-10-R1) | encabezados de los módulos; revisión de Gestamp sección BMW-03-10R1 |
| Función en la celda | Material handler: toma la pieza en pickup 1 o 2 con EOAT 1 (gripper 1), la presenta al pedestal CenterLine de soldadura de tuercas por proyección (3 tuercas, alimentador QFP, timer Bosch), revisa tuercas con sensor y cámara, deja en conveyor o en rechazo; ciclo red rabbit (option 12). El programa del robot también controla el pedestal (CENTERLINE_WELD y PRELOAD en el submit). | `Program/Styles/optiones/style1opt1.src`, `Program/Centerline/*`, `Program/StyleApps/Options/style1app2opt1.src` (sensor), `style1app2opt2.src` (cámara) |
| Respaldo auditado | `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424_1.zip`, `am.ini` `Date=2026-11-10_08-31-30` (hora del controlador), Archive All, sha256 `1567fd5c…`; sacado por el programador de robot y entregado por Edgar Montiel para esta revisión. Reporte de seguridad de WorkVisual `Safety_Report_R10-11_10_2026.pdf` (10/11 10:33, CRC 78FA8691) | `audits/2026-11-10_08-31-30/AUDIT.md`; commit `51c56fa` |

## 2. Resumen del audit

- Revisión de Gestamp del 2026-10-02 (22 puntos): 13 cerrados o aceptados y 9 abiertos (G03, G05, G06, G07, G09,
  G11, G19, G21, G22); de esos, G09, G19 y G21 ya cumplen en código y solo falta la prueba en celda. G11 se reabrió el
  10/11 (un GOTO nuevo en `gun_open_check.src:66-81`). El buy-off depende de cerrar esos 9 y 5 puntos de Ethos que
  sus criterios piden (F43, F21, F31, F14, F38).
- **Seguridad, crítico:** PRELOAD corre en el submit y mueve el pedestal (QFP, pines, soplado) en cualquier modo,
  sin dueño de las salidas (F11, requiere revisión de seguridad con Gestamp).
- **Background de AutomationCore activo otra vez** (respaldo del 14/10, `sps.sub:102`): request to enter, brake test
  pendiente, mastering y estado al PLC como el estándar (C01, C19 cerrados). La condición de request to enter no
  incluye el preload (F11). Work Complete ya se manda al PLC desde `cell.src:65-72` (F46, falta prueba).
- **Detección de colisión apagada** en todo el programa (C09). La herramienta de seguridad es igual al TCP de las
  herramientas 1 y 2 (G02, confirmado con el reporte de seguridad del 10/11). La configuración de seguridad cambió
  otra vez el 10/11 (cell area; CRC 78FA8691) y la declaración de aceptación del reporte está sin firmas.
- Datos de carga: herramienta 1 67.28 kg con centro de masa; herramienta 2 "TOOL 1 WITH PART" 68.28 kg para los
  movimientos con pieza. Falta el protocolo de Load Data Determination como evidencia (G03/C08).
- Entrada al pedestal resuelta: PEDESTAL_CLEAR_CHECK confirma pistola abierta, clamp abierto y pin retraído antes de
  entrar y al salir, con vigilancia por interrupciones (F01 cerrado).
- Verificación de tuercas: ventana de pistola cerrada (sin tuerca / doble tuerca), sensor de tuerca por tuerca y
  cámara. Pendientes: la cámara puede tomar el resultado anterior (F54), ventana de 150 ms contra 200 ms de Gestamp
  (F07). Red rabbit ya con lógica OR y sin borrar el resultado en el drop (G21, falta prueba).
- Módulos sobrantes casi resueltos (G05: queda `pounce` y GlueTech instalado; `movetopurge` borrado el 10/11);
  ediciones en archivos de KUKA sin lista de entrega (C28). Desde el 10/11 el submit ya no llama `GRPg_ChkSetStatePLC`
  (teclas de estado del gripper, F55).
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
| 21 | TCP setup | OK | `TOOL_DATA[1]` y `TOOL_DATA[2]` = `{X 0,Y 0,Z 380.79,A -90,B -90,C -90}` (`$config.dat:234-235`); la herramienta de seguridad 1 "EOAT 1 GE4-001" tiene el mismo TCP (0 / 0 / 380.8, captura del smartHMI del 12/10 y reporte de seguridad del 10/11, G02 cerrado). Medición física del TCP no revisada; herramientas y bases con nombres de otro proyecto (C06). |
| 22 | RTCP (pedestal welder) | Not OK | `BASE_DATA[3]` "NUT WELDER" `{X 21.84,Y 1866.09,Z 658.47,A 90,B 0,C 180}` (`$config.dat:314`) sin medir contra el electrodo fijo (C05). Movimientos del pedestal mezclan base y external TCP (F22, C04: requiere decisión). |
| 23 | Latest Gestamp programming updates / standard | Not OK | 9 de 22 puntos de la revisión de Gestamp abiertos (sección 6). Comparado con NUT07_10R1; AutomationCore_BKG y NutWeld_BKG activos como Gestamp desde el 14/10. |
| 24 | Payloads correct / within spec | Not OK | `LOAD_DATA[1]` 67.28 kg con centro de masa e inercias (`$config.dat:271`); `LOAD_DATA[2]` "TOOL 1 WITH PART" 68.28 kg (la misma + 1 kg, mismo centro de masa, `$config.dat:272`) en los movimientos con pieza. Falta el protocolo de Load Data Determination y la masa real de la pieza (G03/C08, en proceso). `LOAD_A3_DATA` 50 kg (`$config.dat:308`). Capacidad contra carga no revisada. |
| 25 | No unused / commented code | Not OK | Borrados el 14/10: `capchange`, `electrodechange`, `redrabbit`, `safetest`; el 10/11 `movetopurge` (y su llamada en `glue.src`). Quedan `pounce` (plantilla de otra línea) y GlueTech instalado sin uso (G05). GOTO nuevo en `gun_open_check.src:66-81` (G11). Código comentado: quitado el 13/10. |
| 26 | Slave devices unicast | NO REVISADO | Configuración EtherNet/IP no revisada. |
| 27 | I/O bitmap per standard | Not OK | No se comparó contra el bitmap de Gestamp. El código usa nombres de señal (G12 cerrado), pero `KRC_IO.xml` mapea `$OUT[820..979]` e `$IN[820..930]` sobre los mismos bytes del adapter que `$OUT[1..160]` / `$IN[1..111]` (F18, requiere decisión) y hay declaraciones traslapadas de pistolas 2/3 (F17). |
| 28 | No unlabeled spare I/O used | Not OK | `$OUT[470]` declarado `do470Spare` (`automationcoreroutines.dat:1305`) y escrito por NutWeld_Bkg como `dopw1_Hidraulyc_Valve = $PERI_RDY` (`nutweldroutines.src:33`) desde el 11/10: confirmar que no tiene nada conectado. Nombres Spare dobles en `$IN[466/467/470]` (F17). |
| 29 | IP addresses per Gestamp list | NO REVISADO | No revisado. |
| 32 | Collision detection active / sensitive | Not OK | `TQ_STATE FALSE` en los 149 FDAT de movimiento, `BTQM_ACTIVE=FALSE` (`$config.dat:83`), `TQM_ACT` T21..T26 = 100000 (`tm_bib.dat:73`); reacción HALT (C09, F39). |
| 34 | E-stop / gate relays | NO REVISADO | Físico. |
| 35 | Robot Zone Assignment (NA-FM-71-138) | Not OK | El programa no pide ninguna zona (producción, repair, pounce); falta la forma NA-FM-71-138.1 (C11, requiere decisión). |
| 36 | Safety zones (SafeOperation) and recovery | NO REVISADO | Reporte de seguridad del 10/11 (CRC 78FA8691): cell area de 5 esquinas, X -2000 a 3510, Y -2700 a 1800 (cambiada el 10/11 06:41); espacio 1 "Nest Workspace" protegido, siempre activo y sin paro en el límite (solo señala), el pick queda dentro; espacios 2-16 apagados (F42). Los puntos del programa en base 0 quedan a 189 mm o más del cell area con la esfera de la herramienta (cálculo de esta revisión). Herramienta de seguridad igual al TCP (G02 cerrado). `$AXWORKSPACE[1..8]` en `#OFF` (`$machine.dat:378`); los espacios cartesianos solo señalan (F42). Configuración de seguridad y recuperación no revisadas en el controlador. |
| 37 | Aux 24 V off with motors off | NO REVISADO | Físico / eléctrico. |
| 38 | Hard / soft stops | NO REVISADO | Topes mecánicos y límites de software de ejes no revisados. |
| 39 | Adjacent robots not in teach at same time | NO REVISADO | Lógica de celda / PLC no revisada. |
| 40 | Safety settings locked + signature recorded | Not OK | Configuración de seguridad cambiada el 10/10 (herramienta), el 13/10 y el 10/11 06:41 (cell area): versión 56 en el respaldo (WorksheetCrc 2441542264), ParameterCrc 78FA8691 (`SCTLCRC.XML`), igual al reporte de WorkVisual del 10/11 (que dice versión 57). La declaración de aceptación del reporte está sin firmas, sin número de serie y sin código de activación; checklist de aceptación no presentado. Bloqueo de la configuración no revisado. |
| 41 | Repair / maintenance positions | OK | `XREPAIR` (`automationglobalpos.dat:17`); `HomeToRepair` / `RepairToHome` con `di009GoToRepair` (`cell.src:83`, `:88`); `do009RobotAtRepair` calculado en `sps.sub:185` y en AutomationCore_BKG (`automationcoreroutines.src:115`). Prueba en celda no vista. |
| 42 | Interference with peripheral tooling monitored | Not OK | Entrada al pedestal confirmada (F01 cerrado). Pero PRELOAD mueve el pedestal en cualquier modo (F11, crítico) y los permisos de drop-off y de application se revisan después de llegar al punto (`style1drop1opt1.src:38→49`, F48; `style1app2opt1.src:46→56`, F50). |
| 43 | Cannot run auto with simulated I/O | NO REVISADO | No revisado. |
| 44 | Peripheral Ethernet status to PLC | Not OK | Desde el 14/10 AutomationCore_BKG calcula `do048`…`do060` con los mensajes de bus (`automationcoreroutines.src:152-186`), pero `do052EOATVlvMnfldEnetOK` está fijo en TRUE (`:178`, edición en el archivo de KUKA). Prueba con el PLC no vista. |
| 45 | Clear-of-index / zone signals (conveyor) | Not OK | Pickup clear y drop-off clear por AutomationCore (`do065PickupClear1`, `do075DropOffClear1`). El permiso de drop-off al conveyor se pide después de `PTP P5` (F48). |
| 46 | Request-to-enter finishes cycle before stop | NO REVISADO | Desde el 14/10 `doCriticalWZ` lo escribe AC_Request_to_enter (`automationcoreroutines.src:1411-1434`, estándar como R20): niega la entrada con la pistola en trabajo o gripper / brake test / mastering en proceso (C19 cerrado). El preload no está en la condición (F11). Comportamiento con el PLC no revisado. |
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
| C-1 | E-stop / program reset recovery | Not OK | Sin estado seguro completo del pedestal al cancelar o resetear (F10); NutWeld_ProcessReset apaga weld init, programa Bosch, intensify y blow-off. Desde el 14/10 `NUT_STATE_INIT` reinicia el estado de la tuerca al arrancar (`preload.src:260-285`, F38 en proceso); con una tuerca ya en el pin puede alimentar otra. |
| C-2 | Request-to-enter | NO REVISADO | Ver ítem 46. |
| C-3 | Crash conditions robot / tooling | Not OK | Entrada al pedestal con PEDESTAL_CLEAR_CHECK e interrupciones 20-24 (F01 cerrado). Detección de colisión apagada (C09); PRELOAD en cualquier modo (F11); permisos después de llegar (F48, F50). |
| C-4 | Home = initial load position | NO REVISADO | `HomeCheck` antes de cada ciclo (`cell.src:52`); si HOME es la posición de carga inicial no se revisó. |
| C-5 | Poka-yoke / 300 % fastener check | Not OK | Tres chequeos en código: ventana de pistola cerrada (sin tuerca / doble tuerca, `CL_GUN_IN_WINDOW_TIME=150`, `$config.dat:846`; Gestamp pide 200 ms), sensor de tuerca por tuerca (`style1app2opt1.src`, WAIT SEC 0.2 antes de leer) y cámara OK/NG (`style1app2opt2.src:63-68`). Pendientes: resultado de cámara de la pieza anterior (F54), banderas sin reset al inicio (F03), HALT tras el reintento (F07). |
| C-6 | Red rabbit | OK | Desde el 14/10: FAILED con cualquier tuerca (OR), PASSED sin ninguna (`style1app2opt1.src:144-145`); el drop red rabbit ya no borra el resultado; la cámara solo puede dar FAILED (`style1app2opt2.src:63-68`). Prueba en celda pendiente (G21 en proceso). Ciclo red rabbit propio aceptado (G08). |
| C-7 | LVDT / TOX interlock | OK | LPT de la pistola: rango abierto 137000..142000 vigilado por interrupciones 20-21 al entrar y salir del pedestal (`style1app1opt1a.src`, GUN_OPEN_CHECK). TOX: no aplica en R10. |
| C-8 | HMI pantallas de robot | NO REVISADO | Pantallas del PLC/HMI no revisadas. `GripperConfig.xml` del smartHMI desincronizado con `grp_data.dat` (F33). |
| C-9 | Work Complete / fin de ciclo al PLC | OK | Desde el 14/10 `cell.src:65-72` manda `do015WorkComplete` y espera `di015WorkCompleteAckn` con mensaje, después de EndOfCycle (que sigue editado en el archivo de KUKA). Prueba con el PLC pendiente (F46 en proceso). |
| C-10 | Brake test due al PLC | Not OK | `do021BrakeTestReqd` lo escribe otra vez AutomationCore_BKG (14/10); el camino del brake test sigue enseñado con tool/base de otro robot (F47). |

## 5. Desempeño

- Tiempo ciclo: cerrado por Gestamp; fuera del alcance de este documento.
- Fallas recurrentes: tuercas faltantes, 8 reintentos acumulados (`nNutRetryTotal`, `gun_open_check.dat:39`). El
  programador subió la alimentación a 5 s el 10/10 ("el alimentador sopla hasta 5 s") y la regresó a 2 s el 11/10;
  la alimentación no se confirma con `$IN[481] dipw1_FeedComplt` (F13). Atribución (alimentador de Gestamp,
  programa o hardware): no determinada.

## 6. Pendientes / Open issues

\*Programador = programador de robot del integrador; la empresa (Ethos o SGA) no se establece en esta revisión.
"Bloquea buy-off": Sí para los puntos de Gestamp y los que su criterio pide; para los demás, Sí cuando el ítem del
workbook queda Not OK por ese punto.

| # | Descripción | Responsable | Bloquea buy-off |
|---|---|---|---|
| SafeOperation | Checklist de aceptación firmado de la configuración de seguridad actual (CRC 78FA8691, cambios del 10/10, 13/10 y 10/11) y el reporte firmado | Programador\* | Sí (ítem 40) |
| G03 | Protocolo de Load Data Determination de la herramienta 1 | Programador\* | Sí |
| G05 | Borrar `pounce` y desinstalar GlueTech | Programador\* | Sí |
| G06 / F43 | Cambio de electrodo: forma de pedirlo y reset del stepper confirmado | Gestamp / Programador\* | Sí |
| G07 / F21 / F31 | Options 1, 2, 7 y 8 llaman el mismo programa; forms AutomationCore y GripperTech con parámetros ocultos distintos | Gestamp (decisión) / Programador\* | Sí |
| G19 / F14 / F38 | Handshake de la tuerca: código hecho el 14/10; faltan pin vacío antes de alimentar y la prueba (reset con y sin tuerca, corte a mitad de preload) | Programador\* | Sí |
| G21 | Red rabbit: código hecho el 14/10; falta la prueba con la pieza red rabbit y con una buena | Programador\* | Sí |
| G09 | `$OUT[18]` desde los sensores (sps.sub, 10/11): falta la prueba en T1 | Programador\* | Sí |
| G11 | Quitar el GOTO de `gun_open_check.src` (10/11) | Programador\* | Sí |
| G22 | Uso de AutomationCore: Gestamp no ha mandado su lista | Gestamp | Sí |
| F11 | PRELOAD en el submit mueve el pedestal en cualquier modo (crítico) | Gestamp (seguridad) / Programador\* | Sí (ítem 42) |
| F12 / F46 | Verificar con el PLC los bits de AutomationCore y Work Complete; `do052` fijo en TRUE | Programador\* / PLC | Sí (ítem 44) |
| F47 | Camino del brake test enseñado con tool/base de otro robot | Programador\* | Sí (C-10) |
| C09 | Detección de colisión apagada | Programador\* / Gestamp (si se dispensa) | Sí (ítem 32) |
| C11 | Zonas y forma NA-FM-71-138.1 | Gestamp / Ethos | Sí (ítem 35) |
| C05 | Medir el TCP remoto del pedestal | Programador\* | Sí (ítem 22) |
| F48 / F50 | Permisos de drop-off y application antes de llegar | Programador\* | Sí (ítems 42, 45) |
| F10 | Estado seguro del pedestal al cancelar o resetear | Programador\* | Sí (C-1) |
| F54 | Confirmar que la cámara no da el resultado de la pieza anterior | Programador\* / PLC | Sí (C-5) |
| C28 | Lista de ediciones en archivos de KUKA para la entrega | Programador\* / Ethos | No |
| — | Todo lo marcado NO REVISADO en las secciones 3 y 4 | Ethos (en sitio) | Por revisar |

## 7. Backups y entregables

| Respaldo | Fecha (`am.ini`) | Dónde está | Nota |
|---|---|---|---|
| `v431_03_10_r1.zip` | 2026-10-02 | Repositorio `EdgarMontielG/Cell-3_R10`, commit `22a98cc` | Programa original del integrador, tal como se recibió |
| `bmw_03_10_r1.zip` | 2026-10-05 09:43 y 14:46 | Mismo repositorio (`audits/2026-10-05_*`; 14:46 en commit `468e29f`) | Base del cambio de base del 11/10 |
| `V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-10 21:20 | Commit `cd17b34` | Versión de oficina del 05/10 cargada + cambios del programador |
| `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-11 22:32 | Commit `8cb5c7a` | |
| `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-13 07:32 | Commit `6e70821` | Edgar lo entregó como el del 12/10 |
| `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` | 2026-10-14 15:05 | Commit `c401a76` | El zip trae también una orden de compra de Ethos (PDF), que no es parte del respaldo y no se guardó |
| `BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424_1.zip` | 2026-11-10 08:31 | Commit `51c56fa`, rama `claude/hopeful-mendel-mo6t3h` | **Último auditado (base actual)**. Con el reporte de seguridad de WorkVisual del 10/11 (no se guardó en el repositorio) |

- Cada respaldo se importó byte por byte al repositorio y se auditó contra el anterior
  (`audits/<fecha>/AUDIT.md`, `REVISION.es.md`).
- Entregables vigentes (2026-11-10 10:36): `dist/R10_Gestamp_Puntos_*.xlsx`, `dist/R10_Gestamp_reporte_*.pdf`
  (puntos de Gestamp para el buy-off) y `dist/R10_Mejora_Puntos_*.xlsx`, `dist/R10_Mejora_reporte_*.pdf`.
- Entrega del respaldo a Gestamp: no consta en esta revisión (NO REVISADO).
