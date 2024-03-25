import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title,sub_title
from link_bio.components.my_languages import languages_icon,auto_layout_icons
def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Perfiles"),
            link_button("LinkedIn",
                        "Mi Perfil",
                        "https://www.linkedin.com/in/deivis-luis-puertas-sabino-571752242/"
            ),
            link_button("GitHub",
                        "Mi Repositorio",
                        "https://github.com/deivispuertas"
            ),          
        title("Mis Habilidades"),
        sub_title("Lenguajes de Programación"),
            auto_layout_icons(
                    languages_icon("python.png","Python"),
                    languages_icon("java.png","Java"),
                    languages_icon("php.png","PHP"),
                    languages_icon("html.png","HTML"),
                    languages_icon("css.png","CSS"),
                ),
        sub_title("Bases de Datos"),
            auto_layout_icons(
                    languages_icon("mongodb.png","MongoDB"),
                    languages_icon("sql_server.png","SQL Server"),
                    languages_icon("mysql.png","MySQL"),
                    languages_icon("sqlite.png","SQLite"),
                    languages_icon("xampp.png","Xampp")
                ),
     #   title("Proyectos"),
      #  link_button("Proyects",
       #             "Proyectos elaborados",
        #            "/about"
         #           ),
        title("Contacto"),
            link_button("Email",
                        "Mi Correo Electrónico",
                        "mailto:deivispuertas0@gmail.com"
            ),
        width="100%"
    )