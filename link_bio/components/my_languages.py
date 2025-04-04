import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def languages_icon(image: str, language: str) -> rx.Component:
    return chakra.vstack(
        chakra.box(
            chakra.image(
                src=image,
                size="md",
                margin_bottom=Size.DEFAULT.value,
                height="auto",
                max_width="100%"
            ),
            width="100%",
            align="center"
        ),
        rx.text(
            language,
            style=styles.languaje_body_style,
            font_size= Size.MEDIUM.value,
            as_="b",
            align="center"
        ),
        align="center",
        margin_bottom=Size.MEDIUM.value,
        margin_top=Size.DEFAULT.value
    )

def auto_layout_icons(*icons: rx.Component, max_per_row: int = 3) -> rx.Component:
    rows = []
    for i in range(0, len(icons), max_per_row):
        row_icons = icons[i:i + max_per_row]
        if len(row_icons) == 1:  
            row = chakra.flex(
                *row_icons,
                gap="40px",
                margin_bottom=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value,
                align_items="center",  
            )
        else:
            row = chakra.flex(
                *row_icons,
                gap="40px",
                margin_bottom=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value
            )
        rows.append(row)
    return chakra.vstack(
        *rows,
        flex_wrap="wrap",
        width="100%"
    )
