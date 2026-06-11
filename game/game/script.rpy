### INICIO DE LA HISTORIA ### 
default leyo_diario = False

label splashscreen:
    scene black
    stop music
    pause 1.0

    show text "{size=+20}{color=#f00}ADVERTENCIA DE CONTENIDO{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pause 0.5

    show text "{i}Esta historia contiene temáticas adultas, situaciones de alta tensión emocional\ny escenas que pueden resultar sensibles para algunos jugadores.{/i}" at truecenter with dissolve
    pause 3.5
    hide text with dissolve
    pause 1.0

    show text "{size=-5}Este proyecto ha sido desarrollado de forma independiente.\nToda la parte gráfica y artística ha sido generada y editada mediante\nherramientas de Inteligencia Artificial (IA).{/size}" at truecenter with dissolve
    pause 3.5
    hide text with dissolve
    pause 1.0

    show text "{size=-5}Cualquier parecido con personas, hechos u organizaciones reales es mera coincidencia.{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    pause 1.5

    return

# Variable de nombre.
default nombreusuario = "Ellie"
image side pr = "side pr neutra"

default puntos_owen = 0
default puntos_finn = 0
default puntos_leonard = 0
default puntos_naomi = 0

label start:
    show screen phone_button

    scene black 

    play sound "audio/hojear_libro.ogg" # Opcional: sonido de abrir libro
    
    $ nombreusuario = renpy.input("Antes de comenzar el juego, ¿cuál es tu nombre?", length=12)
    $ nombreusuario = nombreusuario.strip()

    if nombreusuario == "":
        $ nombreusuario = "Ellie"

   
    with dissolve  

    # --- FLASHBACK --- #
    
    scene black
    pause 1.0

    "Los gritos ahogados retumbaron en mi cabeza."
   
    play sound "audio/puertametal.opus" 
    with hpunch 
    
    "El sonido metálico de una puerta de seguridad cerrándose de golpe me sobresaltó."
    "Y luego... el silencio denso de la sala de interrogatorios."
    "«Si hablas, te matan. Si te quedas, te matan igual.»"
    "Esa fue la última vez que usé mi verdadero nombre."

    # --- DESPERTAR EN EL AUTOBÚS --- #
    
    
    
label despertar_autobus:
    show autobus:
        blur 20
        linear 4.0 blur 0
    
    show image Solid("#000") as parpado at efecto_parpadeo
    play sound "audio/autobus.opus"

    "Un bache repentino en la carretera me sacude, haciéndome abrir los ojos poco a poco."
    "Mis manos están apretadas en puños y tardo un momento en darme cuenta de ello."

    play music "audio/musicaneutra.opus" fadein 2.0

    "Ni siquiera era consciente de la fuerza que ejercia en mi misma hasta que no vi las medialunas rojas que mis uñas habían dejado en mi palma"
    
    "Miro a mi alrededor, desorientada por una fracción de segundo."
    "Asientos de tela gastada. El zumbido constante del motor. Un olor desagradable a combustible viejo."

    "El recuerdo punzante de esa sala repleta de desesperación y desesperanza me carcome..."
    "Ya no estoy allí."
    "Estoy en un autobús interestatal, a cientos de kilómetros de lo que solía llamar hogar."

    pr neutra "Solo fue un sueño..."
    
    "El conductor carraspea por el altavoz del vehículo."
    "«Próxima y última parada: Residencial Sunrise. Asegúrense de no olvidar sus pertenencias.»"
    
    "Tomo mi mochila. Todo lo que tengo en el mundo ahora cabe ahí dentro."

    # --- LLEGADA AL COMPLEJO Y ENCUENTRO CON FINN --- #

    show autobus at efecto_caminar 
    
    pause 1.2

    scene edificios with dissolve

    "El aire frío de la tarde me golpea el rostro apenas pongo un pie fuera del autobús."
    "Camino un par de cuadras guiándome por las instrucciones que memoricé. No llevo GPS, no llevo mapas en el celular. Todo está en mi cabeza."
    "Dijeron que sería más fácil así, sin registros."
    
    "Finalmente llego a mi destino: un complejo de apartamentos de cuatro pisos, de paredes opacas en color tierra y suelos desgastados."
    "Un poco descuidado estéticamente, solitario."
    "Perfecto para desaparecer."

    "Parto rumbo al callejon. La mochila pesada sobre mis hombros me genera un esfuerzo extra."
    "Al subir las escaleras metálicas, un olor áspero a tabaco me recibe antes que cualquier otra cosa."

    scene cgpasillonocheoscura with dissolve

    "A unos metros, apoyado contra la pared y justo al lado de la que teóricamente sería mi puerta, hay un chico."

    scene pasillonocheoscuradesenfoque

    window hide

    show screen polaroid_finn

    pause

    window show
    scene cgpasillonocheoscura

    $ photo_1 = True

    show finnestandar with dissolve

    "Se ve pensativo, dando la última calada a un cigarrillo. El humo gris se disipa perezosamente en el aire frío."
    "Su postura es relajada, pero sus hombros están tensos. No puedo evitar fijarme de primeras en los tatuajes negros que resaltan su piel."

    "El sonido de mis pasos rompe el silencio."
    
    "Él gira la cabeza hacia mí y me da una rápida repasada de arriba a abajo."

    "Nuestras miradas se cruzan un instante."
    "Por alguna razón mi respiración se agita levemente."
    "No hay una sonrisa de bienvenida, ni sorpresa, ni siquiera curiosidad. Es una mirada pesada, neutra, completamente indescifrable."

    "Sin decir una sola palabra, deja caer la colilla al suelo y la apaga con la punta de su zapatilla."
    "Da media vuelta, abre la puerta del apartamento contiguo al mío y entra, cerrando tras de sí con un golpe seco."

    hide finnestandar
    with hpunch

    "Suelto el aire que no me había dado cuenta que estaba conteniendo y sonrío con ironía."
    pr duda "Sí, hola a ti también vecino nuevo."
    "Me acerco a mi puerta, primera del lado de las escaleras, segundo piso, así lo había memorizado. Saco la llave nueva y la introduzco en la cerradura."

    "Es hora de ver mi nuevo refugio."

    play sound "audio/puertaabrecierra.opus"
    scene bg_habitacion_oscura with fade


    "El interior está a oscuras y huele a encierro y a polvo."
    "Dejo caer la mochila al suelo con un ruido sordo. Me apoyo contra la puerta cerrada y me deslizo hasta sentarme en el suelo."

    "Es oficial."
    "Realmente estoy aquí."

    # --- 5. LA LLAMADA TELEFÓNICA ---

    "El silencio de la habitación se rompe de golpe."

    play sound "audio/celuvibrando.opus"

    "Mi teléfono nuevo empieza a vibrar en mi bolsillo."
    show telefonollamada with moveinbottom
    "Lo saco. La pantalla ilumina la oscuridad con un mensaje simple:"
    "Llamada entrante: Número Privado."

    "Dudo un segundo. Sé perfectamente quién es. Deslizo el dedo por la pantalla y me llevo el aparato a la oreja."

    pr "Estoy aquí."

    bl "Hey, ¿Cómo ha ido el viaje? ¿Pudiste entrar al complejo?"

    "La voz de Bel al otro lado de la línea es suave, profesional. Demasiado tranquila para alguien que maneja vidas como si fueran piezas de ajedrez."

    pr "Sí. Normal. Acabo de entrar al departamento."

    bl "Perfecto. Recuerda, [nombreusuario], el programa cubre el alquiler de tu residencia por los próximos tres meses. Luego de ese tiempo, estás por tu cuenta."
    bl "Necesitas conseguir un trabajo pronto para mantener la fachada."

    pr "Lo tengo claro. La universidad, un trabajo de medio tiempo, no llamar la atención."

    bl "Bien. Tus documentos físicos llegarán mañana a primera hora. Por lo pronto, ya estás inscrita en el sistema del Sunrise College."
    bl "Solo tienes que pasar por administración a buscar tu horario definitivo."

    pr "Entendido."

    "Hay una pequeña pausa en la línea. El tono de Bel se vuelve un poco más suave, más humano."

    bl "Escucha... sé que es abrumador. Borrón y cuenta nueva, es fácil decirlo, pero vivirlo es otra historia."
    bl "Por nada del mundo debes hablar de lo que sucedió. Con nadie. Hasta que estés completamente fuera de peligro, tu vida anterior no existe."

    pr "Lo sé, Bel. Mi vida anterior murió el día del juicio."

    "Por fuera del departamento se escuchó a lo lejos el ruido de unas motocicletas derrapando."
    "Sabía que no viviría en un complejo de lujo, tampoco creía que se tratara de un lugar de mala muerta, sin embargo debía procurar no rondar por la calle una vez que el sol bajara. Por precaución."

    bl "Descansa. Intenta... intentar vivir una vida normal a partir de mañana."

    "Y con esas palabras, la llamada se corta."
    hide telefonollamada with moveoutbottom
    "«Una vida normal...»"
    "Me quedo mirando la pantalla negra del teléfono. Luego miro la habitación vacía."

    pr "Vida normal... Pan comido."

    window hide
    with dissolve

    show screen morning_transition(u"A la mañana siguiente...")
    
    $ renpy.pause(4.0, hard=True)

    scene bg_universidad_exterior
    
    hide screen morning_transition
    with dissolve

    

    "El chirrido de las puertas del autobús al abrirse me dejan via libre a mi primer día en el mundo real."
    
    "Miro la tarjeta de plástico que sostengo en mi mano derecha. Es nueva, los bordes aún están afilados. Tiene una foto mía, pero el nombre y el número de seguro social me son extraños aún."
    
    pr "Oficialmente soy [nombreusuario]. Estudiante de primer año."
    "Me surge la pequeña curiosidad de saber cómo habrían logrado formar una identidad nueva desde cero."
    "Se sentía ilegal, pero no lo era."
    "O eso pensaba, es decir, el programa de protección a testigos se había encargado de todo el papeleo técnico."
    "Ni siquiera pude elegir mi nombre."
    
    "Guardo la identificación en el bolsillo interior de mi chaqueta, cerca del pecho, y observo el Sunrise College mientras alejo aquellos pensamientos divagantes."
    "No era una de esas universidades de Élite, con estatuas y decoraciones florales como las que ya había visto en el pasado, pero era moderna, de ladrillos claros, funcional y, sobre todo, masiva."
    scene entradauni with fade
    "Un océano de estudiantes camina en todas direcciones, charlando, tomando café, existiendo sin preocupaciones. O fingiendo no tenerlas."
    "Es el lugar perfecto para ser una gota más en el agua."

    # --- ADMINISTRACIÓN Y OWEN ---
    
    scene administracion with fade

    "Entro a la puerta de cristal doble que reza: «Administración Estudiantil»."
    "El sonido de una impresora atascada y el olor a café recién preparado inundan mis sentidos."

    show dianaenojo at medio_izq with easeinleft 

    "Una chica de piel morena y rizos salvajes gruñe mientras golpea el lateral de una fotocopiadora gigante."
    
    misterio "¡Mierda! ¡Tengo cincuenta expedientes que imprimir antes del mediodía!"

    "En contraste con su caos absoluto, un chico de cabello castaño revuelto y lentes de armazón negro está sentado cómodamente en un escritorio cercano, balanceándose en su silla."
   
    hide dianaenojo with Dissolve (0.08)
    scene administraciondesenfoque
    window hide
    show screen polaroid_owen
    pause
    window show
    scene administracion
    $ photo_2 = True
    show owenneutro at medio_der with easeinright
    show dianaenojo at medio_izq with easeinleft

    misterio "La violencia física no resolverá tus problemas, mi querida Diana. Solo la paciencia... o un técnico en sistemas de verdad."

    dn "Owen, cállate."
    
    
    hide dianaenojo with Dissolve (0.05)
    "El chico, Owen, se encoge de hombros con una sonrisa divertida. Al girar la cabeza, finalmente nota mi presencia en la entrada."
    hide owenneutro with Dissolve (0.05)
    show owenfeliz at medio_der with Dissolve (0.08)

    "Sus ojos detrás de los lentes se iluminan con genuina curiosidad y me dedica una sonrisa amplia, simpático."

    ow "¡Tenemos gente! Y por la cara de confusión diría que eres recién llegada, ¿Me equivoco?"

    "Su tono es casual y cálido. Demasiado amigable para el nivel de alerta constante al que últimamente me he acostumbrado."

    pr "Buen día... Vengo a buscar mi horario de clases."

    ow "Has venido al lugar indicado. Aunque si esperas que Diana te lo imprima en papel, quizás te gradúes antes de que ese dinosaurio vuelva a funcionar."

    show dianaenojo at medio_izq with hpunch

    "Se escuchó el gruñido bajo de Diana, quien ajena a nuestra conversación continuaba revisando a regañadientes la impresora."
    "Owen ríe por lo bajo, un sonido ligero y contagioso. Se levanta de la silla y se acerca al mostrador frente a mí, apoyando los codos con familiaridad."

    hide dianaenojo with Dissolve (0.08)
    show owenfeliz at center with ease
    
    ow "Soy Owen. Estudiante de segundo año y, aparentemente, asistente no remunerado de aquella loca."
    "Con sus ojos señala en dirección a la morena."
    ow "No por voluntad propia."
    
    pr "Soy [nombreusuario]."

    ow "Un gusto."
    ow "Y dime, ¿Qué carrera estudias?"

    pr "Tecnología e Ingeniería."

    ow "¡No me digas! Estamos en el mismo barco entonces. Ya decía yo que tenías aura de genio informático."

    "Se inclina un poco más hacia adelante, acortando sutilmente la distancia. Su actitud es coqueta, pero de una forma tan natural e inofensiva que, lejos de intimidarme, me descoloca un poco."
    
    ow "¿Sabes qué? Déjame ahorrarte todo el papeleo innecesario."
    
    "Toma una tablet del mostrador y teclea un par de cosas rápidamente."

    ow "Dame tu correo electrónico y te envío tu horario digitalizado directo a tu teléfono. Es más rápido."

    show dianaenojo at left with Dissolve (0.08)
    
    "Diana suspira rendida desde el fondo, secándose una gota de sudor imaginaria de la frente."

    hide dianaenojo with Dissolve (0.08)

    "Dudo un segundo, pero saco mi teléfono nuevo y le dicto la dirección de correo electrónico que habían creado para mi."
    
    $ mail_1 = True
    $ mail_notification = True
    play sound "audio/notificacion.opus"
    show screen mail_notification
    
    "Casi al instante, mi teléfono vibra."
   
    pr "Llegó. Gracias, Owen."

    ow "Un placer, [nombreusuario]. Oye, si tenemos suerte, tal vez compartamos alguna clase de tronco común."

    pr "Tal vez."

    "Guardo el teléfono, sintiendo una extraña ligereza. Por un minuto, solo un minuto, me sentí como una estudiante normal hablando con un chico normal."

    # --- LA SALIDA DE ADMINISTRACIÓN Y LA PRIMERA ELECCIÓN ---
    
    hide owenfeliz
    with dissolve

    "Me despido con un asentimiento y doy media vuelta hacia la salida."

    "Antes de cruzar la puerta, reviso el archivo en mi teléfono. 'Matemática general, Aula C'. "
    "Alzo la vista. A través del cristal, el campus de repente parece un laberinto de pasillos idénticos y estudiantes apresurados."

    "Un pequeño suspiro escapa de mis labios."

    show owenfeliz with easeinright

    ow "¿Estás bien? Tienes cara de no saber dónde te encuentras parada."

    "Me giro sorprendida. Owen ya no está en el escritorio; se ha colgado su mochila al hombro y está de pie a un par de metros de mí."

    pr duda "¿Tan obvia soy?"

    ow "Un poco. Dime, ¿Dónde es tu próxima clase?"
    "Le muestro mi horario desde el celular, Owen acercó su rostro para leer la letra chica y asintió para sí mismo."
    ow "Tengo un hueco libre y estaba a punto de ir a la cafetería que está justo en esa dirección. ¿Quieres que te muestre el camino? Prometo no cobrar por el tour."

    # --- PRIMERA ELECCIÓN DEL JUGADOR ---

    "La oferta es tentadora, dudo un momento antes de responder."
    hide owenfeliz with Dissolve (0.08)

menu:

        "Está bien, es una cita.":
            $ owenbiblio = True
            $ puntos_owen += 5
            jump eleccion_owen_cafe

        "Te lo agradezco mucho, Owen. Pero creo que prefiero perderme un par de veces. Necesito memorizar el campus por mi cuenta.":
            $ owenbiblio = False
            $ puntos_owen += 1
            jump eleccion_sola_amable
            
        "No. Gracias. Estoy bien, encontraré el camino yo sola.":
            $ owenbiblio = False
            jump eleccion_sola_fria



# ------------------------------------------------------------------
# -- RAMA 1: ACEPTA IR CON OWEN
# ------------------------------------------------------------------
label eleccion_owen_cafe:
    
    show owenfeliz at center with Dissolve (0.08)
    "Digo a modo de broma, dejando que mi comisura derecha se elevara en una media sonrisa."
    "Veo como un brillo juguetón ilumina la mirada de Owen."
   
    show owenfeliz:
        center
        zoom 1.0
        ease 0.25 zoom 1.18 yoffset 180

    ow "Esto escaló rápido, me veo en la obligación de advertirte que no beso hasta la tercera cita, así que no intentes nada, te estaré vigilando."
    play sound "audio/protarisa.opus"
    "Se me escapó una pequeña y genuina carcajada."
    
    hide owenfeliz with Dissolve (0.08)
    scene entradauni with fade

    "Caminamos juntos por el campus. El aire de la mañana es fresco y el bullicio de los estudiantes amortigua aquél lado de mi mente que no ha dejado de sobrepensar en todo desde la mañana."
    "Owen resulta ser una compañía muy fácil. Habla lo justo para llenar los vacíos, señalando los puntos clave de la universidad con comentarios sarcásticos."
    
    scene campus with Dissolve (0.12)
    show owenfeliz at center with Dissolve (0.12)

    ow "Ahí a la derecha está la biblioteca. El mejor lugar para dormir si no te importa el olor a desesperación por los exámenes."
    
    pr sonrisa "Lo tendré en mente."

   
    "Me sorprendo a mí misma sonriendo ligeramente. Por un instante, la paranoia retrocede. Soy solo una chica de primer año yendo a su primera clase con un compañero agradable."
   
    scene pasillo with Dissolve (0.12)
   
    "Entramos a uno de los edificios cercanos, un imponente pasillo con varias puertas de roble nos da la bienvenida. Owen se detiene."
    show owenfeliz with Dissolve (0.5)
    ow "Aquella es el aula C. Tengo una cita muy importante con los muffins de la cafetería, así que nuestros caminos se separan aquí."

    pr sonrisa "Gracias, Owen. De verdad."

    ow "No hay de qué, [nombreusuario]. Sobrevive a tu primer día."

    hide owenfeliz with Dissolve (0.8)
    
    "Con un gesto desenfadado de la mano, se aleja por la misma puerta que entramos. Lo observo un segundo antes de cruzar al salón, sintiéndome un poco más anclada a esta nueva realidad."
    
    jump llegada_clase

# ------------------------------------------------------------------
# -- RAMA 2: RECHAZA AMABLEMENTE
# ------------------------------------------------------------------
label eleccion_sola_amable:
    "La sonrisa de Owen dejó de sentirse coqueta para volverse más cordial."

    show owenneutro at center with Dissolve (0.08)

    ow "Tiene sentido. La mejor forma de aprender a nadar es saltando al agua, ¿no?"

    ow "Si te sirve de pista: al salir de administración, gira a la derecha y continúa recto hasta cruzar el patio del campus. No tiene pérdida."

    pr "Derecha y recto. Entendido. Gracias."

    ow "¡Suerte en tu primer día, [nombreusuario]!"

    hide owenneutro with Dissolve (0.08)
    scene entradauni with fade

    "Salgo de la oficina y respiro hondo. Navegar sola por este mar de gente me pone en alerta, pero es estrictamente necesario."
    "Sigo las instrucciones de Owen. Mi mirada escanea inconscientemente a cada persona con la que me cruzo, buscando amenazas donde probablemente solo hay estudiantes con sueño."
    "Pienso a la vez que camino, ¿Llegará el día en que mi estado de alerta disipe y pueda pasar un día sin pensar en inminente peligro?"
    "Tal vez solo necesito darme tiempo."
    "O tal vez jamás vuelva a ser la chica que una vez fuí."
    "Suspiro derrotada."
    scene pasillo with fade
    "Finalmente, el aula C aparece frente a mí."

    jump llegada_clase

# ------------------------------------------------------------------
# -- RAMA 3: RECHAZA FRÍAMENTE
# ------------------------------------------------------------------
label eleccion_sola_fria:
    show owenincomodo with Dissolve (0.12)
    "Aprieto la correa de mi mochila instintivamente, dando medio paso hacia atrás y alzando un muro invisible."
    "Mi respuesta suena más brusca de lo que pretendía. Owen hace una pequeña pausa, tomado por sorpresa, y desvía la mirada hacia un costado aparentemente incómodo, antes de recomponerse con rapidez."
    hide owenincomodo with Dissolve (0.08)
    show owenneutro with Dissolve (0.08)
    ow "Oye, sin problema. Solo intentaba ayudar. El Edificio C está cruzando el patio central."
    "Dude un momento antes de contestar, el pensamiento de haber sido muy brusca cruzó por mi mente y vacilé."
    "Sintiendome algo culpable le sonreí forzadamente por un segundo"
    pr "Gracias."

    scene entradauni with dissolve

    "Doy media vuelta y salgo a paso rápido. Siento su mirada en mi espalda por unos segundos, y me castigo mentalmente."
    "No vine aquí a hacer amigos. Cada persona que me conozca es un riesgo potencial. Cada vínculo es un hilo del que alguien de mi pasado podría tirar."
    "¿Estaba siendo paranóica?"
    "¿Por qué tenía esta extraña sensación de vértigo? Como si alguien en cualquier momento fuera a señalarme con el dedo al grito de 'impostora'."
    "Respiro hondo, intentando regularizarme, mi corazón latia con fuerza y todo a causa unicamente de mis pensamientos."
   
    scene pasillo with fade 
   
    "Me pierdo un par de veces por culpa de los nervios, pero finalmente logro encontrar el pasillo correcto."
    "Más me valía encontrar algo para hacer antes de que mi mente volara a lugares no deseados nuevamente."

    jump llegada_clase

# ------------------------------------------------------------------
# -- PUNTO DE ENCUENTRO: LA CLASE
# ------------------------------------------------------------------
label llegada_clase:
    scene clase with fade
    
    "Empujo la pesada puerta de madera del aula. El sonido de los alumnos instalándose en sus pupitres y abriendo sus laptops llena el espacio."
    "Tomo aire una vez más, caminando hacia un asiento vacío en las filas del fondo."
    "Es hora de empezar."

    # --- PRIMERA CLASE Y LA PRESENTACIÓN DE LEONARD ---

    "Me acomodo en un asiento de la penúltima fila. Desde aquí tengo una vista clara de la puerta y de casi todos los alumnos. Vieja costumbre, instinto de supervivencia."
    "El murmullo general es ensordecedor hasta que un chico entra al aula y, por el rabillo del ojo, noto cómo desentona con el resto."
 
    scene clasedesenfoque
    window hide
    show screen polaroid_leo
    pause
    window show
    scene clase
    $ photo_3 = True
    show leoneutro at entrar_derecha

    "Es rubio, lleva una camisa perfectamente planchada bajo un suéter de punto impecable. Ni una sola arruga. Destaca enormemente entre el mar de sudaderas enormes y camisetas gastadas de los demás estudiantes."
    "Camina con paso medido, casi rígido, buscando un lugar. Sus ojos escanean los asientos vacíos y se dirigen hacia mi fila."

    "Se detiene justo en el pupitre vacío a mi derecha."

    hide leoneutro with Dissolve (0.08)
    show leoapenado with Dissolve (0.08)

    ln "Disculpa... ¿está ocupado?"

    "Su voz es baja, suave, casi ahogada por el ruido del aula. Evita el contacto visual directo, fijando su vista en la superficie del escritorio."

    pr "No. Está libre."

    ln "Gracias."

    hide leoapenado with Dissolve (0.08)

    "Se sienta con un cuidado extremo. Saca de su mochila una laptop reluciente, un cuaderno de notas inmaculado y tres bolígrafos."
    "Los alinea meticulosamente sobre el borde de la mesa, paralelos entre sí. A la misma distancia unos de otros."
    "Observo la escena de reojo. Hay algo fascinante en su necesidad de control y orden. Me pregunto si, al igual que yo, está intentando mantener a raya su propio caos interno."

    pr duda "¿Tres boligrafos?"

    "La pregunta sale de mis labios en un susurro antes de que pueda detenerlo."

    show leoapenadox2 with Dissolve (0.08)
    
    "El chico rubio se congela. Finalmente me mira. Sus ojos son claros y reflejan un pánico momentáneo, como el de un ciervo atrapado en los faros de un coche."

    ln "Yo... eh... es por si alguno se queda sin tinta o se me pierde."
    "Me apené al escucharlo explicarse."

    pr "Lo siento, no quería inmiscuirme. Soy [nombreusuario]."

    ln "Leonard. Pero... Leo está bien."

    hide leoapenadox2 with Dissolve (0.08)

    "Vuelve a desviar la mirada rápidamente hacia la pizarra en blanco del frente. Sus mejillas han tomado un ligero tono rosado."
    "Es tímido. Extremadamente tímido. Y claramente no es de los que disfrutan la charla casual o las interacciones inesperadas. Al menos esa era mi primera impresión."

    "El profesor entra al aula en ese momento, dejando caer un pesado maletín sobre el escritorio principal."
    "Leo exhala lentamente, pareciendo aliviado de que la clase haya comenzado y ya no tenga la obligación social de interactuar."
    "Los murmullos bajan de golpe. En el pizarrón aparece una ecuación extensa."
    "Matemáticas, perfecto. Mi materia favorita."
    "Mentira."
    "El profesor comienza a explicar con la velocidad de alguien convencido de que todos comprenden."
    "Las letras se mezclan frente a mis ojos. Variables, límites, funciones..."
    "En algún punto podría estar escribiendo una receta para invocar demonios y me resultaría igual de lógico."
    "Intento seguirle el ritmo a la clase, incluso pongo toda la voluntad en prestar atención."
    "El profesor deja la tiza."

    show profe with Dissolve (0.12)
    profesor "Si aplicamos derivación implícita aquí… ¿cuál sería el resultado?"
    hide profe with Dissolve (0.08)

    "El aula se llenó de silencio y suspiré aliviada de no ser la única que no tenía idea."
    "Una chica adelante duda, responde la pregunta con indesición."
    "Está mal."
    "Y entonces escucho una voz a mi lado, suave, casi imperceptible."

    show leoneutro with Dissolve (0.08)
    ln "Dos x más y prima."
    
    "Parpadeo y miro de reojo, Leo tiene la vista fija al frente, una mano apoyada junto al teclado, la otra sosteniendo el bolígrafo."
    "No me está hablando, tampoco le está hablando al profesor, solo lo dijo en voz baja, convencido tal vez de que nadie lo oía."
    "El profesor escribe la resolución en la pizarra al cabo de un momento sin obtener una respuesta acertiva, dos x más y prima."

    "Mi mirada vuelve lentamente hacia Leo, no reacciona, ni siquiera cambia de postura."
    hide leoneutro with Dissolve (0.08)
    "El profesor continúa."
    show profe with Dissolve (0.08)
    profesor "Bien. Entonces… si despejamos esta función, ¿qué límite obtenemos?"
    hide profe with Dissolve (0.08)

    "Más silencio, una respuesta equivocada al fondo y el rostro del profesor parecía descomponerse poco a poco."
    "Leo gira apenas la lapicera entre los dedos."
    show leoneutro with Dissolve (0.08)
    ln "Cero."

    "Otro murmullo, tan bajo que probablemente nadie más lo escucha, excepto yo que, sin darme cuenta, comenzaba a prestarle más atención de la debida."
    "El profesor niega otra respuesta de algún estudiante y escribe cero en el pizarrón."
    "Mi mirada va desde la respuesta escrita hasta el rubio con expresión casi desinteresada, como quien supiera ya de antemano todo lo que se está explicando."
    hide leoneutro with Dissolve (0.08)
    "El profesor vuelve a lanzar otra pregunta."
    show profe with Dissolve (0.08)
    profesor "¿Y la derivada de esto?"
    hide profe with Dissolve (0.08)
    "Ni siquiera podía comprender a que se refería cuando decía 'esto', mi cerebro se había rendido ante la eminente realidad, sin embargo, no pude evitar fijar mi vista en cierto rubio esperando inconscientemente que diga la respuesta." 
    show leoneutro with Dissolve (0.08)
    ln "Tres por x al cuadrado."

    "Evidentemente la dijo y unos segundos después el profesor escribe exactamente eso."
    "Mi boca se mueve antes de que pueda detenerme."

    pr admiracion "…brillante."

    "Se escapó de mi boca antes de que pudiera parar a pensar, casi con admiración, mi voz al igual que la de él era bajita pero al parecer, no lo suficiente."
    "Leo gira la cabeza y nuestros ojos se cruzan."

    hide leoneutro with Dissolve (0.08)
    show leoapenadox2 with Dissolve (0.08)

    "Es apenas un segundo, pero lo veo."
    "El desconcierto y la sorpresa tiñen su rostro con un leve sonrojo que fue tomando potencia en menos de un segundo, como si acabara de recordar que existe gente a su alrededor."
    "Desvía la mirada inmediatamente y esta vez es mi rostro el que se tiñe de rojo vergüenza."
    hide leoapenadox2 with Dissolve (0.08)
    show leoapenado with Dissolve (0.08)
    "A riesgo de parecer una acosadora no puedo desviar la mirada al notar que su mano acomoda uno de sus bolígrafos y luego el otro, seguido vuelve a alinear los tres, visiblemente nervioso."
    "Bajo la vista de golpe hacia mi cuaderno"
    hide leoapenado with Dissolve (0.08)
    "Durante el resto de la explicación no vuelve a decir nada, me castigo mentalmente por haber provocado esa reacción."
    "La tiza vuelve a chirriar contra el pizarrón durante varios minutos más hasta que finalmente el profesor da por terminada la clase."
    show profe with Dissolve (0.08)
    profesor "Eso será todo por hoy. Revisen el material y practiquen los ejercicios para la próxima clase."
    hide profe with Dissolve (0.08)
    "Los alumnos se levantan al instante, el salón se vuelve una sinfonía de sillas arrastrándose y conversaciones retomándose."
    "A mi lado Leo guarda sus cosas con la misma precisión de antes, aunque esta vez parece hacerlo más deprisa."
    "Laptop, cuaderno, bolígrafos. Todo desaparece dentro de la mochila en cuestión de segundos."
    "Como si quisiera huir del salón cuanto antes."
    "Y por alguna razón... eso me hace querer decir algo."

    menu:
        "Romper el silencio":
            $ puntos_leonard += 3
            jump leo_hablar

        "Dejarlo ir":
            jump leo_callar


label leo_hablar:

    pr sonrojo "¿Leo?" 

    "Una vez más mi boca traicionera le gana terreno a mi cerebro."
    "Él se detiene en seco al instante."

    show leoapenado with Dissolve (0.08)

    "Su mano queda suspendida a mitad de camino sosteniendo el cierre de la mochila."
    "Me mira entre expectante y claramente nervioso."

    hide leoapenado with Dissolve (0.08)
    show leoapenadox2 with Dissolve (0.08)

    pr sonrojo "Lo de antes..."

    "Vacilo, de repente la oración entera me parece una pésima idea."

    pr sonrojo "Lo siento, no pretendía ser entrometida."

    pr sonrisa "Hubieras destacado si el profesor tuviera un super oído, pareces no necesitar esta clase."

    hide leoapenadox2 with Dissolve (0.08)
    show leoapenado with Dissolve (0.08)

    "Sus pestañas parpadean una vez, luego baja la mirada. Me maldigo internamente, no solía tomar la iniciativa pero la timidez de este muchacho parecía desatar mi lengua de una forma incontrolable."

    ln "No estaba…"

    ln "No estaba intentando responder."

    pr sonrisa "Lo sé."

    "Una sonrisa incómoda apenas me tira de la boca. Leo ajusta el agarre sobre la correa de su mochila y cuando creo que simplemente me va a ignorar su voz suave vuelve a recitar."

    ln "Igual…"

    ln "Gracias."

    "Leo asiente apenas."

    ln "Nos vemos."

    hide leoapenado with fade

    "Y sale del aula antes de que pueda volver a hablar, lo veo desaparecer por la puerta y me descubro mirando el espacio vacío que dejó atrás durante más tiempo del necesario."

    jump despues_leo


label leo_callar:

    "Decido no decir nada. Probablemente ya lo avergoncé suficiente por un día."
    "Leo termina de guardar todo y se pone de pie."

    show leoapenado with Dissolve (0.12)

    "Por un segundo creo que se va a ir sin mirar atrás, pero justo antes de girar hacia la puerta sus ojos claros se desvían apenas hacia mí."
    hide leoapenado with Dissolve (0.08)
    show leoapenadox2 with Dissolve (0.08)
    "Solo un instante, un segundo breve, casi dudoso."
    "Como si estuviera considerando decir algo pero obviamente no lo hace."
    "Solo inclina levemente la cabeza a modo de despedida, un gesto mínimo. Y luego se va."

    hide leoapenadox2 with fade

    "El aula se vacía poco a poco, guardo mis pertenencias antes de marcharme."

    jump despues_leo


label despues_leo:
    
    "Suspiro, primera clase superada. Aún tengo un par de horas libres antes de la siguiente."
    if owenbiblio:
        "Owen mencionó que la biblioteca era un buen lugar para esconderse... y la verdad, un poco de silencio es justo lo que necesito ahora mismo."
    else:
        "Pienso por un momento cuál seria el sitio ideal para esconderse por un rato, me decido por la biblioteca, silencio y calma es justo lo que necesito ahora mismo."

    # ---  FIN DE LA CLASE Y TRANSICIÓN ---

    scene black with dissolve
    pause 1.0

    jump llegada_biblioteca

# ------------------------------------------------------------------
# -- LA BIBLIOTECA Y NAOMI
# ------------------------------------------------------------------
label llegada_biblioteca:
    scene bg_biblioteca with fade

    "El ambiente en la biblioteca es radicalmente distinto, percibo un aromatizante de coco y el sutil sonido de las páginas al pasar."
    "Camino entre las altas estanterías buscando un rincón apartado. No me gustan los espacios abiertos donde cualquiera puede acercarse por la espalda."

    "Encuentro un asiento perfecto: un puff ligeramente desgastado junto a una gran ventana que da a los jardines traseros."
    "Me dejo caer en él con un suspiro de cansancio, un rayo de sol me calienta al instante de forma agradable."

    "Al acomodarme, mi mano roza algo duro en el suelo."
    show cuaderno with moveinbottom
    "Es un cuaderno de cuero negro. No parece un material de estudio normal, esta un poco desgastado en los bordes."

    # --- 11. EL DIARIO EN LA BIBLIOTECA Y EL BAÑO ---

    "Lo levanto con cuidado. No tiene nombre en la tapa. Lo abro por inercia y hojeo un par de páginas rápidamente."
    "Está lleno de caligrafía apretada, tachones y algunos bocetos. Es claramente un diario íntimo. Lo cierro de golpe."

    pr "No es asunto mío."

    hide cuaderno with moveoutbottom

    "Lo guardo en mi mochila. Luego lo dejaría en la oficina de objetos perdidos o en administración."
    "Decido hacer una parada en el baño antes de mi siguiente clase."

    show bg_biblioteca at efecto_caminar 
    
    pause 1.2

    scene bg_bano with Dissolve (0.12)

    "Cuando llego lo noto vacio, el desinfectante industrial me agolpa en la nariz. Entro al último cubículo, cierro el pestillo y cuelgo mi mochila en el gancho de la puerta."
    "Respiro hondo."
    "No había notado la leve tensión que me había acompañado en el cuerpo durante todo el día."
    "Estiro un poco el cuello escuchando como se descontractura."
    "Allí dentro de ese reducido espacio me encontraba sola y se sintió como quitarse un peso de encima por un instante."
    "Daba la impresión de que cargaba una bolsa repleta de pesados secretos y esta era mi parada antes de continuar."

    "De pronto, la puerta principal del baño se abre de golpe, seguida del eco de unos pasos y risas maliciosas, me puse alerta por instinto."

    show chicas with Dissolve (0.12)

    chica1 "¿Viste su cara? Naomi está como loca buscándolo."

    chica2 "Totalmente. Está revisando hasta los basureros. Vaya uno a saber qué clase de sucio secreto tiene escrito en ese diario."

    chica1 "Por algo está tan desesperada. Si lo encontramos nosotras primero, lo subimos al foro de la facultad."

    "Ambas estallan en una risa aguda que me taladra los tímpanos. Se lavan las manos rápidamente y salen del baño, dejando tras de sí un fuerte olor a perfume dulce."

    hide chicas with Dissolve (0.12)
    
    "Me quedo en silencio dentro del cubículo, mirando mi mochila colgada."
    "Un nudo de incomodidad se forma en mi estómago. Conozco esa clase de malicia. Conozco lo que es que alguien quiera destruir tu vida solo por diversión."
    "Siento una punzada de empatía por esa tal Naomi."

    "Miro la cremallera de mi mochila. Estoy segura de que el famoso diario es el mismo que me encontré en la biblioteca."

    # --- SEGUNDA ELECCIÓN DEL JUGADOR ---

    menu:
        "¿Qué hago?"

        "Lo leere.":
            $ leyo_diario = True
            jump eleccion_leer_diario

        "No lo leere.":
            $ leyo_diario = False
            jump eleccion_no_leer

# ------------------------------------------------------------------
# -- RAMA 1: LEER EL DIARIO
# ------------------------------------------------------------------
label eleccion_leer_diario:
    show cuaderno with moveinbottom
    "El instinto de recabar información gana la partida. Saco el cuaderno, me siento en la tapa del inodoro y comienzo a leer."
    "No hay secretos sucios, ni planes macabros. Solo... sentimientos crudos."
    "Las páginas están llenas de poemas románticos, algo cursis y muy íntimos, dedicados a una sola persona: Camile."
    "Por lo que leo, Camile es su mejor amiga. Naomi está profundamente enamorada de ella y aterrorizada de perderla si le confiesa la verdad."

    pr duda "Pobre chica. Si esas víboras publican esto, la destrozarían."

    "Cierro el diario con cuidado y lo guardo de nuevo. Tengo que encontrarla antes de que ella colapse."
    hide cuaderno with moveoutbottom

    jump busqueda_naomi

# ------------------------------------------------------------------
# -- RAMA 2: NO LEER EL DIARIO
# ------------------------------------------------------------------
label eleccion_no_leer:
    "Alejo la mano de la mochila. No."
    "Bastante me han arrebatado a mí como para yo arrebatarle la privacidad a otra persona."
    "Sea lo que sea que haya escrito ahí, es suyo. Y si hay víboras buscándolo para hacerle daño, lo mejor es devolvérselo rápido y en sus propias manos."

    pr "Tengo que encontrar a esta chica antes de que sufra un ataque de pánico."
    
    jump busqueda_naomi

# ------------------------------------------------------------------
# -- PUNTO DE ENCUENTRO: LA BÚSQUEDA Y EL ENCUENTRO
# ------------------------------------------------------------------
label busqueda_naomi:

    scene universidadpasillo with fade

    "Salgo del baño y comienzo a recorrer los pasillos y patios cercanos a la biblioteca."
    "No tardo mucho en encontrarla. Es imposible no notarla."

    window hide
    show screen polaroid_naomi
    pause
    window show
    $ photo_4 = True

    "Una chica de llamativo cabello rojo cereza está agachada cerca de unos casilleros, revisando frenéticamente el interior de su propia mochila, tirando cosas al suelo."
    "Respira de forma entrecortada, casi hiperventilando. Sus ojos reflejan puro pánico, pero sus rostro permanece hábilmente serio."
    "Tiene que ser ella, nadie más se encuentra en la misma situación."
    "Me acerco a paso tranquilo, intentando no asustarla más."

    pr "Disculpa... ¿Tu eres Naomi?"
    "Estaba tan ensimismada en lo que hacía que no me escuchó o bien decidió ignorarme ya que no obtuve respuesta alguna, intenté de nuevo."
    pr "¿Por casualidad buscas esto?"
    show naomienojo with Dissolve (0.12)
    "Saco el cuaderno negro y se lo tiendo. Naomi levanta la vista y se congela."
    "Por un segundo, veo el alivio más absoluto en su rostro. Pero inmediatamente, el terror vuelve, seguido de una barrera defensiva gruesa como el acero."
    with hpunch 
    "Me arranca el cuaderno de las manos con una brusquedad que me hace dar un paso atrás."

    # --- REACCIÓN CONDICIONADA POR TU ELECCIÓN ---

    if leyo_diario:
        # Reacción si lo leíste (Asustada / Defensiva)
        nm "¿Lo... lo leíste? ¡Dime la verdad!"
        
        "Su voz tiembla. Está al borde de las lágrimas, pero su postura es la de un animal acorralado listo para atacar."
        
        pr "Escucha, sí, vi un par de páginas. Pero..."
        $ puntos_naomi -=10
        hide naomienojo with Dissolve (0.08)
        show naomienojox2 with Dissolve (0.08)
        nm "¡Eres una...! ¡No tenías ningún derecho!" with hpunch
        
        pr duda "Baja la voz. Solo te lo traje porque escuché a unas chicas en el baño planeando publicarlo en un foro si lo encontraban."
        pr duda "Tu secreto está a salvo conmigo. No conozco a Camile, no te conozco a ti, y francamente, no me interesa tu vida privada."

        "La mención del nombre le quita el color de la cara. Abraza el cuaderno contra su pecho de forma protectora."

        nm "No sabes nada. Si abres la boca... si dices una sola palabra sobre ella..."

        pr duda "Relájate. Has de cuenta que no existo."

        "Me mira con una mezcla de odio, terror y desconfianza. Da un paso atrás y se da la vuelta, huyendo a paso rápido por el pasillo."
        hide naomienojox2 with Dissolve (0.08)

    else:
        # Reacción si NO lo leíste (Aliviada / Pasivo-Agresiva)
        nm "¿Lo abriste? ¿Leíste algo?"
        
        "Me escudriña con la mirada, buscando cualquier signo de burla en mi rostro."
        
        pr "No. Lo encontré en el puff de la biblioteca y lo guardé. Iba a llevarlo a administración, pero escuché a unas chicas en el baño queriendo encontrarlo para molestarte."
        $ puntos_naomi += 1
        "Naomi suelta un suspiro tembloroso. Sus hombros bajan un centímetro, visiblemente aliviada, pero su tono sigue siendo cortante y venenoso."
        
        nm "Claro. Como si alguien en este pozo de víboras tuviera decencia. De seguro lo hojeaste."
        
        pr duda "Si lo hubiera hecho, te lo diría. Guárdalo mejor la próxima vez."

        "Naomi me lanza una mirada ácida, aferrando el cuaderno con ambas manos."
        
        nm "No necesito tus consejos. Y no creas que te debo un favor por esto. Solo... no te metas en mis asuntos."
        
        "Levanta la barbilla con altivez, aunque le tiemblan ligeramente las manos, y se aleja marchando con rapidez hacia la salida."
        hide naomienojo with Dissolve (0.08)

    # --- RESOLUCIÓN DEL ENCUENTRO ---

    "Me quedo sola en el pasillo, procesando la interacción."

    pr duda "De nada, supongo."

    "Sacudo la cabeza. Esta universidad tiene más drama del que puedo manejar en mi primer día."
    "Será mejor que vuelva a mi rutina de pasar desapercibida."

    # --- EL REGRESO AL APARTAMENTO Y EL CIERRE DEL DÍA ---

    scene black with dissolve
    pause 1.5

    "El resto del día transcurre sin mayores incidentes. Clases, pasillos llenos, caras desconocidas."
    "Nunca creí que terminaría estudiando en la rama de informática, siempre fuí una chica más artística que metódica."
    "Aunque últimamente me siento tan perdida que ya no puedo asegurar ni mis gustos."
    "La linea entre mi yo del pasado y esta nueva identidad comenzaba a ponerse levemente borrosa, y no tenía claro aún si se trataba de un mecanismo de defensa o si directamente comenzaba a olvidar quién era yo antes de todo."
    "Puede que un poco de ambas."

    scene edificiosatardecer with fade
    play music "audio/musicaneutrax2.opus" fadein 2.0 if_changed

    "El sol ya comenzaba su descenso tiñiendo el cielo de naranja cuando bajo del autobús frente al complejo de apartamentos."
    "El aire es helado, y el único sonido es el zumbido eléctrico de una farola intermitente cerca de las escaleras."

    "El cansancio me pesa en los huesos. No solo el agotamiento físico de caminar por un campus enorme, sino el peso de mantener inconscientemente la guardia alta."
    
    scene pasillodepaatardecer with dissolve

    "Subo al segundo piso, arrastrando los pies. Mi mente ya está repasando si me queda algo comestible en la pequeña nevera."
    "Pensar en ello me recordó que debía pasarme por el super mañana por la mañana, y a la vez ese pensamiento me llevó a la idea de conseguir trabajo."
    "Nunca había necesitado de un trabajo de verdad, no significa que no haya trabajado jamás, pero siempre se me era otorgado, es decir, no recordaba tener una entrevista por empleo en la vida."

    "Al llegar al pasillo, el familiar olor a tabaco me detiene en seco."

    "Ahí está él..."

    pause 0.5
    show finnllamada at medio_izq with dissolve

    "Ni siquiera conozco aún su nombre pero me genera una curiosidad innegable."

    "Está distraido, con el ceño fruncido, mirando hacia un punto muerto."
    "La brasa de su cigarrillo brilla intensamente cada vez que le da una calada nerviosa. Tiene el teléfono presionado contra la oreja, y su postura es completamente distinta a la calma apática de ayer."

    "Está tenso. Como la cuerda de un arco a punto de romperse, hablando en voz baja, áspera."

    fn "Ya te lo dije. No me presiones."

    "Me quedo inmóvil, pegada a la pared de la escalera, debatiendo si avanzar o retroceder. Mi instinto dice 'aléjate de los problemas', pero mis pies no se mueven."

    fn "No. Escúchame bien... no voy a hacerlo. Tengo cosas más importantes de las que ocuparme ahora."

    "Suelta una maldición ahogada y aparta el teléfono de su oreja con violencia."

    "Es entonces cuando gira la cabeza."

    hide finnllamada with Dissolve (0.08)
    show finnllamadax2 at medio_izq with Dissolve (0.08)

    "Y descubre que por alguna razón me había quedado quieta observandolo."
    
    "Por un instante, el tiempo parece congelarse en ese pasillo ya poco iluminado."
    
    "Me preparo para que me grite, para que me pregunte qué demonios estoy escuchando. Pero no lo hace."

    "Su mirada se clava en la mía. No hay hostilidad directa, pero tampoco es una mirada vacía."
    "Es intensa. Cargada de una frustración y una sombra que reconozco demasiado bien."
    "Debajo del ceño fruncido, de la ropa ancha y esa actitud distante... hay algo magnético."
    
    pr duda "(¿Por qué tiene que lucir tan... peligroso?)"

    "Un escalofrío que no tiene nada que ver con el frío me recorre la espalda. No es miedo. Es una curiosidad abrumadora."

    "La conexión dura apenas un segundo."
    "Finn corta la llamada, tira el cigarrillo a medio terminar y se gira hacia su puerta, ignorándome por completo."
    hide finnllamadax2 with Dissolve (0.12)

    "El siseo de su cerradura rompe el hechizo."

    "Reacciono, bajando la mirada apresuradamente y caminando casi a trote hacia mi propia puerta."

    scene habitacionatardecer with hpunch

    "Entro y pongo el cerrojo de golpe."
    "Me apoyo contra la madera fría, con el corazón latiendo un poco más rápido de lo normal."

    "¿De qué estaba hablando? ¿Quién lo presionaba?"

    "Me dejó caer en el colchón de un salto."

    pr duda "No me interesa, no es asunto mío."

    "Pero mientras la oscuridad de la habitación me envuelve, la imagen de esos ojos azules, fríos y frustrados, se niega a desaparecer de mi mente."

    "Me convenzo de que solo me encandiló su belleza, eso me mantiene lo suficientemente tranquila para consiciliar el sueño."
    window hide

    # --- FIN DEL CAPÍTULO 1 ---

    scene black with fade
    pause 2.0

    show text "{size=+20}FIN DEL CAPÍTULO 1{/size}\n\nGracias por jugar la demo." at truecenter with dissolve
    pause 4.0
    hide text with dissolve

    return

    