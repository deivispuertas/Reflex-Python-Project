import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def title(text: str) -> rx.Component:
   return chakra.heading(
                text,
                size="lg", 
                style=styles.title_style
          )

def sub_title(text:str) -> rx.Component:
   return chakra.vstack(
            chakra.heading(
                  text,
                  size="md",
                  align_items="center",
                  style=styles.sub_tittle_style
            )
          )