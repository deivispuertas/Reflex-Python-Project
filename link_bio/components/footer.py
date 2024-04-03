import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size,Spacing
from link_bio.styles.colors import Color
from link_bio.styles.colors import TextColor as Txtcolor

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src= "reflexlogo.png",
            height= Size.BIG.value,
            weight= Size.VERY_BIG.value,
            bg= Txtcolor.HEADER.value,
            alt= "Logotipo de Reflex. El nombre de la aplicación dentro de un casillero",
            padding= "2px",
            border= "4px",
        ),
        rx.chakra.link(
            f"© 2024-{datetime.date.today().year} Frog 🐸 By Deivis Puertas V1.",
            href= const.REFLEX_URL,
            is_external=True,
            font_size= Size.MEDIUM.value,
            margin_top= Size.LARGE.value
        ),
        rx.chakra.text(
            "This entire website was created using Reflex-Chakra-Python with 💚 from Perú to the world ",
            font_size= Size.MEDIUM.value,
            margin_top= Size.ZERO.value,
            padding_x= Size.LARGE.value
        ),
        padding_y= Size.VERY_BIG.value,
        spacing= Spacing.SMALL.value,
        color= Txtcolor.FOOTER.value
    )