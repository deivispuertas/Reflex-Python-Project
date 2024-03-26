import reflex as rx
from enum import Enum


# Constans
MAX_WIDTH="560px"

# Sizes
class Size(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    SEMIDEFAULT= "0.9em"
    DEFAULT= "1em"
    BIG= "2em"

# Styles

BASE_STYLE={    
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