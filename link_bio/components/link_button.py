import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(title: str,body: str, image:str,url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width= Size.BIG.value,
                    height= Size.BIG.value,
                    margin= Size.MEDIUM.value
                ),
                rx.chakra.vstack(
                    rx.text(
                        title,
                        style= styles.button_tittle_style
                    ),
                    rx.text(
                        body,
                        style= styles.button_body_style
                    ),
                    spacing= Size.SMALL.value,
                    align_items= "start",
                    margin = Size.ZERO.value
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"    
    )

