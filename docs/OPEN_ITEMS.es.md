# Puntos abiertos — robot R10 (BMW-03-10-R1)

*Archivo generado por `tools/make_items_md.py` a partir de `docs/open_items.json` — no se edita a mano.*

Actualizado: 2026-10-07. Pendientes: **87** de 102. El detalle técnico de cada punto (en inglés, para Gestamp) está en [FINDINGS.md](FINDINGS.md); el proceso en [PROCESO.es.md](PROCESO.es.md).

**Puntos de Gestamp (G01–G22)**: revisión de Gestamp del 2026-10-02 (BMW-03-10R1), con su texto original. 9 están corregidos en la versión de oficina y falta probarlos en celda (estado *Corregido en oficina - probar en celda*). Los Fnn/Cnn son de la revisión de Ethos (numeración del R20); los marcados "Calvin #n" también están en la lista de Calvin (2026-10-03), verificada punto por punto. Esta lista es la única que se usa.

## Resumen — puntos de Gestamp

| ID | Gestamp | Punto | Sev. | Responsable | Estado | Ver |
|---|---|---|---|---|---|---|
| G01 | Robot name needs to change | Cambiar el nombre del robot | Medio | Programador robot (en celda) / Gestamp confirma el formato | **Abierto** | C02 |
| G02 | Safety Tool is not equal to Default TCP | Herramienta de seguridad igual al TCP de la herramienta 1 | Alto | Programador robot / Seguridad | **Abierto** | F42 |
| G03 | Tool 1 is used without Load data determination | Determinar los datos de carga (herramienta 1 con y sin pieza) | Alto | Programador robot / Puesta en marcha | **Abierto** | C08, F39, C09 |
| G04 | Program Red Rabbit() is blocked, might be an unnecessary copy | Programa RedRabbit bloqueado: borrado | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F19 |
| G05 | Unused programs | Programas sin uso | Bajo | Programador robot / Gestamp controles | **Requiere decisión** | G04, C28 |
| G06 | Electrode change confirmation only 0.1 s, no handshake | Cambio de electrodo: confirmación de 0.1 s y sin handshake | Medio | Programador robot / Gestamp controles | **Requiere decisión** | F43, F12 |
| G07 | Multiple options in Style_1 call the same sub-program | Options 1, 2, 7 y 8 de Style_1 llaman el mismo programa | Alto | Gestamp controles / Programador robot | **Requiere decisión** | F02 |
| G08 | Separate Auto-Red Rabbit program that doesn't match production | El ciclo red rabbit no sigue el camino de producción | Alto | Gestamp controles / Programador robot | **Requiere decisión** | F19, G21 |
| G09 | Part control to PLC is set/reset instead of reflecting the real part controls | Pieza en gripper al PLC fijada por programa, no por los sensores | Medio | Programador robot / Gestamp controles | **Requiere decisión** | F12, C01, C16 |
| G10 | Gripper commands not used at all times | Comandos de gripper GripperTech en todos los movimientos de gripper | Medio | Programador robot / Puesta en marcha | **Abierto** | F31, F33, C22, F40 |
| G11 | Use of Goto labels | Sin GOTO ni etiquetas | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F30, F07 |
| G12 | Use of I/O numbers instead of signal names | Nombres de señal en lugar de números de E/S | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F17, C23, F29 |
| G13 | Poor programming (10 lines for nut present) | Código simplificado (nut present en una línea, duplicados fuera) | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F28, F03, F31 |
| G14 | Gripper opened before the part control check | Revisar gripper vacío antes del comando de gripper | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |  |
| G15 | Names, variables and comments not in English | Nombres, variables y comentarios en inglés | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | C26, F36 |
| G16 | NO variables for e.g. stroke limits | Constantes para límites de carrera, presiones y tiempos | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F16, F44, F41 |
| G17 | Nut_weld_Retry logic useless | Lógica Nut_weld_Retry inútil | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F24 |
| G18 | NO check for Weld OK, just weld finished | Sin chequeo de soldadura buena | Alto | Programador robot / Puesta en marcha | **Requiere decisión** | F08 |
| G19 | Next_Nut_Ready logic can fail at block selection, reset, reboot | Handshake de la tuerca frágil ante selección de bloque, reset y reinicio | Alto | Programador robot | **Abierto** | F38, F14 |
| G20 | Change of xP0 deletes Request_next_nut inside inline forms | Request_next_nut y NUT_START fuera de los inline forms | Alto | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** | F32, F14 |
| G21 | Style1app2Opt1 will not work for RedRabbit | El nut check no funciona para red rabbit | Alto | Gestamp controles / Programador robot | **Requiere decisión** | F19, G08 |
| G22 | Use of AutomationCore is wrong in multiple places | Uso incorrecto de AutomationCore | Alto | Gestamp controles / Programador robot | **Requiere decisión** | F12, C01, F46, F21, F20, C11, C12, C18, C19, C14, F35 |

## Resumen — puntos de Ethos

| ID | Punto | Sev. | Responsable | Estado |
|---|---|---|---|---|
| F01 | Entrada al pedestal sin confirmar gun abierto, clamp abierto y QFP regresado | Crítico | Programador robot | **Abierto** |
| F02 | Options 2, 7 y 8 no evalúan el sensor de tuercas: solo decide la cámara | Alto | Programador robot + Gestamp controles | **Requiere decisión** |
| F03 | PARTPRESENT1..3 y bscrapGE4 no se resetean al inicio del ciclo (Calvin #8) | Alto | Programador robot | **Abierto** |
| F04 | Dry cycle se cuelga en la primera weld app: PRELOAD borra NUT_READY y nunca lo pone | Alto | Programador robot | **Abierto** |
| F05 | Dry cycle releído en cada paso: un cambio a mitad de ciclo deja pasar pieza incompleta | Alto | Programador robot | **Abierto** |
| F06 | Ciclos vacíos o silenciosos: pick ambiguo, style u option desconocidos | Alto | Programador robot | **Abierto** |
| F07 | Chequeo de gun cerrado: HALT sin mensaje como manejo de falla | Alto | Programador robot | **Abierto** |
| F08 | Resultado de soldadura Bosch no evaluado: weld complete se toma como soldadura buena (Calvin #2) | Alto | Programador robot + Gestamp controles | **Requiere decisión** |
| F09 | Resultado del flujo de agua descartado; $OUT[475] forzado en ON | Alto | Programador robot + Puesta en marcha | **Abierto** |
| F10 | Sin estado seguro del pedestal al cancelar o resetear el programa | Alto | Programador robot | **Abierto** |
| F11 | PRELOAD en el submit mueve el pedestal en cualquier modo, sin dueño de las salidas | Crítico | Seguridad + Programador robot | **Requiere decisión** |
| F12 | Background de AutomationCore y NutWeld deshabilitado: los bits de estado al PLC no cambian | Alto | Gestamp controles + Programador robot | **Requiere decisión** |
| F13 | PRELOAD sin timeouts por paso, sin falla y banderas de tuerca lista sin confirmar alimentación (Calvin #6) | Medio | Programador robot | **Abierto** |
| F14 | NUT_READY no se consume al soldar; la siguiente tuerca depende solo de TRIGGERs (Calvin #11) | Medio | Programador robot | **Abierto** |
| F15 | Unos 35 WAIT FOR sobre entradas de proceso sin timeout ni mensaje (Calvin #1) | Medio | Programador robot | **Abierto** |
| F16 | Posición del pin superior nunca verificada | Medio | Programador robot / Puesta en marcha | **Abierto** |
| F17 | Declaraciones traslapadas; nombres dobles en los bits del pedestal | Medio | Programador robot | **Abierto** |
| F18 | KRC_IO.xml mapea $OUT[820..979] y $IN[820..930] sobre los mismos bytes del adapter PLC | Medio | Gestamp controles / Programador robot | **Requiere decisión** |
| F19 | Red rabbit: el ciclo no puede dar resultado y suelta la pieza por un mapeo duplicado (Calvin #26) | Alto | Programador robot / Gestamp controles | **Requiere decisión** |
| F20 | Reject sin permiso del PLC para la posición de rechazo; Application 1 sin liberar | Medio | Programador robot / Gestamp controles | **Requiere decisión** |
| F21 | Parámetros ocultos de inline forms AutomationCore no coinciden con la llamada | Medio | Programador robot | **Abierto** |
| F22 | Movimientos del pedestal mezclan modo base y external TCP | Medio | Ethos (Edgar) / Programador robot | **Requiere decisión** |
| F23 | Posición del LPT armada con 3 bytes en otro orden que en R20 | Bajo | Puesta en marcha / Programador robot | **Abierto** |
| F24 | Camino de retry de soldadura muerto: NUT_WELD_RETRY nunca es TRUE (Calvin #27) | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |
| F25 | Feed de respaldo en CENTERLINE_WELD: pulso de feed de duración cero (Calvin #19) | Bajo | Programador robot | **Abierto** |
| F26 | Timers $TIMER[10..15] de PRELOAD y CENTERLINE_WELD sin constantes con nombre | Bajo | Programador robot | **Abierto** |
| F27 | Confirmar en celda funciones de comentarios corregidos: blow-off, pines, programa Bosch | Bajo | Puesta en marcha / Gestamp controles | **Abierto** |
| F28 | Sensor de tuerca leído al llegar al punto; el dwell iba después de la lectura | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |
| F29 | Faro KL50L2: lógica muerta y un bit sin mapear | Bajo | Programador robot / Puesta en marcha | **Abierto** |
| F30 | Style1Opt1 sin GOTO: un camino IF/ELSE por ciclo | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |
| F31 | Forms GripperTech: parámetros ocultos de otro gripper; drop red rabbit con el gripper 3 (Calvin #25) | Medio | Programador robot / Puesta en marcha | **Abierto** |
| F32 | TRIGGERs y resets escritos a mano dentro de folds de inline form (Calvin #28) | Medio | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |
| F33 | GripperConfig.xml del HMI desincronizado con grp_data.dat | Medio | Programador robot | **Abierto** |
| F34 | CENTERLINE_HOME: polaridad de $OUT[473] y falta el reset del Bosch | Bajo | Programador robot / Puesta en marcha | **Requiere decisión** |
| F35 | El mastering reference deja $OUT[930] en ON para siempre | Medio | Programador robot | **Abierto** |
| F36 | $IN[227] declarado con dos nombres (NUT_PRESENT1, di227SensorCamera) | Bajo | Programador robot (prueba en celda) | **Corregido en oficina - probar en celda** |
| F37 | ~~Presión de intensificado no confirmada antes de weld start: no aplica en R10~~ (Calvin #1) | - | Programador robot | No aplica |
| F38 | Estado de la tuerca no se reinicializa al arrancar, en reset ni después de un reinicio (Calvin #11) | Alto | Programador robot | **Abierto** |
| F39 | Supervisión de par en cero; chequeo de datos de carga solo avisa; carga tecleada (Calvin #16) | Medio | Programador robot / Puesta en marcha | **Abierto** |
| F40 | Drops y reject abren el gripper sin confirmar pieza; el drop red rabbit se mueve antes de gripper vacío (Calvin #25) | Medio | Programador robot | **Abierto** |
| F41 | Tiempos de PRELOAD, límite de flujo de agua y esperas fijas sin constantes (Calvin Std 5) | Bajo | Programador robot | **Abierto** |
| F42 | Envolventes de trabajo por software apagadas (Calvin #30) | Bajo | Programador robot / Seguridad / Gestamp | **Requiere decisión** |
| F43 | Cambio de electrodo: reset de stepper por pulso de 0.1 s y handshake que no cierra (Calvin #29) | Medio | Programador robot / Gestamp controles | **Requiere decisión** |
| F44 | Palabra de presión del gun escrita en dos órdenes de bytes (405/1820 contra 39425) | Alto | Puesta en marcha / Programador robot | **Abierto** |
| F45 | ~~Rutinas de clamps: grippers 2-4 deshabilitados, solo existe el gripper 1~~ (Calvin #23) | Bajo | Programador robot | Cerrado - depuración |
| F46 | EndOfCycle del proveedor editado: Work Complete nunca se manda al PLC | Medio | Gestamp controles / Ethos (Edgar) | **Requiere decisión** |
| F47 | Camino del brake test enseñado con tool 3 / base 1 de otro robot | Medio | Programador robot / Puesta en marcha | **Abierto** |
| F48 | Drop al conveyor: interlock de drop-off movido después de la aproximación (corregido); AtDrop3 re-enseñado (se conserva) | Alto | Programador robot / Gestamp controles | **Corregido en oficina - probar en celda** |
| F49 | AutomationCore_BKG activado y editado sin decisión registrada | Alto | Gestamp controles + Programador robot | **Requiere decisión** |
| F50 | Permiso de aplicación 1 (nut check / cámara) revisado después de llegar a P22 | Alto | Programador robot | **Abierto** |
| F51 | ~~Apps de soldadura duplicadas por estación de pick (A/B): cada cambio va en las dos~~ | Bajo | Programador robot | Sin acción - documentado |
| F52 | Tiempo ciclo: el robot espera ~4 s la tuerca antes de las tuercas 2 y 3 (la precarga arrancaba hasta después de soldar) | Alto | Programador robot | **Corregido en oficina - probar en celda** |
| C01 | ~~AutomationCore_Bkg deshabilitado: el estatus al PLC no se actualiza~~ | - | Gestamp controles / Ethos (Edgar) | Se cierra con otro punto |
| C02 | Designación BMW-03-10-R1 en los encabezados; confirmar formato con Gestamp | - | Ethos (Edgar) / Gestamp controles | **Requiere decisión** |
| C03 | ~~Encabezado estándar Gestamp en cada módulo del integrador~~ | - | Programador robot | Cerrado - depuración |
| C04 | Movimientos de pedestal interpolados sobre el dado fijo (external TCP) | - | Ethos (Edgar) / Programador robot | **Requiere decisión** |
| C05 | TCP remoto del pedestal (BASE_DATA[3]) sin medir | - | Puesta en marcha / Programador robot | **Abierto** |
| C06 | Herramientas y bases con nombre: nombres de otro proyecto | - | Programador robot | **Abierto** |
| C07 | Un user frame por utillaje: picks, nut check, reject y drops en WORLD | - | Gestamp controles / Ethos (Edgar) | **Requiere decisión** |
| C08 | Datos de carga: LOAD_DATA[1] tecleado; sin carga con/sin pieza | - | Programador robot / Puesta en marcha | **Abierto** |
| C09 | Detección de colisión apagada en todo el programa; la reacción es un HALT | - | Programador robot / Puesta en marcha | **Abierto** |
| C10 | Falta el programa de mastering ZERO_G1 | - | Programador robot | **Abierto** |
| C11 | Zonas sin documentar: ninguna zona pedida, falta la forma NA-FM-71-138.1 | - | Ethos (Edgar) / Gestamp controles | **Requiere decisión** |
| C12 | Pounce común: el ciclo no pasa por pounce y do007RobotAtPounce no se calcula | - | Gestamp controles / Ethos (Edgar) | **Requiere decisión** |
| C13 | ~~Manejo de zonas coherente~~ | - | Programador robot | No aplica |
| C14 | Brake test: el 'due' no se reporta y el camino usa tool/base de otro robot | - | Programador robot | **Abierto** |
| C15 | ~~Dry cycle seleccionable y sin colgar el robot~~ | - | Programador robot | Se cierra con otro punto |
| C16 | ~~Pieza presente / pieza en gripper~~ | - | Programador robot | Se cierra con otro punto |
| C17 | ~~Verificación de tuercas y red rabbit~~ | - | Programador robot | Se cierra con otro punto |
| C18 | ~~Handshakes AutomationCore de pick, application y drop~~ | - | Programador robot | Se cierra con otro punto |
| C19 | Request to enter: doCriticalWZ nunca se escribe; el PLC ve entrada permitida | - | Programador robot / Seguridad | **Requiere decisión** |
| C20 | Conteo de soldaduras al final del ciclo: #CHECK apagado y WeldNoRequired distinto de 3 | - | Programador robot | **Abierto** |
| C21 | Fallas por mensajes AutomationCore: ningún HALT sin mensaje ni WAIT FOR FALSE | - | Programador robot | **Abierto** |
| C22 | Grippers por inline forms GripperTech | - | Programador robot / Puesta en marcha | **Abierto** |
| C23 | ~~Nombres AutomationCore para la E/S, sin direcciones literales~~ | - | Programador robot | Se cierra con otro punto |
| C24 | ~~Los comentarios nombran la señal con su dirección~~ | - | Programador robot | Cerrado - depuración |
| C25 | ~~Inline forms consistentes con el código~~ | - | Programador robot | Se cierra con otro punto |
| C26 | ~~Solo inglés en comentarios, títulos de fold y &COMMENT~~ | - | Programador robot | Cerrado - depuración |
| C27 | ~~Proceso controlado por robot no compartido; regla de dos procesos~~ | - | Ethos (Edgar) | No aplica |
| C28 | Ediciones del integrador en archivos del proveedor: listarlas en la entrega | - | Ethos (Edgar) / Programador robot | **Abierto** |

---

## G01 — Cambiar el nombre del robot

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 1. Texto de Gestamp: *"Robot name needs to change"*

**Severidad:** Medio · **Tipo:** Configuración en celda · **Responsable:** Programador robot (en celda) / Gestamp confirma el formato · **Estado:** Abierto

**Módulos:** `am.ini`, `C/KRC/Roboter/Rdc/RobotData.xml`, `$ROBNAME (smartHMI)`

**Qué está mal.** El nombre del robot en el controlador sigue siendo V431_03_10_R1 (am.ini: RobName; RobotData.xml: RobotName); también da nombre a los respaldos (v431_03_10_r1.zip). Gestamp identifica esta estación como BMW-03-10R1.

**Qué hacer.** Pedir a Gestamp el texto exacto del nombre (p. ej. BMW_03_10_R1; el guion puede no ser aceptado). Cambiarlo en el smartHMI (Puesta en servicio → Datos del robot → Nombre del robot) en modo experto. El encabezado de los programas ya dice BMW-03-10-R1 (depuración, C02).

**Criterio de cierre** (se verifica en el respaldo):

* Formato confirmado por Gestamp por escrito (correo adjunto a la lista).
* En el respaldo, am.ini (RobName) y C/KRC/Roboter/Rdc/RobotData.xml (RobotName) traen el nombre nuevo; el nombre del archivo de respaldo también.
* Si el formato confirmado difiere de BMW-03-10-R1, la línea "; Robot 03-10-R1 (...)" de los encabezados se ajusta igual (C02).

**Evidencia del programador.** Correo de Gestamp con el formato; captura de la pantalla Datos del robot con el nombre nuevo.

**Depende de / se cierra con:** C02

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 1 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - avance parcial: El nombre del robot ya es BMW_03_10_R1 (am.ini y RobotData.xml). Falta el formato confirmado por Gestamp por escrito (criterio 1); si difiere, se cambia otra vez.
* 2026-10-05 — Integrado: El nombre BMW_03_10_R1 se conserva en la versión integrada. Falta el formato confirmado por Gestamp.

---

## G02 — Herramienta de seguridad igual al TCP de la herramienta 1

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 2. Texto de Gestamp: *"Safety Tool is not equal to Default TCP"*

**Severidad:** Alto · **Tipo:** Configuración de seguridad · **Responsable:** Programador robot / Seguridad · **Estado:** Abierto

**Módulos:** `C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml`, `$config.dat (TOOL_DATA[1])`

**Qué está mal.** No se puede verificar desde el respaldo: la geometría de la herramienta de seguridad vive en el controlador de seguridad, no en texto. La bitácora de seguridad muestra tres cambios a la herramienta 1 el 2026-08-30. TOOL_DATA[1] (TOOL 1, EOAT 1) = {X 0, Y 0, Z 380.79, A -90, B -90, C -90}.

**Qué hacer.** En el smartHMI comparar el TCP de la herramienta de seguridad 1 con TOOL_DATA[1] y corregirlo (y las esferas de la herramienta si aplica). Es un cambio de configuración de seguridad: nueva suma de verificación y prueba de aceptación (checklist de SafeOperation).

**Criterio de cierre** (se verifica en el respaldo):

* Captura de la herramienta de seguridad 1 con el TCP igual a TOOL_DATA[1] del respaldo.
* Checksum nuevo anotado y checklist de aceptación firmado por quien tenga la autorización.

**Evidencia del programador.** Capturas antes/después, checksum y checklist.

**Depende de / se cierra con:** F42

**Nota.** Conviene hacerlo en la misma sesión de seguridad que F42 (espacios de SafeOperation). Si G03 o C06 cambian TOOL_DATA[1], repetir la comparación.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 2 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G03 — Determinar los datos de carga (herramienta 1 con y sin pieza)

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 3. Texto de Gestamp: *"Tool 1 is used without Load data determination"*

**Severidad:** Alto · **Tipo:** Prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `$config.dat (LOAD_DATA[1])`, `KRC/STEU/Mada/$custom.dat ($LDC_CONFIG[1])`

**Qué está mal.** LOAD_DATA[1] = {M 210, CM X 270 Y 0 Z 240, J 105/105/105}: valores redondos tecleados, no determinados. El chequeo de datos de carga de la herramienta 1 solo avisa ($LDC_CONFIG[1] = #WARNONLY). Con datos de carga falsos la detección de colisión y la dinámica no son confiables (C08, C09, F39).

**Qué hacer.** Correr KUKA Load Data Determination para la herramienta 1 (EOAT 1) sin pieza y con la pieza GE4; declarar la carga con pieza (segunda herramienta o carga adicional, según el estándar Gestamp) y usarla en los movimientos con pieza.

**Criterio de cierre** (se verifica en el respaldo):

* LOAD_DATA[1] en $config.dat ya no es {M 210, CM {X 270, Y 0, Z 240}, J {105, 105, 105}}: trae masa, centro de masa e inercias determinados.
* Existe la carga con pieza (si difiere 5 % o más) y los movimientos entre el cierre del gripper en el pick y su apertura en drop, drop red rabbit o reject la usan (C08).
* Protocolo de Load Data Determination (captura o archivo) con fecha.

**Evidencia del programador.** Captura del resultado de Load Data Determination sin y con pieza, con fecha.

**Depende de / se cierra con:** C08, F39, C09

**Nota.** Calvin describe el R10 como robot de pistola; es un robot de manejo (EOAT 1 + pieza). Los hechos se sostienen.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 3 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G04 — Programa RedRabbit bloqueado: borrado

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 4. Texto de Gestamp: *"Program Red Rabbit() is blocked, might be an unnecessary copy"*

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/Utilities/redrabbit.src`, `KRC/R1/Program/Utilities/RedRabbit.dat`

**Qué está mal.** redrabbit.src (copia de una celda de birlos) se bloqueaba con WAIT FOR FALSE justo después del INI, nadie lo llamaba y no podía enlazar. El ciclo red rabbit real es Style1Opt10AutoRR (option 12), que tiene sus propios problemas (F19).

**Qué hacer.** Hecho en la depuración (commit 0e1ea54): redrabbit.src y RedRabbit.dat borrados, con la razón en tools/cleanup_allowlist; tools/check_cleanup.py prueba que nada los referencía. Falta que desaparezcan del controlador al cargar la versión de oficina: un restore no borra archivos, hay que borrarlos a mano.

**Criterio de cierre** (se verifica en el respaldo):

* En el respaldo no están KRC/R1/Program/Utilities/redrabbit.src ni RedRabbit.dat (borrados también en el controlador).
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* El programa carga sin errores de compilación (captura del navegador del smartPAD sin módulos en rojo). Un ciclo red rabbit (option 12) corre igual que antes de la carga (sus defectos siguen en F19). Anotar fecha.

**Evidencia del programador.** Captura del navegador sin redrabbit y fecha del ciclo red rabbit.

**Depende de / se cierra con:** F19

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 4 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G05 — Programas sin uso

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 5. Texto de Gestamp: *"Unused programs"*

**Severidad:** Bajo · **Tipo:** Código + configuración · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Centerline/centerline_loop.src`, `KRC/R1/safetest.src`, `KRC/R1/Program/MoveToPurge.src`, `KRC/R1/TP/GLUETECH`, `11 módulos borrados por la depuración (tools/cleanup_allowlist)`

**Qué está mal.** Había 11 módulos que nada llamaba: CENTERLINE_WELD1, trigger1-3, CK1STXXX, POUNCE, capchange, electrodechange, redrabbit y las dos copias AutoRR del nut check y de la cámara; además CENTERLINE_LOOP (lazo manual de válvulas del pedestal sin salida ni interlocks). Quedan safetest.src (lazo PTP sin fin a un punto, prueba manual que nada llama) y el paquete GlueTech (TP/GLUETECH y Program/MoveToPurge.src), instalado en un robot de soldadura de tuercas y sin uso.

**Qué hacer.** Hecho: la depuración borró los 11 módulos (razón y prueba en tools/cleanup_allowlist) y la oficina borró CENTERLINE_LOOP.src (tools/code_changes.json). Falta: (1) decidir con Gestamp si safetest se queda como prueba manual documentada o se borra; (2) desinstalar GlueTech desde el smartHMI (es un paquete instalado: no se borra a mano); (3) borrar en el controlador los módulos borrados al cargar la versión de oficina.

**Criterio de cierre** (se verifica en el respaldo):

* En el respaldo no están los 11 módulos borrados por la depuración ni KRC/R1/Program/Centerline/centerline_loop.src (borrados también en el controlador: un restore no borra archivos).
* safetest: decisión de Gestamp anotada en la lista; si se borra, no está en el respaldo; si se queda, su encabezado dice para qué prueba es y quién la usa.
* GlueTech desinstalado: no aparece en la lista de paquetes del smartHMI, y ni KRC/R1/TP/GLUETECH ni Program/MoveToPurge.src están en el respaldo.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* El programa carga sin errores de compilación (captura del navegador del smartPAD sin módulos en rojo). Un ciclo completo en automático sale bien. Anotar fecha.

**Evidencia del programador.** Decisión sobre safetest; captura de la lista de paquetes instalados después de desinstalar GlueTech.

**Depende de / se cierra con:** G04, C28

**Nota.** Parte de oficina hecha (12 módulos borrados en el repositorio); falta la decisión de safetest, la desinstalación de GlueTech y el borrado en el controlador.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 5 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - pendiente: Los 22 archivos borrados en la depuración siguen en el controlador; dos copias AutoRR fueron editadas (sin uso).

---

## G06 — Cambio de electrodo: confirmación de 0.1 s y sin handshake

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 6. Texto de Gestamp: *"Electrode change confirmation only 0.1 s, no handshake"*

**Severidad:** Medio · **Tipo:** Decisión + código · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/cell.src`

**Qué está mal.** En gunelectrodechange.src el reset del stepper es PULSE(dopw1_StepperReset,TRUE,0.1) ($OUT[485]) sin confirmar $IN[487] dipw1_EndOfStepper, y el handshake con el PLC no cierra (F43). Además la rutina nunca corre: cell.src la llama con $OUT[111..113], que solo escribe AutomationCore_Bkg, deshabilitado (F12).

**Qué hacer.** Ver F43: definir con Gestamp cómo se pide el cambio de electrodo (bit del PLC o contador), confirmar el reset del stepper y cerrar el handshake por niveles.

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen los criterios de F43.

**Evidencia del programador.** Ver F43.

**Depende de / se cierra con:** F43, F12

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 6 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G07 — Options 1, 2, 7 y 8 de Style_1 llaman el mismo programa

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 7. Texto de Gestamp: *"Multiple options in Style_1 call the same sub-program"*

**Severidad:** Alto · **Tipo:** Decisión Gestamp + código · **Responsable:** Gestamp controles / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

**Qué está mal.** Style_1 manda las options 1, 2, 7 y 8 a Style1Opt1. El nut check (style1app2opt1) solo decide la option 1; con 2, 7 u 8 decide solo la cámara y, si no contesta ni OK ni NG, bscrapGE4 conserva su valor anterior (F02).

**Qué hacer.** Gestamp define qué es cada option. Cada option distinta tiene su propio programa o su propia evaluación; si son iguales a la 1, las evaluaciones las incluyen.

**Criterio de cierre** (se verifica en el respaldo):

* Definición de options por escrito de Gestamp.
* Se cumplen los criterios de F02.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Definición de Gestamp y prueba por option.

**Depende de / se cierra con:** F02

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 7 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G08 — El ciclo red rabbit no sigue el camino de producción

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 8. Texto de Gestamp: *"Separate Auto-Red Rabbit program that doesn't match production"*

**Severidad:** Alto · **Tipo:** Decisión + código · **Responsable:** Gestamp controles / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

**Qué está mal.** El red rabbit (option 12, Style1Opt10AutoRR) tiene su propio pick y su propio drop. El drop cierra el gripper 1 con salidas escritas a mano, suelta con el form del gripper 3 (que comparte la E/S del gripper 1), se mueve antes de confirmar gripper vacío, y el ciclo no puede dar resultado al PLC (F19).

**Qué hacer.** Definir con Gestamp el procedimiento red rabbit: número de option, qué pieza (qué tuercas faltan), qué se espera de cada chequeo y dónde termina la pieza. Reusar el pick y los chequeos de producción y cambiar solo lo necesario.

**Criterio de cierre** (se verifica en el respaldo):

* Procedimiento red rabbit de Gestamp por escrito.
* Se cumplen los criterios de F19.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Procedimiento y prueba red rabbit con resultado esperado.

**Depende de / se cierra con:** F19, G21

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 8 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G09 — Pieza en gripper al PLC fijada por programa, no por los sensores

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 9. Texto de Gestamp: *"Part control to PLC is set/reset instead of reflecting the real part controls"*

**Severidad:** Medio · **Tipo:** Decisión + código · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/System/sps.sub`

**Qué está mal.** $OUT[18] do018Part1InGripper lo pone el inline form OUT 18 de los picks (fuera de dry cycle) y lo quitan el drop al conveyor, el drop red rabbit y RejectGE4; si la pieza se cae o alguien la quita a mano, el PLC sigue viendo pieza. PARTPRESENT1..3 no son señales al PLC: son las banderas internas del nut check (su problema es F03).

**Qué hacer.** Que $OUT[18] siga a los sensores $IN[253] di253PartPresent1 y $IN[254] di254PartPresent2 en todo momento (una línea en sps.sub, o donde decida Gestamp) y quitar los OUT 18 de picks, drops y reject.

**Criterio de cierre** (se verifica en el respaldo):

* $OUT[18] se escribe en un solo lugar, a partir de di253/di254; los inline forms OUT 18 de picks, drops y RejectGE4 ya no están.
* Prueba: quitar la pieza a mano del gripper en T1 → $OUT[18] OFF de inmediato; con la pieza tomada → ON. Anotar fecha.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Dónde se escribe y prueba con fecha.

**Depende de / se cierra con:** F12, C01, C16

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 9 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G10 — Comandos de gripper GripperTech en todos los movimientos de gripper

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 10. Texto de Gestamp: *"Gripper commands not used at all times"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`, `C/KRC/User/TP/Gripper_SpotTech/GripperConfig.xml`

**Qué está mal.** El drop red rabbit cierra el gripper 1 con salidas escritas a mano ($OUT[249] OFF, $OUT[250] ON, sin check) y suelta con el form del gripper 3. Los forms SET de los tres picks y del drop al conveyor traían parámetros ocultos de otro gripper (setgripper=4;setstate=2) y cada SET con check iba seguido de un GRPg_Check redundante (F31). GripperConfig.xml está desincronizado con grp_data.dat (F33).

**Qué hacer.** Hecho en oficina: parámetros ocultos de los forms SET de los tres picks y del drop al conveyor corregidos a setgripper=1 con el estado de la llamada; GRPg_Check redundantes quitados (picks, drop al conveyor, RejectGE4). Falta: drop red rabbit con forms GripperTech del gripper 1 (F31, F19) y re-sincronizar GripperConfig.xml (F33).

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen los criterios de F31 y F33.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en el smartPAD: abrir y confirmar (Cmd OK) un form Gripper SET de un pick y el del drop al conveyor sin cambiar nada; en el respaldo siguiente la llamada sigue siendo GRPg_SetStateAndCheck(1, ...) con el mismo estado. Un ciclo completo en automático de estación 1 y de estación 2. Anotar fecha.

**Evidencia del programador.** Ver F31 y F33; fecha de la prueba Cmd OK y del ciclo.

**Depende de / se cierra con:** F31, F33, C22, F40

**Nota.** Parte de oficina hecha (parámetros ocultos y GRPg_Check redundantes, tools/code_changes.json); falta el drop red rabbit y F33.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 10 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G11 — Sin GOTO ni etiquetas

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 11. Texto de Gestamp: *"Use of Goto labels"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** Había GOTO en 9 módulos: saltos de dry cycle (picks, weld apps, nut check), retry muerto, salto de tuerca precargada y chequeo de gun cerrado en CENTERLINE_WELD, y la estructura de Style1Opt1.

**Qué hacer.** Hecho en oficina: todos los GOTO y etiquetas se quitaron. Dry cycle = IF NOT di004UseDryCycle; tuerca precargada = IF NOT NUT_READY; chequeo de gun cerrado = LOOP/EXIT (después del HALT los timers se rearrancan, F07); Style1Opt1 = un IF/ELSE por ciclo con la estación leída una vez en nPickStation (F30). tools/check_equivalence.py muestra que, fuera de esos puntos, la lógica es la misma que en la base fb8a4c8. Falta probar en celda.

**Criterio de cierre** (se verifica en el respaldo):

* En el respaldo ningún módulo del integrador (KRC/R1/Program, KRC/R1/cell.src, sps.sub) tiene GOTO ni etiquetas.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en celda: un ciclo sin dry cycle de estación 1 y uno de estación 2 (T1 y automático), un rechazo por nut check (option 1), un ciclo red rabbit (option 12), un pick en dry cycle (sin espera de pieza; el ciclo se sigue colgando en la primera weld app por F04, igual que antes) y el timeout de gun cerrado en T1 sin tuerca (HALT, START: vuelve a dar timeout si sigue sin cerrar). Anotar fecha y resultado de cada uno.

**Evidencia del programador.** Fecha y resultado de cada prueba.

**Depende de / se cierra con:** F30, F07

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 11 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Auditoría - avance en el original: El programador quitó los GOTO por su cuenta en el programa original (apps, CENTERLINE_WELD, picks, nut check, cámara, Style1Opt1). La lógica es equivalente a la versión de oficina; hay que integrarla en la versión depurada, no cargar la suya.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G12 — Nombres de señal en lugar de números de E/S

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 12. Texto de Gestamp: *"Use of I/O numbers instead of signal names"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/System/$config.dat`

**Qué está mal.** PRELOAD, CENTERLINE_WELD, CENTERLINE_HOME y sps.sub usaban $IN[n]/$OUT[n] literales para el pedestal, el agua y el faro KL50L2.

**Qué hacer.** Hecho en oficina: los bits del pedestal recibieron nombre AutomationCore en automationcoreroutines.dat (do498UpperPinExtend, do499UpperPinRetract, do501PartClampClose, do502PartClampOpen, do503QFPAdvance, do504QFPReturn, do505QFPNutBlowOff, di466PartClampOpen, di467PartClampClosed, di470QFPAdvanced), los tres bits del faro en $config.dat (CL_BeaconBit3001/3008/3024) y el código usa nombres (también los NutWeld dopw1_/dipw1_). Las direcciones no cambiaron. Los inline forms estándar de KUKA (WAIT FOR, OUT) siguen generando $IN[n]/$OUT[n] con el nombre en el form: así es el estándar y no se reescriben a mano.

**Criterio de cierre** (se verifica en el respaldo):

* En el respaldo ninguna línea ejecutable del integrador fuera de un inline form KUKA usa $IN[n]/$OUT[n] literal (la auditoría lo revisa).
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* El programa carga sin errores de compilación (captura del navegador del smartPAD sin módulos en rojo). Un ciclo completo en automático sale bien. Anotar fecha.

**Evidencia del programador.** Captura del navegador y fecha del ciclo de prueba.

**Depende de / se cierra con:** F17, C23, F29

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 12 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G13 — Código simplificado (nut present en una línea, duplicados fuera)

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 13. Texto de Gestamp: *"Poor programming (10 lines for nut present)"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** Cada revisión de tuerca de style1app2opt1 eran unas 10 líneas (GOTO de dry cycle, IF que solo ponía TRUE, dwell después de leer). Había código repetido: un GRPg_Check del mismo estado después de cada GRPg_SetStateAndCheck y las líneas de upper pin extend dobles en la alimentación local de CENTERLINE_WELD.

**Qué hacer.** Hecho en oficina: cada revisión de tuerca es "WAIT SEC 0.2 / PARTPRESENTn = di227NutPresent1" dentro de IF NOT di004UseDryCycle (lee con el robot parado y escribe TRUE o FALSE; F28, F03); se quitaron los GRPg_Check redundantes (picks, drop al conveyor, RejectGE4), las líneas dobles de upper pin y la etiqueta WELD_END sin uso.

**Criterio de cierre** (se verifica en el respaldo):

* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en automático con option 1: 5 ciclos con pieza buena sin rechazo por tuercas; un ciclo con una tuerca faltante (o una pieza red rabbit) termina en RejectGE4; PARTPRESENT1..3 leídos en el display de variables. En cada pick, drop y reject el gripper confirma su estado con GRPg_SetStateAndCheck, sin el GRPg_Check extra. Anotar fecha y resultado.

**Evidencia del programador.** Fecha, número de ciclos y resultado.

**Depende de / se cierra con:** F28, F03, F31

**Nota.** Con options 2, 7 y 8 el sensor sigue sin decidir (F02): la prueba de tuerca faltante se hace con option 1.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 13 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G14 — Revisar gripper vacío antes del comando de gripper

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 14. Texto de Gestamp: *"Gripper opened before the part control check"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`

**Qué está mal.** Los tres picks abrían el gripper y después revisaban que no hubiera pieza.

**Qué hacer.** Hecho en oficina: la espera de gripper vacío ($IN[253] di253PartPresent1 y $IN[254] di254PartPresent2 OFF, inline form WAIT FOR) se movió antes del primer form Gripper SET (GRPg_SetStateAndCheck(1, 1, ...)) en los tres picks.

**Criterio de cierre** (se verifica en el respaldo):

* En los tres picks la espera de gripper vacío está antes del primer comando de gripper.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en T1: con una pieza en el gripper al iniciar el pick, el robot se queda en la espera sin mover el gripper. Anotar fecha.

**Evidencia del programador.** Fecha y resultado.

**Nota.** Los drops y el reject (abrir sin confirmar pieza) son F40.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 14 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G15 — Nombres, variables y comentarios en inglés

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 15. Texto de Gestamp: *"Names, variables and comments not in English"*

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/System/$config.dat`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** Comentarios en español y nombres mal escritos: NUT_STAR, di100/di101CameraJudment, do106/di106PartRejeted, la carpeta Program/Styles/optiones; $IN[227] se llamaba di227SensorCamera aunque es el sensor de tuercas (F36).

**Qué hacer.** Hecho: comentarios, títulos de fold y &COMMENT en inglés (depuración, C26); en oficina NUT_STAR → NUT_START, CameraJudment → CameraJudgment, PartRejeted → PartRejected, di227SensorCamera → di227NutPresent1 (F36) y la carpeta Styles/optiones renombrada Styles/Options. Quedan "Hidraulyc_Valve" en las declaraciones del paquete NutWeld (archivo del proveedor, ningún programa del integrador lo usa) y el texto 'do106PartRejeted' de los inline forms OUT 106 de RejectGE4 (se corrige solo si se reabre el form).

**Criterio de cierre** (se verifica en el respaldo):

* La auditoría no encuentra comentarios en español ni los nombres viejos (NUT_STAR, Judment, Rejeted, di227SensorCamera) en código ejecutable ni en declaraciones del respaldo.
* En el controlador ya no existe la carpeta KRC/R1/Program/Styles/optiones: style1opt1 y Style1Opt10AutoRR están solo en Styles/Options (la carpeta vieja se borra a mano; si queda, hay dos módulos con el mismo nombre).
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* El programa carga sin errores de compilación (captura del navegador del smartPAD sin módulos en rojo). Un ciclo completo en automático sale bien. Anotar fecha.

**Evidencia del programador.** Captura del navegador sin errores y fecha del ciclo.

**Depende de / se cierra con:** C26, F36

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 15 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G16 — Constantes para límites de carrera, presiones y tiempos

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 16. Texto de Gestamp: *"NO variables for e.g. stroke limits"*

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`

**Qué está mal.** CENTERLINE_WELD tenía escritos la ventana del LPT con gun cerrado (69000..73000), el límite de gun abierto (120000), los tiempos del chequeo de gun cerrado (1000 y 300 ms), las palabras de presión (405, 1820, 39425) y el programa Bosch (2). CL_GUN_WELD_MIN/MAX estaban declaradas 65000..76000 y sin uso.

**Qué hacer.** Hecho en oficina: fold CENTERLINE CONTROL de $config.dat con CL_GUN_WELD_MIN/MAX = 69000/73000 (la ventana que el código siempre revisó), CL_GUN_OPEN_MIN, CL_GUN_CLOSE_TIMEOUT, CL_GUN_IN_WINDOW_TIME, CL_GUN_PRESS_BASE/WELD/REST (405/1820/39425, los valores en uso; el orden de bytes sigue por confirmar, F44) y CL_WELD_PROGRAM; CENTERLINE_WELD y CENTERLINE_HOME los usan. Mismos valores. La verificación del pin superior sigue en F16; los tiempos de PRELOAD y el límite de agua en F41.

**Criterio de cierre** (se verifica en el respaldo):

* No quedan esos números en líneas ejecutables de CENTERLINE_WELD / CENTERLINE_HOME.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Un ciclo de soldadura completo en automático; valores leídos en el display de variables iguales a los del fold CENTERLINE CONTROL. Anotar fecha.

**Evidencia del programador.** Fecha del ciclo de prueba.

**Depende de / se cierra con:** F16, F44, F41

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 16 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G17 — Lógica Nut_weld_Retry inútil

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 17. Texto de Gestamp: *"Nut_weld_Retry logic useless"*

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** NUT_WELD_RETRY nunca se ponía en TRUE: las tres ramas GOTO RETRY_NUT1 no hacían nada (F24).

**Qué hacer.** Hecho en oficina (opción A de F24, como en R20): se borraron las ramas, las etiquetas y la variable. Sin cambio de comportamiento.

**Criterio de cierre** (se verifica en el respaldo):

* NUT_WELD_RETRY y RETRY_NUT1 no aparecen en el respaldo.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Un ciclo completo en automático con las 3 tuercas, sin errores. Anotar fecha.

**Evidencia del programador.** Ciclo completo sin errores, con fecha.

**Depende de / se cierra con:** F24

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 17 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G18 — Sin chequeo de soldadura buena

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 18. Texto de Gestamp: *"NO check for Weld OK, just weld finished"*

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** CENTERLINE_WELD toma weld complete ($IN[483] dipw1_WeldComplete) como soldadura buena; la falla Bosch $IN[485] no se lee y sus dos nombres se contradicen (dipw1_Fault en NutWeld, di485NoFaults en AutomationCore) (F08).

**Qué hacer.** Confirmar en celda la señal de soldadura OK / falla del timer Bosch y su polaridad; después de weld complete revisarla y, si es NOK, mensaje y la pieza a RejectGE4. Usar la señal NutWeld del bus ($IN[485]); el patrón del CENTERLINE_WELD1 borrado usaba señales Bosch de AutomationCore que no están en el bus de este robot.

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen los criterios de F08.

**Evidencia del programador.** Ver F08.

**Depende de / se cierra con:** F08

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 18 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G19 — Handshake de la tuerca frágil ante selección de bloque, reset y reinicio

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 19. Texto de Gestamp: *"Next_Nut_Ready logic can fail at block selection, reset, reboot"*

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/System/$config.dat`, `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

**Qué está mal.** El handshake de la tuerca vive en globales persistentes de $config.dat (NUT_READY declarado TRUE, NUT_START, NEXT_NUT_READY, NUT_PRELOAD_STEP, STEP*DONE...). Nada las inicializa al arrancar el programa, en reset ni al reiniciar el controlador (F38). Una selección de bloque sobre un fold de movimiento salta el TRIGGER que pide la tuerca, y NUT_READY no se consume al soldar (F14): la tuerca 1 puede pasar con un TRUE viejo, y con la petición de la tuerca 2 o 3 saltada la app espera NEXT_NUT_READY para siempre.

**Qué hacer.** Ver F38 (inicialización del estado) y F14 (consumo de NUT_READY y petición en el flujo).

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen los criterios de F38 y F14.

**Evidencia del programador.** Ver F38 y F14.

**Depende de / se cierra con:** F38, F14

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 19 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G20 — Request_next_nut y NUT_START fuera de los inline forms

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 20. Texto de Gestamp: *"Change of xP0 deletes Request_next_nut inside inline forms"*

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

**Qué está mal.** Los TRIGGER de la siguiente tuerca (NUT_STAR en P12/P10 de los picks, Request_next_nut() en el fold P0 de las apps 1 y 2) y los resets del red rabbit estaban escritos dentro de folds de inline form: un Touch Up o reabrir el form los borraba (F32).

**Qué hacer.** Hecho en oficina: cada TRIGGER quedó justo antes de su fold de movimiento (posición del form SYN OUT de KUKA: mismo movimiento, mismo punto de disparo; se conservan DISTANCE = 0 y 1); los resets del red rabbit van después del fold DropOff[2] Reset. La robustez ante selección de bloque, reset y reinicio sigue en F14 y F38 (G19).

**Criterio de cierre** (se verifica en el respaldo):

* Ningún fold de inline form contiene líneas escritas a mano (la auditoría lo revisa).
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba: abrir el inline form PTP P12 de style1pick1opt1 y PTP P0 de style1app1opt1 y confirmarlos con Cmd OK sin cambiar nada (sin Touch Up, que reenseña el punto); el TRIGGER sigue antes de cada fold. Después, un ciclo completo en automático: NUT_READY y NEXT_NUT_READY (display de variables) pasan a FALSE y vuelven a TRUE una vez por tuerca (3 preloads por pieza). Anotar fecha.

**Evidencia del programador.** Fecha y resultado.

**Depende de / se cierra con:** F32, F14

**Nota.** Diferencia con la versión anterior: antes el TRIGGER estaba dentro del fold y una selección de bloque sobre ese movimiento lo ejecutaba; ahora está una línea arriba y hay que seleccionar la línea del TRIGGER. En operación normal, paso a paso en T1 y Touch Up no cambia nada. La solución de fondo es F14.

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 20 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## G21 — El nut check no funciona para red rabbit

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 21. Texto de Gestamp: *"Style1app2Opt1 will not work for RedRabbit"*

**Severidad:** Alto · **Tipo:** Decisión + código · **Responsable:** Gestamp controles / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`

**Qué está mal.** El ciclo red rabbit corre como option 12 y style1app2opt1 solo tiene CASE 1 y CASE 10: con option 12 no se pone ni $OUT[141] do141RedRabbitFailed ni $OUT[142] do142RedRabbitPassed; la cámara solo escribe bscrapGE4 (F19).

**Qué hacer.** Con la definición de la pieza red rabbit (G08), evaluar el resultado esperado: passed si el chequeo detecta la falta, failed si no; un solo resultado combinado de sensor y cámara para la option que use el red rabbit.

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen los criterios de F19 para el nut check y la cámara.

**Evidencia del programador.** Ver F19.

**Depende de / se cierra con:** F19, G08

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 21 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## G22 — Uso incorrecto de AutomationCore

**Origen:** Gestamp - Robot Program Review - Findings (2026-10-02), BMW-03-10R1, punto 22. Texto de Gestamp: *"Use of AutomationCore is wrong in multiple places"*

**Severidad:** Alto · **Tipo:** Decisión Gestamp + código · **Responsable:** Gestamp controles / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `inline forms AutomationCore`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/cell.src`, `KRC/R1/Program/masref_user.src`

**Qué está mal.** Gestamp no dice en qué lugares. Lo que encontramos: AutomationCore_Bkg deshabilitado (F12, C01), EndOfCycle del proveedor editado sin Work Complete (F46), parámetros ocultos de forms que no coinciden con la llamada (F21), reject sin drop-off ni liberación de application 1 (F20), ninguna zona pedida (C11), pounce no usado (C12), handshakes (C18), request to enter (C19), brake test (C14) y do930 que queda en ON (F35).

**Qué hacer.** Pedir a Gestamp la lista concreta y atenderla junto con los puntos relacionados.

**Criterio de cierre** (se verifica en el respaldo):

* Lista de Gestamp recibida y anotada aquí.
* Cada lugar de la lista corregido y auditado.

**Evidencia del programador.** Lista de Gestamp.

**Depende de / se cierra con:** F12, C01, F46, F21, F20, C11, C12, C18, C19, C14, F35

**Historial:**

* 2026-10-04 — Alta (Gestamp): Punto 22 de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1).

---

## F01 — Entrada al pedestal sin confirmar gun abierto, clamp abierto y QFP regresado

**Severidad:** Crítico · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** Antes del LIN de aproximación a la pose de soldadura (2 m/s) las weld apps solo esperan la bandera del preload: NUT_READY en style1app1opt1, NEXT_NUT_READY en style1app1opt2 y opt3. PRELOAD pone esas banderas después de mandar gun open, upper pin retract y clamp open sin leer retroalimentación, y en el paso 20 da por regresado el QFP por tiempo ($TIMER[12], 800 ms) sin leer $IN[482] dipw1_SpearHome. CENTERLINE_WELD revisa clamp abierto ($IN[466]) y QFP regresado ($IN[482]) con el robot ya en la pose, y gun abierto (CL_GunStrokePositionLPT > CL_GUN_OPEN_MIN) solo al final. Si el gun o el clamp quedaron cerrados (válvula pegada, falta de aire, una corrida cancelada de CENTERLINE_LOOP), el robot mete pieza y EOAT contra el electrodo, el clamp o el slide.

**Qué hacer.** En cada weld app, después de la espera de NUT_READY / NEXT_NUT_READY e inmediatamente antes del LIN de aproximación, una espera supervisada (timeout, mensaje que nombre la condición que falta, $OUT[4] do004ProcessFault) de gun abierto, clamp abierto y QFP regresado y no avanzado. En PRELOAD, el paso 20 no termina sin $IN[482] dipw1_SpearHome ON. Las esperas que ya existen dentro de CENTERLINE_WELD se quedan.

**Criterio de cierre** (se verifica en el respaldo):

* En style1app1opt1, opt2 y opt3, inmediatamente antes del LIN de aproximación (P20, P6 y P13 respectivamente), después de la espera de NUT_READY / NEXT_NUT_READY y fuera de cualquier fold de inline form, existe una espera supervisada (timeout + mensaje + $OUT[4] do004ProcessFault) de: CL_GunStrokePositionLPT > CL_GUN_OPEN_MIN, $IN[466] di466PartClampOpen ON, $IN[482] dipw1_SpearHome ON y $IN[470] di470QFPAdvanced OFF. Corre también en dry cycle, porque el LIN de aproximación se ejecuta en los dos casos.
* La espera detiene el advance run (WAIT FOR, o WAIT SEC 0 antes de una evaluación con IF o lazo): la condición sobre CL_GunStrokePositionLPT, que es una variable y no una entrada, no se evalúa por adelantado.
* En PRELOAD, paso 20: STEP20DONE (y por tanto NUT_READY / NEXT_NUT_READY = TRUE) exige $IN[482] dipw1_SpearHome ON además de $TIMER[12].
* Prueba en T1 con override reducido, una por condición: clamp no abierto, QFP no regresado y gun no abierto (sensor desconectado o válvula sin aire). En cada caso el robot se detiene antes del LIN de aproximación con el mensaje que nombra la condición y $OUT[4] ON, y continúa solo al corregirla. Anotar fecha, override y resultado de cada caso.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F01) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Módulos cambiados; timeout elegido (ms) y texto del mensaje; por cada condición probada: cómo se provocó, fecha, override, punto donde se detuvo el robot y mensaje mostrado.

**Nota.** No quitar las esperas de $IN[466] y $IN[482] dentro de CENTERLINE_WELD. Si F04 condiciona la espera de NUT_READY a no-dry, no la mueve después del LIN de aproximación. No protege contra un segundo preload encolado (F11). Si F23 cambia la composición del LPT, el límite de gun abierto se revisa con ella. Avance 2026-10-05: el gun abierto se confirma antes de entrar (GUN_OPEN_CHECK) y se vigila con interrupts 20-22 mientras el robot entra y sale; el aire ($IN[3132]) está desactivado hasta probar el presostato.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - avance parcial: Nuevo GUN_OPEN_CHECK antes de entrar y al terminar la soldadura (gun en 137000-142000, submit corriendo, agua; aire desactivado hasta probar $IN[3132]) e interrupts 20-22 con BRAKE F mientras el robot entra y sale. Falta: clamp abierto ($IN[466]) y QFP regresado ($IN[482]) antes de entrar, y la prueba en celda. Los límites 137000/142000 están dos veces (interrupts y GUN_OPEN_CHECK.dat): unificar con las constantes de G16.
* 2026-10-05 — Integrado - avance parcial: GUN_OPEN_CHECK e interrupts 20-22 del programador integrados en la versión depurada (rango 137000-142000 en GUN_OPEN_CHECK.dat; CL_GUN_OPEN_MIN eliminado). Falta clamp abierto $IN[466] y QFP regresado $IN[482] antes de entrar, y la prueba en celda.
* 2026-10-05 — Revisión independiente: GUN_OPEN_CHECK e interrupts 20-22: KRL válido e integración fiel. Huecos: los interrupts solo disparan en el cambio FALSE→TRUE; al salir se reactivan después de las esperas de clamp/QFP y de la presión de reposo, y al entrar el submit solo se revisa al inicio de GUN_OPEN_CHECK. Corrección: INTERRUPT ON 20-22 antes de cada GUN_OPEN_CHECK. Además: tras reconocer GUN_OPEN_LOST el robot puede quedar parado sin mensaje; la vigilancia se apaga un punto antes de salir; una selección de paso salta el interlock.
* 2026-10-05 — Integrado - correcciones de la revisión: Versión integrada sobre el respaldo de las 14:46: INTERRUPT ON 20-22 antes de cada GUN_OPEN_CHECK (entrada y después de soldar) y mensaje de estado en GUN_OPEN_LOST después del reconocimiento. Sigue pendiente clamp abierto / QFP regresado antes de entrar.

---

## F02 — Options 2, 7 y 8 no evalúan el sensor de tuercas: solo decide la cámara

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot + Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** Style_1 manda las options 1, 2, 7 y 8 a Style1Opt1. El nut check (style1app2opt1) decide solo CASE 1 (escribe bscrapGE4) y CASE 10 (salidas red rabbit), sin CASE 2/7/8 ni DEFAULT: con 2, 7 u 8 el resultado del sensor no se usa y bscrapGE4 conserva su último valor. La cámara (style1app2opt2) no tiene switch de option: pone FALSE con OK y no-NG, TRUE con no-OK y NG, y cualquier otra combinación lo deja igual. nOption es una máscara de bits (GetOptions). Si el PLC manda option 2, falta la tuerca 3, el sensor la ve y la cámara no (o no contesta ni OK ni NG), la pieza va al conveyor bueno.

**Qué hacer.** Pedir por escrito al programador del PLC qué options manda producción. Evaluar el sensor en todas las options de producción (CASE explícitos o la regla que confirme el PLC); poner bscrapGE4 = TRUE al inicio de cada inspección y FALSE solo en la rama de pase explícito; una option desconocida da falla con mensaje y $OUT[4] do004ProcessFault.

**Criterio de cierre** (se verifica en el respaldo):

* Respuesta escrita del programador PLC (Gestamp) con la lista de options que manda producción, adjunta a la lista.
* En style1app2opt1 toda option de producción que llega a Style1Opt1 (1, 2, 7, 8 o las confirmadas) entra en la evaluación del sensor; ninguna sale sin escribir bscrapGE4.
* bscrapGE4 = TRUE se asigna antes de leer $IN[227] di227NutPresent1 (nut check) y antes de pedir la cámara con $OUT[80] do080RepositionTooling1; bscrapGE4 = FALSE solo aparece en la rama de pase. En la cámara, una combinación de $IN[100]/$IN[101] distinta de OK ON y NG OFF deja la pieza en scrap.
* Ninguna option pasa en silencio: una option que no es de producción ni red rabbit da mensaje y $OUT[4] do004ProcessFault y bscrapGE4 queda en TRUE.
* Prueba en celda con option 2 (y 7/8 si producción las usa): (1) pieza con una tuerca faltante termina en RejectGE4 aunque la cámara dé OK (cámara simulada desde el PLC); (2) pieza con las 3 tuercas termina en Style1Drop1Opt1; (3) cámara NG termina en RejectGE4. Anotar fecha, option, caso y destino de la pieza.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F02) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Nombre de quien respondió por el PLC, fecha y lista de options; criterio implementado; resultado de los tres casos de prueba con option y fecha.

**Nota.** Option 12 (red rabbit) es F19. bscrapGE4 lo tocan también F03 (TRUE al inicio del ciclo), F05 (dry cycle) y F08 (falla de soldadura): revisarlos juntos. En style1app2opt2 no abrir el form Application[1] Reset: su AC_CmdParam=2 oculto no coincide con la llamada (F21). C17 depende de este punto.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - corregido sin marcar: Sensor y cámara evalúan nOption 1, 2, 7 y 8; la cámara sin resultado válido da scrap. Falta la prueba en celda (una tuerca faltante con option 2) y la confirmación del PLC de qué options manda.
* 2026-10-05 — Integrado - avance parcial: Sensor y cámara deciden para options 1, 2, 7 y 8; la cámara sin resultado válido da scrap. Faltan: respuesta escrita del PLC con las options de producción, bscrapGE4 = TRUE antes de leer, falla con mensaje para una option desconocida y la prueba en celda.

---

## F03 — PARTPRESENT1..3 y bscrapGE4 no se resetean al inicio del ciclo

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** PARTPRESENT1..3 son globales persistentes de $config.dat. Se borran al final de Style1Opt1, en RejectGE4 y en el drop red rabbit, nunca al inicio del ciclo. bscrapGE4 solo lo escriben el sensor con option 1, la cámara y RejectGE4 (FALSE). Si un ciclo pasa el nut check, se detiene en el handshake de la cámara y se cancela, el siguiente arranca con los valores viejos.

**Qué hacer.** Al inicio de cada ciclo, antes del pick, borrar PARTPRESENT1..3 y poner bscrapGE4 = TRUE. Asignar cada bandera desde el sensor en los dos sentidos (hecho en oficina, G13).

**Criterio de cierre** (se verifica en el respaldo):

* En Style1Opt1, antes de cualquier pick, PARTPRESENT1..3 = FALSE y bscrapGE4 = TRUE.
* En Style1Opt10AutoRR, antes del pick, PARTPRESENT1..3 = FALSE (el nut check es compartido con el red rabbit).
* En style1app2opt1 cada uno de los 3 checks asigna PARTPRESENTn = di227NutPresent1 (TRUE o FALSE) (hecho en oficina, G13).
* Prueba en celda: cancelar un ciclo después del nut check (p. ej. en la espera de $IN[80] di080ToolRepositioned1), reiniciar y verificar en la pantalla de variables que PARTPRESENT1..3 = FALSE y bscrapGE4 = TRUE antes de llegar al nut check. Anotar fecha y valores leídos.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F03) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Dónde se hace el reset; captura de la pantalla de variables al reiniciar, con fecha.

**Depende de / se cierra con:** F02

**Nota.** Hecho en oficina: el nut check asigna PARTPRESENTn en los dos sentidos y lee con el robot parado (G13, F28). Falta el reset al inicio del ciclo. bscrapGE4 = TRUE al inicio depende de F02: con options 2/7/8 el sensor no decide y la cámara puede dejarlo sin tocar. C17 depende de este punto. Calvin #8 llama "part present al PLC" a PARTPRESENT1..3; son banderas internas (lo del PLC es G09).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - sin cambio: PARTPRESENTn sigue poniéndose solo en TRUE y se lee antes del WAIT SEC 0.2; se limpia al final de Style1Opt1, no al inicio.

---

## F04 — Dry cycle se cuelga en la primera weld app: PRELOAD borra NUT_READY y nunca lo pone

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** Los picks ponen NUT_START por TRIGGER en P12 / P10 aunque esté activo el dry cycle. PRELOAD acepta el arranque (NUT_READY = FALSE, NUTCYCLE_ACTIVE = TRUE), pero sus pasos solo corren con $IN[4] di004UseDryCycle OFF, así que no vuelve a poner NUT_READY. La tuerca 1 espera NUT_READY antes de su rama de dry cycle; las tuercas 2 y 3 esperan NEXT_NUT_READY, que tampoco pone nadie. Con dry cycle el robot se queda esperando para siempre en la primera weld app, sin mensaje y con el robot in cycle.

**Qué hacer.** Que el dry cycle no pase por esperas que nadie va a cumplir ni deje un preload a medias: no iniciar preload en dry cycle y dejar las banderas en TRUE, o condicionar las esperas a no-dry sin cambiarlas de lugar (siguen antes del LIN de aproximación, F01) y evitar que PRELOAD quede con NUTCYCLE_ACTIVE en TRUE. Verificar el cuelgue en el robot antes del cambio.

**Criterio de cierre** (se verifica en el respaldo):

* En style1app1opt1..3, en producción la espera de NUT_READY / NEXT_NUT_READY sigue antes del LIN de aproximación (P20, P6, P13), junto con la espera de F01. Con dry cycle no se ejecuta ninguna espera que dependa de PRELOAD.
* En PRELOAD, con dry cycle activo un NUT_START no deja NUTCYCLE_ACTIVE = TRUE con NUT_READY = FALSE; al terminar un dry cycle no queda un preload iniciado ni un NUT_START pendiente que alimente una tuerca al quitar el dry cycle.
* Prueba en celda: con dry cycle desde el inicio, ciclo completo desde la estación 1 y desde la estación 2 hasta el final del ciclo; después, sin dry cycle, un ciclo productivo con una sola tuerca alimentada para cada soldadura (sin doble tuerca ni espera infinita). Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F04) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Resultado antes del cambio (¿se colgó en la primera weld app?: sí/no); opción implementada; resultado de los dos dry cycles y del ciclo productivo posterior, con fecha.

**Nota.** Si ya existe la bandera de dry cycle latcheada de F05, usarla aquí. El arranque de PRELOAD es el mismo código que el gate de F11: coordinar. Al cerrarse este punto y F05 se cierra C15.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F05 — Dry cycle releído en cada paso: un cambio a mitad de ciclo deja pasar pieza incompleta

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** $IN[4] di004UseDryCycle se lee por separado en los picks, en cada weld app, en los tres bloques del nut check y en su decisión, en PRELOAD y en sps.sub; nunca se latchea. La cámara no tiene prueba de dry cycle. En dry cycle el sensor no toca bscrapGE4. Si se sueldan las tuercas 1 y 2 y el dry cycle se activa antes de la pose de la tuerca 3 (con su preload terminado), la tuerca 3 se salta y, si la cámara dice OK, una pieza con 2 tuercas va al drop bueno.

**Qué hacer.** Leer $IN[4] una sola vez al inicio del ciclo en una bandera declarada y usar solo esa bandera en todo el ciclo (picks, weld apps, nut check, cámara y PRELOAD). En dry cycle exigir gripper vacío o mandar la pieza a rechazo.

**Criterio de cierre** (se verifica en el respaldo):

* Existe una sola bandera de dry cycle declarada con comentario (p. ej. en $config.dat), asignada desde $IN[4] di004UseDryCycle una sola vez al inicio del ciclo, antes del pick, y nada la cambia hasta el final del ciclo.
* En los picks, style1app1opt1..3, style1app2opt1, style1app2opt2 y PRELOAD no queda ninguna lectura ejecutable de di004UseDryCycle; solo de la bandera (la de sps.sub para el agua se resuelve en F09).
* Con la bandera en TRUE se cumple, y está comentado en el código, uno de: (a) el pick verifica gripper vacío después de cerrar ($IN[253] y $IN[254] OFF) y da falla con mensaje si hay pieza; o (b) la pieza termina en RejectGE4 y nunca en Style1Drop1Opt1.
* Prueba en celda en producción (option 1), con la pieza de prueba segregada: activar $IN[4] desde el PLC (1) durante un preload y (2) con el preload de la tuerca 3 terminado y el robot yendo a su pose. En los dos casos el ciclo en curso termina como productivo (3 soldaduras e inspecciones), la celda no se cuelga y el ciclo siguiente corre en dry cycle. Anotar fecha, momento del cambio y destino de la pieza.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F05) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Nombre de la bandera y módulo donde se asigna; opción elegida, (a) o (b); resultado de los dos casos con fecha.

**Nota.** Que PRELOAD use la bandera latcheada evita además el cuelgue de F04 cuando el dry cycle cambia durante un preload. En style1pick1opt2 no abrir los forms PickUp[2]: su AC_CmdParam=1 oculto no coincide con la llamada (F21).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F06 — Ciclos vacíos o silenciosos: pick ambiguo, style u option desconocidos

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/cell.src`

**Qué está mal.** Style1Opt1 hace pick en la estación 1 solo con di065 AND NOT di066 y en la estación 2 con lo inverso; con las dos señales o ninguna en ON no corre nada (nPickStation = 0), se borran las banderas y el ciclo termina. cell.src tiene un DEFAULT vacío para styles distintos de 1. Style_1 contesta una option desconocida con WAIT FOR FALSE: espera infinita sin mensaje ni falla al PLC.

**Qué hacer.** Sustituir los defaults silenciosos por falla (mensaje AutomationCore + $OUT[4] do004ProcessFault) y esperar con mensaje a que exista exactamente un permiso de pick antes de elegir estación.

**Criterio de cierre** (se verifica en el respaldo):

* En Style1Opt1, mientras $IN[65] di065PickupMachine1 y $IN[66] di066PickupMachine2 no tengan exactamente una en ON, el robot espera con un mensaje que nombra ambas señales (con ambas en ON además $OUT[4] do004ProcessFault); no existe camino por Style1Opt1 que termine sin pick.
* En cell.src, el DEFAULT del SWITCH nStyle muestra mensaje y pone $OUT[4] do004ProcessFault, y un style no ejecutado no llega a EndOfCycle.
* En Style_1 no queda WAIT FOR FALSE; el DEFAULT muestra mensaje con el número de option y pone $OUT[4] do004ProcessFault.
* En los dos DEFAULT la falla se sostiene hasta que el operador o el PLC la reconoce (diálogo o mensaje con acuse); no es un pulso que MaintainSystem borra en la siguiente vuelta de CELL.
* Prueba en celda con el PLC: (1) style distinto de 1, (2) option no válida, (3) $IN[65] y $IN[66] ambas ON, (4) ambas OFF y después una sola en ON. En cada caso hay mensaje en el smartPAD; en (1) a (3) además $OUT[4] ON hasta el acuse; en (4) el ciclo sigue normal al quedar una sola en ON. Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F06) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Texto de cada mensaje y cómo se reconoce; resultado de las cuatro pruebas con fecha.

**Depende de / se cierra con:** F02

**Nota.** La lista de options válidas en Style_1 sale de la respuesta del PLC de F02 (hoy 1, 2, 7, 8 y 12). Hoy EndOfCycle no manda Work Complete (F46): un ciclo vacío no se distingue de uno bueno en el PLC. Contribuye a C21.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F07 — Chequeo de gun cerrado: HALT sin mensaje como manejo de falla

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** CENTERLINE_WELD arranca $TIMER[14] (CL_GUN_CLOSE_TIMEOUT, 1000 ms) y $TIMER[15] (CL_GUN_IN_WINDOW_TIME, 300 ms) y confirma el gun cerrado con CL_GunStrokePositionLPT en CL_GUN_WELD_MIN..MAX (69000..73000). Al vencer el timeout pone NUT_READY = FALSE y ejecuta HALT sin mensaje que diga la falla. En el respaldo recibido, además, los timers no se rearrancaban después del resume y el lazo podía girar para siempre.

**Qué hacer.** Cambiar el HALT por un diálogo que nombre la falla (sin tuerca / doble tuerca / gun no cerró) con Retry, y Abort que abra gun y clamp y mande la pieza a rechazo.

**Criterio de cierre** (se verifica en el respaldo):

* En CENTERLINE_WELD no queda HALT en el chequeo de gun cerrado.
* Al vencer el timeout se muestra un diálogo AutomationCore (Set_KrlDlg o equivalente) con $OUT[4] do004ProcessFault ON, que nombra la falla (según CL_GunStrokePositionLPT respecto a la ventana) y ofrece Retry y Abort.
* Retry vuelve a armar el timeout y el tiempo en ventana: un segundo timeout es posible (hecho en oficina para el HALT actual, G11).
* Abort abre el gun ($OUT[472] dopw1_GunWork OFF, $OUT[471] dopw1_GunHome ON) y el clamp ($OUT[501] do501PartClampClose OFF, $OUT[502] do502PartClampOpen ON), no da weld start ($OUT[483] dopw1_WeldInit) para esa tuerca, y la pieza termina en RejectGE4.
* Prueba en T1, sin pieza, sin nadie en el pedestal y con el timer Bosch sin corriente de soldadura: cerrar el gun sin tuerca en el pin: aparece el diálogo; Retry sin corregir hace que el diálogo vuelva a salir; Abort abre gun y clamp. Anotar fecha, valor de CL_GunStrokePositionLPT leído y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F07) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Texto del diálogo y teclas; valor de CL_GunStrokePositionLPT en la falla; resultado de Retry y de Abort; cómo se marca el rechazo; fecha.

**Nota.** Hecho en oficina (G11): el chequeo es LOOP/EXIT y después del HALT los dos timers se rearrancan, así que un segundo timeout es posible. Falta el diálogo con Retry/Abort en lugar del HALT. Si el rechazo se marca en bscrapGE4, revisar la misma trampa que en F08 (F02/F03). Las salidas de Abort pueden compartir la rutina de estado seguro de F10. Contribuye a C21.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - avance en el original: En el original del programador los dos timers se reinician después del HALT (igual que la versión de oficina). Sigue sin mensaje y sin do004ProcessFault: el criterio no se cumple completo.

---

## F08 — Resultado de soldadura Bosch no evaluado: weld complete se toma como soldadura buena

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot + Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** CENTERLINE_WELD pone $OUT[483] dopw1_WeldInit, espera solo $IN[483] dipw1_WeldComplete y sigue. $IN[485] no se lee en ningún código activo y sus dos nombres se contradicen (dipw1_Fault en NutWeld, di485NoFaults en AutomationCore). La espera de feed complete está comentada. Los chequeos posteriores revisan presencia de tuerca, no calidad de soldadura.

**Qué hacer.** Confirmar la polaridad de $IN[485] con la lista de I/O del timer Bosch. Después, esperar weld complete O falla con timeout; en falla o timeout: liberar presión, abrir el gun, marcar la pieza como scrap y mostrar mensaje.

**Criterio de cierre** (se verifica en el respaldo):

* Polaridad de $IN[485] confirmada con la lista de I/O de Bosch (documento y página) o con prueba en celda (valor leído con el timer en falla y sin falla), adjunta a la lista.
* En CENTERLINE_WELD, después de $OUT[483] dopw1_WeldInit ON, la espera es $IN[483] dipw1_WeldComplete O falla ($IN[485] con la polaridad confirmada) con timeout; el código usa el nombre de $IN[485] que coincide con esa polaridad.
* En falla o timeout: presión base (CL_GUN_PRESS_BASE, con el orden de bytes que confirme F44), intensify liberado ($OUT[473] dopw1_Nut1Intensify_Home en reposo, $OUT[494] dopw1_BlowOff OFF), $OUT[483] dopw1_WeldInit OFF, gun abierto, mensaje con $OUT[4] do004ProcessFault, y la pieza termina en RejectGE4 aunque después pasen el nut check y la cámara.
* Prueba en celda: provocar una falla del timer Bosch durante una soldadura (o simularla según el manual Bosch): el robot no sigue como soldadura buena, el gun abre, aparece el mensaje y la pieza va a RejectGE4. Anotar fecha, cómo se provocó la falla y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F08) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fuente de la polaridad de $IN[485]; timeout elegido; cómo se marca el scrap; resultado de la prueba de falla con fecha.

**Depende de / se cierra con:** F44

**Nota.** Si F02/F03 ponen bScrapGE4 = TRUE al inicio de cada inspección y FALSE en el pase, una falla de soldadura guardada solo en bScrapGE4 se borraría: usar una bandera propia. $OUT[484] dopw1_FaultReset nunca se pulsa: definir cómo se recupera el timer después de una falla. El CENTERLINE_WELD1 borrado (patrón que cita Calvin) usaba señales Bosch de AutomationCore que no están en el bus de este robot: no copiar sus direcciones. La espera de $IN[479] sí está activa en R10 (F37), sin timeout (F15).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F09 — Resultado del flujo de agua descartado; $OUT[475] forzado en ON

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot + Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** sps.sub calcula SV0500_FLOW y CL_WaterOK = (SV0500_FLOW > 1230), pero pone la BOOL dipw1_WaterOk (una señal NutWeld convertida en variable por el integrador) en TRUE en las dos ramas: el resultado del flujo se tira. Nada en la ruta de soldadura lee ninguna de las dos, ni la temperatura del transformador $IN[475] dipw1_XtfmrTempOk. El límite es > 1230 mientras el comentario viejo decía "1230 = water OK". sps.sub pone $OUT[475] dopw1_StartWater en TRUE en cada ciclo fuera de dry cycle, nunca lo apaga, ignora $IN[13] di013WaterEnable y sobrescribe el water-off de CENTERLINE_HOME y GunElectrodeChange.

**Qué hacer.** Escribir el resultado real del flujo (FALSE con flujo bajo); exigir agua OK y temperatura de transformador OK antes de $OUT[483] dopw1_WeldInit, con espera supervisada; manejar $OUT[475] desde $IN[13] di013WaterEnable, encendiendo y apagando; confirmar el límite de flujo.

**Criterio de cierre** (se verifica en el respaldo):

* En sps.sub, con SV0500_FLOW bajo el límite la bandera de agua usada por la soldadura queda en FALSE (ya no hay TRUE en las dos ramas); una sola bandera (CL_WaterOK o dipw1_WaterOk) y la otra se quita o se deja documentada.
* En CENTERLINE_WELD, antes de $OUT[483] dopw1_WeldInit ON, existe una espera supervisada (timeout + mensaje + $OUT[4] do004ProcessFault) de agua OK y $IN[475] dipw1_XtfmrTempOk ON; sin ellas no hay weld start.
* En sps.sub, $OUT[475] dopw1_StartWater se escribe en ambos sentidos según $IN[13] di013WaterEnable; una sola lógica decide $OUT[475] (el water-off de CENTERLINE_HOME y de gunelectrodechange se respeta o se quita, y el comentario dice quién manda).
* El límite de SV0500_FLOW (valor y operador) coincide con un valor confirmado por escrito (Gestamp o CenterLine) y el ;CHECK: del límite en sps.sub se elimina.
* Prueba en celda: (1) con $IN[13] OFF, $OUT[475] pasa a OFF; (2) con el agua cerrada el robot no da weld start y muestra mensaje; (3) con agua y transformador normales la soldadura arranca. Anotar fecha y SV0500_FLOW leído con agua normal y con agua cerrada.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F09) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Documento con el límite de flujo; SV0500_FLOW con agua normal y cerrada; valor de $IN[475] en condición normal; resultado de las tres pruebas con fecha.

**Nota.** Antes de cargar, confirmar con el PLC que $IN[13] di013WaterEnable llega en ON en producción. Si se reactiva AutomationCore_Bkg (F12), su escritura de $OUT[475] se quita o pasa a ser la única. IO_MAP lista $IN[475] como mapeado y sin leer.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - corregido sin marcar: sps.sub calcula dipw1_WaterOk del sensor Parker (flujo en 0.1 l/min, mínimo 150 con histéresis 10) y $OUT[475] sigue a $IN[13] di013WaterEnable. GUN_OPEN_CHECK espera agua antes de entrar. Falta: confirmar el mínimo (el comentario cita una medición del 20R1) y la prueba en celda sin agua.
* 2026-10-05 — Integrado - avance parcial: El agua se calcula del SV0500 (mínimo 150 = 15 l/min, histéresis 10) y GUN_OPEN_CHECK la exige antes de entrar y al salir; $OUT[475] sigue a $IN[13]. Faltan: espera de agua y transformador antes del weld start en CENTERLINE_WELD, límite confirmado por escrito y la prueba en celda.
* 2026-10-05 — Evidencia parcial: Respaldo 14:46: nWaterFlow = 233 (23.3 l/min) con agua normal en este robot, arriba del mínimo de 15 l/min. Falta la prueba con agua cerrada y la espera antes del weld start.

---

## F10 — Sin estado seguro del pedestal al cancelar o resetear el programa

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/cell.src`, `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** El único hook de reset de programa (interrupt 91 de sps.sub, RESET_OUT, con $PRO_STATE1 = #P_FREE) borra los bits de PGNO. Nada regresa a estado seguro clamp, gun, palabra de presión, intensify, blow-off, weld start o contactor enable al cancelar. Si la soldadura se cuelga y el operador cancela y reinicia, la pieza queda sujeta en el gun cerrado y el diálogo HomeCheck de AutomationCore puede mover PTP HOME en T1 jalando el gripper contra ella. Si el timer Bosch se resetea con WeldInit todavía en alto, puede arrancar una soldadura mientras alguien manipula la pieza.

**Qué hacer.** Una rutina que lleve el pedestal a estado seguro al cancelar o resetear el programa (weld start y contactor off, presión base, intensify y blow-off off, gun y clamp abiertos) y bloquear el movimiento a HOME mientras el clamp o el gun estén cerrados. Abrir gun y clamp sin enabling switch se decide con la revisión de seguridad de F11.

**Criterio de cierre** (se verifica en el respaldo):

* Existe una rutina de estado seguro del pedestal que se ejecuta cuando el programa se cancela ($PRO_STATE1 = #P_FREE) y cuando se resetea ($PRO_STATE1 = #P_RESET).
* La rutina deja: $OUT[483] dopw1_WeldInit OFF, $OUT[481] dopw1_WeldContactEnable OFF, $OUT[482] dopw1_WeldOnExternal OFF, CL_GunPressureCmd = presión base (valor según F44), $OUT[473] dopw1_Nut1Intensify_Home en su reposo, $OUT[494] dopw1_BlowOff OFF, $OUT[476] dopw1_StartFeed OFF.
* La rutina deja además gun abierto y clamp abierto, salvo que la revisión de seguridad de F11 decida por escrito que en cancel/reset no se mueven actuadores sin enabling switch; en ese caso no los toca, el comentario cita esa decisión y la protección es el bloqueo de HOME.
* En cell.src ningún camino llega a InitializeSystem(), HOME() o HomeCheck() mientras el gun no esté abierto (CL_GunStrokePositionLPT > CL_GUN_OPEN_MIN) o el clamp no esté abierto ($IN[466] di466PartClampOpen ON): espera supervisada con mensaje y $OUT[4] do004ProcessFault, sin movimiento.
* Prueba en T1, sin pieza, sin nadie en el pedestal y con el timer Bosch sin corriente: detener CENTERLINE_WELD con el clamp cerrado y cancelar el programa; leer cada salida de la lista. Repetir con reset. Después, con el clamp detectado como no abierto, seleccionar CELL: el robot no se mueve a HOME y muestra mensaje. Anotar fecha y valores leídos.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F10) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Dónde se dispara la rutina; decisión de F11 sobre gun y clamp; valores de I/O leídos; resultado de la prueba de bloqueo de HOME; fecha.

**Depende de / se cierra con:** F11, F44

**Nota.** Las salidas de soldadura y el bloqueo de HOME no dependen de F11 y se pueden hacer ya. Preferir los folds USER de sps.sub y no tocar los folds AUTOEXT. Si se reactiva AutomationCore_Bkg (F12) sin quitar sus escrituras de weld enable, anula este estado seguro.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F11 — PRELOAD en el submit mueve el pedestal en cualquier modo, sin dueño de las salidas

**Severidad:** Crítico · **Tipo:** Código + prueba en celda · **Responsable:** Seguridad + Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** sps.sub llama PRELOAD en cada ciclo del submit, en todos los modos. Una vez que NUT_START se pone (por TRIGGER de movimiento, que también dispara al ir paso a paso en T1), PRELOAD escribe por su cuenta feed, QFP, gun, pins, clamp y blow-off; CENTERLINE_WELD y CENTERLINE_HOME escriben las mismas salidas y ninguno revisa al otro. NUT_START solo se consume sin preload activo: una solicitud durante un preload arranca un segundo preload justo después. En T1, un operador que pasa P12 paso a paso y camina al pedestal ve moverse feed, gun, clamp, slide y pins durante unos 4 s sin enabling switch.

**Qué hacer.** Primero la revisión de seguridad: ¿se corta el aire del pedestal al abrir la puerta? Después: un solo dueño del pedestal; PRELOAD solo corre con automático externo, $MOVE_ENABLE y una liberación del lado del robot; los programas manuales esperan o abortan PRELOAD antes de escribir válvulas; una solicitud durante un preload activo no deja pasar al robot con una bandera de un solo ciclo.

**Criterio de cierre** (se verifica en el respaldo):

* Revisión de seguridad documentada (Gestamp / Seguridad) que responde si el aire del pedestal se corta con la puerta abierta, con referencia al plano o a una prueba física con fecha, adjunta a la lista.
* En PRELOAD (o en su llamada en sps.sub), el arranque y los pasos están condicionados a $MODE_OP == #EX, $MOVE_ENABLE TRUE y una bandera de liberación declarada que pone y quita el programa del robot; con la condición en FALSE, PRELOAD no escribe ninguna salida del pedestal.
* Si la condición cae con un preload a medias, el comportamiento está escrito en un comentario de PRELOAD y un preload interrumpido no puede terminar en NUT_READY / NEXT_NUT_READY = TRUE sin haber completado sus pasos.
* PRELOAD no arranca mientras CENTERLINE_WELD o CENTERLINE_HOME están corriendo, y esos programas no escriben válvulas del pedestal mientras NUTCYCLE_ACTIVE es TRUE.
* Un NUT_START recibido con un preload activo no produce una bandera de un solo ciclo de submit que el robot pueda tomar como buena.
* En T1/T2 el ciclo no se queda esperando NUT_READY sin mensaje.
* Prueba en celda, sin nadie en el pedestal: (1) en T1, correr el pick paso a paso hasta pasar P12 y soltar el enabling switch: el pedestal no se mueve; (2) con CELL cancelado, poner NUT_START = TRUE desde la pantalla de variables: el pedestal no se mueve; (3) en automático externo, un ciclo productivo completo alimenta y suelda las 3 tuercas. Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F11) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Documento de la revisión de seguridad; nombre de la bandera de liberación y dónde se pone y se quita; comportamiento elegido; resultado de las tres pruebas con fecha.

**Nota.** El gate toca el mismo arranque de PRELOAD que F04: coordinar. Relacionado con F10, F12 (doCriticalWZ), F13, F14 y F38.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F12 — Background de AutomationCore y NutWeld deshabilitado: los bits de estado al PLC no cambian

**Severidad:** Alto · **Tipo:** Decisión Gestamp · **Responsable:** Gestamp controles + Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/TP/NutWeld/nutweldroutines.src`, `KRC/R1/System/$config.dat`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/cell.src`

**Qué está mal.** En sps.sub las llamadas NutWeld_BKG ( ) y AutomationCore_BKG ( ) estaban comentadas (los folds quedaron vacíos). Por eso nunca se escriben: brake test pendiente ($OUT[21] do021BrakeTestReqd), mastering pendiente ($OUT[22]), alarma de batería ($OUT[6]), robot en pounce ($OUT[7] do007RobotAtPounce, lo usa HomeCheck), cambio de electrodo pendiente ($OUT[111..113], que cell.src revisa: GunElectrodeChange nunca corre, F43), weld mode, bits de nodos de bus, speed not 100 %, doCriticalWZ ($OUT[145]) y nivel de tolva. La edición de AutomationCore en bas.src sigue deteniendo cada PTP/LIN cuando el PLC pide entrar ($IN[6] di006RequestToEnter), pero doCriticalWZ queda en FALSE y el PLC ve entrada permitida mientras PRELOAD o CENTERLINE_WELD siguen moviendo el pedestal.

**Qué hacer.** Decidir con Gestamp si el background task es obligatorio. Si se reactiva: antes quitar sus escrituras de weld enable que pelean con CENTERLINE_WELD y su water-on ($OUT[475]), y cerrar F35 ($OUT[930] en ON bloquearía toda request to enter) y F17 (NutWeld_BKG). Si no: reproducir en sps.sub los bits requeridos.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión escrita de Gestamp (nombre, fecha): reactivar AutomationCore_BKG y/o NutWeld_BKG, o reproducir los bits en sps.sub.
* Si se reactiva AutomationCore_BKG: F35 está cerrado antes; en automationcoreroutines.src ya no hay escrituras de weld enable por dry cycle ni de $OUT[475] que contradigan F09; cada cambio en el archivo del proveedor queda en la lista de C28.
* Si se reactiva NutWeld_BKG: F17 está cerrado antes (nombres de pistola 2/3 traslapados con CL_GunPressureCmd).
* Si se reproducen en sps.sub: se escriben en cada ciclo $OUT[21], $OUT[22], $OUT[6], $OUT[7], $OUT[46], los bits de nodo de bus que Gestamp pida, $OUT[146], $OUT[145] doCriticalWZ, el nivel de tolva y la petición de cambio de electrodo que se acuerde en F43, con la lógica aprobada por escrito.
* En cualquier caso, $OUT[145] doCriticalWZ está en TRUE (entrada no permitida) mientras CENTERLINE_WELD corre o PRELOAD está activo.
* Prueba en celda: verificar desde el PLC cada bit que se pueda provocar (p. ej. override < 100 % en automático externo; una solicitud de entrada durante CENTERLINE_WELD no recibe permiso); los demás se revisan en código. Anotar fecha y resultado por bit.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F12) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Documento o correo de Gestamp con la decisión; lista de cambios en archivos del proveedor; tabla de bits verificados con resultado y fecha.

**Depende de / se cierra con:** F17, F35

**Nota.** Ethos (Edgar) lleva la pregunta a Gestamp. Al cerrarse se cierra C01; aporta a C12, C14 y C19.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - cambio sin decisión: El programador activó AutomationCore_BKG en sps.sub y editó la rutina del proveedor (sin soldadores 2-3, Request to Enter sin WAIT). La decisión de Gestamp no está registrada. Ver F49.
* 2026-10-05 — Integrado - pendiente decisión: AutomationCore_BKG queda activo en la versión integrada, como lo dejó el programador. Falta la decisión de Gestamp (F49).
* 2026-10-05 — Integrado: Background de AutomationCore apagado otra vez en la versión integrada (F49).

---

## F13 — PRELOAD sin timeouts por paso, sin falla y banderas de tuerca lista sin confirmar alimentación

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/System/$config.dat`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`

**Qué está mal.** En PRELOAD los pasos 0 y 10 esperan los switches del QFP ($IN[482] dipw1_SpearHome, $IN[470] di470QFPAdvanced) sin límite de tiempo y sin mensaje; el paso 20 corre solo con timers. NUT_PRELOAD_FAULT nunca se pone TRUE. NUT_READY / NEXT_NUT_READY se ponen por tiempos fijos (2000 ms de feed, 500 ms tras el avance, 800 ms de blow-off, 800 ms tras mandar regresar el QFP) sin leer $IN[481] dipw1_FeedComplt (en el bus) ni $IN[480] dipw1_HopperLowLevel. Con la tolva vacía se declara tuerca lista sin tuerca; si un switch no llega, el robot espera sin mensaje.

**Qué hacer.** Agregar a cada condición que PRELOAD espera un timeout que ponga NUT_PRELOAD_FAULT = TRUE y detenga la secuencia sin poner las banderas de tuerca lista; exigir feed complete y nivel de tolva OK; las weld apps esperan tuerca lista O falla y, con falla, dan mensaje y $OUT[4] sin entrar al pedestal. PRELOAD corre en el submit: timeouts con timers revisados en cada ciclo, sin bloquear.

**Criterio de cierre** (se verifica en el respaldo):

* En PRELOAD toda condición que la secuencia espera (QFP regresado/avanzado en los pasos 0 y 10, QFP regresado al final del paso 20, $IN[481] dipw1_FeedComplt) tiene timeout; al vencer: NUT_PRELOAD_FAULT = TRUE, queda registrado el paso y la señal, y la secuencia no pone NUT_READY ni NEXT_NUT_READY.
* PRELOAD no contiene WAIT FOR ni WAIT SEC (corre en el submit).
* Existe al menos una asignación NUT_PRELOAD_FAULT = TRUE en código activo, y la falla solo se borra en un punto definido (reset del operador o rutina de reset), dicho en el comentario.
* Fuera de dry cycle, NUT_READY / NEXT_NUT_READY = TRUE solo con $IN[481] visto ON durante la alimentación, $IN[480] en nivel OK (polaridad confirmada) y QFP regresado confirmado al final del paso 20.
* En style1app1opt1..3 la espera previa al LIN de aproximación termina con la bandera de tuerca lista o con NUT_PRELOAD_FAULT; con falla hay mensaje, $OUT[4] do004ProcessFault ON y el robot no ejecuta el LIN de aproximación.
* Prueba en celda: (a) tolva vacía o alimentador apagado: no hay tuerca lista, aparece el mensaje y el robot no entra al pedestal; (b) aire del QFP cerrado: timeout del paso con mensaje. Anotar fecha, timeout y texto del mensaje.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F13) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Timeout por condición (ms); polaridad de $IN[480] y $IN[481] leída en el smartPAD; resultado de las pruebas (a) y (b) con fecha.

**Depende de / se cierra con:** F01, F11

**Nota.** Calvin lo califica Alto (#6). Se queda en Medio: con una tuerca faltante el gun cierra fuera de la ventana 69000..73000 y el chequeo de gun cerrado detiene el ciclo (F07); la celda para, la pieza no sale mala. Timers nuevos: ver F26.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-07 — Avance parcial (F52): El paso 20 ya termina con el QFP regresado confirmado ($IN[482] ON, $IN[470] OFF) en vez de 800 ms. Timeouts, falla y feed complete siguen pendientes.

---

## F14 — NUT_READY no se consume al soldar; la siguiente tuerca depende solo de TRIGGERs

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** NUT_READY significa 'tuerca cargada' pero solo se borra cuando PRELOAD acepta una petición nueva o en el timeout de gun cerrado, nunca cuando la soldadura consume la tuerca. La siguiente tuerca se pide solo por TRIGGER de movimiento (picks en P12/P10, final de las apps 1 y 2). Un ciclo cancelado puede dejar una tuerca en el pin y el siguiente pick alimenta otra (doble tuerca); un TRIGGER del pick saltado deja pasar la tuerca 1 con un TRUE viejo y sin tuerca: solo la ventana del LPT (F07) evita soldar sin tuerca. El pick red rabbit también arranca un preload aunque no sigue ninguna soldadura.

**Qué hacer.** Borrar NUT_READY en el flujo de soldadura en cuanto la tuerca se consumió; confirmar el pin vacío antes de alimentar; pedir la siguiente tuerca con una instrucción en el flujo (no solo en un TRIGGER), en main run; una petición repetida no debe provocar una segunda alimentación.

**Criterio de cierre** (se verifica en el respaldo):

* En CENTERLINE_WELD después de $IN[483] dipw1_WeldComplete, o inmediatamente después de CENTERLINE_WELD() en style1app1opt1..3, existe NUT_READY = FALSE (y la bandera que usen las tuercas 2 y 3) antes de salir del pedestal.
* La petición de la tuerca 1 (picks) y de las tuercas 2 y 3 (final de style1app1opt1 y opt2) existe como instrucción en el flujo, fuera de TRIGGER, precedida de un paro de advance run; en las apps va después del movimiento que saca pieza y EOAT del alcance del QFP y de los pines.
* En PRELOAD una petición que llega con preload activo o con tuerca cargada sin consumir no arranca otra alimentación.
* Antes de alimentar se confirma pin vacío: por sensor si existe (nombre y dirección), o por estado si se confirma en sitio que no hay sensor; el comentario del paso dice cuál.
* El pick red rabbit no pide preload, o la lista anota por qué sí.
* Prueba en celda: (a) cancelar el ciclo con tuerca precargada y reiniciar desde home: no hay doble tuerca; (b) cancelar después de soldar la tuerca 1 y reiniciar con selección de paso en style1app1opt2: el robot no entra a soldar sin preload nuevo. Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F14) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Cómo se confirma el pin vacío; resultado de las pruebas (a) y (b) con fecha.

**Depende de / se cierra con:** F11, F25, F32, F38

**Nota.** Trampa de advance run: una asignación o llamada escrita después de un movimiento corre varios movimientos antes de que el robot llegue; sin paro de advance run PRELOAD movería QFP y pines con la pieza todavía en el pedestal. IO_MAP marca $IN[468] y $IN[469] como switches sin identificar: confirmar en sitio si alguno es el sensor de pin. Los TRIGGER ya no están dentro de inline forms (G20/F32).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F15 — Unos 35 WAIT FOR sobre entradas de proceso sin timeout ni mensaje

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/cell.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`

**Qué está mal.** Las esperas de Bosch ready/complete, presión de intensificado ($IN[479]), ventanas del LPT, gun open, clamp abierto/cerrado, QFP avanzado/regresado, NUT_READY / NEXT_NUT_READY, el handshake de la cámara ($IN[80]) y las de gripper vacío / pieza presente son WAIT FOR sin supervisión. Si una señal no llega, el robot queda parado 'en ciclo' sin mensaje que diga qué espera y sin falla al PLC. No se usa el idioma de AutomationCore (SetWaitingMessage).

**Qué hacer.** Una rutina de espera supervisada con timeout, $OUT[4] do004ProcessFault y mensaje que nombre la señal con dirección, con reintento; usarla en todas las esperas de dispositivo y proceso. En el pedestal, el abort deja weld start apagado y gun y clamp abiertos (coordinar con F10). Las esperas de permiso del PLC llevan al menos mensaje de espera. Entregar la tabla de esperas con su timeout.

**Criterio de cierre** (se verifica en el respaldo):

* En los módulos listados no queda espera sin timeout sobre $IN[466], $IN[467], $IN[470], $IN[479] dipw1_IntensfPresOk, $IN[482], $IN[483], $IN[484], CL_GunStrokePositionLPT, NUT_READY, NEXT_NUT_READY, $IN[80] di080ToolRepositioned1 ni $IN[253]/$IN[254].
* Al vencer un timeout: $OUT[4] do004ProcessFault ON, mensaje que nombra la señal con dirección, y el programa no continúa sin la condición (reintento o abort explícito).
* En CENTERLINE_WELD y CENTERLINE_HOME el abort de una espera vencida deja el pedestal abierto: primero $OUT[483] dopw1_WeldInit OFF, luego gun abierto y clamp abierto.
* En cell.src la espera de $IN[8] di008ReturnFromRepair tiene al menos mensaje de espera que nombra la señal.
* La lista trae una tabla módulo / señal / timeout (s) / reacción que coincide con el código del respaldo.
* Prueba en T1: provocar una espera vencida por grupo: pedestal (clamp sin aire), intensificado ($IN[479]), cámara ($IN[80] sin respuesta), Bosch (ready ausente) y gripper (pieza presente); anotar mensaje, $OUT[4] y fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F15) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Tabla de esperas con timeout y reacción; resultado de las pruebas con texto del mensaje y fecha.

**Depende de / se cierra con:** F01, F07, F10

**Nota.** Los forms GripperTech (GRPg_SetStateAndCheck) ya revisan el estado del gripper con su estrategia de error (3 s): no cuentan aquí. SetWaitingMessage no tiene timeout y, si el operador borra el mensaje, la espera termina como 'simulada': no usarlo tal cual en esperas del pedestal. Las esperas de PRELOAD son F13; el WAIT FOR FALSE de Style_1 es F06. C21 se cierra con F06, F07 y F15.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F16 — Posición del pin superior nunca verificada

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/System/$config.dat`, `KRC/R1/System/sps.sub`

**Qué está mal.** sps.sub arma CL_WeldPinPosition ($IN[591..606] CL_PIN_BYTE0..1) y ningún programa lo lee. CL_PIN_WELD_MIN/MAX (10000..13500) están declaradas y sin uso. Al final de la soldadura el pin superior se manda regresar 0.2 s después de ver el gun abierto, sin confirmación, y la app retira la pieza.

**Qué hacer.** En CENTERLINE_WELD, confirmar con espera supervisada el pin superior en posición de soldadura (CL_PIN_WELD_MIN..MAX) antes de $OUT[483] dopw1_WeldInit, y retraído antes de terminar. Declarar la ventana de retraído con valores medidos, sin traslape con la de soldadura.

**Criterio de cierre** (se verifica en el respaldo):

* En CENTERLINE_WELD, antes de dopw1_WeldInit = TRUE, hay espera supervisada (timeout + mensaje + $OUT[4] do004ProcessFault) de CL_WeldPinPosition dentro de CL_PIN_WELD_MIN..CL_PIN_WELD_MAX.
* Después del comando de retraer ($OUT[499] do499UpperPinRetract ON) y antes del END hay espera supervisada de CL_WeldPinPosition dentro de una ventana de retraído declarada como constantes en $config.dat.
* Las ventanas coinciden con los valores medidos anotados en la lista (la tabla del encabezado da retraído 27252, extendido 6602, soldadura 11674) y no se traslapan; la tabla del encabezado coincide con las constantes.
* Las ventanas del gun usan CL_GUN_WELD_MIN/MAX y CL_GUN_OPEN_MIN (hecho en oficina, G16).
* Prueba en celda en T1: provocar que el pin superior no llegue a la ventana de soldadura: no hay weld start y aparece el mensaje; anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F16) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Valores de CL_WeldPinPosition leídos con el pin retraído, extendido y en posición de soldadura, y límites elegidos. Resultado de la prueba con fecha.

**Depende de / se cierra con:** F27

**Nota.** Hecho en oficina (G16): la ventana del gun son constantes: CL_GUN_WELD_MIN/MAX = 69000..73000 (la que el código siempre revisó; estaban declaradas 65000..76000 sin uso) y CL_GUN_OPEN_MIN. Falta la verificación del pin superior. La asignación de válvulas de pines está por confirmar (F27).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F17 — Declaraciones traslapadas; nombres dobles en los bits del pedestal

**Severidad:** Medio · **Tipo:** Código · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/TP/NutWeld/nutweldroutines.dat`

**Qué está mal.** CL_GunPressureCmd ($OUT[506..521]) se traslapa con los nombres AutomationCore do512..do521 y NutWeld dopw2_*; CL_LPT_BYTE0..3 ($IN[559..590]) con dipw3_* y di561..di590; CL_PIN_BYTE0/1 ($IN[591..606]) con aiNutSensorPW3. Las pistolas 2 y 3 no existen en este robot. $IN[466], $IN[467] y $IN[470] siguen con un segundo nombre Spare (di466Spare...). $OUT[477]/$OUT[478] tienen nombres invertidos entre NutWeld (LevelOk/LowLevel) y AutomationCore (LowLevel/LevelOk). $OUT[500] (do500Reserved) no tiene función conocida.

**Qué hacer.** Marcar como retirados los nombres de pistola 2/3 que se traslapan y los Spare sobrantes, documentar el nombre correcto de $OUT[477]/$OUT[478] e identificar $OUT[500]. Hacerlo antes de reactivar cualquier background task (F12) y actualizar el proyecto WorkVisual.

**Criterio de cierre** (se verifica en el respaldo):

* $IN[466], $IN[467], $IN[470], $OUT[498], $OUT[499] y $OUT[501..505] tienen nombre AutomationCore y el código del pedestal no usa direcciones literales (hecho en oficina, G12).
* Las declaraciones de pistola 2/3 que se traslapan con CL_GunPressureCmd, CL_LPT_BYTE0..3 y CL_PIN_BYTE0/1 y los nombres Spare de $IN[466/467/470] llevan comentario de retirados, y ningún programa del integrador los lee ni escribe.
* $OUT[477]/$OUT[478]: el comentario de la declaración dice cuál nombre es el correcto (confirmado con F29).
* $OUT[500] recibe nombre después de confirmar en celda qué mueve, o deja de usarse.
* Ninguna dirección cambió; cada edición en archivos del proveedor (automationcoreroutines.dat, nutweldroutines.dat) aparece en la lista de C28.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F17) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Qué mueve $OUT[500] (confirmado en celda) o constancia de que ya no se usa; fecha en que se actualizó el proyecto WorkVisual desde el controlador.

**Depende de / se cierra con:** F29

**Nota.** Hecho en oficina (G12): nombres AutomationCore para $IN[466], $IN[467], $IN[470], $OUT[498], $OUT[499] y $OUT[501..505], y el código del pedestal usa solo nombres. Falta lo de los criterios 2 a 4. No 'corregir' las palabras de presión aquí: eso es F44. C23 se cierra con este punto.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F18 — KRC_IO.xml mapea $OUT[820..979] y $IN[820..930] sobre los mismos bytes del adapter PLC

**Severidad:** Medio · **Tipo:** WorkVisual / configuración · **Responsable:** Gestamp controles / Programador robot · **Estado:** Requiere decisión

**Módulos:** `C/KRC/Roboter/Config/User/Common/KRC_IO.xml`, `KRC/R1/Program/masref_user.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/TP/BrakeTest/braketeststart.src`, `KRC/R1/TP/BrakeTest/braketestback.src`

**Qué está mal.** Igual que en R20: $OUT[820..979] está mapeado a los mismos 20 bytes del EIP-ADAPTER que $OUT[1..160], y $IN[820..930] a los mismos que $IN[1..111] (más $IN[973..979]). Así do930MasterRefInProcess cae en el bit del PLC de $OUT[111] do111Gun1ElectrodeChange y di823ToolIDBit0 es físicamente $IN[4] di004UseDryCycle. Como en R10 $OUT[930] se queda en ON después del primer mastering reference (F35), el PLC ve el bit de cambio de electrodo de la pistola 1 encendido.

**Qué hacer.** Revisar en WorkVisual el tamaño de assembly del adapter y acordar con controles Gestamp el mapa de tags. Ningún par de rangos KRC debe compartir bytes del adapter; do930/do931 y cualquier otra señal 8xx/9xx que se use van en bits propios acordados, o se dejan de usar. El cambio se hace en WorkVisual y se despliega; KRC_IO.xml no se edita a mano.

**Criterio de cierre** (se verifica en el respaldo):

* En KRC_IO.xml no hay dos entradas <Out> ni dos <In> que cubran los mismos bits del mismo segmento EIP-ADAPTER.
* do930MasterRefInProcess, do931BrakeTestInProcess, di823ToolIDBit0 y di825ToolIDBit1 están en bits propios del mapa acordado, o ningún código activo los usa.
* El tamaño de assembly acordado con Gestamp está en la lista (captura de WorkVisual).
* Prueba fuera de ciclo: correr el mastering reference y confirmar en el PLC que el tag de $OUT[111] no cambia; cambiar $IN[4] desde el PLC y confirmar que di823ToolIDBit0 no lo sigue. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F18) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Mapa de tags robot-PLC acordado con Gestamp, adjunto; fecha del deploy y resultado de la prueba.

**Depende de / se cierra con:** F35

**Nota.** KRC_IO.xml lo genera WorkVisual: cambiarlo en el proyecto, desplegar y después cargar el proyecto actualizado. Si se reactiva AutomationCore_Bkg (F12), su request to enter lee do930..do932: este punto se cierra antes.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F19 — Red rabbit: el ciclo no puede dar resultado y suelta la pieza por un mapeo duplicado

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`

**Qué está mal.** Style_1 corre el red rabbit como option 12 (Style1Opt10AutoRR), que llama el nut check y la cámara de producción. El nut check pone las salidas red rabbit solo para CASE 10: con option 12 nunca se pone $OUT[141] do141RedRabbitFailed ni $OUT[142] do142RedRabbitPassed; la cámara solo escribe bscrapGE4. El drop red rabbit (style1drop1opt2AutoRR) primero cierra el gripper 1 con salidas escritas a mano ($OUT[249] OFF, $OUT[250] ON) y después "abre" con GRPg_SetStateAndCheck(3, 1, ...). El gripper 3 está inactivo en grp_data.dat pero configurado en la misma E/S que el gripper 1 y GRPg_SetState no mira la bandera de activo: el gripper 1 sí abre y el check del gripper 1 OPEN pasa. La liberación funciona solo por ese mapeo duplicado. Después el robot se mueve (LIN P23) antes de esperar gripper vacío, y las salidas se borran en el drop, antes de que el PLC las lea; MaintainSystem las borra otra vez al inicio del siguiente ciclo.

**Qué hacer.** Decidir con Gestamp el procedimiento red rabbit (número de option, qué es un pase: todas las tuercas faltantes vistas por sensor Y cámara), evaluarlo en un solo lugar con un veredicto exclusivo que se mantenga hasta que el PLC lo lea, soltar con el gripper 1 y esperar gripper vacío antes de moverse.

**Criterio de cierre** (se verifica en el respaldo):

* Procedimiento red rabbit de Gestamp por escrito (option, pieza, resultado esperado de cada chequeo), adjunto.
* Para la option red rabbit el resultado sale de una sola evaluación que combina sensor y cámara y asigna las dos salidas en el mismo punto: exactamente una de $OUT[141] / $OUT[142] en TRUE y la otra en FALSE; resultado contradictorio, parcial o cámara sin respuesta dan Failed.
* El veredicto se mantiene hasta que el PLC lo lee (con el handshake de fin de ciclo que decida F46); ya no se borra en style1drop1opt2AutoRR antes del fin del ciclo.
* style1drop1opt2AutoRR suelta con un form GripperTech del gripper 1 (GRPg_SetStateAndCheck(1, 1, ...)), sin salidas $OUT[249]/$OUT[250] escritas a mano ni forms del gripper 3, y espera gripper vacío ($IN[253] y $IN[254] OFF) antes de LIN P23.
* Prueba en celda: correr el red rabbit con la pieza red rabbit y otra vez con una pieza buena de 3 tuercas; anotar qué ve el PLC en $OUT[141]/$OUT[142] al final del ciclo (esperado: Passed con la red rabbit, Failed con la buena) y que la pieza se suelta y el robot no se mueve antes de gripper vacío. Fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F19) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Descripción de la pieza red rabbit y regla de veredicto; lectura del PLC en las dos pruebas, con fecha.

**Depende de / se cierra con:** F46, F31, F40, F03

**Nota.** Gestamp (puntos 8 y 21) describe lo mismo; G08 y G21 se cierran con este punto. Mientras no se cambie, no reconfigurar el gripper 3 en GripperTech ni re-sincronizar GripperConfig.xml quitándole esa E/S (F33): el drop red rabbit dejaría de soltar. Hecho en oficina (G20): los resets del red rabbit ya están fuera del fold DropOff[2] Reset.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - avance parcial: Con option 12 el sensor y la cámara ya ponen $OUT[141]/$OUT[142]. No es un veredicto exclusivo (los dos chequeos pueden poner Failed y Passed a la vez) y el drop red rabbit los sigue borrando antes del fin de ciclo.
* 2026-10-05 — Integrado - avance parcial: Option 12 ya pone $OUT[141]/$OUT[142] en sensor y cámara. Falta el veredicto único y que el drop no lo borre antes de que el PLC lo lea.

---

## F20 — Reject sin permiso del PLC para la posición de rechazo; Application 1 sin liberar

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

**Qué está mal.** RejectGE4 abre el gripper sobre la posición de rechazo (LIN P23) sin AC_DropOffCheck ni petición de zona. Cuando el nut check decide scrap, Style1Opt1 va a RejectGE4 y se salta el AC_Application(1,True) del final de style1app2opt2, así que Application 1 queda ocupada hasta MaintainSystem. La trampa del inline form OUT 106 (dato oculto 5:TRUE) ya la corrigió la depuración.

**Qué hacer.** Antes de entrar a la posición de rechazo, pedir permiso al PLC con el mecanismo AutomationCore que se acuerde con controles Gestamp y liberarlo al salir. En el camino de rechazo por nut check, liberar Application 1 igual que en el camino bueno.

**Criterio de cierre** (se verifica en el respaldo):

* En Style1Opt1, en el camino de rechazo por nut check se ejecuta AC_Application(1,TRUE) (o lo que pone $OUT[70] do070ApplicationClear1 ON) antes de que termine el ciclo; todo camino que pasó por AC_ApplicationCheck(1) tiene su liberación.
* En RejectGE4, antes de LIN P23, hay petición de permiso con el número acordado (AC_DropOffCheck(n) o zona) con espera y mensaje, y su liberación después de salir de la posición (P24 o después).
* Si se agregan inline forms AutomationCore, su AC_CmdParam oculto corresponde a la llamada según la convención de F21.
* Prueba en celda: con el permiso de rechazo apagado en el PLC el robot se detiene antes de P23 con mensaje y continúa al darlo; después de un rechazo por nut check el PLC ve $OUT[70] ON al terminar el ciclo. Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F20) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Número de drop-off o zona y señal del PLC acordados; resultado de la prueba con fecha.

**Depende de / se cierra con:** F21

**Nota.** La liberación de Application 1 se puede hacer ya; el interlock espera la definición del PLC. No reabrir los forms OUT 106 de RejectGE4. C18 se cierra con F20, F21 y F46.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Integrado - avance: RejectGE4 libera la aplicación 1 por TRIGGER en P23, también después de un scrap del sensor (antes nunca se liberaba en esa ruta). El lugar de rechazo sigue sin interlock con el PLC.

---

## F21 — Parámetros ocultos de inline forms AutomationCore no coinciden con la llamada

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

**Qué está mal.** style1pick1opt2 tiene AC_CmdParam=1 en sus dos folds de pick pero llama AC_pickUPCheck(2) / AC_pickUP(2,True); style1app2opt2 tiene AC_CmdParam=2 y llama AC_Application(1,True); style1drop1opt1 tiene AC_CmdParam=2 y llama DropOff 1, mientras el drop red rabbit tiene AC_CmdParam=2 y llama DropOff 2: no hay un desfase constante. Abrir y confirmar uno de estos forms regenera la llamada desde el parámetro oculto y puede cambiar el número de pickup, application o drop-off. La depuración no tocó esas líneas y puso un ;WARNING: sobre cada fold.

**Qué hacer.** Establecer en el smartPAD qué escribe el form AutomationCore en AC_CmdParam para cada tipo y número (insertando el form en un módulo de prueba) y, con esa convención, corregir el parámetro oculto de cada fold. Corregir el parámetro, nunca la llamada.

**Criterio de cierre** (se verifica en el respaldo):

* La convención queda anotada en la lista para cada tipo de form usado (PickUp, Application, DropOff) con foto del form insertado en un módulo de prueba y el AC_CmdParam que genera. El módulo de prueba no queda en el controlador.
* Todos los folds ';Params IlfProvider=ac_zoneilf' cumplen la convención: style1pick1opt2 (2 folds), style1app2opt2 (1), style1drop1opt1 (2), style1drop1opt2AutoRR (2), y los de style1pick1opt1, style1pick1opt1AutoRR y style1app2opt1 si la convención los contradice.
* Las llamadas AC_ son las mismas del respaldo anterior; solo cambió la línea ;Params.
* Prueba en el smartPAD: abrir y confirmar (Cmd OK) cada form corregido; en el respaldo siguiente el cuerpo de cada fold es la misma llamada de antes. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F21) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Foto del form de prueba por tipo y convención; lista de folds corregidos con valor anterior y nuevo; resultado de la prueba Cmd OK con fecha.

**Depende de / se cierra con:** F32

**Nota.** Cambiar la llamada para que coincida con el parámetro cambiaría el pickup o drop-off real: no hacerlo. La verificación de la depuración protege las líneas ;Params: en este punto su cambio es el esperado y se declara en tools/code_changes.json.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F22 — Movimientos del pedestal mezclan modo base y external TCP

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Ethos (Edgar) / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.dat`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.dat`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.dat`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** De los 22 movimientos enseñados en base 3 "NUT WELDER", 11 corren en modo base y 11 en external TCP; las tres presentaciones de soldadura (P19 en la app 1, P16 en las apps 2 y 3) están en modo base. Gestamp pide movimientos de pedestal interpolados alrededor del dado fijo (C04). Ningún movimiento de producción usa la herramienta 2 en R10 (el único era redrabbit.src, borrado).

**Qué hacer.** Decidir una regla de frame para el pedestal y, con BASE_DATA[3] medido (C05), re-enseñar los movimientos del pedestal de forma consistente.

**Criterio de cierre** (se verifica en el respaldo):

* La regla de frame del pedestal está anotada en la lista (qué movimientos de base 3 van en external TCP y cuáles en modo base; quién decidió y fecha).
* Cada FDAT con BASE_NO 3 usado por un movimiento tiene el IPO_FRAME que pide la regla.
* Si la regla usa external TCP, BASE_DATA[3] es el valor medido en sitio (C05) y todos los puntos de base 3 se re-enseñaron o verificaron en T1 después del cambio (lista de puntos).
* Prueba en T1 a velocidad reducida con pieza: las tres presentaciones llegan a su pose sin contacto; en el primer ciclo con soldadura CL_GunStrokePositionLPT con el gun cerrado queda en CL_GUN_WELD_MIN..MAX en cada tuerca. Anotar lectura por tuerca y fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F22) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Regla de frame decidida; valor de BASE_DATA[3] y método; puntos re-enseñados o verificados; lecturas del LPT por tuerca.

**Depende de / se cierra con:** C05, F32

**Nota.** Cambiar BASE_DATA[3] mueve físicamente los 22 puntos de base 3: no correr en automático sin verificarlos. Los TRIGGER ya no están dentro de folds (F32), así que un Touch Up no los borra. C04 se cierra con este punto y C05.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F23 — Posición del LPT armada con 3 bytes en otro orden que en R20

**Severidad:** Bajo · **Tipo:** Confirmar en sitio · **Responsable:** Puesta en marcha / Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/System/$config.dat`, `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** R10 arma CL_GunStrokePositionLPT = BYTE1*65536 + BYTE2*256 + BYTE3 (sps.sub): 24 bits, CL_LPT_BYTE0 sin usar, así que el desbordamiento de 32 bits de R20 no existe aquí. R20 arma el valor con los cuatro bytes en el orden BYTE1, BYTE0, BYTE3, BYTE2 con el mismo mapeo de bus. Una de las dos no es el formato del BTL6.

**Qué hacer.** Confirmar el formato de salida del BTL6 de este pedestal (manual Balluff o configuración del transductor). Con el gun abierto el valor debe leer unos 139800 (tabla del encabezado de CENTERLINE_WELD) y con el gun sobre la tuerca unos 70900.

**Criterio de cierre** (se verifica en el respaldo):

* Formato del BTL6 confirmado (documento y página, o configuración leída del transductor) y anotado en la lista.
* La fórmula de sps.sub corresponde a ese formato; si cambia, la lista trae CL_GunStrokePositionLPT leído antes y después con gun abierto y cerrado sobre tuerca, y las ventanas (CL_GUN_WELD_MIN/MAX, CL_GUN_OPEN_MIN) siguen siendo válidas.
* Si se pasa a componer 32 bits, el cálculo no puede desbordar INT (protección como en el F23 de R20).
* Comentarios según docs/CONVENTIONS.md; el ;CHECK: (F23) de sps.sub y la nota de $config.dat se quitan o se actualizan.

**Evidencia del programador.** Documento del formato; lecturas de CL_GunStrokePositionLPT con gun abierto y cerrado sobre tuerca.

**Nota.** Si el formato confirmado es el de R20, el punto se abre también allá. No tocar las ventanas sin medir.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F24 — Camino de retry de soldadura muerto: NUT_WELD_RETRY nunca es TRUE

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** NUT_WELD_RETRY nunca se ponía TRUE, así que las tres ramas GOTO RETRY_NUT1 de style1app1opt1..3 nunca corrían.

**Qué hacer.** Decisión A (como en R20): borrar las ramas, las etiquetas y la variable. Hecho en oficina (G17).

**Criterio de cierre** (se verifica en el respaldo):

* Decisión anotada: A (borrar), Ethos, 2026-10-04, por el punto 17 de Gestamp.
* En KRC/R1 no aparece NUT_WELD_RETRY ni RETRY_NUT1.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Un ciclo completo en automático con las 3 tuercas sin errores. Anotar fecha.

**Evidencia del programador.** Ciclo completo sin errores, con fecha.

**Nota.** Sin cambio de comportamiento: las ramas nunca corrían. Si algún día se diseña un retry, el disparo natural es el Retry del diálogo de F07 y necesita F14.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## F25 — Feed de respaldo en CENTERLINE_WELD: pulso de feed de duración cero

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Bajo · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** Si NUT_READY está en FALSE al entrar, CENTERLINE_WELD alimenta su propia tuerca con la pieza ya en la pose: avanza el QFP, pone $OUT[476] dopw1_StartFeed ON e inmediatamente OFF (la espera de $IN[481] dipw1_FeedComplt está comentada), espera WAIT SEC 1.5 y regresa el QFP. Ese pulso puede no llegar nunca al bus, y el programa sigue igual con o sin tuerca.

**Qué hacer.** Quitar el camino de alimentación local, o cambiarlo por una petición de preload con espera de NUT_READY. Entrar con NUT_READY en FALSE tiene que terminar en una falla visible o en una espera con timeout, nunca en un cierre de gun sin tuerca.

**Criterio de cierre** (se verifica en el respaldo):

* En centerline_weld.src no queda ninguna escritura a ON de $OUT[476] dopw1_StartFeed ni de $OUT[503] do503QFPAdvance: la alimentación queda solo en la secuencia de preload.
* Si NUT_READY es FALSE al entrar, CENTERLINE_WELD no cierra clamp ni gun sin un preload terminado: (a) se detiene con mensaje y $OUT[4] do004ProcessFault ON; o (b) pide un preload (solo si NUTCYCLE_ACTIVE es FALSE) y espera NUT_READY con timeout, y al vencer da mensaje y $OUT[4].
* Prueba en T1 sin pieza, con el robot fuera del pedestal y nadie en él: NUT_READY = FALSE por corrección de variable y CENTERLINE_WELD solo: con (a) se detiene con mensaje; con (b) pide o espera el preload y, con el preload impedido, da timeout con mensaje sin cerrar clamp ni gun. Anotar opción, fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F25) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Opción elegida, (a) o (b); resultado de la prueba en T1; fecha.

**Depende de / se cierra con:** F11, F14

**Nota.** No se acepta 'arreglarlo' alargando el pulso. Calvin (#19) propone reactivar la espera de $IN[481] dipw1_FeedComplt con timeout en el camino local; Ethos (Edgar, 2026-10-04) decidió para R10 lo mismo que para R20: se mantiene el criterio de este punto, quitar el camino local o convertirlo en petición de preload. Si se elige (b), confirmar antes en celda que un preload (QFP, pines, blow-off) puede correr con la pieza en la pose de soldadura; si no puede, la opción es (a). La etiqueta NUT_READY: ya no existe: G11 cambió el salto por IF NOT NUT_READY. F01, F11, F13 y F14 tocan el mismo módulo y las mismas variables: coordinar.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-04 — Decisión: Se mantiene el criterio de F25 frente a la propuesta de Calvin #19, igual que en R20 (decisión de Edgar, 2026-10-04).

---

## F26 — Timers $TIMER[10..15] de PRELOAD y CENTERLINE_WELD sin constantes con nombre

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** PRELOAD usa $TIMER[10..13] y CENTERLINE_WELD $TIMER[14..15], con el índice escrito como número. No chocan con código activo del proveedor. La depuración dejó comentarios de propiedad, pero el código sigue con índices literales. Al terminar un preload se detienen $TIMER[10..12] pero no $TIMER[13].

**Qué hacer.** Declarar en $config.dat un nombre por cada índice de timer usado, con comentario de programa dueño y uso; usar esos nombres en PRELOAD y CENTERLINE_WELD. Detener $TIMER[13] al terminar el preload.

**Criterio de cierre** (se verifica en el respaldo):

* $config.dat declara un nombre para cada índice de $TIMER que usan PRELOAD y CENTERLINE_WELD, con comentario de dueño y uso; cada nombre declarado se usa.
* En PRELOAD.src y centerline_weld.src no queda ningún $TIMER[n] ni $TIMER_STOP[n] con índice numérico.
* Fuera de PRELOAD y CENTERLINE_WELD ningún módulo que se ejecute usa esos índices; tampoco son timers del proveedor (torque monitoring 7, 8 y 18; NutWeld 41 y 42; AutomationCore 55).
* Al completar un preload, PRELOAD detiene $TIMER[13] igual que los de feed, advance y return.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F26) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Confirmación de que el proyecto WorkVisual se actualizó desde el controlador después del cambio en $config.dat.

**Nota.** Si F07 o F13 cambian la forma de temporizar, ajustar la asignación. Antes de cualquier deploy de WorkVisual, cargar el proyecto desde el controlador.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-07 — Nota (F52): PRELOAD ya no usa $TIMER[12]; la medición de tiempo ciclo usa $TIMER[16]. Dueños anotados en $config.dat.

---

## F27 — Confirmar en celda funciones de comentarios corregidos: blow-off, pines, programa Bosch

**Severidad:** Bajo · **Tipo:** Confirmar en sitio · **Responsable:** Puesta en marcha / Gestamp controles · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/PRELOAD.src`

**Qué está mal.** La depuración corrigió comentarios que contradecían al código: UPPER PIN EXTEND sobre el retract, LOWER PIN RETURN y CL_LowerPinRetreated sobre el advance, SCHEDULE 7 sobre el programa 2, QFP ADV sobre la verificación de QFP regresado, y los comentarios en español del pedestal. Ahora describen el código, pero nadie ha confirmado en la celda qué hace físicamente cada salida. Quedan cinco ;CHECK: (F27): tres en centerline_weld.src y dos en PRELOAD.src.

**Qué hacer.** Confirmar en la celda, con los planos del pedestal CenterLine o forzando salidas en T1 (sin pieza, robot fuera del pedestal, nadie en él): (1) qué acciona $OUT[494] dopw1_BlowOff, que se conmuta durante el feed y durante el intensify; (2) la asignación de válvulas de los pines: superior $OUT[498]/$OUT[499], inferior $OUT[495] dopw1_AdvancePin y $OUT[496] dopw1_ReturnPin; (3) que el programa 2 (gdopw1_SpotNumber = CL_WELD_PROGRAM) es el schedule Bosch previsto.

**Criterio de cierre** (se verifica en el respaldo):

* En la lista, para cada uno de los tres puntos: resultado, cómo se confirmó, quién y fecha.
* Los cinco ;CHECK: que citan (F27) se quitaron o se cambiaron por un ;NOTE: con el hecho confirmado.
* Ningún punto se cierra con una contradicción pendiente: si la confirmación contradijo al código, el respaldo trae la corrección o la lista remite al punto nuevo.
* Comentarios según docs/CONVENTIONS.md; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Para cada punto: lo observado, hoja del plano o foto, y foto de la lista de programas del timer Bosch con el programa 2. Fecha y quién confirmó.

**Nota.** El programa Bosch lo confirma quien administra el timer (Gestamp). Se puede hacer en la misma visita que F34 y F44. Con lo confirmado se actualiza docs/IO_MAP.md.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F28 — Sensor de tuerca leído al llegar al punto; el dwell iba después de la lectura

**Severidad:** Bajo · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

**Qué está mal.** Cada revisión de tuerca hacía LIN (paro exacto, P28, P32, P36), leía $IN[227] y después WAIT SEC 0.2: el asentamiento quedaba después de la muestra.

**Qué hacer.** Hecho en oficina (G13): cada revisión es WAIT SEC 0.2 y luego PARTPRESENTn = di227NutPresent1; la lectura se hace con el robot parado y una tuerca faltante escribe FALSE (parte de F03).

**Criterio de cierre** (se verifica en el respaldo):

* En style1app2opt1, en los tres bloques NUT CHECK, PARTPRESENTn se asigna después de WAIT SEC 0.2.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en automático, override 100 %, fuera de dry cycle y con option 1: ciclos consecutivos con pieza buena sin ningún rechazo por la revisión de tuercas; un ciclo con pieza red rabbit (option 12) deja PARTPRESENT1..3 en FALSE en el display de variables antes del drop. Anotar fecha, número de ciclos y resultado.

**Evidencia del programador.** Fecha, override, número de ciclos y estado de PARTPRESENT1..3 en el ciclo red rabbit.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## F29 — Faro KL50L2: lógica muerta y un bit sin mapear

**Severidad:** Bajo · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/System/$config.dat`, `C/KRC/Roboter/Config/User/Common/KRC_IO.xml`

**Qué está mal.** sps.sub maneja el KL50L2 a partir de $OUT[478]/$OUT[477], que solo escribe NutWeld_Bkg, deshabilitado: el bloque nunca actúa. Rojo pone $OUT[3008] y $OUT[3024]; verde pone $OUT[3001] y apaga $OUT[3024]; $OUT[3008] y $OUT[3001] nunca se apagan. $OUT[3001] no está mapeado (KRC_IO.xml mapea $OUT[3000], [3008], [3016], [3024]) y R20 usa $OUT[3000] y $OUT[3016] para el mismo faro.

**Qué hacer.** Confirmar el mapa de bits del KL50L2; (a) manejar el faro directo desde $IN[480] dipw1_HopperLowLevel con encendido y apagado explícitos, usando bits mapeados con nombre; o (b) quitar el bloque.

**Criterio de cierre** (se verifica en el respaldo):

* Mapa de bits del KL50L2 de este pedestal confirmado (qué bit es cada color) y anotado.
* Con (a): la polaridad de $IN[480] confirmada en celda; el bloque lee $IN[480], no $OUT[477]/$OUT[478], y en cada ciclo deja cada bit usado en un estado definido; solo usa bits mapeados en KRC_IO.xml. Con (b): el bloque ya no existe y ningún módulo escribe esos bits.
* Con (a): prueba en celda con la tolva en nivel bajo y en nivel OK; el faro cambia con el nivel. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F29) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Opción elegida; estado de $IN[480] con tolva baja y llena; estado del faro; fecha.

**Nota.** Hecho en oficina (G12): los tres bits tienen nombre (CL_BeaconBit3001, CL_BeaconBit3008, CL_BeaconBit3024); la lógica no cambió. Los nombres se ajustan cuando se confirme el mapa. La opción (b) deja el faro siempre apagado: avisar a Gestamp.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F30 — Style1Opt1 sin GOTO: un camino IF/ELSE por ciclo

**Severidad:** Bajo · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** Style1Opt1 usaba GOTO para terminar el ciclo después de un RejectGE4 y para no correr la estación 2 después de un ciclo de estación 1 (las tres etiquetas eran una sola salida). Gestamp no permite GOTO (G11).

**Qué hacer.** Hecho en oficina: la estación se lee una vez en nPickStation (1, 2 o 0) y el resto es un IF/ELSE: después de cada RejectGE4() no corre nada más; la estación 1 nunca corre la 2; todos los caminos terminan en el borrado de PARTPRESENT1..3. Con ninguna estación sigue siendo un ciclo vacío (F06).

**Criterio de cierre** (se verifica en el respaldo):

* En style1opt1.src no hay GOTO ni etiquetas y se conservan las tres propiedades: (1) después de RejectGE4() no corren ni la cámara ni el drop; (2) un ciclo de estación 1 no corre la estación 2; (3) todos los caminos pasan por el borrado de PARTPRESENT1..3.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en celda: un ciclo bueno de estación 1, uno de estación 2, un rechazo por nut check y uno por cámara (si se puede provocar). Anotar fecha y resultado.

**Evidencia del programador.** Fecha y resultado de cada prueba.

**Nota.** Si F03 o F06 cambian style1opt1.src, se vuelven a revisar las tres propiedades.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## F31 — Forms GripperTech: parámetros ocultos de otro gripper; drop red rabbit con el gripper 3

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`

**Qué está mal.** R10 usa forms GripperTech en picks, drops y reject; solo el gripper 1 está activo en grp_data.dat ($OUT[249]/[250], $IN[257]/[258]). En los tres picks y en el drop al conveyor los forms SET traían setgripper=4;setstate=2 mientras el código llama GRPg_SetStateAndCheck(1, 1 o 2, ...): abrir y confirmar uno de esos forms regeneraba la llamada para el gripper 4 ($OUT[251]/[252], $IN[259]/[260], en el bus), el gripper 1 ya no se movía y el check daba timeout (3 s). Cada SET con check iba seguido de un GRPg_Check redundante. El drop red rabbit escribe $OUT[249]/[250] a mano y suelta con el gripper 3, que comparte la E/S del gripper 1 (F19).

**Qué hacer.** Hecho en oficina (G10): parámetros ocultos de los forms SET de picks y drop al conveyor corregidos a setgripper=1 con el estado de la llamada; GRPg_Check redundantes quitados. Falta: reemplazar las salidas escritas a mano y el form del gripper 3 del drop red rabbit por forms del gripper 1 (con F19) y probar en celda.

**Criterio de cierre** (se verifica en el respaldo):

* En los módulos listados cada form Gripper SET/CHECK tiene en su línea ;Params el mismo gripper y estado que su llamada (hecho en oficina para picks y drop al conveyor) y no queda GRPg_Check que repita el check del SET anterior.
* style1drop1opt2AutoRR no escribe $OUT[249]/$OUT[250] a mano y no usa forms del gripper 3; ningún módulo de producción usa los grippers 2-4.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en el smartPAD: abrir y confirmar (Cmd OK) un form SET de cada módulo; en el respaldo siguiente las llamadas no cambiaron. En T1 sin pieza: con un switch del gripper 1 desconectado el check da su error (estrategia 1) en pick, drop y reject. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F31) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Lista de forms revisados; resultado de la prueba Cmd OK y de la prueba con switch desconectado; fecha.

**Depende de / se cierra con:** F33, F19

**Nota.** Parte de oficina hecha (tools/code_changes.json, G10, G13, G14). No guardar la configuración de GripperTech en el HMI mientras F33 esté abierto.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F32 — TRIGGERs y resets escritos a mano dentro de folds de inline form

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

**Qué está mal.** Los TRIGGER de NUT_STAR (picks, P12 / P10) y de Request_next_nut() (final de las apps 1 y 2, en el fold P0) estaban escritos a mano dentro de folds de inline form de movimiento; el drop red rabbit tenía los resets de banderas dentro del form DropOff[2] Reset. Un Touch Up o reabrir el form los borraba: la tuerca 1 se quedaba sin preload (NUT_READY con un TRUE viejo, F14) o la tuerca 2/3 esperaba NEXT_NUT_READY para siempre.

**Qué hacer.** Hecho en oficina (G20): cada TRIGGER quedó justo antes de su fold de movimiento (posición del form SYN OUT de KUKA: mismo movimiento, mismo punto de disparo); los resets del red rabbit van después del fold DropOff[2] Reset.

**Criterio de cierre** (se verifica en el respaldo):

* Los folds PTP P12 (style1pick1opt1, style1pick1opt1AutoRR), P10 (style1pick1opt2) y P0 (style1app1opt1 y opt2) contienen solo las líneas que genera el form; los TRIGGER están fuera, inmediatamente antes.
* El fold DropOff[2] Reset de style1drop1opt2AutoRR contiene solo su ;Params y AC_DropOff (2,True); los resets se ejecutan después.
* Los encabezados ;FOLD ... ;%{PE} de los folds tocados son idénticos a los del respaldo recibido: no se reabrió ningún form.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Prueba en T1 o en automático con override reducido, fuera de dry cycle: en un ciclo completo NUT_READY y NEXT_NUT_READY pasan a FALSE y vuelven a TRUE una vez por tuerca (3 preloads por pieza). Un ciclo red rabbit deja $OUT[141], $OUT[142] y PARTPRESENT1..3 en FALSE. Anotar fecha.

**Evidencia del programador.** Resultado de la prueba de ciclo; fecha.

**Nota.** Gestamp (punto 20) describe exactamente esto para xP0. Una selección de bloque sobre el fold salta el TRIGGER (hay que seleccionar la línea del TRIGGER): F14, F38.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## F33 — GripperConfig.xml del HMI desincronizado con grp_data.dat

**Severidad:** Medio · **Tipo:** WorkVisual / configuración · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `C/KRC/User/TP/Gripper_SpotTech/GripperConfig.xml`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`

**Qué está mal.** GripperConfig.xml (plug-in del HMI, idéntico al de R20) tiene todos los grippers inactivos con E/S dummy, mientras grp_data.dat tiene el gripper 1 activo en $OUT[249..250] / $IN[257..258] (y el gripper 3 inactivo en la misma E/S). Si alguien guarda la configuración de GripperTech en el smartHMI, grp_data.dat se regenera con la E/S dummy: cada GRPg_SetStateAndCheck(1, ...) mandaría y revisaría los bits equivocados.

**Qué hacer.** Mientras no se re-sincronice, nadie guarda la configuración de GripperTech en el HMI. Re-sincronizar el XML con grp_data.dat (gripper 1 activo, mismas salidas, entradas y estados) y comprobar que un guardado desde el HMI regenera un grp_data.dat equivalente.

**Criterio de cierre** (se verifica en el respaldo):

* Control en cada respaldo mientras el punto esté abierto: grp_data.dat conserva GRPg_Grp[1] con Act TRUE, salidas 249/250 y entradas 257/258 (nadie guardó desde el HMI).
* Para cerrar, el GripperConfig.xml del respaldo tiene el gripper 1 activo con salidas 249/250 y entradas 257/258 sin GhostMode, y los valores por estado coinciden con grp_data.dat.
* Guardado de prueba desde el HMI hecho entre dos respaldos: GRPg_Grp, GRPg_GrpPar y GRPg_State del gripper 1 no cambian, y el drop red rabbit sigue soltando (o F19/F31 ya lo pasaron al gripper 1).

**Evidencia del programador.** Cómo se re-sincronizó y fecha; foto de la configuración de GripperTech; en qué respaldo se hizo el guardado de prueba.

**Depende de / se cierra con:** F31

**Nota.** Editar grp_data.dat a mano no cierra el punto. Un deploy de WorkVisual también puede regenerarlo. Mientras el drop red rabbit use el gripper 3 (F19), la re-sincronización debe conservar su E/S o el drop dejará de soltar.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F34 — CENTERLINE_HOME: polaridad de $OUT[473] y falta el reset del Bosch

**Severidad:** Bajo · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** CENTERLINE_HOME pone $OUT[473] dopw1_Nut1Intensify_Home en OFF, mientras CENTERLINE_WELD lo deja en ON en reposo. CENTERLINE_HOME no resetea weld start ($OUT[483]), contactor enable ($OUT[481]), weld on ($OUT[482]) ni el número de programa ($OUT[486..493]). Su water-off lo sobrescribe sps.sub (F09) y PRELOAD puede reescribir sus salidas (F11).

**Qué hacer.** Confirmar en la celda qué hace $OUT[473] en ON y su estado de reposo, y dejar el mismo valor en CENTERLINE_HOME y CENTERLINE_WELD. Agregar a CENTERLINE_HOME el reset del Bosch (se puede hacer ya).

**Criterio de cierre** (se verifica en el respaldo):

* En la lista: función física de $OUT[473] y su estado de reposo, cómo se confirmó y fecha.
* CENTERLINE_HOME y CENTERLINE_WELD escriben el mismo valor de reposo para $OUT[473].
* CENTERLINE_HOME pone $OUT[483] dopw1_WeldInit OFF, $OUT[481] dopw1_WeldContactEnable OFF, $OUT[482] dopw1_WeldOnExternal OFF y gdopw1_SpotNumber = 0.
* Prueba en T1 sin pieza, robot fuera del pedestal y nadie en él: poner $OUT[481] y $OUT[482] en ON y gdopw1_SpotNumber = 2 desde el display, correr CENTERLINE_HOME y verificar los resets y $OUT[473] en el reposo confirmado. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F34) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Función de $OUT[473] observada, estado de reposo decidido y resultado de la prueba; fecha.

**Nota.** Para la prueba no forzar $OUT[483]. Si F10 crea una rutina de estado seguro, CENTERLINE_HOME puede llamarla. Se puede confirmar en la misma visita que F27.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F35 — El mastering reference deja $OUT[930] en ON para siempre

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/masref_user.src`, `KRC/R1/System/masref_main.src`

**Qué está mal.** MASREFSTARTG1 pone do930MasterRefInProcess en TRUE y MASREFBACKG1 lo pone en TRUE otra vez al final, donde la línea vieja comentada ponía do828 en FALSE. Nada más escribe $OUT[930]: después de la primera prueba de mastering reference queda en ON para siempre. La rutina de request to enter de AutomationCore (edición del integrador) niega la entrada mientras está en ON, así que si se reactiva el background (F12) la request to enter queda bloqueada. $OUT[930] cae además en el bit del PLC de $OUT[111] (F18). El camino cierra el gripper 1 antes de ir al switch de referencia.

**Qué hacer.** Poner do930MasterRefInProcess en FALSE al final de MASREFBACKG1, después del último movimiento de regreso.

**Criterio de cierre** (se verifica en el respaldo):

* En masref_user.src, MASREFBACKG1 termina con do930MasterRefInProcess = FALSE después del último movimiento; MASREFSTARTG1 es el único TRUE.
* Prueba en T1 (sin pieza en el gripper): correr el mastering reference; $OUT[930] está en ON durante la prueba y en OFF al terminar; el PLC ve el tag de $OUT[111] en OFF al final (F18). Anotar fecha.
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F35) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fecha y estado de $OUT[930] antes, durante y después de la prueba.

**Depende de / se cierra con:** F18

**Nota.** Requisito antes de reactivar AutomationCore_Bkg (F12). masref_user no es módulo del ciclo de producción.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Severidad subida a Alto: Con AutomationCore_BKG activo (F49), $OUT[930] pegado en ON impide conceder el Request to Enter: $OUT[145] doCriticalWZ queda en TRUE y AC_PointArrival ya no detiene el robot cuando el operador pide entrar. Corregir F35 antes de producción.
* 2026-10-05 — Severidad regresa a Medio: Con el background apagado en la versión integrada, $OUT[930] pegado ya no impide el Request to Enter. Sigue pendiente apagar $OUT[930] al final de la referencia de masterización.

---

## F36 — $IN[227] declarado con dos nombres (NUT_PRESENT1, di227SensorCamera)

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot (prueba en celda) · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`

**Qué está mal.** $IN[227] estaba declarado como NUT_PRESENT1 en $config.dat y como di227SensorCamera en automationcoreroutines.dat: es el sensor de tuercas, no la cámara.

**Qué hacer.** Hecho en oficina (G15): di227SensorCamera renombrado di227NutPresent1 y la declaración NUT_PRESENT1 de $config.dat borrada; el nut check y los comentarios usan di227NutPresent1.

**Criterio de cierre** (se verifica en el respaldo):

* En todo KRC/ del respaldo, $IN[227] tiene una sola declaración SIGNAL: di227NutPresent1.
* NUT_PRESENT1 y di227SensorCamera ya no aparecen en código ni declaraciones de KRC/.
* La edición en automationcoreroutines.dat aparece en la lista de ediciones del integrador en archivos del proveedor (C28).
* Respaldo completo (Archive → All) después de cargar en el robot la versión de oficina (zip de tools/build_archive.py): los módulos coinciden con el zip entregado (la auditoría lo compara), los módulos borrados o movidos ya no están en el controlador (un restore no borra archivos) y el proyecto WorkVisual se actualizó desde el controlador antes de cualquier deploy.
* El programa carga sin errores de compilación (captura del navegador del smartPAD sin módulos en rojo). Un ciclo con option 1 lee las 3 tuercas (PARTPRESENT1..3 en TRUE en el display de variables). Anotar fecha.

**Evidencia del programador.** Captura del navegador sin errores y fecha del ciclo.

**Depende de / se cierra con:** C28

**Nota.** Cambia $config.dat: un deploy desde el proyecto WorkVisual viejo restauraría la declaración NUT_PRESENT1.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - no cargado: Respaldo bmw_03_10_r1 (2026-10-05): la versión de oficina no está cargada; el robot tiene el programa original (29 archivos idénticos al respaldo de partida, 16 editados encima del original). Sin prueba posible.
* 2026-10-05 — Integrado - por probar: Sigue en la versión integrada (658424_R10_2026-10-05_0819.zip, armada sobre el respaldo del programador). Cargarla y hacer la prueba de este punto.

---

## F37 — Presión de intensificado no confirmada antes de weld start: no aplica en R10

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** No aplica

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** En R20 la espera de presión de intensificado está desactivada (Calvin #1). R10 conserva WAIT FOR dipw1_IntensfPresOk ($IN[479]) en CENTERLINE_WELD antes de weld start, como dice Calvin.

**Qué hacer.** Nada en este punto. La espera no tiene timeout (F15) y la presión que recibe de verdad el regulador es F44.

**Criterio de cierre** (se verifica en el respaldo):

* Se reabre si la espera de $IN[479] dipw1_IntensfPresOk de CENTERLINE_WELD se desactiva o se quita.

**Depende de / se cierra con:** F15, F44

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424: el punto 1 de Calvin (20R1) no aplica en R10.

---

## F38 — Estado de la tuerca no se reinicializa al arrancar, en reset ni después de un reinicio

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`

**Qué está mal.** El handshake de la tuerca vive en globales persistentes de $config.dat (NUT_READY declarado TRUE, NUT_START, NUTCYCLE_ACTIVE, NUT_PRELOAD_STEP, STEP0/10/20DONE, STEP10_ADV_STARTED, NEXT_NUT_READY / NEXT_NUT_REQUEST). Nada las inicializa al arrancar el programa, al cancelar o resetear, ni al arrancar el controlador; después de un reinicio a mitad de un preload, PRELOAD retoma el paso guardado; después de una selección de bloque los TRIGGER del handshake se saltan.

**Qué hacer.** Una rutina de inicialización llamada desde el USER INIT de sps.sub, desde cell.src antes del primer ciclo y desde la rutina de estado seguro de F10, que derive NUT_READY de la E/S real. Un preload interrumpido nunca termina en tuerca lista.

**Criterio de cierre** (se verifica en el respaldo):

* Existe una rutina de inicialización del estado de la tuerca, llamada desde el USER INIT de sps.sub y desde cell.src antes del primer ciclo (y desde la rutina de F10), que deja NUTCYCLE_ACTIVE = FALSE, NUT_PRELOAD_STEP = 0, STEP*DONE y STEP10_ADV_STARTED en FALSE, NUT_START y NEXT_NUT_REQUEST en FALSE, y NUT_READY / NEXT_NUT_READY a partir de la E/S real.
* La seguridad del ciclo ya no depende del valor inicial declarado en $config.dat.
* Prueba en celda: (a) cortar el ciclo a mitad de un preload y reiniciar el controlador: PRELOAD no retoma el paso y las banderas reflejan el pin; (b) reset del programa con tuerca precargada y sin ella: el siguiente ciclo no suelda sin tuerca ni alimenta una segunda. Anotar fecha y resultado.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F38) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Dónde se llama la rutina y resultado de las dos pruebas.

**Depende de / se cierra con:** F14, F10, F11, F13

**Nota.** Gestamp (punto 19) pide lo mismo; G19 se cierra con este punto y F14. F14 cubre el consumo de NUT_READY; F10 el estado seguro de las salidas.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #11).

---

## F39 — Supervisión de par en cero; chequeo de datos de carga solo avisa; carga tecleada

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Configuración + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/STEU/Mada/$custom.dat`, `KRC/R1/System/$config.dat`, `KRC/R1/System/bas.src`

**Qué está mal.** $TORQMON_DEF[1..12] y $TORQMON_COM_DEF[1..12] están en 0 en KRC/STEU/Mada/$custom.dat (líneas 80-104). $LDC_CONFIG[1] = {UNDERLOAD #WARNONLY, OVERLOAD #WARNONLY}: el chequeo de datos de carga solo avisa. LOAD_DATA[1] = M 210, CM {270, 0, 240}, J {105, 105, 105}: redondos, tecleados (Gestamp punto 3). Todos los movimientos de producción corren con TQ_STATE FALSE.

**Qué hacer.** Con los datos de carga determinados (G03/C08), definir $TORQMON_DEF / $TORQMON_COM_DEF según el manual de KUKA (o dejar por escrito por qué se quedan) y decidir la reacción del chequeo de datos de carga de la herramienta 1.

**Criterio de cierre** (se verifica en el respaldo):

* En el respaldo $TORQMON_DEF y $TORQMON_COM_DEF tienen valores definidos, o la lista trae la justificación escrita (referencia al manual) de dejarlos en 0.
* $LDC_CONFIG[1] tiene la reacción acordada con Gestamp (p. ej. OVERLOAD #STOPROBOT), anotada.
* Prueba en celda después de G03: un ciclo completo en automático sin falsos paros por par ni por carga. Anotar fecha y valores.

**Evidencia del programador.** Valores puestos, referencia del manual y fecha de la prueba.

**Depende de / se cierra con:** G03, C08, C09

**Nota.** Es machine data: hacerlo en la misma visita que C09. Calvin describe R10 como robot de pistola; es de manejo: los hechos se sostienen.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #16).

---

## F40 — Drops y reject abren el gripper sin confirmar pieza; el drop red rabbit se mueve antes de gripper vacío

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** G14 corrigió el orden al inicio de los picks. El drop al conveyor y RejectGE4 abren el gripper sin confirmar antes $IN[253] di253PartPresent1 y $IN[254] di254PartPresent2 ON: una pieza perdida en el camino se "entrega" y $OUT[18] se apaga como si nada. El drop red rabbit se mueve (LIN P23) antes de esperar gripper vacío.

**Qué hacer.** Espera supervisada de pieza presente antes de abrir en los dos drops y en RejectGE4; espera de gripper vacío antes de alejarse en el drop red rabbit.

**Criterio de cierre** (se verifica en el respaldo):

* En style1drop1opt1, style1drop1opt2AutoRR y RejectGE4 hay una espera de $IN[253] y $IN[254] ON antes del form que abre el gripper (fuera de dry cycle, como las demás esperas de pieza).
* En style1drop1opt2AutoRR la espera de gripper vacío está antes de LIN P23.
* Prueba en T1: quitar la pieza del gripper antes de llegar al drop: el robot se detiene antes de abrir con mensaje. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F40) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fecha y resultado.

**Depende de / se cierra con:** G14, G10, F31, F19

**Nota.** Si F19 reescribe el drop red rabbit, el orden de este punto va incluido.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #25).

---

## F41 — Tiempos de PRELOAD, límite de flujo de agua y esperas fijas sin constantes

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Bajo · **Tipo:** Código · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** G16 llevó a constantes la ventana del gun, las presiones y los tiempos del chequeo de gun cerrado. Quedan números: los tiempos de PRELOAD (2000, 500, 800 y 800 ms), el límite de flujo SV0500_FLOW > 1230 de sps.sub y los WAIT SEC fijos de CENTERLINE_HOME y CENTERLINE_WELD.

**Qué hacer.** Declarar constantes con nombre en $config.dat (mismos valores) y usarlas en el código; registrar los nombres en tools/renames.json para que check_equivalence muestre que el valor no cambió.

**Criterio de cierre** (se verifica en el respaldo):

* En PRELOAD.src, sps.sub, CENTERLINE_HOME.src y centerline_weld.src no quedan esos números en líneas ejecutables: usan constantes de $config.dat con los mismos valores.
* Un ciclo completo en automático sin cambio de tiempo de ciclo. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F41) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Lista de constantes y fecha del ciclo.

**Depende de / se cierra con:** G16, F26, F09

**Nota.** Si F13 o F09 cambian esos valores, se declaran directamente con el valor nuevo.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin Std 5).

---

## F42 — Envolventes de trabajo por software apagadas

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Bajo · **Tipo:** Configuración / decisión · **Responsable:** Programador robot / Seguridad / Gestamp · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Mada/$machine.dat`, `KRC/STEU/Mada/$custom.dat`, `C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml`

**Qué está mal.** $AXWORKSPACE[1..8] y $CYLWORKSPACE[1..8] están en #OFF (KRC/R1/Mada/$machine.dat, líneas 378-385 y 403-410). $WORKSPACE[1] y [2] (KRC/STEU/Mada/$custom.dat) están en #OUTSIDE: solo señalan, no detienen el robot. SafeOperation tiene un espacio de monitoreo "Nest Workspace" (última edición 2026-09-13). No está documentado qué cubren los espacios de seguridad.

**Qué hacer.** Decidir con Gestamp si hacen falta envolventes de software con paro además de SafeOperation; si no, dejar por escrito, con captura del smartHMI, qué cubren el Cell area y los espacios de seguridad.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión anotada en la lista (quién y fecha).
* Si se activan: valores en el respaldo y prueba en T1 de que el robot se detiene al entrar a la zona. Si no: captura de la configuración de SafeOperation (Cell area y espacios) adjunta.
* $WORKSPACE[1] y [2]: uso documentado (qué salida dan y quién la lee) o en #OFF.

**Evidencia del programador.** Decisión y capturas.

**Depende de / se cierra con:** G02

**Nota.** Conviene hacerlo en la misma sesión de seguridad que G02.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #30).

---

## F43 — Cambio de electrodo: reset de stepper por pulso de 0.1 s y handshake que no cierra

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Medio · **Tipo:** Decisión + código · **Responsable:** Programador robot / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/cell.src`

**Qué está mal.** En gunelectrodechange.src el reset del stepper es PULSE(dopw1_StepperReset,TRUE,0.1) ($OUT[485]) sin revisar $IN[487] dipw1_EndOfStepper; $OUT[92] do092RobotCapChg1Cmplt solo se apaga si $OUT[111] ya está en OFF, y $OUT[91] do091RobotReadyCapChange se apaga sin esperar a que el PLC baje $IN[92]. Las esperas no tienen timeout. cell.src llama GunElectrodeChange cuando $OUT[111..113] están en ON, pero esas salidas solo las escribe el background deshabilitado (F12): tal como está, el cambio de electrodo nunca corre. Calvin cita electrodechange.src, una copia vieja que nada llamaba (borrada en la depuración); la rutina viva tiene el mismo patrón.

**Qué hacer.** Decidir con Gestamp cómo se pide el cambio (bit del PLC o contador); confirmar el reset del stepper con $IN[487]; cerrar el handshake por niveles; supervisar las esperas; quitar de la rutina lo de pistolas 2 y 3.

**Criterio de cierre** (se verifica en el respaldo):

* Forma de pedir el cambio de electrodo acordada con Gestamp por escrito, y cell.src llama la rutina con esa petición, fuera de ciclo.
* El reset del stepper se confirma con $IN[487] (espera supervisada) en lugar de solo un pulso de 0.1 s.
* do092 y do091 se apagan siempre al terminar, después de que el PLC bajó su petición; ninguna salida del handshake queda en ON.
* Prueba en celda: petición, cambio, confirmación, reset de stepper confirmado y regreso a home. Anotar fecha.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F43) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Señal de petición acordada y resultado de la prueba.

**Depende de / se cierra con:** F12, F15, C20

**Nota.** Gestamp (punto 6) pide lo mismo; G06 se cierra con este punto.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #29).
* 2026-10-05 — Auditoría - riesgo nuevo: Con AutomationCore_BKG activo, do111Gun1ElectrodeChange sigue a dipw1_EndofStepper: cell.src ya llama GunElectrodeChange cuando el stepper llega al final. El camino que F43 describe como nunca ejecutado ahora corre: probarlo antes de producción.
* 2026-10-05 — Integrado - riesgo: En la versión integrada GunElectrodeChange se ejecuta al final del stepper. Probar antes de producción.
* 2026-10-05 — Riesgo activo: Con el background activo, el cambio de electrodo corre al final del stepper y espera $IN[92] del PLC en un diálogo; nunca se ha probado. Además $OUT[111] comparte bit del adaptador con $OUT[930] (F18).

---

## F44 — Palabra de presión del gun escrita en dos órdenes de bytes (405/1820 contra 39425)

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Puesta en marcha / Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/Program/Centerline/centerline_weld.src`, `C/KRC/Roboter/Config/User/Common/KRC_IO.xml`

**Qué está mal.** CL_GunPressureCmd ($OUT[506..521]) está mapeado en KRC_IO.xml igual que en R20: el regulador recibe la palabra con los bytes intercambiados. En R20 todos los valores se escriben intercambiados (0.30 MPa = 1365 se escribe 21765). R10 escribe 405 (general, CL_GUN_PRESS_BASE) y 1820 (intensify, CL_GUN_PRESS_WELD, "0.40 MPa" en la tabla) sin intercambiar, y 39425 (= 0.09 MPa intercambiado, CL_GUN_PRESS_REST) al final de cada soldadura. Si el regulador de R10 no está configurado distinto, el comando general le llega como 38145 y el de intensify como 7175, fuera de 0..4095; si no intercambia, el que queda fuera de rango es 39425. Uno de los dos juegos está mal, y el gun reposa con 39425 entre soldaduras. $IN[479] se cumple en producción, así que la presión de soldadura está al menos arriba del ajuste del presostato.

**Qué hacer.** Leer en celda el display del ITV (o su salida de monitor) en reposo, con el gun cerrado antes del intensify y durante el intensify; comparar con la configuración del regulador (orden de bytes, rango de 12 bits). Escribir los tres valores en el orden que espera el regulador, como constantes (ya existen, G16).

**Criterio de cierre** (se verifica en el respaldo):

* Lecturas del ITV en reposo, con gun cerrado antes del intensify y durante el intensify, con fecha, y la configuración del regulador (orden de bytes y rango) anotadas en la lista.
* CL_GUN_PRESS_BASE, CL_GUN_PRESS_WELD y CL_GUN_PRESS_REST en $config.dat están en el mismo orden de bytes, el que confirma la lectura, y su comentario da la presión en MPa; la presión de soldadura sigue siendo la que Gestamp aprueba por escrito.
* La tabla de presiones del encabezado de CENTERLINE_WELD y los ;CHECK: (F44) se actualizan.
* Prueba en celda: un ciclo completo; el ITV muestra la presión esperada en cada fase y $IN[479] se cumple en el intensify. Anotar fecha y lecturas.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F44) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Lecturas del ITV antes y después del cambio, configuración del regulador y aprobación de Gestamp de la presión de soldadura.

**Depende de / se cierra con:** G16

**Nota.** Cambiar los valores cambia la presión real de soldadura de un proceso que ya produce: coordinar con Gestamp (proceso) antes de cargar. F08 y F10 usan la presión base que salga de aquí. Se puede hacer en la misma visita que F27.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F45 — Rutinas de clamps: grippers 2-4 deshabilitados, solo existe el gripper 1

**Origen:** Revisión Ethos (2026-10-04).

**Severidad:** Bajo · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** Cerrado - depuración

**Módulos:** `KRC/R1/Program/Utilities/closeandcheckallclamps.src`, `KRC/R1/Program/Utilities/openandcheckallclamps.src`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`

**Qué está mal.** CloseAndCheckAllClamps / OpenAndCheckAllClamps (solo las llama el mastering reference) tenían comentados el set y el check de los grippers 2-4. Los grippers 2-4 están inactivos en grp_data.dat: el 3 duplica la E/S del gripper 1, el 4 apunta a $OUT[251]/[252], $IN[259]/[260] (sin función en el EOAT de R10) y las entradas del 2 ($IN[269..272]) no están en el bus. Reactivarlos no agregaría nada.

**Qué hacer.** Hecho en la depuración: se quitaron los folds deshabilitados (solo líneas de comentario) y se documentó que las rutinas manejan solo el gripper 1. Sin cambio de comportamiento.

**Criterio de cierre** (se verifica en el respaldo):

* Las rutinas siguen manejando solo el gripper 1 y su comentario lo dice (verificación de regresión en cada respaldo).
* Se reabre si el EOAT de R10 recibe un gripper 2-4 con función real.

**Historial:**

* 2026-10-04 — Alta (Calvin): Revisión Ethos del respaldo 658424; el punto sale de la lista de Calvin (Calvin #23).

---

## F46 — EndOfCycle del proveedor editado: Work Complete nunca se manda al PLC

**Severidad:** Medio · **Tipo:** Decisión Gestamp · **Responsable:** Gestamp controles / Ethos (Edgar) · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/cell.src`

**Qué está mal.** La rutina del proveedor EndOfCycle (automationcoreroutines.src) se editó en este robot (;======SL====): do015WorkComplete = TRUE, la espera de di015WorkCompleteAckn y do005RobotInCycle = FALSE están comentados. Work Complete nunca va al PLC; Robot In Cycle baja hasta el inicio de la siguiente vuelta (MaintainSystem). R20 tiene la rutina estándar. La celda corre, así que el PLC no espera Work Complete de 10R1, pero es un handshake del estándar Gestamp (C18, C20).

**Qué hacer.** Decidir con Gestamp y el programador del PLC: restaurar la rutina del proveedor o documentar la desviación.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión escrita de Gestamp (quién y fecha).
* Si se restaura: EndOfCycle es igual a la rutina estándar de AutomationCore (comparada con la de R20); el PLC maneja Work Complete. Prueba en celda: el PLC ve $OUT[15] do015WorkComplete en cada ciclo, contesta $IN[15] y $OUT[5] do005RobotInCycle baja al terminar. Anotar fecha.
* Si se mantiene: la edición está en la lista de C28 y el comentario de cell.src cita la decisión.
* Comentarios según docs/CONVENTIONS.md; el ;WARNING: (F46) de cell.src se quita o se actualiza.

**Evidencia del programador.** Decisión de Gestamp y resultado de la prueba.

**Depende de / se cierra con:** C28

**Nota.** El veredicto red rabbit (F19) y el conteo de soldaduras (C20) dependen de este handshake.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F47 — Camino del brake test enseñado con tool 3 / base 1 de otro robot

**Severidad:** Medio · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/TP/BrakeTest/braketeststart.src`, `KRC/R1/TP/BrakeTest/braketestback.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** TP/BrakeTest/braketeststart.src mueve PTP a m y h (la misma pose, 2.6 m de alto) con Tool[3] y Base[1]; el texto del fold dice "Tool 3" y "3-30-R1 03-20B", copiado de otro robot. En R10 la base 1 es "10A" y la herramienta 3 "TOOL 3". Los puntos son cartesianos, así que el camino depende de lo que tengan la herramienta 3 y la base 1. braketestback.src regresa con la herramienta 1. Los archivos del proveedor también traen la edición de do931BrakeTestInProcess.

**Qué hacer.** Correr el brake test despacio en T1 y re-enseñar el camino con tool 1 / base 0 (de preferencia puntos de ejes).

**Criterio de cierre** (se verifica en el respaldo):

* Los folds de braketeststart.src ya no muestran Tool[3] ni Base[1]:3-30-R1: usan tool 1 / base 0 o puntos de ejes.
* Prueba en T1 a velocidad reducida: el brake test sale de HOME, llega a su pose sin interferencia y regresa a HOME. Anotar fecha y override.
* La edición en archivos del proveedor queda en la lista de C28.
* Comentarios del código cambiado según docs/CONVENTIONS.md (inglés, señal con dirección y nombre); los ;CHECK:/;NOTE:/;WARNING: que citan (F47) se quitan o se actualizan; el cambio está declarado en tools/code_changes.json y tools/check_equivalence.py pasa; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Puntos re-enseñados y fecha de la prueba.

**Depende de / se cierra con:** C28

**Nota.** Re-enseñar edita archivos del proveedor (TP/BrakeTest): listarlo en C28. C06 y C14 dependen de este punto.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## F48 — Drop al conveyor: interlock de drop-off movido después de la aproximación (corregido); AtDrop3 re-enseñado (se conserva)

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Gestamp controles · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

**Qué está mal.** AC_DropOffCheck(1) (espera $IN[75] di075DropOffMachine1) estaba antes de cualquier movimiento; ahora va después de PTP P5 y PTP P1: el robot se acerca al conveyor sin permiso del PLC. AtDrop3 se re-enseñó con 26° más en B y 34° en C, sin explicación.

**Qué hacer.** Hecho en oficina: la versión integrada deja AC_DropOffCheck(1) antes del primer movimiento, como estaba. AtDrop3 se conserva como lo enseñó el programador el 2026-10-05: así la pieza cae mejor en el conveyor (validado por Edgar Montiel con el programador).

**Criterio de cierre** (se verifica en el respaldo):

* AC_DropOffCheck(1) antes del primer movimiento hacia el conveyor (versión integrada).
* Prueba en celda con la versión integrada: con $IN[75] di075DropOffMachine1 OFF el robot espera antes de moverse hacia el conveyor (mensaje de espera); con $IN[75] ON hace 5 ciclos dejando la pieza en AtDrop3 sin contacto ni marca. Anotar fecha y resultado.
* Respaldo completo con la versión integrada cargada: style1drop1opt1.src/.dat coinciden con el zip entregado (la auditoría lo compara).

**Evidencia del programador.** Resultado de la prueba del interlock y de los 5 ciclos de drop, con fecha.

**Nota.** Razón del re-enseñado de AtDrop3 (B 4.3° → 30.1°, C -0.3° → -34.8°): la pieza cae mejor en el conveyor. Validado por Edgar Montiel con el programador el 2026-10-05.

**Historial:**

* 2026-10-05 — Alta (auditoría): Encontrado en el respaldo bmw_03_10_r1.
* 2026-10-05 — Corregido en oficina: Excluido de la integración por decisión de Edgar: el zip integrado regresa el interlock de drop-off antes del primer movimiento y AtDrop3 al punto original. Probar 5 ciclos de drop al conveyor.
* 2026-10-05 — Decisión: Edgar: se conserva el AtDrop3 del programador (la pieza cae mejor en el conveyor; validado con él). Solo el interlock de drop-off regresa a su lugar original.
* 2026-10-05 — Respaldo 14:46: El programador además quitó PTP P1: un LIN de 330 mm de P5 a AtDrop3 bajando 166 mm a unos 30°, con el permiso de drop-off en P5. En la versión integrada el robot espera el permiso en el punto de cámara P3 con la aplicación 1 ya liberada: mover AC_Application(1,TRUE) a después de salir de la cámara.
* 2026-10-05 — Integrado: P1 se conserva (preguntar al programador por qué lo quitó). La aplicación 1 ya no se libera en el punto de cámara: la libera un TRIGGER en el primer movimiento fuera de la cámara (P5 del drop, P23 del rechazo, P28 del red rabbit).

---

## F49 — AutomationCore_BKG activado y editado sin decisión registrada

**Severidad:** Alto · **Tipo:** Decisión Gestamp + código · **Responsable:** Gestamp controles + Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

**Qué está mal.** sps.sub ahora llama AutomationCore_BKG (F12). Escribe cada ciclo los bits de estado al PLC (aire, agua, tolvas, nut ready/fault, batería, velocidad), auto-selecciona CELL en EXT, pone do004ProcessFault en cada reset de programa, activa el camino de cambio de electrodo (F43) y el Request to Enter ($OUT[145] doCriticalWZ). La rutina del proveedor se editó: sin soldadores 2-3 y Request to Enter sin WAIT (antes congelaba el submit).

**Qué hacer.** Registrar la decisión de Gestamp de activar el background. Probar en celda cada salida nueva con el PLC (aire, agua, tolvas, nut ready/fault, request to enter) y el cambio de electrodo. Documentar las ediciones del proveedor (C28).

**Criterio de cierre** (se verifica en el respaldo):

* Decisión de Gestamp por escrito (activar AutomationCore_BKG; NutWeld_BKG sigue apagado o se decide aparte).
* Prueba en celda con el PLC: request to enter concedido solo sin gun en trabajo ni gripper/brake test/mastering en proceso; cada bit de estado leído en el PLC con su condición forzada; un cambio de electrodo completo (F43).
* Ediciones del proveedor listadas en la entrega (C28).

**Evidencia del programador.** Correo de Gestamp, tabla de señales probadas con fecha y resultado, prueba de cambio de electrodo.

**Depende de / se cierra con:** F12, F43, C28

**Nota.** La edición del Request to Enter es razonable: el WAIT original detenía todo el submit (posición del gun, preload, gripper) mientras la petición estaba activa.

**Historial:**

* 2026-10-05 — Alta (auditoría): Encontrado en el respaldo bmw_03_10_r1.
* 2026-10-05 — Integrado - pendiente decisión: Activación y ediciones del proveedor integradas tal como estaban en el robot; comentarios ;CHECK: en sps.sub, cell.src y gunelectrodechange. Falta decisión de Gestamp y prueba con el PLC y del cambio de electrodo.
* 2026-10-05 — Revisión independiente - riesgos confirmados: (1) Request to Enter: con $OUT[930] pegado (F35) el robot ya no se detiene al pedir entrar. (2) El background escribe $OUT[481]/$OUT[482] (habilitaciones del Bosch) cada ciclo y pisa las de CENTERLINE_WELD; en dry cycle puede colgar WAIT FOR dipw1_Ready. (3) Cambio de electrodo activo sin probar (F43). (4) AC_MODE sin inicializar en el CWRITE del auto select. (5) do004ProcessFault en cada reset. (6) bACEntryGranted persistente. Corre así en el robot desde el 2026-10-05.
* 2026-10-05 — Integrado - background apagado: El background de AutomationCore se apaga otra vez hasta que Gestamp decida y se corrijan sus problemas; el submit pone $OUT[145] y $OUT[111] en OFF al arrancar. Las ediciones del proveedor quedan, inactivas (C28).

---

## F50 — Permiso de aplicación 1 (nut check / cámara) revisado después de llegar a P22

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

**Qué está mal.** En el respaldo de las 14:46 el programador movió AC_ApplicationCheck(1) (espera $IN[70]) a después de PTP P22. P22 es el punto de aproximación de la estación de inspección (unos 170 mm del punto de cámara P6 y 480 mm abajo de los puntos del nut check): el robot entra sin permiso del PLC mientras $OUT[70]/$OUT[24] siguen diciendo que está libre.

**Qué hacer.** Dejar AC_ApplicationCheck(1) antes del primer movimiento, como en la versión integrada. Si se movió por tiempo de ciclo, ver con el PLC si se puede pedir el permiso antes (al salir del pedestal).

**Criterio de cierre** (se verifica en el respaldo):

* AC_ApplicationCheck(1) antes de PTP P22 en el respaldo.
* Prueba en celda: con $IN[70] OFF el robot espera antes de moverse a P22 (mensaje de espera); con $IN[70] ON el ciclo sigue normal. Anotar fecha y resultado.

**Evidencia del programador.** Resultado de la prueba con fecha; razón del cambio si la hubo.

**Historial:**

* 2026-10-05 — Alta (auditoría): Encontrado en el respaldo de las 14:46; confirmado por revisión independiente.
* 2026-10-05 — Integrado: No se integra: en la versión integrada AC_ApplicationCheck(1) queda antes de PTP P22.

---

## F51 — Apps de soldadura duplicadas por estación de pick (A/B): cada cambio va en las dos

**Severidad:** Bajo · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** Sin acción - documentado

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1A..3B`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** El programador partió las tres apps de soldadura por estación de pick: A (estación 1, posiciones sin cambio) y B (estación 2, posiciones de soldadura re-enseñadas 1-5 mm porque la pieza queda distinta en el gripper). El código de A y B es el mismo.

**Qué hacer.** Se integra tal cual. Cualquier cambio posterior a una app de soldadura se hace en A y en B.

**Criterio de cierre** (se verifica en el respaldo):

* Documentado; se revisa en cada auditoría que A y B sigan iguales en código.

**Historial:**

* 2026-10-05 — Alta (auditoría): Integrado en la versión depurada.

---

## F52 — Tiempo ciclo: el robot espera ~4 s la tuerca antes de las tuercas 2 y 3 (la precarga arrancaba hasta después de soldar)

**Severidad:** Alto · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Corregido en oficina - probar en celda

**Módulos:** `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/CL_CYCLE_TIME.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1A..3B`, `KRC/R1/System/$config.dat`

**Qué está mal.** Gestamp pide 12 s por pieza de proceso de soldadura con el robot parado (sin contar movimientos). En el video del 2026-10-05 son ~20 s: por tuerca ~2.8 s de llegada a soldadura y ~1.2 s para salir, y antes de las tuercas 2 y 3 ~4 s esperando la tuerca. Esa espera es toda la precarga (alimentar 2000 ms, avance del QFP, soplo 800 ms, 800 ms tras el regreso), que arrancaba hasta que el robot salía del pedestal, aunque alimentar la tuerca al shuttle solo necesita el shuttle en casa.

**Qué hacer.** Etapa 1 (hecha en oficina): las apps 1 y 2 piden alimentar la siguiente tuerca al shuttle en cuanto su tuerca está lista (NUT_FEED_START); PRELOAD alimenta mientras el robot entra y suelda y espera; Request_next_nut a la salida (app 1 en P8 como antes, app 2 ahora en P05 en vez de P0) solo carga la tuerca al pin. Paso 20 termina con el QFP regresado confirmado. PRELOAD y CENTERLINE_WELD ya no se pisan $OUT[494] ni $OUT[476] durante la soldadura. Medición de tiempos CL_CYCLE_TIME ($TIMER[16]) por paso, últimos 10 ciclos por tuerca. Etapa 2 (pendiente, con datos de la medición y OK de CenterLine/Bosch): recortes dentro de CENTERLINE_WELD.

**Criterio de cierre** (se verifica en el respaldo):

* Prueba en T1: el shuttle no se mueve con la pieza en el pedestal; solo con el robot en P8/P0/P5/P05/P20 de la app 3.
* Una tuerca por alimentación (sin doble tuerca en el shuttle); tuercas 2 y 3 en el pin antes de que el robot entre.
* Dry cycle encendido y apagado; reset de programa a media pieza y rearranque: la tuerca ya alimentada se carga en la siguiente petición, no se alimenta otra.
* 10 ciclos en automático y respaldo: tools/cycle_times.py muestra la espera de tuerca de las tuercas 2 y 3 cerca de 0 y el tiempo de robot parado por pieza.
* Etapa 2 decidida con los tiempos medidos (o documentado que no se hace).

**Evidencia del programador.** Resultado de las pruebas con fecha y el respaldo después de 10 ciclos en automático.

**Nota.** Etapa 1 de tiempo ciclo. Ganancia esperada ~3 s por tuerca 2 y 3: de ~20 s a ~13-14 s de robot parado por pieza. La medición (CL_CYCLE_TIME) se quita al cerrar el tema de tiempo ciclo.

**Historial:**

* 2026-10-07 — Alta: Análisis del video y del código; el dueño confirma que se puede alimentar la tuerca durante la soldadura.
* 2026-10-07 — Corregido en oficina: Etapa 1 y medición; revisión independiente antes de la entrega.

---

## C01 — AutomationCore_Bkg deshabilitado: el estatus al PLC no se actualiza

**Severidad:** - · **Tipo:** Decisión Gestamp · **Responsable:** Gestamp controles / Ethos (Edgar) · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`

**Qué está mal.** El estándar Gestamp pide que el background task de AutomationCore mantenga el estatus hacia el PLC. En sps.sub la llamada AutomationCore_BKG ( ) estaba comentada (fold Automation Core PLC vacío), así que nunca se escriben, entre otros, $OUT[21], $OUT[22], $OUT[6], $OUT[7] do007RobotAtPounce, $OUT[111..113], los bits de bus OK, $OUT[146] ni $OUT[145] doCriticalWZ. Es el mismo problema que F12.

**Qué hacer.** Se atiende en F12.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierra F12.

**Evidencia del programador.** La evidencia se registra en F12.

**Depende de / se cierra con:** F12

**Nota.** Al cerrar F12 se actualiza también el ;NOTE: de sps.sub que cita (F12, C01).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C02 — Designación BMW-03-10-R1 en los encabezados; confirmar formato con Gestamp

**Severidad:** - · **Tipo:** Información Gestamp · **Responsable:** Ethos (Edgar) / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/HOME.src`, `KRC/R1/Program/masref_user.src`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/Program/Utilities/closeandcheckallclamps.src`, `KRC/R1/Program/Utilities/openandcheckallclamps.src`, `KRC/R1/safetest.src`

**Qué está mal.** Los 31 encabezados de los módulos del integrador dicen "; Line - BMW G65 (cell 03)" y "; Robot 03-10-R1 (BMW-03-10-R1[-PNW1|-MH1])". La revisión de Gestamp (2026-10-02) llama a esta estación BMW-03-10R1 (el encabezado de la hoja no se ve en la foto; el contenido coincide con este respaldo). El encabezado viejo de HOME decía "Line - Volvo".

**Qué hacer.** Confirmar con Gestamp el formato exacto (BMW-03-10R1 o BMW-03-10-R1), el nombre de línea y los códigos PNW1/MH1; si difiere, ajustar los encabezados.

**Criterio de cierre** (se verifica en el respaldo):

* Confirmación escrita de Gestamp del formato, nombre de línea y códigos de dispositivo.
* Los encabezados del respaldo usan ese formato; los módulos nuevos también.

**Evidencia del programador.** Correo o documento de Gestamp; si cambió, cuántos módulos se actualizaron.

**Nota.** Un nombre de módulo KRL no admite '-' (máximo 24 caracteres): la designación vive en el encabezado y en &COMMENT. El nombre del robot en el controlador es G01.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C03 — Encabezado estándar Gestamp en cada módulo del integrador

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** Cerrado - depuración

**Módulos:** `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/HOME.src`, `KRC/R1/Program/masref_user.src`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/Program/Utilities/closeandcheckallclamps.src`, `KRC/R1/Program/Utilities/openandcheckallclamps.src`, `KRC/R1/safetest.src`

**Qué está mal.** Los módulos del integrador no traían el encabezado estándar Gestamp. La depuración lo agregó a los 31 módulos (después del fold INI, o tras el DEF si no hay INI); los .dat no llevan encabezado.

**Qué hacer.** Nada que corregir. Mantener el encabezado y ponerlo en todo módulo nuevo con el formato de docs/CONVENTIONS.md.

**Criterio de cierre** (se verifica en el respaldo):

* Ningún módulo que hoy tiene el bloque '; Gestamp Standards' lo pierde en el respaldo.
* Todo .src nuevo del integrador trae el bloque completo (Gestamp Standards / Line / Robot 03-10-R1 (designación) / Application) y un &COMMENT con 03-10-R1.

**Nota.** Solo verificación de regresión en cada respaldo. El encabezado nunca va dentro de un fold de tech package ni de un inline form.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C04 — Movimientos de pedestal interpolados sobre el dado fijo (external TCP)

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Ethos (Edgar) / Programador robot · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

**Qué está mal.** El estándar Gestamp (Pedestal Applications, Remote TCP) pide que los movimientos en el pedestal se interpolen alrededor del dado fijo (external TCP con la base 3 NUT WELDER). De los 22 movimientos en base 3, 11 van en external TCP y ninguna de las tres presentaciones de soldadura (P19 de la app 1, P16 de las apps 2 y 3) lo usa (F22).

**Qué hacer.** Decidir y dejar por escrito la convención de frames del pedestal (la del estándar o una excepción aprobada por Gestamp) y re-enseñar en T1 los movimientos de pedestal con esa convención.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión escrita de la convención de frames del pedestal adjunta a la lista.
* Se cumplen los criterios de F22 y C05.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C04) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Decisión escrita; la evidencia de re-enseñanza se registra en F22.

**Depende de / se cierra con:** C05, F22

**Nota.** Cambiar solo la casilla extTCP del inline form sin re-enseñar el punto cambia la posición física. C05 y C04 van en el mismo respaldo.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C05 — TCP remoto del pedestal (BASE_DATA[3]) sin medir

**Severidad:** - · **Tipo:** Confirmar en sitio · **Responsable:** Puesta en marcha / Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

**Qué está mal.** El estándar pide el origen del TCP remoto a 1/4 de pulgada (6.35 mm) del electrodo, dado o pin estacionario en dirección axial, con +X y +Y a escuadra con el dado. BASE_DATA[3] NUT WELDER vale {X 21.84, Y 1866.09, Z 658.47, A 90, B 0, C 180}: no hay registro de que se haya medido con ese criterio.

**Qué hacer.** Verificar el mastering y medir en sitio la herramienta fija del pedestal con el procedimiento KUKA de herramienta fija, con el origen y la orientación del estándar, y guardar el resultado en BASE_DATA[3]. En el mismo respaldo se re-enseñan (C04/F22) o verifican los 22 puntos en base 3.

**Criterio de cierre** (se verifica en el respaldo):

* Registro de medición adjunto: método KUKA de herramienta fija, referencia física, cómo se dio el desfase axial de 6.35 mm y la orientación X/Y, error mostrado, valores resultantes, fecha y verificación de mastering previa.
* BASE_DATA[3] del respaldo es el valor medido y BASE_NAME[3] sigue siendo NUT WELDER.
* Prueba en T1: con la pieza en una pose de soldadura, jog de orientación en external TCP: la pieza gira sobre el electrodo sin desplazarse; anotar resultado.
* En el mismo respaldo en que cambia BASE_DATA[3], cada punto en Base[3] (style1app1opt1..3, RejectGE4, style1app2opt2) está re-enseñado o la lista anota que se recorrió en T1 y quedó correcto.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C05) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Foto de la pantalla de resultado de la medición; verificación de mastering; resultado de la prueba de giro; lista de puntos en base 3 con lo hecho.

**Nota.** Cambiar BASE_DATA[3] mueve físicamente todos los puntos en base 3: no correr en automático hasta re-enseñarlos o verificarlos en T1.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C06 — Herramientas y bases con nombre: nombres de otro proyecto

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/TP/BrakeTest/braketeststart.src`

**Qué está mal.** El estándar pide herramientas y bases con nombre y ninguna herramienta sin nombre en producción. Las herramientas se llaman "TOOL 1".."TOOL 3" (sin decir qué son) y las bases "10A", "20B" y "PED SEALER" vienen de otro proyecto. Los nombres viejos de herramienta en el texto de los folds ya los refrescó la depuración. El brake test usa la herramienta 3 y la base 1 con nombres de 03-30-R1 (F47).

**Qué hacer.** Dar nombre descriptivo a la herramienta 1 (EOAT 1) y a las bases usadas, y limpiar o renombrar las que no se usan; con F47 el brake test deja de usar tool 3 / base 1.

**Criterio de cierre** (se verifica en el respaldo):

* En $config.dat TOOL_NAME y BASE_NAME de cada herramienta y base usada describen lo que son (p. ej. EOAT 1, NUT WELDER); las que no se usan quedan vacías o con su nombre real.
* Ningún movimiento de producción ni de servicio usa una herramienta o base sin nombre o con nombre de otro robot (F47 cerrado).
* Prueba: abrir un form de movimiento de cada módulo de producción y confirmar que muestra el nombre nuevo sin cambiar el punto (sin Touch Up). Anotar fecha.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C06) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Lista de nombres anterior y nuevo; fecha.

**Depende de / se cierra con:** F47

**Nota.** Renombrar una herramienta no mueve puntos; cambiar sus datos sí. No usar TOOL 2 para otra cosa sin revisar que ningún punto la use.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C07 — Un user frame por utillaje: picks, nut check, reject y drops en WORLD

**Severidad:** - · **Tipo:** Decisión Gestamp · **Responsable:** Gestamp controles / Ethos (Edgar) · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** El estándar pide un user frame (base) por utillaje. Las estaciones de pick, el nut check, la cámara, el reject y los drops están enseñados casi todos en WORLD (la aproximación a la cámara P6 y la salida del reject P24 en Base[3]). BASE_DATA[1] "10A" y [2] "20B" tienen nombres de otro proyecto.

**Qué hacer.** Que Gestamp decida si exige bases por utillaje en esta estación o acepta WORLD por escrito. Si las exige: verificar el mastering, medir una base por utillaje, con nombre, y re-enseñar en T1 los puntos de cada utillaje en su base.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión escrita de Gestamp adjunta: (a) acepta WORLD y el punto se cierra sin cambio de código; o (b) exige una base por utillaje.
* Si (b): cada utillaje tiene su BASE_DATA medida y su BASE_NAME; los movimientos de aproximación, trabajo y salida usan esa base; registro de medición y prueba en T1 y en automático con fecha.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C07) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Decisión de Gestamp; si se miden bases, registro y pruebas.

**Nota.** Cambiar la base de un punto sin re-enseñarlo cambia su posición física. Si se re-enseñan trayectorias, revisar después C08 y C09.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C08 — Datos de carga: LOAD_DATA[1] tecleado; sin carga con/sin pieza

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** El estándar pide un payload por escenario de carga, determinado (LoadDataDetermination): EOAT sin pieza y con pieza, salvo que difieran menos de 5 %. LOAD_DATA[1] = {M 210, CM X 270 Y 0 Z 240, J 105/105/105}, valores redondos tecleados (F39), y no hay datos de carga con pieza.

**Qué hacer.** Determinar con LoadDataDetermination la carga del EOAT 1 sin pieza y con la pieza GE4 (G03). Si difieren 5 % o más, dos juegos de datos y cada trayectoria usa el que corresponde.

**Criterio de cierre** (se verifica en el respaldo):

* LOAD_DATA[1] coincide con el resultado de LoadDataDetermination del EOAT 1 sin pieza.
* Si la carga con pieza difiere 5 % o más: otra herramienta con TOOL_DATA idéntico a TOOL_DATA[1], nombre y LOAD_DATA con pieza, usada por los movimientos con pieza (del cierre del gripper en el pick a su apertura en drop, drop red rabbit o reject); si difieren menos, la lista anota las dos masas.
* Ningún movimiento de producción usa una herramienta con LOAD_DATA por defecto o cero.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C08) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Resultados de LoadDataDetermination sin y con pieza, fecha y quién lo corrió.

**Depende de / se cierra con:** G03, F39

**Nota.** Si se edita el FDAT directo en el .dat, actualizar también el texto Tool[n]:<nombre> del fold. Los datos de carga correctos son requisito para C09.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C09 — Detección de colisión apagada en todo el programa; la reacción es un HALT

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/System/$config.dat`, `KRC/R1/TP/AutomationCore/automationglobalpos.dat`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/HOME.src`, `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/masref_user.src`

**Qué está mal.** El estándar pide la detección de colisión activa todo el tiempo; apagarla requiere aprobación escrita. $TORQMON está en 0 (F39) y todos los movimientos de producción tienen TQ_STATE FALSE. tm_useraction, la reacción a una colisión, solo hace HALT (C21).

**Qué hacer.** Activar la detección y ajustarla en celda con el método del estándar, con los datos de carga ya correctos (C08). Si no se puede, conseguir la aprobación escrita de Gestamp para operar sin ella.

**Criterio de cierre** (se verifica en el respaldo):

* Opción A: detección activa (bTQM_KCPSTATUS = TRUE y TQ_STATE TRUE en los FDAT de los movimientos que corren en automático, incluidos FHOME y los de automationglobalpos.dat); excepciones anotadas con su razón; valores de sensibilidad anotados; ciclos en automático externo a 100 % sin disparo en falso, con número de ciclos y fecha.
* Opción B: aprobación escrita de Gestamp para operar sin detección de colisión, adjunta, y el ;NOTE: de tm_useraction la cita.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C09) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Opción A: foto de bTQM_ACTIVE en automático externo, tabla de valores y ciclos sin disparo en falso. Opción B: documento de Gestamp.

**Depende de / se cierra con:** C08, F39

**Nota.** TQ_STATE se puede cambiar en el FDAT del .dat sin reabrir el inline form. Los cambios en automationglobalpos.dat son ediciones de archivos del proveedor: listarlas en C28.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C10 — Falta el programa de mastering ZERO_G1

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/ZERO_G1.src (nuevo)`

**Qué está mal.** El estándar pide un programa ZERO_G1: trayectoria segura de home a la posición de mastering, una pausa y regreso. En el respaldo no existe; solo está la prueba de mastering reference de KUKA (masref_main, masref_user).

**Qué hacer.** Crear ZERO_G1 con su encabezado: arranca en HOME, va por puntos libres de interferencia a la posición de mastering, se detiene para la revisión visual con mensaje y regresa a HOME.

**Criterio de cierre** (se verifica en el respaldo):

* Existe ZERO_G1.src (y su .dat) en KRC/R1/Program con el bloque '; Gestamp Standards' y &COMMENT, y está declarado en tools/code_changes.json (added_files).
* Arranca y termina en HOME; la pose de mastering es igual a $MAMES[1..6] de $machine.dat (A1 -20, A2 -120, A3 110, A4 0, A5 0, A6 0), con pausa explícita y mensaje que pide revisar las marcas; si no se alcanza en un paso, dos poses (A1-A3, luego A4-A6) con el visto bueno de Ingeniería Gestamp.
* Prueba en T1 con override reducido: HOME, pose de mastering y regreso sin contacto; foto de las marcas de cada eje; fecha.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C10) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fotos de las marcas de mastering y fecha de la prueba.

**Nota.** La pausa de ZERO_G1 es una detención intencional de verificación, no manejo de falla (no cuenta contra C21).

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C11 — Zonas sin documentar: ninguna zona pedida, falta la forma NA-FM-71-138.1

**Severidad:** - · **Tipo:** Información Gestamp · **Responsable:** Ethos (Edgar) / Gestamp controles · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`

**Qué está mal.** El estándar pide que cada entrada y salida de zona lleve un comentario con este robot, la zona y el robot socio, y la forma NA-FM-71-138.1 (Robot Zone Assignment). En R10 no se pide ninguna zona en ninguna parte (producción, repair, pounce).

**Qué hacer.** Conseguir de Gestamp los robots de la celda 03 y las trayectorias que interfieren con R10, llenar NA-FM-71-138.1 y que Gestamp la apruebe. Después pedir y liberar en el programa cada zona de la forma, con el comentario completo.

**Criterio de cierre** (se verifica en el respaldo):

* NA-FM-71-138.1 llena y aprobada por Gestamp, adjunta (o constancia escrita de que R10 no comparte zonas).
* Toda zona de la forma tiene su petición y su liberación en el módulo correspondiente, con el comentario 'Zn ENTER/EXIT 03-10-R1 ... WITH <robot socio>' y el AC_CmdParam del form igual al número de zona.
* Prueba en celda por zona: R10 espera en la petición mientras la zona está ocupada y su salida de zona libre está OFF dentro y ON al salir; anotar fecha.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C11) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Forma aprobada; fecha y resultado por zona.

**Nota.** HOME debe quedar libre de toda interferencia (estándar). La coherencia pedir/liberar es C13.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C12 — Pounce común: el ciclo no pasa por pounce y do007RobotAtPounce no se calcula

**Severidad:** - · **Tipo:** Decisión Gestamp · **Responsable:** Gestamp controles / Ethos (Edgar) · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/TP/AutomationCore/automationglobalpos.dat`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/cell.src`

**Qué está mal.** El estándar pide un pounce común por el que pasan todos los programas de estilo. El ciclo de R10 no pasa por ningún pounce y $OUT[7] do007RobotAtPounce solo lo escribe AutomationCore_Bkg, deshabilitado (F12), así que HomeCheck nunca ejecuta PounceToHome.

**Qué hacer.** Que Gestamp decida si exige el pounce común. Si sí: enseñar o verificar XPOUNCE, hacer que el ciclo pase por él y que do007 se calcule (vía F12). Si no: aprobación escrita y comentar que HomeToPounce y PounceToHome no se usan.

**Criterio de cierre** (se verifica en el respaldo):

* Decisión escrita de Gestamp adjunta.
* Si se exige: Style1Opt1 y Style1Opt10AutoRR pasan por el mismo pounce; XPOUNCE verificado en T1 con la herramienta 1; $OUT[7] se escribe cíclicamente y HomeCheck ejecuta PounceToHome con el robot en el pounce; prueba con fecha.
* Si no se exige: el comentario de HomeToPounce y PounceToHome dice que no se usan por decisión de Gestamp.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C12) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Decisión de Gestamp; si aplica, fecha y resultado de la prueba de do007.

**Depende de / se cierra con:** F12

**Nota.** Re-enseñar XPOUNCE edita automationglobalpos.dat, archivo del proveedor: listarlo en C28.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C13 — Manejo de zonas coherente

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** No aplica

**Módulos:** `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`

**Qué está mal.** R10 no usa zonas: no hay nada que pedir y liberar de forma incoherente.

**Qué hacer.** Nada hoy. Si C11 o C12 agregan zonas, cada trayectoria pide antes de entrar y libera al salir exactamente las zonas que cruza.

**Criterio de cierre** (se verifica en el respaldo):

* Se reabre si C11 o C12 agregan zonas: entonces cada zona pedida se libera al salir de ella (no solo por MaintainSystem), con prueba en T1 de las salidas de zona libre.

**Depende de / se cierra con:** C11

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C14 — Brake test: el 'due' no se reporta y el camino usa tool/base de otro robot

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/TP/BrakeTest/braketeststart.src`, `KRC/R1/TP/BrakeTest/braketestback.src`, `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`

**Qué está mal.** El estándar pide reportar al PLC cuando el brake test está pendiente y ejecutarlo en home. El brake test corre a petición del PLC ($IN[21] di021BrakeTestRequest) después de HomeCheck, pero $OUT[21] do021BrakeTestReqd solo lo escribe AutomationCore_Bkg, deshabilitado (F12): el PLC nunca sabe que está pendiente. El camino de inicio está enseñado con tool 3 / base 1 de otro robot (F47), y los archivos del proveedor traen la edición de do931BrakeTestInProcess, que además cae en un bit del adapter compartido (F18).

**Qué hacer.** Calcular do021BrakeTestReqd cíclicamente ($BRAKETEST_MONTIME, $BRAKETEST_REQ_EX, $BRAKETEST_REQ_INT) por F12 o en sps.sub; mantener la señal de brake test en proceso hasta que el robot regresó; acordar con Gestamp el bit (F18); re-enseñar el camino (F47).

**Criterio de cierre** (se verifica en el respaldo):

* $OUT[21] do021BrakeTestReqd se escribe en cada ciclo del submit con la condición de brake test pendiente.
* La señal de brake test en proceso se apaga después del último movimiento de regreso, con el robot en HOME, y su bit está acordado con Gestamp (F18).
* Prueba en celda: con el brake test pendiente el PLC ve do021 ON; al pedir di021 el robot sale de HOME, hace el test y regresa a HOME; do021 baja al terminar. Anotar fecha.
* La edición en archivos del proveedor queda listada en C28.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C14) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fecha y resultado de la prueba.

**Depende de / se cierra con:** F12, F18, F47

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C15 — Dry cycle seleccionable y sin colgar el robot

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/System/sps.sub`

**Qué está mal.** El estándar pide dry cycle seleccionable desde el PLC sin que el robot se cuelgue. Hoy se cuelga en la primera weld app (F04), y como $IN[4] se lee en cada paso, cambiarlo a medio ciclo puede soltar como buena una pieza sin soldar ni inspeccionar (F05).

**Qué hacer.** Se atiende en F04 y F05.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran F04 y F05.

**Evidencia del programador.** La evidencia se registra en F04 y F05.

**Depende de / se cierra con:** F04, F05

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C16 — Pieza presente / pieza en gripper

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** Los picks esperan gripper vacío antes del primer comando de gripper (G14) y pieza presente después de cerrar; drops y reject esperan gripper vacío después de abrir. Pero $OUT[18] do018Part1InGripper está latcheado por programa, no sigue a los sensores (Gestamp punto 9), y los drops y el reject no confirman la pieza antes de abrir (F40).

**Qué hacer.** Se atiende en G09 y F40.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran G09 y F40.
* Se reabre si un cambio quita o salta alguna espera de pieza fuera de dry cycle.

**Evidencia del programador.** La evidencia se registra en G09 y F40.

**Depende de / se cierra con:** G09, F40

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C17 — Verificación de tuercas y red rabbit

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/System/$config.dat`

**Qué está mal.** El estándar pide verificar las tuercas y comprobar la detección con red rabbit. Las options 2, 7 y 8 no evalúan el sensor (F02); PARTPRESENT1..3 y bscrapGE4 no se resetean al inicio del ciclo (F03); el ciclo red rabbit no puede dar resultado (F19).

**Qué hacer.** Se atiende en F02, F03 y F19.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran F02, F03 y F19.

**Evidencia del programador.** La evidencia se registra en F02, F03 y F19.

**Depende de / se cierra con:** F02, F03, F19

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C18 — Handshakes AutomationCore de pick, application y drop

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`

**Qué está mal.** Los handshakes de pick, application y drop están pareados, salvo: RejectGE4 abre el gripper sin AC_DropOffCheck y un rechazo desde el nut check no libera Application 1 (F20); los parámetros ocultos de varios forms no coinciden con la llamada (F21); y EndOfCycle no manda Work Complete (F46).

**Qué hacer.** Se atiende en F20, F21 y F46.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran F20, F21 y F46.

**Evidencia del programador.** La evidencia se registra en F20, F21 y F46.

**Depende de / se cierra con:** F20, F21, F46

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C19 — Request to enter: doCriticalWZ nunca se escribe; el PLC ve entrada permitida

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Seguridad · **Estado:** Requiere decisión

**Módulos:** `KRC/R1/System/sps.sub`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/centerline_weld.src`

**Qué está mal.** El estándar pide respetar la petición de entrada del PLC. El robot se detiene en el siguiente punto cuando sube $IN[6] di006RequestToEnter (TRIGGER AC_PointArrival en bas.src), pero $OUT[145] doCriticalWZ solo lo escribe AutomationCore_Bkg, deshabilitado (F12): queda FALSE y el PLC ve entrada permitida mientras PRELOAD o CENTERLINE_WELD siguen accionando el pedestal (F11). Si se reactiva el background, $OUT[930] en ON (F35) bloquearía toda entrada.

**Qué hacer.** Que doCriticalWZ se escriba cíclicamente y diga entrada no permitida mientras haya un proceso que no se detiene en un punto (preload, soldadura, brake test, mastering reference). Cómo depende de F12; qué pasa con el pedestal al abrir la puerta depende de la revisión de seguridad de F11.

**Criterio de cierre** (se verifica en el respaldo):

* $OUT[145] doCriticalWZ se escribe en cada ciclo del submit.
* Su condición incluye PRELOAD con un paso activo y CENTERLINE_WELD en ejecución (o el estado real del pedestal), además de do930/do931/do932 ya corregidos (F35, F18).
* Prueba en celda: sin proceso de pedestal, $IN[6] detiene el robot en el siguiente punto con doCriticalWZ OFF; con un preload y con una soldadura en curso, doCriticalWZ queda ON mientras dura el proceso. Anotar fecha.
* Resultado de la revisión de seguridad de F11 adjunto.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C19) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fecha y resultado de las pruebas; documento de la revisión de seguridad.

**Depende de / se cierra con:** F12, F11, F35

**Nota.** AC_Request_to_enter contiene un WAIT FOR dentro del submit: evaluarlo antes de reactivar AutomationCore_Bkg. Cambiar automationcoreroutines.src es edición de archivo del proveedor: C28.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C20 — Conteo de soldaduras al final del ciclo: #CHECK apagado y WeldNoRequired distinto de 3

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/TP/AutomationCore/automationcoredata.dat`

**Qué está mal.** El estándar pide verificar al final del ciclo que se hicieron todas las soldaduras. En EndOfCycle (automationcoreroutines.src, editado en este robot, F46) AC_Process_Count(#CHECK) está comentado. WeldNoRequired en automationcoredata.dat no vale 3 para las options de producción ([1,1]=1, [1,2]=2, [1,7]=6, [1,8]=4). AC_Process_Count(#Count1up) solo lo llama NutWeld_Weld del proveedor, que este programa no usa: CENTERLINE_WELD no cuenta.

**Qué hacer.** Contar una soldadura por cada soldadura buena en CENTERLINE_WELD (con el resultado de F08), poner WeldNoRequired = 3 en las options de producción y activar la verificación al final del ciclo, con $OUT[47] do047QualityFault si no coincide.

**Criterio de cierre** (se verifica en el respaldo):

* CENTERLINE_WELD llama AC_Process_Count(#Count1up) una vez por tuerca y solo con soldadura buena (F08).
* WeldNoRequired[1,1], [1,2], [1,7] y [1,8] = 3 (más las options que confirme F02) y la del red rabbit = 0.
* AC_Process_Count(#CHECK) se ejecuta al final de cada ciclo de producción y el conteo arranca en 0 en cada ciclo, también después de un ciclo cancelado.
* Prueba en celda: ciclo normal con do047 OFF; ciclo con una soldadura faltante (método seguro anotado) con do047 ON; ciclo cancelado seguido de uno completo con do047 OFF; resultado en dry cycle definido con F05. Anotar fecha.
* Si se modifica EndOfCycle, la edición queda listada en C28 (y es coherente con lo que decida F46).
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C20) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Fecha y resultado de las pruebas con el estado de do047QualityFault.

**Depende de / se cierra con:** F46, F08, F02, F05

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C21 — Fallas por mensajes AutomationCore: ningún HALT sin mensaje ni WAIT FOR FALSE

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/cell.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`

**Qué está mal.** El estándar pide que toda falla salga por mensajes AutomationCore con falla al PLC. Hoy: Style_1 contesta una option desconocida con WAIT FOR FALSE y hay ciclos vacíos sin falla (F06); CENTERLINE_WELD maneja el timeout de gun cerrado con HALT sin mensaje (F07); unos 35 WAIT FOR no tienen timeout ni mensaje (F15); y tm_useraction, la reacción a colisión, solo hace HALT.

**Qué hacer.** Cerrar F06, F07 y F15, y en tm_useraction dar mensaje y $OUT[4] do004ProcessFault antes de detener.

**Criterio de cierre** (se verifica en el respaldo):

* F06, F07 y F15 cerrados.
* tm_useraction pone $OUT[4] do004ProcessFault ON y muestra un mensaje de celda que nombra la colisión antes de detener el programa.
* En KRC/R1/Program, cell.src y sps.sub no queda WAIT FOR FALSE, y cada HALT que quede va precedido de mensaje y $OUT[4] ON (salvo la pausa de ZERO_G1, C10).
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C21) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** Si la detección de colisión está activa (C09): fecha y resultado de la prueba de reacción.

**Depende de / se cierra con:** F06, F07, F15

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C22 — Grippers por inline forms GripperTech

**Severidad:** - · **Tipo:** Código + prueba en celda · **Responsable:** Programador robot / Puesta en marcha · **Estado:** Abierto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/TP/GripperSpotTech/grp_data.dat`

**Qué está mal.** Cumple en parte: picks, drop al conveyor y RejectGE4 usan forms GripperTech. Los parámetros ocultos de esos forms eran de otro gripper (corregido en oficina, F31) y el drop red rabbit escribe el gripper 1 a mano y suelta con el gripper 3 (F19, F31). GripperConfig.xml está desincronizado (F33).

**Qué hacer.** Se atiende en F31, F33 y F19.

**Criterio de cierre** (se verifica en el respaldo):

* Se cumplen F31, F33 y F19: en los módulos listados toda acción de gripper es un form GripperTech del gripper 1 con parámetros iguales a la llamada.
* General: comentarios nuevos o cambiados según docs/CONVENTIONS.md (inglés, señal con dirección); el comentario que cite (C22) se quita o se actualiza; ningún encabezado de inline form ni línea dentro de un fold de form cambia sin estar declarado (F32, F21, F31).

**Evidencia del programador.** La evidencia se registra en F31, F33 y F19.

**Depende de / se cierra con:** F31, F33, F19

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C23 — Nombres AutomationCore para la E/S, sin direcciones literales

**Severidad:** - · **Tipo:** Código · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/System/sps.sub`, `KRC/R1/System/$config.dat`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

**Qué está mal.** El estándar pide nombres de señal estilo AutomationCore y no direcciones literales. Hecho en oficina (G12) fuera de los inline forms de KUKA; quedan los nombres traslapados de pistola 2/3 y los Spare sobrantes (F17), el mapa del faro (F29) y el nombre único de $IN[227] (F36, hecho en oficina).

**Qué hacer.** Se atiende en F17, F29 y F36.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran F17, F29 y F36.

**Evidencia del programador.** La evidencia se registra en F17, F29 y F36.

**Depende de / se cierra con:** F17, F29, F36

**Nota.** Los inline forms estándar de KUKA (WAIT FOR, OUT) generan $IN[n]/$OUT[n] con el nombre en el form: no se reescriben a mano.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C24 — Los comentarios nombran la señal con su dirección

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** Cerrado - depuración

**Módulos:** `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/HOME.src`, `KRC/R1/Program/masref_user.src`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/Program/Utilities/closeandcheckallclamps.src`, `KRC/R1/Program/Utilities/openandcheckallclamps.src`, `KRC/R1/safetest.src`

**Qué está mal.** Los comentarios no nombraban la señal. La depuración comentó cada acción de E/S y cada espera con dirección y nombre (docs/IO_MAP.md), en inglés, y tools/check_cleanup.py verificó que cada nombre esté declarado en esa dirección.

**Qué hacer.** Nada. Mantener el formato en todo código nuevo o cambiado.

**Criterio de cierre** (se verifica en el respaldo):

* Toda acción de E/S o espera nueva o cambiada del respaldo tiene en las líneas de arriba un comentario con dirección y nombre declarado.
* Ningún comentario nuevo o cambiado escribe '$IN/$OUT[n] nombre' con un nombre no declarado en ese índice.

**Nota.** Solo verificación de regresión en cada respaldo.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C25 — Inline forms consistentes con el código

**Severidad:** - · **Tipo:** Código · **Responsable:** Programador robot · **Estado:** Se cierra con otro punto

**Módulos:** `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`

**Qué está mal.** El estándar pide que los inline forms coincidan con el código que generan. La depuración corrigió donde era seguro (form OUT 106 de RejectGE4, F20) y dejó ;WARNING: en el resto: parámetros ocultos AutomationCore (F21), parámetros ocultos GripperTech (F31, corregidos en oficina en picks y drop al conveyor) y líneas escritas a mano dentro de folds (F32, corregido en oficina).

**Qué hacer.** Se atiende en F21, F31 y F32.

**Criterio de cierre** (se verifica en el respaldo):

* Se cierra cuando se cierran F21, F31 y F32.

**Evidencia del programador.** La evidencia se registra en F21, F31 y F32.

**Depende de / se cierra con:** F21, F31, F32

**Nota.** El form OUT 106 de RejectGE4 ya corregido no debe volver a 5:TRUE.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C26 — Solo inglés en comentarios, títulos de fold y &COMMENT

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Programador robot · **Estado:** Cerrado - depuración

**Módulos:** `KRC/R1/cell.src`, `KRC/R1/System/sps.sub`, `KRC/R1/Program/Styles/style_1.src`, `KRC/R1/Program/Styles/Options/style1opt1.src`, `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`, `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`, `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`, `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`, `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`, `KRC/R1/Program/Utilities/RejectGE4.src`, `KRC/R1/Program/Centerline/PRELOAD.src`, `KRC/R1/Program/Centerline/Request_next_nut.src`, `KRC/R1/Program/Centerline/centerline_weld.src`, `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`, `KRC/R1/Program/HOME.src`, `KRC/R1/Program/masref_user.src`, `KRC/R1/Program/tm_useraction.src`, `KRC/R1/Program/Utilities/hometopounce.src`, `KRC/R1/Program/Utilities/pouncetohome.src`, `KRC/R1/Program/Utilities/hometorepair.src`, `KRC/R1/Program/Utilities/repairtohome.src`, `KRC/R1/Program/Utilities/gunelectrodechange.src`, `KRC/R1/Program/Utilities/closeandcheckallclamps.src`, `KRC/R1/Program/Utilities/openandcheckallclamps.src`, `KRC/R1/safetest.src`

**Qué está mal.** Había comentarios fuera de inglés. La depuración dejó comentarios, títulos de fold y &COMMENT en inglés; los identificadores mal escritos se renombraron en oficina (G15).

**Qué hacer.** Nada. Todo comentario, título de fold, &COMMENT y mensaje nuevo va en inglés.

**Criterio de cierre** (se verifica en el respaldo):

* No aparece texto en español en comentarios, títulos de fold o &COMMENT nuevos o cambiados del respaldo.
* Si se renombra un identificador del integrador, se renombra en la declaración y en todas sus referencias en el mismo respaldo, y los módulos compilan.

**Nota.** Los renombres de oficina (NUT_START, CameraJudgment, PartRejected, di227NutPresent1, carpeta Styles/Options) se prueban en la celda con G15.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C27 — Proceso controlado por robot no compartido; regla de dos procesos

**Severidad:** - · **Tipo:** Sin acción · **Responsable:** Ethos (Edgar) · **Estado:** No aplica

**Qué está mal.** Cumple: R10 hace manejo de material (no cuenta como proceso) y un solo proceso, la soldadura de tuercas en el pedestal CenterLine, que controla solo este robot.

**Qué hacer.** Nada.

**Criterio de cierre** (se verifica en el respaldo):

* Se reabre solo si R10 pasa de dos procesos o si otro robot empieza a usar el pedestal CenterLine.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).

---

## C28 — Ediciones del integrador en archivos del proveedor: listarlas en la entrega

**Severidad:** - · **Tipo:** Procedimiento · **Responsable:** Ethos (Edgar) / Programador robot · **Estado:** Abierto

**Módulos:** `KRC/R1/System/bas.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.src`, `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`, `KRC/R1/TP/GripperSpotTech/Grp_Func.src`, `KRC/R1/TP/GripperSpotTech/grp_user.src`, `KRC/R1/TP/BrakeTest/braketeststart.src`, `KRC/R1/TP/BrakeTest/braketestback.src`, `KRC/R1/TP/GLUETECH`, `KRC/R1/Program/MoveToPurge.src`

**Qué está mal.** El estándar pide paquetes del proveedor sin modificar. Hay ediciones del integrador en bas.src (TRIGGER AC_PointArrival en cada juego de parámetros PTP/LIN), automationcoreroutines.src (EndOfCycle sin Work Complete, F46; agua y faro; speed not 100; Stop_at_End_of_Cycle en MaintainSystem; request to enter con do930..932), Grp_Func.src (do121GripperFault), grp_user.src (do932GripperInProcess) y BrakeTest (do931, camino con tool 3 / base 1, F47). GlueTech está instalado sin uso (G05). Una actualización de paquete las borraría sin aviso.

**Qué hacer.** Mantener una lista de entrega con cada edición en archivos del proveedor (archivo, rutina o fold, qué cambia y por qué), incluidas las de oficina y las que agreguen otros puntos, y entregarla con el respaldo final.

**Criterio de cierre** (se verifica en el respaldo):

* Documento de entrega adjunto con las ediciones de la sección 'Integrator edits found inside vendor files' de docs/FINDINGS.md más las nuevas, cada una con archivo, rutina o fold, cambio y razón.
* En cada respaldo, todo cambio en archivos KUKA de sistema o de tech package (KRC/R1/TP/**, KRC/R1/System/ salvo $config.dat y sps.sub) o en machine data, respecto al último estado auditado, aparece en esa lista con fecha; un cambio sin listar reabre el punto.
* La versión final refleja lo decidido en F12, F46 y lo cambiado por C09, C12, C14, C19, C20, C22, F17, F36 y F47.

**Evidencia del programador.** Documento de entrega con fecha de la última revisión.

**Depende de / se cierra con:** F12, F46, C09, C12, C14, C19, C20

**Nota.** No es requisito deshacer las ediciones existentes, sino que queden listadas. Ediciones de oficina en archivos del proveedor: automationcoreroutines.dat (nombres do498/499/501..505, di466/467/470, di227NutPresent1, CameraJudgment, PartRejected). Agregarlas a la lista de entrega.

**Historial:**

* 2026-10-04 — Alta (Ethos): Revisión Ethos del respaldo 658424 (v431_03_10_r1.zip del 2026-10-02).
* 2026-10-05 — Auditoría - ediciones nuevas: Ediciones nuevas en archivos del proveedor: automationcoreroutines.src (AutomationCore_Bkg, AC_Request_to_enter), automationcoreroutines.dat (bACEntryGranted), nutweldroutines.dat (nMaxGunNr=1, dipw1_AirOK en $IN[3132]). Listarlas en la entrega.
* 2026-10-05 — Integrado - ediciones listadas: Ediciones del proveedor integradas y declaradas en tools/code_changes.json: automationcoreroutines.src/.dat, nutweldroutines.dat.
