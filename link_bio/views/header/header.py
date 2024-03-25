import reflex as rx
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
                    "@deivisdev",
                    margin_top="0px !important"
                ),
                rx.chakra.hstack(
                    link_icon("https://www.facebook.com/deivis.puertas"),
                    link_icon("https://www.instagram.com/deivis_puertas/"),
                    link_icon("https://twitter.com/Deivis_tk")
                ), 
                align_items="start",
            )
        ),
        rx.chakra.flex(
            info_text("+13", "años de experencia"),
            rx.chakra.spacer(),
            info_text("+13", "años de experencia"),
            rx.chakra.spacer(),
            info_text("+13", "años de experencia"),
            width="100%"
        ),
        rx.chakra.text("""Soy Ingeniero de Sistemas e Informática que esta por culminar la carrera.
                   Actualmente estoy aprendiendo el Lenguaje de Python para desempeñarme en
                   el ámbito de la Programación y el Data science. Aquí podras encontrar 
                   información para contactarme !Bienvenid@s!"""),
        spacing=Size.BIG.value,
        align_items="start" 
    )