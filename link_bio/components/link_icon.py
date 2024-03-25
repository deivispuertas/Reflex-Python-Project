import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.chakra.link(
        rx.icon(
            tag="link"
        ),
        href=url,
        is_external=True
    )