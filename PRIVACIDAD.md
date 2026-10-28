# Política de Privacidad de Críptico Club

**Versión de revisión:** 28 de octubre de 2026
**Servicio:** Críptico Club — Discord Activity
**Idioma:** español · [English](../en/privacy/)
**Condiciones del Servicio:** [Consultar](../terminos/)

## 1. Responsable y contacto

El responsable del tratamiento de los datos gestionados por Críptico Club es **Antonio Pérez Serrano**, persona física, bajo la denominación comercial **Zerep Games**, que no constituye una sociedad independiente.

**Dirección facilitada por el titular:** Calle Licenciado Cascales, 30260, Murcia, España.

**Correo para consultas y ejercicio de derechos:** **zerep.a.p.s@gmail.com** (asunto recomendado: **«Support CripticoClub»**).

Discord trata los datos de su plataforma de acuerdo con su propia Política de Privacidad. No somos responsables del conjunto de tratamientos independientes realizados por Discord.

## 2. Qué información utilizamos

- **Identidad Discord:** ID de usuario estable, username, imagen de avatar y, cuando se autentique el acceso a un servidor, ID del servidor y pertenencia verificada. No solicitamos la contraseña de Discord ni leemos mensajes privados.
- **Juego:** idioma, reto diario, respuestas incorrectas, pistas empleadas, letras reveladas, puntuación, XP, rachas, historial y estadísticas necesarias para clasificaciones globales o por servidor.
- **Premium:** identificadores de SKU y de derechos de acceso comunicados por Discord, fechas de vigencia, renovación, revocación y última comprobación. No recibimos los datos completos de tarjeta bancaria.
- **Contribuciones:** texto del críptico, solución, explicación, idioma, dificultad, firma pública o anonimato, estado editorial, fecha de envío, revisión, notas del moderador y constancia de la licencia de uso aceptada. El username mostrado como firma puede quedar fijado según el valor existente al enviar.
- **Aceptación de condiciones:** identificador de cuenta, fecha y versión de las Condiciones aceptadas. El consentimiento contractual para publicar crípticos y autorizar posibles usos editoriales/entrenamiento de IA se diferencia de los permisos para tratar datos personales.
- **Datos técnicos:** identificadores aleatorios de petición, plantilla de ruta, método HTTP, estado, tiempos de respuesta, métricas agregadas y errores. La API está diseñada para evitar registrar tokens y Discord IDs en estos eventos; el proxy y los servicios externos podrían tratar dirección IP y otros metadatos técnicos.

Las fuentes tipográficas empleadas por el frontend están alojadas con la propia aplicación y no requieren Google Fonts.

## 3. Finalidades y bases jurídicas

| Finalidad                                                                                             | Base jurídica orientativa                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inicio de sesión, juego diario, progreso, perfil, rankings e historial                                | Ejecución del servicio solicitado (art. 6.1.b RGPD).                                                                                                       |
| Registro de aceptación de Condiciones, entrega y comprobación de ventajas Premium                     | Ejecución del contrato y, en su caso, cumplimiento de obligaciones legales (arts. 6.1.b y 6.1.c RGPD).                                                     |
| Recepción y revisión de propuestas presentadas voluntariamente, gestión de firma editorial y licencia | Ejecución de las condiciones de participación; para la atribución y difusión de identificadores, se valorarán las garantías pertinentes (art. 6.1.b RGPD). |
| Seguridad, prevención de abusos, diagnóstico y defensa de reclamaciones                               | Interés legítimo proporcionado (art. 6.1.f RGPD).                                                                                                          |
| Obligaciones tributarias, contables y solicitudes de autoridades competentes                          | Cumplimiento de obligaciones legales (art. 6.1.c RGPD), cuando existan.                                                                                    |

No utilizamos los datos de partidas para publicidad personalizada ni enviamos mensajes promocionales directos de Zerep Games. El acceso al juego no exige enviar propuestas.

## 4. Propuestas e inteligencia artificial

El envío de un críptico es voluntario. **Para enviar una propuesta es necesario aceptar una licencia de utilización de su contenido**, incluida la posibilidad contractual de un futuro uso del **texto del enunciado** para entrenamiento o mejora de modelos de IA, en los términos explicados en las Condiciones del Servicio. No es necesario enviar propuestas para jugar.

**No se ha activado el entrenamiento de modelos con propuestas de usuarios.** OpenAI es el proveedor previsto para una futura asistencia editorial; aún no se ha desplegado esa integración. Las entradas enviadas a la API de OpenAI no se usan por defecto para entrenar sus modelos, salvo habilitación específica del cliente.

Si se introduce un proveedor editorial externo, **solo se prevé remitir el texto del enunciado**, después de revisión y eliminación de datos personales detectables. No se prevé enviar el ID de Discord, username, avatar, solución, explicación ni otras referencias de cuenta. El contenido que introduzca un jugador puede incluir datos personales accidentalmente: **no se considerará anónimo sin una comprobación previa**.

La licencia de uso de una obra no sustituye la base jurídica necesaria para tratar datos personales que aparezcan en ella ni anula los derechos reconocidos por el RGPD. Si en el futuro se habilita un entrenamiento externo, se verificará antes su compatibilidad jurídica, contractual y técnica, sus condiciones y las garantías necesarias, y se actualizará esta Política cuando proceda.

## 5. Información visible para otros jugadores

En el juego podrán mostrarse rankings, resultados y estadísticas relacionadas con el username de Discord. Las propuestas pendientes y las notas internas de moderación no se hacen públicas.

Los crípticos publicados mostrarán por defecto el **username de Discord existente al enviar la propuesta**, salvo elección de anonimato previa al envío. Esta firma es una instantánea, no una clave de identificación del jugador; las relaciones internas se basan en el ID estable de Discord. Si cambia el username posteriormente, la firma de una publicación anterior no cambia automáticamente.

Cuando se elimine la cuenta, las propuestas conservadas se desvincularán del perfil y se retirarán los identificadores de autor accesibles por los procesos habilitados. Las versiones publicadas con firma editorial independiente pueden requerir intervención adicional. Las publicaciones ya difundidas en plataformas externas pueden subsistir en copias de terceros, sin perjuicio de las solicitudes legalmente procedentes.

No se revelará con antelación la fecha programada de un críptico aprobado; una aprobación no garantiza su publicación. Cuando existan avisos internos, se informará de su aprobación sin indicar la fecha de salida.

## 6. Proveedores y destinatarios

- **Discord:** autenticación, pertenencia a servidores, distribución de Activity, compra Premium, cobros y cancelación de suscripciones, conforme a sus propias condiciones.
- **Infraestructura de alojamiento:** despliegue proyectado en **Kubernetes en España**, con PostgreSQL en el clúster. Su administrador tendrá funciones de infraestructura; **el acceso a datos personales y credenciales deberá estar restringido mediante permisos específicos**, con controles verificables antes del lanzamiento.
- **Cloudflare:** previsto para **Tunnel, acceso público, proxy y funciones de protección como WAF**, según los servicios finalmente activados. Puede tratar metadatos de conexión que deben verificarse en la configuración real.
- **Grafana:** monitorización y visualización de métricas técnicas. Se prevé su uso como herramienta de observabilidad; no se incorpora analítica publicitaria de usuarios. Su modalidad de alojamiento y acceso deberán verificarse.
- **GitHub Pages:** alojamiento público de estas Condiciones y de la Política de Privacidad; su titular puede procesar datos técnicos de visitantes conforme a sus propias condiciones.
- **OpenAI:** proveedor **previsto, no integrado actualmente** para asistencia editorial de crípticos, bajo las limitaciones explicadas en el apartado 4.

Los accesos técnicos de colaboradores o proveedores se restringirán a lo imprescindible para la prestación del servicio. No vendemos datos de jugadores a anunciantes.

## 7. Transferencias internacionales

Discord, GitHub, Cloudflare u otros prestadores pueden participar en tratamientos fuera del Espacio Económico Europeo. El hecho de alojar PostgreSQL en España no garantiza por sí solo que todos los accesos o tratamientos permanezcan en España.

Antes de activar integraciones que supongan transferencias internacionales se verificarán las entidades proveedoras, los países implicados, los subencargados y las garantías exigibles, incluidas decisiones de adecuación o cláusulas contractuales cuando proceda. Puede solicitarse información sobre los proveedores efectivos a través del correo de contacto.

## 8. Conservación y eliminación

| Categoría                                          | Tratamiento y conservación                                                                                                                                                                                                                                                                            |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta, progresión y partidas                      | Se conservan mientras se necesita la cuenta para prestar el juego y se eliminan cuando el jugador utiliza el procedimiento autenticado de borrado, salvo obligaciones legales. **La eliminación automática tras 24 meses de inactividad es un criterio proyectado, no un proceso operativo todavía.** |
| Contribuciones pendientes                          | **Plazo editorial previsto: 90 días desde el envío** si siguen pendientes. La depuración automática por antigüedad todavía no está desplegada.                                                                                                                                                        |
| Contribuciones rechazadas                          | **Plazo editorial previsto: 30 días desde el rechazo**. La depuración automática todavía no está desplegada.                                                                                                                                                                                          |
| Contribuciones aprobadas, aún no publicadas        | **Plazo editorial previsto: hasta 12 meses desde la aprobación**. La depuración automática todavía no está desplegada.                                                                                                                                                                                |
| Contribuciones publicadas                          | El contenido puede conservarse durante la licencia de explotación vigente. Al eliminar una cuenta se desvinculan las propuestas de su autor; el tratamiento de firmas editoriales independientes aún necesita completarse.                                                                            |
| Notas de revisión editorial                        | Para propuestas publicadas, **30 días desde la publicación** como criterio previsto. Las notas de propuestas rechazadas se gestionarán conforme al plazo de estas. La rotación automática está pendiente.                                                                                             |
| Avisos internos de aprobación, rechazo o caducidad | **30 días desde la generación**, una vez se habilite la función de notificaciones. Actualmente la consulta del estado puede realizarse en la Activity, pero no se garantiza el envío automático de avisos.                                                                                            |
| Datos Premium                                      | La eliminación de cuenta suprime los registros de acceso de Críptico Club; **no cancela los pagos gestionados por Discord**. Los registros legalmente exigibles podrían conservarse durante sus plazos obligatorios.                                                                                  |
| Solicitudes de privacidad y soporte                | Criterio de conservación de **hasta 12 meses desde el cierre**, salvo que exista obligación legal, reclamación o controversia que justifique un plazo distinto.                                                                                                                                       |
| Logs, métricas y trazas técnicas                   | **Objetivo de rotación: 30 días**, pendiente de verificar en el despliegue, almacenamiento y agregadores.                                                                                                                                                                                             |
| Copias de seguridad                                | **Plan de una copia diaria**, con cifrado y rotación máxima de **30 días** dentro de la infraestructura prevista. Su implementación y restauración están pendientes de comprobación. Los datos borrados pueden persistir temporalmente en copias hasta su rotación.                                   |

No afirmamos que un proceso de eliminación automática no desplegado esté funcionando. Los plazos previstos se convertirán en compromisos operativos tras implementar y probar los correspondientes mecanismos.

## 9. Borrado de cuenta y derechos

En **Perfil → Ajustes** se incluye una opción **«Eliminar cuenta y datos»**, con confirmación. El borrado autenticado elimina los registros del jugador, su historial de partidas, XP, rachas, pertenencia vinculada, derechos Premium guardados por la aplicación y aceptaciones de Términos. **Los crípticos enviados pueden mantenerse sin relación con la cuenta ni firma dentro de las propuestas de moderación.** El vínculo con una versión editorial ya publicada puede necesitar un tratamiento adicional.

**Eliminar los datos de Críptico Club no cancela una suscripción Premium de Discord.** Para evitar nuevos cobros, cancélala también desde la sección de suscripciones de Discord.

Puedes solicitar acceso, rectificación, supresión, limitación, oposición y portabilidad cuando proceda, así como retirar consentimientos para tratamientos fundados realmente en consentimiento, enviando un correo a **zerep.a.p.s@gmail.com**. Podrá comprobarse de forma proporcionada la identidad del solicitante.

También puedes reclamar ante la [Agencia Española de Protección de Datos](https://www.aepd.es/).

## 10. Seguridad, cookies y tecnologías

El acceso se verifica mediante Discord y los controles de autorización del backend. Los tokens de sesión de la Activity están previstos para gestión temporal en memoria; no se solicita la contraseña de Discord. La aplicación utiliza identificadores técnicos y controles de integridad de peticiones y puntuaciones.

No se prevé analítica publicitaria propia, píxeles publicitarios ni perfilado comercial. Los servicios de Discord, Cloudflare, GitHub Pages y las funciones de seguridad pueden utilizar cookies u otros datos técnicos de acuerdo con sus propias políticas. La configuración real de cookies, almacenamiento, registros y conexiones se revisará antes de su lanzamiento definitivo.

## 11. Cambios en esta Política

Publicaremos una versión revisada cuando cambien de manera relevante las finalidades, los proveedores, los datos tratados o los plazos de conservación. Cuando sea legalmente necesario, informaremos y solicitaremos una nueva autorización antes del tratamiento correspondiente. Las versiones española e inglesa deben mantener el mismo contenido sustancial.

**Correo de contacto:** **zerep.a.p.s@gmail.com**
**Condiciones del Servicio:** [Consultar](../terminos/)
