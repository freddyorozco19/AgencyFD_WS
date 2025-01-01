import streamlit as st
import streamlit_antd_components as sac
from modules.RegisterData import RegisterData
from modules.MatchAnalysis import Android, Finance
from modules.EventingData import Samsung
from modules.SchedulerData import Account
from PIL import Image

# Configuración inicial
im = Image.open("IsotipoFF0046.ico")
st.set_page_config(
    page_title="Antd components in Streamlit",
    layout='centered',
    page_icon=im)
def Home():
    st.header('WIN STATS')
    st.markdown('''A streamlit application that uses antd components.''')
def redirect_to_new_tab(url):
    """Abre una URL directamente en una nueva pestaña."""
    st.markdown(f'''
        <script>
            window.open("{url}", "_blank");
        </script>
    ''', unsafe_allow_html=True)
def main():
    with st.sidebar:
        menu_item = sac.menu(
            index=0,  # La opción predeterminada seleccionada es "Home".
            open_all=False,
            items=[
                sac.MenuItem('Home', icon='calendar3'),
                sac.MenuItem('Samsung', icon='box-fill',
                    children=[
                        sac.MenuItem('Match Analysis', icon='apple'),
                        sac.MenuItem('Google', icon='google',
                            children=[
                                sac.MenuItem('Android', icon='android2'),
                                sac.MenuItem('Finance', icon='bank'),
                            ],
                        ),
                        sac.MenuItem('Products', icon='phone-flip'),
                    ]
                ),
                sac.MenuItem('RegisterData', icon='credit-card-2-front-fill', 
                    children=[
                        sac.MenuItem('Football Division', icon='bank'),
                        sac.MenuItem('Colombian Players', icon='apple'),
                        sac.MenuItem('Colombian U23 Players', icon='link')],        
                ),
                sac.MenuItem('Storage', icon='bank')
        ]
        )
        st.divider()
    # Diccionario de acciones
    menu_actions = {
        'Home': Home,
        'RegisterData': RegisterData,
        'Android': Android,
        'Finance': Finance,
        'Samsung': Samsung,
        'Account': Account,
        'External Link': lambda: redirect_to_new_tab("https://opproccesdata.streamlit.app/")  # Redirige automáticamente
    }
    # Ejecutar la acción correspondiente
    if menu_item in menu_actions:
        menu_actions[menu_item]()
if __name__ == '__main__':
    main()
