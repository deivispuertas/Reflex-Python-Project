import reflex as rx
from enum import Enum
from .colors import Color as Color

# Constans
MAX_WIDTH="560px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    SEMIDEFAULT= "0.9em"
    DEFAULT= "1em"
    LARGE= "1.5em"
    BIG= "2em"
    VERY_BIG= "4em"

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
    "background_color": Color.BACKGROUND.value,   
    rx.chakra.button:{
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.chakra.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

title_style= dict(
        width="100%",   
        padding_top=Size.DEFAULT.value
)

sub_tittle_style= dict(
        width="100%",
        padding_top=Size.MEDIUM.value
)

button_tittle_style = dict(
    font_size=Size.DEFAULT.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value
)