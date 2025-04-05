import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as Txtcolor
from link_bio.styles.colors import Color
import reflex_chakra as chakra

def navbar() -> rx.Component:
    return chakra.hstack(
        chakra.box(
            chakra.span("dev", color= Color.PRIMARY.value),
            chakra.span("puertas", color=Color.PRIMARY.value),
            style= styles.navbar_title_style
        ),
        position="sticky",
        bg= Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )