import streamlit as st
import streamlit_antd_components as sac
import webbrowser
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
    st.markdown('''A strea23mlit application that uses antd components.''')

def open_url():
    webbrowser.open_new_tab('https://opproccesdata.streamlit.app/')
    st.stop()  # Detiene la ejecución después de abrir la URL

def main():
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
                sac.MenuItem('Otra App', icon='box-arrow-up-right')
            ],        
        )

    menu_actions = {
        'Home': Home,
        'Apple': Apple,
        'Android': Android,
        'Finance': Finance,
        'Samsung': Samsung,
        'Account': Account,
        'Otra App': open_url
    }

    if menu_item in menu_actions:
        menu_actions[menu_item]()

if __name__ == '__main__':
    main()
