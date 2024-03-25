import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def languages_icon(image: str,language: str) -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.flex(
         rx.chakra.box(
                    rx.chakra.image(
                        src=image,
                        size="md",
                        margin_bottom=Size.DEFAULT.value
                    ),
                    rx.chakra.vstack(
                        rx.text(language,style=styles.button_body_style),
                        align_items="center"
                    ),
                width="100%",   
            )
        )
    )

def auto_layout_icons(*icons: rx.Component, max_per_row: int = 6) -> rx.Component:
    rows = [rx.chakra.flex(
                *icons[i:i+max_per_row],gap="40px", margin_bottom=Size.MEDIUM.value,margin_top=Size.DEFAULT.value) for i in range(0, len(icons),
                max_per_row)]
    return rx.chakra.vstack(
                rx.chakra.flex(
                    *rows,
                    flex_wrap="wrap", 
                    width="100%"
                ),
                align_items="center",
            )
