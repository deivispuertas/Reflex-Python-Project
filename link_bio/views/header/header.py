import reflex as rx
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.components.info_text import info_text

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(name="Deivis Puertas", size="xl"),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "Deivis Puertas 🐸",
                    size="lg"
                ),
                rx.chakra.text(
                    "@deivisdev_science",
                    margin_top="0px !important"
                ),
                rx.chakra.hstack(
                    link_icon(const.FACEBOOK_URL),
                    link_icon(const.INSTAGRAM_URL),
                    link_icon(const.TWITTER_X_URL),
                    link_icon(const.SPOTIFY_URL),
                    link_icon(const.TIKTOK_URL)
                ), 
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),
        rx.chakra.flex(
            info_text("+1", "Año de experiencia"),
            rx.chakra.spacer(),
            info_text("+3", "Certificados"),
            rx.chakra.spacer(),
            info_text("+1", "Proyecto público"),
            width="100%"
        ),
        rx.chakra.text("""Soy Ingeniero de Sistemas e Informática que esta por culminar la carrera.
                   Actualmente estoy aprendiendo el Lenguaje de Python para desempeñarme en
                   el ámbito de la Programación y el Data science. Aquí podras encontrar 
                   información para contactarme !Bienvenid@s!"""),
        spacing=Size.BIG.value,
        align_items="start" 
    )