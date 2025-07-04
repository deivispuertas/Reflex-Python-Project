import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title,sub_title
from link_bio.components.my_languages import languages_icon,auto_layout_icons
from link_bio.styles.styles import Size as Size
import reflex_chakra as chakra

def links() -> rx.Component:
        return chakra.vstack(
                title("Perfiles"),
                link_button(
                        "LinkedIn",
                        "Mi Perfil",
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL
                ),
                link_button(
                        "GitHub",
                        "Mi Repositorio",
                        "icons/github.svg",
                        const.GITHUB_URL
                ),         
                title("Mis Habilidades"),
                sub_title("Lenguajes de Programación"),
                        auto_layout_icons(
                                languages_icon(
                                        "python.png",
                                        "Python"
                                ),
                                languages_icon(
                                        "java.png",
                                        "Java"
                                ),
                                languages_icon(
                                        "php.png",
                                        "PHP"
                                ),
                                languages_icon(
                                        "html.png",
                                        "HTML"
                                ),
                                languages_icon(
                                        "css.png",
                                        "CSS"
                                ),
                        ),
                sub_title("Bases de Datos"),
                        auto_layout_icons(
                                languages_icon(
                                        "mongodb.png",
                                        "MongoDB"
                                ),
                                languages_icon(
                                        "sql_server.png",
                                        "SQL Server"
                                ),
                                languages_icon(
                                        "mysql.png",
                                        "MySQL"
                                ),
                                languages_icon(
                                        "sqlite.png",
                                        "SQLite"
                                ),
                                languages_icon(
                                        "xampp.png",
                                        "Xampp"
                                ),
                                languages_icon(
                                        "oracle.png",
                                        "Oracle"
                                ),
                                languages_icon(
                                "postgre.png",
                                "Postgre SQL"
                                )
                        ),
                sub_title('Softwares de Análisis'),
                        auto_layout_icons(
                                languages_icon(
                                "powerbi.png",
                                "Power BI"
                                ),
                                languages_icon(
                                "tableau.png",
                                "Tableau"
                                ),
                                languages_icon(
                                "googleanalytics.png",
                                "Google Analytics"
                                ),
                                languages_icon(
                                "googlecolab.png",
                                "Google Colab"
                                ),
                                languages_icon(
                                "jupyter.png",
                                "Jupyter"
                                ),
                        ),
                sub_title("Plus"),
                        auto_layout_icons(
                                languages_icon("git.png"
                                        ,"Git"
                                ),
                                languages_icon("blender.png",
                                        "Blender"
                                ),
                                languages_icon("adobe_photoshop.png",
                                        "Photoshop"
                                ),
                                languages_icon("vensim_logo.png",
                                        "Vensim PLE"
                                )
                        ),
        #   title("Proyectos"),
        #  link_button("Proyects",
        #             "Proyectos elaborados",
                #            "/about"
                #           ),
                title("Contactos"),
                link_button("Email",
                        "Mi Correo Electrónico",
                        "icons/email.svg",
                        const.GMAIL_URL
                ),
                # title("Curriculum Vitae"),
                width="100%",
                spacing=Size.MEDIUM.value,
        )