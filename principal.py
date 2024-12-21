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
    st.markdown('''A streamlit application that uses antd components.''')

def redirect_to_external_url():
    # URL a la que quieres redirigir
    url = "https://opproccesdata.streamlit.app/"
    
    # Código JavaScript para la redirección
    js_code = f"""
        <script>
            window.location.href = "{url}";
        </script>
    """
    st.components.v1.html(js_code, height=0)
    
    # Mensaje mientras se redirecciona
    st.info("Redirigiendo...")

def main():
    # Crear un estado para controlar la redirección
    if 'redirect_requested' not in st.session_state:
        st.session_state.redirect_requested = False

    with st.sidebar:
        menu_item = sac.menu(
            index=0,
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
                sac.MenuItem('Otra App', icon='box-arrow-up-right'),
            ],        
        )

    # Si se selecciona "Otra App", activar la redirección
    if menu_item == 'Otra App' and not st.session_state.redirect_requested:
        st.session_state.redirect_requested = True
        redirect_to_external_url()
    else:
        menu_actions = {
            'Home': Home,
            'Apple': Apple,
            'Android': Android,
            'Finance': Finance,
            'Samsung': Samsung,
            'Account': Account
        }
        if menu_item in menu_actions:
            menu_actions[menu_item]()

if __name__ == '__main__':
    main()
