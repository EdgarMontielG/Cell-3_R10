# Cambio de base y revisión contra el estándar de Gestamp (respaldo NUT07_10R1), 2026-10-11

Decisión de Edgar (2026-10-11, igual que en R20 el 09-10/10):

- La base auditada es el programa del programador: su último respaldo, `bmw_03_10_r1.zip` del 2026-10-05
  14:46 (sha256 `5449a841…`), importado byte por byte en el commit `468e29f`. La versión de oficina queda en el
  historial (commit `84442ac`) como referencia; `tools/audit_base.json` guarda los dos commits.
- Cada respaldo nuevo se audita contra el anterior. La auditoría ya no marca los módulos que borró la oficina ni
  las reglas de la depuración. Los 12 módulos sobrantes (22 archivos) se siguen solo en G05 y no se evalúan hasta
  que la celda esté probada al 100 %.
- Criterio: no se le exige al programador más de lo que hace el respaldo de Gestamp `nut07_10r1.zip` (robot
  NUT07_10R1, serie 658415, KSS 8.3.29, 2026-08-18; paquete NutWeld con spear, 3 tuercas, cambiador de
  herramienta, sin CenterLine ni PRELOAD: los puntos del pedestal se comparan por analogía). El respaldo se revisó
  en la conversación de R20; aquí se aplican sus conclusiones. En los puntos G el argumento es "igual que su propio
  respaldo", pero el cierre final lo acepta Gestamp.
- No llegó respaldo nuevo del robot: todo se revisó sobre el del 05/10 14:46.

## Los 16 puntos "Corregido en oficina", contra su programa

| Punto | Su programa | Resultado |
|---|---|---|
| G11 Sin GOTO | Sin GOTO ni etiquetas en módulos activos (solo en trigger1-3, sobrantes) | Cerrado |
| F30 Style1Opt1 | Sin GOTO; cumple en código las tres propiedades | En proceso: falta la prueba en celda |
| G04 RedRabbit | redrabbit.src sigue (sobrante) | Se cierra con G05 |
| G12 Nombres de señal | 91 líneas con $IN/$OUT numérico en PRELOAD, CENTERLINE_WELD, CENTERLINE_HOME y sps.sub; direcciones del pedestal declaradas Reserved/Spare | Abierto |
| G13 / F28 Nut check | `IF $IN[227] THEN PARTPRESENTn=TRUE` y el WAIT 0.2 después de leer | Abierto (F28 se cierra con G13) |
| G14 Gripper vacío | El comando del gripper (línea 40) va antes de la espera (49-50) en los 3 picks | Abierto |
| G15 Inglés | Comentarios en inglés; quedan CameraJudment, PartRejeted, carpeta optiones | Abierto (NUT_STAR no impide el cierre) |
| G16 Constantes | Números escritos en CENTERLINE_WELD y CENTERLINE_HOME | Abierto |
| G17 / F24 Retry | LOOP con NUT_WELD_RETRY que nunca se pone en TRUE | Abierto (F24 se cierra con G17) |
| G20 / F32 Código en folds | TRIGGER de NUT_STAR y Request_next_nut dentro de los folds; borrados del red rabbit dentro de DropOff[2] Reset | Abierto (F32 se cierra con G20) |
| F36 $IN[227] | Sigue declarado dos veces | Abierto |
| F48 Drop | AC_DropOffCheck(1) después de PTP P5 | Abierto (AtDrop3 se conserva) |
| F52 Tiempo ciclo etapa 1 | No está en su programa | Abierto: palanca d) del plan de tiempo ciclo |

## Estándar de Gestamp aplicado

| Punto | Respaldo de Gestamp / R20 | Resultado en R10 |
|---|---|---|
| G01 Nombre | NUT07_10R1; Bosch de R20 G65-03-20-R1-PNW1-WC | Abierto: por analogía NUT03_10R1, confirmar con Gestamp |
| G03 / C08 Carga | Una carga determinada por herramienta, sin carga con pieza | Abierto con el criterio reducido; LOAD_DATA[1] sigue tecleado |
| G06 / F43 Electrodo | cell.src llama GunElectrodeChange con do111 | Su cell.src ya lo hace igual; depende del reset del stepper (Gestamp) |
| G07 / F02 Options | Un option por estación, cada uno con su programa | Requiere decisión (cambio o aceptación de Gestamp); F02 se cierra con G07: el nut check ya evalúa 1, 2, 7 y 8 |
| G08 Red rabbit | Pick y drop propios, nut check de producción | Aceptado sin cambio (el nuestro además corre la cámara) |
| G09 Pieza en gripper | $OUT[18] con inline forms OUT en pick, drop y reject | Aceptado sin cambio |
| G10 GripperTech | GRPg_SetStateAndCheck / GRPg_Check en pick, drop y reject | Se cierra con F31/F33: ya los usa en todos; el drop red rabbit suelta con el gripper 3 (F31) |
| G18 / F08 Weld OK | WeldInitiate solo espera WeldComplete | Aceptado sin cambio; timeout y mensaje siguen en F15/C21 |
| G21 / F19 Resultado red rabbit | FAILED con cualquier tuerca (OR); borrado solo en MaintainSystem | Abierto: el nuestro usa AND y el drop borra do141/do142 |
| C01, C19 | AutomationCore_BKG activo, mismo código | Cerrados |
| C14 Brake test | do021 lo escribe el BKG; braketestback apaga do931 | Se cierra con F47 (camino con tool/base de otro robot) |
| C12 Pounce | No lo usa en el ciclo | Aceptado sin cambio |
| F49 BKG activado | Activo en el sps.sub de Gestamp | Aceptado sin cambio |
| F46 Work Complete | EndOfCycle estándar con Work Complete (R20 ya lo tiene) | Abierto |
| F12 NutWeld_BKG | Activo en Gestamp | Abierto: faltan las señales del soldador que usa el PLC |
| F20 Reject | RejectGE4 no pide permiso de drop-off | Requisito quitado; queda liberar Application 1 en el rechazo por nut check |
| F21 Forms AutomationCore | AC_CmdParam oculto = número de la llamada | Abierto: 5 forms no coinciden |
| F50 Permiso de aplicación | Cada programa de revisión hace su propio check / release | Abierto |
