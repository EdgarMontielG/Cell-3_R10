# Celda 3 — robot R10 (BMW-03-10-R1) — depuración y correcciones de la revisión Gestamp

KUKA KR C4, KSS 8.3.29, robot con número de serie 658424, línea BMW G65,
celda 03, estación 03-10-R1 (Gestamp: BMW-03-10R1). Proyecto WorkVisual
`V431-03-10R1_v6Active_Centerline_18`; el nombre del robot en el
controlador sigue siendo `V431_03_10_R1` (punto G01).

El robot toma la pieza GE4 de la estación 1 o 2 con el EOAT 1, la presenta
tres veces a un pedestal CenterLine de soldadura de tuercas por proyección
(timer Bosch, transductor LPT en la pistola), revisa las tres tuercas con
sensor y cámara, y deja la pieza en el conveyor o la rechaza. Es la misma
operación que el R20; la diferencia de proceso es la tuerca (M6/M8) y el
número de tuercas (tres en lugar de cinco). Los hallazgos conservan la
numeración del R20 para poder comparar los dos robots.

*English version: [README.md](README.md)*

## Estado

El programa ya corrió en producción y **no** ha sido aceptado por Gestamp.
Este repositorio contiene el respaldo del controlador tal como llegó
(commit `22a98cc`, respaldo `v431_03_10_r1.zip` del 2026-10-02), más una
depuración que cambia **lo que lee una persona, no lo que hace el robot**:

* comentarios, títulos de fold y `&COMMENT` en inglés, corregidos donde
  contradecían al código;
* cada acción de I/O y cada espera sobre una señal comentada con la
  dirección y el nombre de la señal — `;GUN OPEN - SIGNALS $OUT[472]
  dopw1_GunWork OFF, $OUT[471] dopw1_GunHome ON`;
* el encabezado estándar Gestamp en cada módulo del integrador, con la
  designación `BMW-03-10-R1` y el código de dispositivo (PNW1 pedestal,
  MH1 manejo de material);
* código basura eliminado: once módulos que nadie llama (21 archivos con
  sus `.dat`), código comentado, 856 declaraciones y puntos sin uso — cada
  módulo borrado y cada declaración eliminada aparece con su razón en
  `tools/cleanup_allowlist.json` y `tools/cleanup_allowlist.d/*.json`;
* trampas desactivadas o señaladas: un inline form cuyos datos ocultos
  convertían un reset en set (RejectGE4), los folds desactivados de los
  grippers 2-4, y líneas `;WARNING:` sobre folds que no deben reabrirse.

Los problemas de comportamiento encontrados **no se corrigieron** en la
depuración: requieren decisión del responsable y prueba en celda. Están en
**[docs/FINDINGS.md](docs/FINDINGS.md)** (en inglés, para poder enviarlo a
Gestamp o al programador): F01–F47 (dos críticos; F37 no aplica en el R10;
F44–F47 son solo del R10) y 28 puntos de cumplimiento Gestamp (C01–C28). El
código los referencia con comentarios `;CHECK: ... (Fnn)`.

El 2026-10-02 Gestamp revisó el programa y entregó 22 puntos para esta
estación (G01–G22, con el texto de Gestamp; verificación punto por punto en
FINDINGS.md). La lista de Calvin del 2026-10-03 también se verificó punto por
punto para el 10R1. Parte de los puntos de Gestamp se **corrigió en la
oficina** en un segundo paso que sí cambia código (ver *Correcciones de
oficina*): sin GOTO, nombres de señal en lugar de números de E/S, nut check
en una línea, gripper vacío revisado antes del comando de gripper,
parámetros ocultos de GripperTech corregidos, nombres en inglés, constantes
para los límites de carrera y las presiones, retry de soldadura muerto
eliminado y los TRIGGER de la siguiente tuerca fuera de los inline forms.
Falta probarlos en celda.

## Prueba de que el comportamiento no cambió

```
python3 tools/check_cleanup.py --head fb8a4c8
```

compara cada archivo KRL del commit de la depuración contra el respaldo
original (primer commit) después de quitar lo que el compilador ignora —
comentarios, líneas vacías, sangría. Lo que queda debe ser idéntico línea por
línea, salvo las eliminaciones listadas en el allowlist. También verifica
que:

* nada borrado o eliminado siga referenciado en código vivo;
* cada encabezado de inline form con datos del smartPAD siga sin cambios,
  al igual que las líneas dentro del form (solo se puede actualizar un
  nombre de herramienta viejo en el texto visible; el único cambio de datos
  de un form, en RejectGE4, está en el allowlist), y que las líneas
  `;Params` de AutomationCore no se hayan tocado;
* cada comentario que nombra una señal junto a una dirección nombre una
  señal realmente declarada en esa dirección;
* cada archivo conserve sus fines de línea (el respaldo mezcla archivos CRLF
  y LF) y siga en ASCII, y que la estructura de folds y bloques no quede
  peor que antes.

Si algo falla, termina con código de salida distinto de cero.

## Correcciones de oficina (revisión Gestamp)

El segundo paso cambia código, así que no se puede probar igual al respaldo.
En su lugar cada cambio se declara y se prueba que el resto no cambió:

```
python3 tools/check_equivalence.py [--diff]
```

compara cada archivo KRL contra el commit de la depuración después de quitar
comentarios y escribir cada nombre de señal como su dirección y cada
constante como su valor (`tools/renames.json`): los renombres desaparecen y
solo queda la lógica que cambió. Cada archivo cambiado, agregado, borrado o
movido tiene que estar en `tools/code_changes.json` con los puntos que
atiende; si no, falla. Los cambios y la prueba en celda que pide cada uno
están en los puntos abiertos (estado *Corregido en oficina - probar en
celda*) y en la sección 3 del PDF.

## Carga en el robot

La versión de oficina cambia código: hacer las pruebas en celda de los puntos
"Corregido en oficina - probar en celda" antes de producción. Es un cambio de
programa en una celda productiva:

1. Sacar un respaldo nuevo del robot. Si difiere del último respaldo auditado
   (hoy `bmw_03_10_r1.zip` del 2026-10-05, en `audits/`), alguien cambió el
   robot después — hay que auditar e integrar antes de cargar.
2. Generar el respaldo a cargar sobre el último respaldo auditado:

   ```
   python3 tools/build_archive.py <bmw_03_10_r1.zip> dist/
   ```

   genera `dist/658424_R10_AAAA-MM-DD_HHMM.zip` (fecha y hora del centro de
   México, igual que el Excel y el PDF).

   Copia el respaldo entrada por entrada, reemplaza los archivos
   modificados, omite los módulos eliminados, escribe los dos archivos de
   `Styles/optiones` en `Styles/Options`, agrega los módulos nuevos e imprime
   las listas; compara nombres sin mayúsculas, como el controlador. Solo
   acepta el respaldo original o uno auditado (su sha256 está en
   `audits/*/summary.json`); con cualquier otro, si un archivo que tendría que
   reemplazar u omitir no es el del respaldo 658424, se detiene sin escribir
   nada (ver paso 1). Ese zip es el registro completo de la versión; al
   programador se le entrega el paquete:

   ```
   python3 tools/make_package.py <respaldo auditado.zip> <zip de build_archive> dist/
   ```

   genera `dist/R10_paquete_AAAA-MM-DD_HHMM.zip`: solo los programas que
   difieren del robot, en sus carpetas del controlador, y `LEEME.txt` con las
   listas de reemplazar, agregar y borrar. Se carga por WorkVisual (proyecto
   abierto desde el robot, deploy), que además comprueba que compila. Hay que
   **borrar en el controlador los
   veintidós archivos marcados "left out"** (21 de la depuración, uno de las
   correcciones de oficina) **y la carpeta `Program/Styles/optiones`** — un
   restore no borra archivos que no vienen en el respaldo.
3. En el smartPAD, abrir una vez cada módulo modificado: sin error en el
   navegador y con los folds abriendo y cerrando normal.
4. Correr un ciclo productivo con override reducido en T1, luego en
   automático, y las pruebas en celda de las correcciones de oficina
   (sección 3.3 del PDF).
5. **WorkVisual.** Los proyectos que vienen dentro del respaldo
   (`C/KRC/User/ProjectRoot/...wvs`, también el nuevo `BMW-03-10R1_v8`)
   traen los archivos *viejos*, incluido `$config.dat` y los módulos
   borrados; el 2026-10-05 un deploy así regresó el programa original al
   robot. Al activar el proyecto se copian de vuelta al controlador si su
   checksum difiere. Antes de que alguien vuelva a hacer deploy desde
   WorkVisual, cargar el proyecto desde el controlador (o actualizarlo con
   estos archivos) y guardarlo; si no, el deploy restaura el programa viejo
   sin avisar.

No abrir ni confirmar inline forms viejos al editar comentarios en el
smartPAD (Cmd OK / Touch Up): varios traen parámetros ocultos que no
coinciden con el código (F21). Y no guardar la configuración de GripperTech
en el HMI hasta re-sincronizar `GripperConfig.xml` (F33).

## Estructura

```
KRC/, C/, Registry/, am.ini   el respaldo del controlador (depurado)
docs/FINDINGS.md              hallazgos y cumplimiento Gestamp - empezar aquí
docs/IO_MAP.md                el nombre de cada dirección usada en el programa
docs/CONVENTIONS.md           qué puede y qué no puede cambiar; formato de comentarios
tools/check_cleanup.py        prueba de que se cambiaron comentarios, no comportamiento
tools/cleanup_allowlist.json  los módulos borrados, cada uno con su razón
tools/cleanup_allowlist.d/    las demás eliminaciones ejecutables, con su razón
tools/check_equivalence.py    correcciones de oficina: diff de lógica sin renombres, todo cambio declarado
tools/code_changes.json       cada cambio de código posterior a la depuración, con sus puntos
tools/renames.json            identificadores renombrados y constantes para check_equivalence
tools/build_archive.py        genera el zip completo de la versión, sobre el último respaldo auditado
tools/make_package.py         genera el paquete para el programador: programas que cambian y lista de borrado
docs/open_items.json          lista maestra (G01-G22 de Gestamp, F01-F47, C01-C28), estado e historial
docs/OPEN_ITEMS.es.md         vista legible de los puntos abiertos (generada)
docs/PROCESO.es.md            el proceso diario de cierre y auditoría
tools/audit_backup.py         audita un respaldo diario contra el último estado auditado
tools/test_audit_backup.py    pruebas de la herramienta de auditoría
tools/make_items_xlsx.py      genera el Excel de puntos abiertos para el programador
tools/make_items_md.py        genera docs/OPEN_ITEMS.es.md
tools/make_report.py          genera el PDF (resumen, depuración, puntos abiertos, todos los comentarios)
dist/                         Excel y PDF generados (nombre con fecha y hora; tools/naming.py)
audits/                       una carpeta por respaldo auditado (AUDIT.md, summary.json)
```

`Log Files/` del respaldo original (bitácoras del KRC) no está en el control
de versiones; `build_archive.py` lo copia del zip original.

## Cierre de puntos abiertos

A partir de aquí el programador modifica el programa para cerrar los puntos
abiertos, actualiza la copia en Excel de la lista
(`dist/R10_Puntos_Abiertos_AAAA-MM-DD_HHMM.xlsx`) y al final de cada día manda
un respaldo completo del robot. Cada respaldo se audita con
`tools/audit_backup.py` contra el último estado auditado: qué cambió en el
código, si cada punto marcado como corregido cumple su criterio de cierre y si
se rompió algo más. Después se actualiza `docs/open_items.json`, se regeneran
el Excel y el PDF y se hace commit. El proceso está en
[docs/PROCESO.es.md](docs/PROCESO.es.md).

## Fuera de alcance

Los archivos de sistema de KUKA, los tech packages y las rutinas estándar de
Gestamp (AutomationCore, NutWeld, GripperTech, BrakeTest, GlueTech) no se
editaron, con estas excepciones: las partes del integrador en `$config.dat` y
`sps.sub` y los user hooks de KUKA `masref_user.src` y `tm_useraction.src` se
depuraron igual que los módulos del integrador; se eliminaron restos del
integrador sin uso en `$config.dat` y `automationcoreroutines.dat`; y se
editaron comentarios en `automationcoredata.dat`,
`automationcoreroutines.dat` y `nutweldroutines.dat`. Las correcciones de
oficina agregaron constantes y las señales del faro a `$config.dat` y
renombraron las señales del pedestal y de la cámara en
`automationcoreroutines.dat` (mismas direcciones, punto C28). Las rutinas del
proveedor (`TP/**/*.src`, `bas.src`) no cambiaron. Las modificaciones del
integrador encontradas *dentro* de esos archivos del proveedor — en
particular `EndOfCycle` sin Work Complete (F46) — se listan en
[docs/FINDINGS.md](docs/FINDINGS.md) para que una actualización de paquete no
las pierda sin que nadie se dé cuenta.
