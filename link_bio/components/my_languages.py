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
                        rx.text(
                            language,
                            style= styles.languaje_body_style,
                            font_size= Size.SEMIDEFAULT.value,
                            as_= "b",
                            align= "center"
                        )
                    ),
                width= "100%"  
            )
        ),
        justify_content="center"
    )

def auto_layout_icons(*icons: rx.Component, max_per_row: int = 5) -> rx.Component:
    rows = []
    for i in range(0, len(icons), max_per_row):
        row_icons = icons[i:i + max_per_row]
        if len(row_icons) == 1:  # Si hay solo una imagen en la fila
            row = rx.chakra.flex(
                *row_icons,
                gap="40px",
                margin_bottom=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value,
                align_items="center",  # Centra verticalmente la única imagen en la fila
                justify_content="center"  # Centra horizontalmente la única imagen en la fila
            )
        else:
            row = rx.chakra.flex(
                *row_icons,
                gap="40px",
                margin_bottom=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value
            )
        rows.append(row)
    return rx.chakra.vstack(
        *rows,
        flex_wrap="wrap",
        width="100%"
    )
