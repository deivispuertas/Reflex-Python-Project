import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as Txtcolor
from .fonts import Font, FontWeight

# Constans
MAX_WIDTH="560px"

# Sizes

STYLESHEETS= [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

class Size(Enum):
    ZERO = "0px !important"
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    SEMIDEFAULT= "0.9em"
    DEFAULT= "1em"
    LARGE= "1.5em"
    BIG= "2em"
    VERY_BIG= "4em"
    MUCH_BIG= "6em"

#Spacing 
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"


# Styles

BASE_STYLE={ 
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGTH.value,
    "background_color": Color.BACKGROUND.value,  
    rx.chakra.heading: {
        "color": Txtcolor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    }, 
    rx.chakra.button:{
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": Txtcolor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.chakra.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style= dict(
       font_family= Font.LOGO.value,
       font_weight= FontWeight.MEDIUM.value,
       font_size= Size.LARGE.value
)

title_style= dict(
        width= "100%",
        padding_top= Size.DEFAULT.value
)

sub_tittle_style= dict(
        width= "100%",
        font_family= Font.TITLE.value,
        font_weight= FontWeight.MEDIUM.value,
        padding_top= Size.MEDIUM.value,
        color= Txtcolor.CONTENT_SUB.value
)

button_tittle_style = dict(
    font_family= Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size= Size.DEFAULT.value,
    color= Txtcolor.HEADER.value
)

button_body_style = dict(
    font_weight= FontWeight.LIGTH.value,
    font_size= Size.MEDIUM.value,
    color= Txtcolor.CONTENT.value
)

languaje_body_style = dict(
    font_weight= FontWeight.MEDIUM.value,
    font_size= Size.MEDIUM.value,
    color= Txtcolor.CONTENT_IMAGES.value
)