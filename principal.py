import streamlit as st
import streamlit_antd_components as sac
from modules.RegisterData import Apple
from modules.MatchAnalysis import Android, Finance
from modules.EventingData import Samsung
from modules.SchedulerData import Account
from PIL import Image

# Configuración inicial
im = Image.open("IsotipoFF0046.ico")
st.set_page_config(
    page_title="Antd components in Streamlit",
    layout='centered',
    page_icon=im
)

def Home():
    st.header('WIN STATS')
    st.markdown('''A streamlit applicatillon that uses antd components.''')

def open_external_link():
    """Muestra un enlace que abre una URL en una nueva pestaña."""
    st.markdown('''
        <a href="https://opproccesdata.streamlit.app/" target="_blank" style="text-decoration:none;">
            <button style="background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">
                Abrir OpproccesData
            </button>
        </a>
    ''', unsafe_allow_html=True)

def main():
    with st.sidebar:
        menu_item = sac.menu(
            index=0,  # La opción predeterminada seleccionada es "Home".
            open_all=False,
            items=[
                sac.MenuItem('Home', icon='calendar3'),
                sac.MenuItem(
                    'Products',
                    icon='box-fill',
                    children=[
                        sac.MenuItem('Match Analysis', icon='apple'),
                        sac.MenuItem(
                            'Google',
                            icon='google',
                            children=[
                                sac.MenuItem('Android', icon='android2'),
                                sac.MenuItem('Finance', icon='bank'),
                            ],
                        ),
                        sac.MenuItem('Samsung', icon='phone-flip'),
                    ]
                ),
                sac.MenuItem('Register Data', icon='credit-card-2-front-fill'),
                sac.MenuItem('External Link', icon='link')  # Nuevo ítem
            ],        
        )

    # Diccionario de acciones
    menu_actions = {
        'Home': Home,
        'Apple': Apple,
        'Android': Android,
        'Finance': Finance,
        'Samsung': Samsung,
        'Account': Account,
        'External Link': open_external_link  # Abre el enlace en una nueva pestaña
    }

    # Ejecutar la acción correspondiente
    if menu_item in menu_actions:
        menu_actions[menu_item]()

if __name__ == '__main__':
    main()
