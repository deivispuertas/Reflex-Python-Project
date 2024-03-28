import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size,Spacing
from link_bio.styles.colors import Color

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
            margin_top= Size.ZERO.value
        ),
        align="center",
        padding_bottom=Size.VERY_BIG.value,
        padding_y= Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.SMALL.value,
    )

