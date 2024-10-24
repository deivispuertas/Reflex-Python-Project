import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def link_button(title: str,body: str, image:str,url: str) -> rx.Component:
    return chakra.link(
        chakra.button(
            chakra.hstack(
                chakra.image(
                    src=image,
                    width= Size.BIG.value,
                    height= Size.BIG.value,
                    margin= Size.MEDIUM.value,
                    alt= title
                ),
                chakra.vstack(
                    rx.text(
                        title,
                        style= styles.button_tittle_style
                    ),
                    rx.text(
                        body,
                        style= styles.button_body_style
                    ),
                    align_items="start",
                    spacing= Size.SMALL.value,
                    margin = Size.ZERO.value,
                    padding_y= Size.SMALL.value,
                    padding_right= Size.SMALL.value
                ),
                width= "100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%"    
    )

