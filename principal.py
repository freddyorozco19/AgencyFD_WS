import streamlit as st
import streamlit_antd_components as sac
from modules.RegisterData import Apple
from modules.MatchAnalysis import Android, Finance
from modules.EventingData import Samsung
from modules.SchedulerData import Account
from PIL import Image
im = Image.open("IsotipoFF0046.ico")
st.set_page_config(
    page_title="Antd components in Streamlit",
    layout='centered',
    page_icon=im
)

def Home():
    st.header('WIN STATS')
    st.markdown('''A streamlit applicaDSAtion that uses antd components.''')

def redirect_to_url(url):
    """Redirecciona automáticamente a una URL."""
    st.markdown(f'''
        <meta http-equiv="refresh" content="0; url={url}">
    ''', unsafe_allow_html=True)

def main():
    with st.sidebar:
        menu_item = sac.menu(
            index=0,  # refers to the Home
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
        'External Link': lambda: redirect_to_url("https://opproccesdata.streamlit.app/")  # Redirige a otra página
    }

    # Ejecutar la acción correspondiente
    if menu_item in menu_actions:
        menu_actions[menu_item]()

if __name__ == '__main__':
    main()
