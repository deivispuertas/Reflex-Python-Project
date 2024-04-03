import reflex as rx
from link_bio.components.navbaar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size



#class State(rx.State):
#    pass

def index() -> rx.Component:
   return rx.chakra.box(   
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.LARGE.value,
                padding= Size.BIG.value
            )
        ),
        footer()
    )

def about()-> rx.Component:
    return rx.chakra.text("About Page")


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
        index,
        title="Deivis Puertas | Programación y Data Science",
        description= "Hola, mi nombre es Deivis Puertas. Soy Estudiante de  Ingeniería de Sistemas e Informática, ahora estoy aprendiendo el lenguaje python y desarrolle mi website usando el lenguaje Python con Reflex.",
        image="frog.ico"
)
app.add_page(about)
# app.compile() reflex ya no lo requiere ahora es automático
"""
rx.link(
            rx.button("Click to go to About"),
            href="/about"
        )
"""