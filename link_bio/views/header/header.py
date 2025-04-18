import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size,Spacing
from link_bio.styles.colors import TextColor as Txtcolor
from link_bio.styles.colors import Color 
import reflex_chakra as chakra

def header() -> rx.Component:
    return chakra.vstack(
        chakra.hstack(
            chakra.avatar(
                    name= "Deivis Puertas", 
                    size= "2xl",
                    src= "avatar.jpg",  
                    color= Txtcolor.BODY.value,
                    bg= Color.CONTENT.value,
                    padding= "2px",
                    border= "4px",
                    border_color= Color.SECONDARY.value
            ),
            chakra.vstack(
                chakra.heading(
                    "Deivis Puertas 🐸",
                    size="lg"
                ),
                chakra.text(
                    "@devpuertas",
                    margin_top= Size.ZERO.value,
                    color= Txtcolor.BODY.value
                ),
                chakra.hstack(
                    link_icon(
                        "icons/facebook.svg",
                        const.FACEBOOK_URL,
                        "Facebook"
                    ),
                    # link_icon(
                    #     "icons/instagram.svg",
                    #     const.INSTAGRAM_URL,
                    #     "Instagram"
                    # ),
                    link_icon(
                        "icons/x-twitter.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    # link_icon(
                    #     "icons/linkedin.svg",
                    #     const.LINKEDIN_URL,
                    #     "Linkedin"
                    # ),
                    link_icon(
                        "icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    # link_icon(
                    #     "icons/tiktok.svg",
                    #     const.TIKTOK_URL,
                    #     "Tiktok"
                    # ),
                    spacing= Spacing.BIG.value,
                    padding_top= Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        chakra.flex(
            info_text(
                "+8 meses", 
                "Exp. Laboral"
            ),
            chakra.spacer(),
            info_text(
                "+7", 
                "Proyectos Públicos"
            ),
            chakra.spacer(),
            info_text(
                "+50", 
                "Certificados"
            ),
            chakra.spacer(),
            info_text(
                "+2", 
                "Idiomas"
            ),
            width="100%"
        ),
        chakra.text(
                   """
                   Bachiller en Ingeniería de Sistemas e Informática de 
                   la Universidad Nacional "Santiago Antúnez de Mayolo". Actualmente estoy 
                   especializandome en el ambito de Análisis de Datos, Data Science con Python y Desarrollo 
                   Web. Aquí podras encontrar información para contactarme.
                   !Bienvenid@s!
                   """,
                   font_size= Size.SEMIDEFAULT.value,
                   color= Txtcolor.BODY.value,
                   text_align="justify"
         ),
        spacing=Size.BIG.value,
        align_items="start",
        justify_content="center"
    )

def experience() -> int:
    return datetime.date.today().year - 2024