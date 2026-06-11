# Definimos el video para que Ren'Py sepa qué archivo usar y que se repita (loop)
image video_fondo_menu = Movie(play="images/video_menu.webm", loop=True)


# Definición de personajes según tu lista
define pr = Character("[nombreusuario]", color="#ffffff", image="pr")
image side pr = "side pr neutra"
define ow = Character("Owen", color="#ffffff")
define ln = Character("Leonard", color="#ffffff")
define nm = Character("Naomi", color="#ffffff") 
define bl = Character("Bel", color="#ffffff")
define dn = Character("Diana", color="#ffffff")
default nombre_finn = "Vecino" # Este es el nombre que aparecerá al inicio
define fn = Character("[nombre_finn]", color="#ffffff")
define misterio = Character("???", color="#ffffff")
define profesor = Character("Profesor", color="#ffffff")
define chica1 = Character("Chica 1", color="#ffffff")
define chica2 = Character("Chica 2", color="#ffffff")

# Creamos posiciones más centradas
transform medio_izq:
    xalign 0.25
    yalign 1.0

transform medio_der:
    xalign 0.75
    yalign 1.0


##### IMAGENES DE FONDO #####
image bg_universidad_exterior = "images/fondos/bg_universidad_exterior.png"
image flash = "images/fondos/flashback.png"
image bus = "images/fondos/autobuslleno.png"
image admi = "images/fondos/administracion.png"
image pasillo = "images/fondos/universidadpasillo.png"
image clase = "images/fondos/salonclase.png"
image edi = "images/fondos/edificioprincipal.png"
image cgpasillonocheoscura = "images/Fondos/cgpasillonocheoscura.png"
image cg_finn_pasillo = "images/Fondos/cg_finn_pasillo.png"
image edificios = "images/Fondos/edificios.png"
image bg_habitacion_oscura = "images/Fondos/bg_habitacion_oscura.png"
image bg_biblioteca = "images/Fondos/bg_biblioteca.png"
image bg_bano = "images/Fondos/bg_bano.png"
image bg_pasillo_exterior = "images/Fondos/bg_pasillo_exterior.png"
image entradauni = "images/Fondos/entradauni.png"
image finn_fumando = "images/Fondos/finn_fumando.png"
image finn_mirada = "images/Fondos/finn_fumando2.png"
image pasillodesenfoque = "images/Fondos/pasillonocheoscuradesenfoque.png"
image pasillodepaatardecer = "images/Fondos/pasillodepaatardecer.png"
image edificiosatardecer = "images/Fondos/edificiosatardecer.png"
image administraciondesenfoque = "images/Fondos/administraciondesenfoque.png"
image clasedesenfoque = "images/Fondos/clasedesenfoque.png"
image pasillounidesenfoque = "images/Fondos/pasillounidesenfoque.png"
image campus = "images/Fondos/campus.png"
image habitacionatardecer = "images/Fondos/habitacionatardecer.png"

##### SPRITES #####
image owenneutro = "images/Sprites/Owen/owenneutro.png"
image owenfeliz = "images/Sprites/Owen/owenfeliz.png"
image owenincomodo = "images/Sprites/Owen/owenincomodo.png"
image diananeutra = "images/Sprites/Diana/diananeutra.png"
image dianafeliz = "images/Sprites/Diana/dianafeliz.png"
image dianasonrojo = "images/Sprites/Diana/dianasonrojo.png"
image dianaenojo = "images/Sprites/Diana/dianaenojo.png"
image naomineutra = "images/Sprites/Naomi/naomineutra.png"
image naomienojo = "images/Sprites/Naomi/naomienojo.png"
image naomifeliz = "images/Sprites/Naomi/naomifeliz.png"
image leoneutro = "images/Sprites/Leonard/leoneutro.png"
image leosonrisa = "images/Sprites/Leonard/leosonrisa.png"
image leoenojado = "images/Sprites/Leonard/leoenojado.png"
image chicas = "images/Extras/chicas.png"
image polaroid_finn = "images/Sprites/Finn/polaroid_finn.png"
image naomi_polaroid = "images/Sprites/Naomi/naomi_polaroid.png"
image owen_polaroid = "images/Sprites/Owen/owen_polaroid.png"
image finnllamada = "images/Sprites/Finn/finnllamada.png"
image polaroid_leo = "images/Sprites/Leonard/polaroid_leo.png"
image owensonrisa = "images/Sprites/Owen/owensonrisa.png"
image leoapenado = "images/Sprites/Leonard/leoapenado.png"
image profe = "images/Extras/profe.png"
image leoapenadox2 = "images/Sprites/Leonard/leoapenadox2.png"
image naomienojox2 = "images/Sprites/Naomi/naomienojox2.png"
image pr neutra = "images/protagonista_neutra.png"
image pr duda = "images/protagonista_duda.png"
image pr sonrojo = "images/protagonista_sonrojo.png"

transform polaroid_appear:

    alpha 0.0
    zoom 0.85

    ease 0.35 alpha 1.0 zoom 1.0

screen polaroid_finn():

    modal True

    add "polaroid_finn" at polaroid_appear:

        xalign 0.5
        yalign 0.5

    textbutton "✕":

        xpos 1310
        ypos 1

        text_size 45
        text_color "#FFFFFF"

        background None

        action Hide("polaroid_finn")

screen polaroid_naomi():

    modal True

    add "naomi_polaroid" at polaroid_appear:

        xalign 0.5
        yalign 0.5

    textbutton "✕":

        xpos 1310
        ypos 1

        text_size 45
        text_color "#FFFFFF"

        background None

        action Hide("polaroid_naomi")

screen polaroid_owen():

    modal True

    add "owen_polaroid" at polaroid_appear:

        xalign 0.5
        yalign 0.5

    textbutton "✕":

        xpos 1310
        ypos 1

        text_size 45
        text_color "#FFFFFF"

        background None

        action Hide("polaroid_owen")

screen polaroid_leo():

    modal True

    add "polaroid_leo" at polaroid_appear:

        xalign 0.5
        yalign 0.5

    textbutton "✕":

        xpos 1310
        ypos 1

        text_size 45
        text_color "#FFFFFF"

        background None

        action Hide("polaroid_leo")




image side pr neutra:
    "protagonista_neutra.png"

    xsize 400 ysize 400  
    radius 200.0      
    xalign 0.0
    yalign 1.0
    xoffset 20 
    yoffset 0  

image side pr duda:
    "protagonista_duda.png"

    xsize 400 ysize 400  
    radius 200.0      
    xalign 0.0
    yalign 1.0
    xoffset 20 
    yoffset 0  

image side pr sonrojo:
    "protagonista_sonrojo.png"

    xsize 400 ysize 400  
    radius 200.0      
    xalign 0.0
    yalign 1.0
    xoffset 20 
    yoffset 0  

image side pr sonrisa:
    "protagonista_sonrisa.png"

    xsize 400 ysize 400  
    radius 200.0      
    xalign 0.0
    yalign 1.0
    xoffset 20 
    yoffset 0 

image side pr admiracion:
    "protagonista_admiracion.png"

    xsize 400 ysize 400  
    radius 200.0      
    xalign 0.0
    yalign 1.0
    xoffset 20 
    yoffset 0 



##### EXTRAS #####
image llamada = "images/Extras/telefonollamada.png"
image cuaderno = "images/Extras/cuaderno.png"


##### MAPAS #####
screen mapapasillo():
    modal True
    
    imagebutton:
        idle "extras/flechasalon.png"
        action Jump("clase")

    imagebutton:
        idle "extras/flechacampus.png"
    

screen mapaedificio():
    modal True

    imagebutton:
        idle "extras/flechapasillo.png"
        action Jump("pasillo")
        xpos 100 ypos 100 # Te recomiendo añadir posiciones o "align"

    imagebutton:
        idle "extras/flechabiblioteca.png"
        action Jump("biblio") 

    imagebutton:
        idle "extras/flechaentrada.png"
        action Jump("uni") 



##### VIDEOS Y EFECTOS #####
style titulo_tiempo:
    is text
    size 70
    color "#ffffff" outlines [ (2, "#000000") ]xalign 0.5 yalign 0.5 layout "subtitle"

# 2. DEFINICIÓN DE LAS ANIMACIONES (TRANSFORMS)
# Esta animación hace que el fondo negro aparezca y desaparezca suavemente.
transform morning_fadein_fadeout:
    on show:
        alpha 0.0           # Empieza totalmente transparente
        linear 1.0 alpha 1.0 # Tarda 1.0s en volverse negro
    on hide:
        linear 1.0 alpha 0.0 # Tarda 1.0s en desaparecer

# Esta animación hace que el texto aparezca, espere y desaparezca.
transform morning_text_fadein_fadeout:
    on show:
        alpha 0.0           # Empieza totalmente transparente
        pause 0.5           # Espera 0.5s antes de aparecer
        linear 0.5 alpha 1.0 # Tarda 0.5s en aparecer
        pause 2.5           # Espera 2.5s visible
        linear 0.5 alpha 0.0 # Tarda 0.5s en desaparecer
# --- FIN DEL ARCHIVO ---


##### MAPA #####

# 1. Definimos la pantalla del mapa
screen mapa_entrada_universidad():
    # El fondo de la universidad (1920x1080)
    add "Fondos/bg_universidad_exterior.png"

    # El botón que abarca toda la pantalla
    imagebutton:
        xpos 0
        ypos 0
        idle "Mapa/botonentrada.png"       # La puerta cerrada en su sitio con fondo transparente
        hover "Mapa/botonentradaopen.png"  # La puerta abierta en su sitio con fondo transparente
        
        # IMPORTANTE: focus_mask True es OBLIGATORIO aquí
        # para que el juego ignore las partes transparentes del botón
        focus_mask True 
        
        action Jump("entrar_a_la_u")


transform efecto_parpadeo:
    # Empezamos con la pantalla totalmente negra
    alpha 1.0
    # Abre un poco los ojos
    linear 0.5 alpha 0.4
    # Los cierra rápido
    linear 0.2 alpha 1.0
    # Los abre más (se ve más el fondo)
    linear 0.8 alpha 0.2
    # Los cierra otra vez con cansancio
    linear 0.4 alpha 1.0
    # Los abre finalmente por completo
    linear 1.2 alpha 0.0

# Movimiento de caminar
transform efecto_caminar:
    linear 0.2 yoffset -10
    linear 0.2 yoffset 0
    repeat 3 # Repite el paso 3 veces



init python:
    # Esta función se ejecutará cada vez que un personaje hable
    def automatic_blur(trans, st, at):
        # Si hay un personaje en pantalla (tag "pr", "finn", etc.)
        if renpy.get_showing_tags():
            # Aplicamos un blur suave de 3.0 al fondo
            trans.blur = 3.0
        else:
            # Si no hay nadie hablando, quitamos el blur
            trans.blur = 0.0
        return 0

# Definimos el ATL que usaremos para el fondo
transform blur_master_f:
    function automatic_blur

#### TRANSFORMS ####

transform entrar_derecha:
    xalign 1.3
    yalign 1.0
    linear 0.8 xalign 0.7

transform salir_derecha:
    xalign 0.7
    yalign 1.0
    linear 0.8 xalign 1.3

define quick = Dissolve(0.12)

transform medio_izq:
    xalign 0.3
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0