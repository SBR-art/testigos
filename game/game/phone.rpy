default photo_1 = False
default photo_2 = False
default photo_3 = False
default photo_4 = False

default mail_1 = False
default mail_notification = False


screen phone_button():

    imagebutton:

        idle "images/gui/phone_icon.png"

        xalign 0.98
        yalign 0.02

        action Show("phone_menu")


transform phone_show:

    yoffset 1200

    ease .35 yoffset 0


screen phone_menu():

    modal True

    add Solid("#00000066")

    button:

        background None

        xpos 0
        ypos 0

        xsize 1920
        ysize 1080

        action Hide("phone_menu")

    add "images/gui/phone_bg.png" at phone_show:
        xalign 0.5
        yalign 0.5

    # FILA 1

    imagebutton:
        idle "images/gui/msg_icon.png"
        xpos 820
        ypos 250
        at phone_show, Transform(zoom=0.55)
        action Show("messages_screen")

    imagebutton:
        idle "images/gui/gallery_icon.png"
        xpos 925
        ypos 250
        at phone_show, Transform(zoom=0.55)
        action Show("gallery_screen")

    imagebutton:
        idle "images/gui/save_icon.png"
        xpos 1030
        ypos 250
        at phone_show, Transform(zoom=0.55)
        action Show("save_screen")

    # FILA 2

    imagebutton:
        idle "images/gui/history_icon.png"
        xpos 820
        ypos 390
        at phone_show, Transform(zoom=0.55)
        action Show("history_screen")

    imagebutton:
        idle "images/gui/settings_icon.png"
        xpos 925
        ypos 390
        at phone_show, Transform(zoom=0.55)
        action Show("settings_screen")

    imagebutton:
        idle "images/gui/home_icon.png"
        xpos 1030
        ypos 390
        at phone_show, Transform(zoom=0.55)
        action MainMenu()

    # FILA 3

    imagebutton:
        idle "images/gui/mail_icon.png"
        xpos 820
        ypos 530
        at phone_show, Transform(zoom=0.55)
        action Show("mail_screen")

    # FILA INFERIOR

    imagebutton:
        idle "images/gui/llamada_icon.png"
        xpos 820
        ypos 855
        at phone_show, Transform(zoom=0.55)
        action NullAction()

    imagebutton:
        idle "images/gui/location_icon.png"
        xpos 925
        ypos 855
        at phone_show, Transform(zoom=0.55)
        action NullAction()

    imagebutton:
        idle "images/gui/camera_icon.png"
        xpos 1030
        ypos 855
        at phone_show, Transform(zoom=0.55)
        action NullAction()


screen messages_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_chats.png":
        xalign 0.5
        yalign 0.5

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("messages_screen")

screen gallery_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_images.png":
        xalign 0.5
        yalign 0.5

    # FOTO 1
    if photo_1:

        imagebutton:
            idle "images/gui/polaroid1.png"
            xpos 820
            ypos 290
            at Transform(zoom=0.60)
            action Show("photo_view",
                image_name="images/Sprites/Finn/polaroid_finn.png")

    else:
        add "images/gui/locked_photo.png":
            xpos 820
            ypos 290
            at Transform(zoom=0.60)


    # FOTO 2
    if photo_2:

        imagebutton:
            idle "images/gui/polaroid2.png"
            xpos 925
            ypos 290
            at Transform(zoom=0.60)
            action Show("photo_view",
                image_name="images/Sprites/Owen/owen_polaroid.png")

    else:
        add "images/gui/locked_photo.png":
            xpos 925
            ypos 290
            at Transform(zoom=0.60)


    # FOTO 3
    if photo_3:

        imagebutton:
            idle "images/gui/polaroid3.png"
            xpos 1030
            ypos 290
            at Transform(zoom=0.60)
            action Show("photo_view",
                image_name="images/Sprites/Leonard/polaroid_leo.png")

    else:
        add "images/gui/locked_photo.png":
            xpos 1030
            ypos 290
            at Transform(zoom=0.60)


    # FOTO 4
    if photo_4:

        imagebutton:
            idle "images/gui/polaroid4.png"
            xpos 820
            ypos 390
            at Transform(zoom=0.60)
            action Show("photo_view",
                image_name="images/Sprites/Naomi/naomi_polaroid.png")

    else:
        add "images/gui/locked_photo.png":
            xpos 820
            ypos 390
            at Transform(zoom=0.60)


    # BOTÓN ATRÁS GALERÍA
    imagebutton:
        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("gallery_screen")

screen photo_view(image_name):

    modal True

    add Solid("#000000CC")

    add image_name:
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/gui/atras_chat.png"

        xpos 1312
        ypos 1

        at Transform(zoom=0.30)

        action Hide("photo_view")

screen mail_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_mail.png":
        xalign 0.5
        yalign 0.5

    if mail_1:

        imagebutton:

            idle "images/gui/mail_1.png"

            xpos 820
            ypos 280
            at Transform(zoom=0.80)

            action Show("mail_1_screen")

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("mail_screen")

screen mail_1_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/mail_11.png":
        xalign 0.5
        yalign 0.5

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 935
        ypos 825

        at Transform(zoom=0.30)

        action Hide("mail_1_screen")

    imagebutton:

        idle "images/gui/archivo_adjunto.png"

        xpos 835
        ypos 300

        at Transform(zoom=0.70)

        action NullAction()

transform notification_anim:

    on show:
        yoffset -200
        ease .35 yoffset 0

    on hide:
        ease .35 yoffset -200

screen mail_notification():

    timer 6.0 action [
        Hide("mail_notification"),
        SetVariable("mail_notification", False)
        ]

    if mail_notification:

        imagebutton:

            idle "images/gui/noti_mail.png"

            xpos 1100
            ypos 30

            at notification_anim

            action [
                Hide("mail_notification"),
                SetVariable("mail_notification", False),
                Show("mail_1_screen")
                ]

screen save_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_save.png":
        xalign 0.5
        yalign 0.5

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("save_screen")

    # SLOT 1

    imagebutton:

        idle "images/gui/slot_empty.png"
        xpos 830
        ypos 285
        action FileSave(1)

    # SLOT 2
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 970
        ypos 285
        action FileSave(2)

    # SLOT 3
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 830
        ypos 450
        action FileSave(3)

    # SLOT 4
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 970
        ypos 450
        action FileSave(4)

    # SLOT 5
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 830
        ypos 615
        action FileSave(5)

    # SLOT 6
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 970
        ypos 615
        action FileSave(6)

    # SLOT 7
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 830
        ypos 775
        action FileSave(7)

    # SLOT 8
    imagebutton:
        idle "images/gui/slot_empty.png"
        xpos 970
        ypos 775
        action FileSave(8)

screen history_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_history.png":
        xalign 0.5
        yalign 0.5

    viewport:

        xpos 820
        ypos 270

        xsize 260
        ysize 640

        mousewheel True
        draggable True

        vbox:

            spacing 8

            for h in _history_list:

                text h.what:
                    size 20
                    color "#3a3a3a"
                    outlines []
                    xmaximum 240

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("history_screen")

screen settings_screen():

    modal True

    add Solid("#00000066")

    add "images/gui/phone_settings.png":
        xalign 0.5
        yalign 0.5

    text "Velocidad del texto":
        xpos 810
        ypos 300
        color "#3a3a3a"
        size 22

    bar:

        xpos 810
        ypos 340
        xsize 280
        value Preference("text speed")

    text "Volumen música":
        xpos 810
        ypos 450
        color "#3a3a3a"
        size 22

    bar:
        xpos 810
        ypos 490
        xsize 280
        value Preference("music volume")

    text "Volumen efectos":
        xpos 810
        ypos 600
        color "#3a3a3a"
        size 22

    bar:
        xpos 810
        ypos 640
        xsize 280
        value Preference("sound volume")

    text "Pantalla":
        xpos 810
        ypos 740
        color "#3a3a3a"
        size 22

    textbutton "Ventana":
        xpos 830
        ypos 780
        text_size 20
        action Preference("display", "window")

    textbutton "Completa":
        xpos 960
        ypos 780
        text_size 20
        action Preference("display", "fullscreen")

    text "Auto":
        xpos 810
        ypos 860
        color "#3a3a3a"
        size 22

    textbutton "Activar":
        xpos 900
        ypos 855
        text_size 20
        action Preference("auto-forward", "toggle")

    imagebutton:

        idle "images/gui/atras_chat.png"

        xpos 1060
        ypos 200

        at Transform(zoom=0.30)

        action Hide("settings_screen")