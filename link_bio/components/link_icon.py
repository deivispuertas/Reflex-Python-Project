import reflex as rx
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def link_icon(image:str, url: str, alt: str) -> rx.Component:
    return chakra.link(
        rx.image(
            src= image,
            width= Size.DEFAULT.value,
            alt= alt
        ),
        href= url,
        is_external= True
    )