import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(src="favicon.ico"),
        rx.chakra.link(
            f"© 2024-{datetime.date.today().year} Frog 🐸 By Deivis Puertas V1.",
            href=const.REFLEX_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.chakra.text(
            "This entire website was created using Reflex-Python with ♥ from Perú to the world ",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        align="center",
        padding_bottom="9",
    )

