import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def languages_icon(image: str, language: str) -> rx.Component:
    return chakra.vstack(
        chakra.image(
            src=image,
            height="60px",  # altura fija para uniformidad
            margin_bottom="0.5rem",
            object_fit="contain"
        ),
        rx.text(
            language,
            style=styles.languaje_body_style,
            font_size=Size.MEDIUM.value,
            as_="b",
            text_align="center"
        ),
        spacing="0.5rem",
        align="center",
        width="100px",  # ancho fijo para alinear mejor
    )

def auto_layout_icons(*icons: rx.Component, max_per_row: int = 3) -> rx.Component:
    rows = []
    for i in range(0, len(icons), max_per_row):
        row_icons = icons[i:i + max_per_row]
        row = chakra.flex(
            *row_icons,
            justify="center",
            gap="40px",
            wrap="wrap",
            margin_bottom=Size.MEDIUM.value,
            margin_top=Size.DEFAULT.value
        )
        rows.append(row)
    return chakra.vstack(
        *rows,
        spacing="1rem",
        width="100%"
    )