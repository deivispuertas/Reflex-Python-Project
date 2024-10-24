import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color 
from link_bio.styles.colors import TextColor as Txtcolor
import reflex_chakra as chakra


def info_text(title: str, body: str) -> rx.Component:
    return chakra.flex(
        chakra.box(
            chakra.span(
                title, 
                font_weight="bold", 
                color=Color.PRIMARY.value
            ),
            f" {body}", 
            font_size=Size.MEDIUM.value,
            color=Txtcolor.BODY.value
        ),
        width="25%",
        direction="column",
        align="center",
        justify_content="center",
    )

