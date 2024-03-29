import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as Txtcolor
from link_bio.styles.colors import Color 

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                    name= "Deivis Puertas", 
                    size= "2xl",
                    src= "avatar.jpg",  
                    color= Txtcolor.BODY.value,
                    bg= Color.CONTENT.value,
                    padding= "2px",
                    border= "4px",
                    border_color= Color.PRIMARY.value

            ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "Deivis Puertas 🐸",
                    size="lg"
                ),
                rx.chakra.text(
                    "@deivisdev_science",
                    margin_top= Size.ZERO.value,
                    color= Txtcolor.BODY.value
                ),
                rx.chakra.hstack(
                    link_icon(
                        const.FACEBOOK_URL
                    ),
                    link_icon(
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        const.TWITTER_X_URL
                    ),
                    link_icon(
                        const.SPOTIFY_URL
                    ),
                    link_icon(
                        const.TIKTOK_URL
                    )
                ), 
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),
        rx.chakra.flex(
            info_text(
                "+100", 
                "Horas de Estudio"
            ),
            rx.chakra.spacer(),
            info_text(
                "+1", 
                "Proyecto Público"
            ),
            rx.chakra.spacer(),
            info_text(
                "+3", 
                "Certificados"
            ),
            width="100%"
        ),
        rx.chakra.text(
                   """
                   Soy Ingeniero de Sistemas e Informática que esta por culminar la carrera.
                   Actualmente estoy aprendiendo el Lenguaje de Python para desempeñarme en
                   el ámbito de la Programación y el Data science. Aquí podras encontrar 
                   información para contactarme !Bienvenid@s!
                   """,
                   font_size= Size.MEDIUM.value,
                   color= Txtcolor.BODY.value
         ),
        spacing=Size.BIG.value,
        align_items="start" 
    )

def experience() -> int:
    return datetime.date.today().year - 2024