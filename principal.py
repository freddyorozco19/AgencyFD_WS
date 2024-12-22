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

@st.cache_resource
def get_other_url():
   return "https://opproccesdata.streamlit.app/"

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
               # La URL como ítem del menú
               sac.MenuItem('https://opproccesdata.streamlit.app/', icon='box-arrow-up-right')
           ],        
       )

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
   elif menu_item == 'https://opproccesdata.streamlit.app/':
       st.markdown(f'[Haz clic aquí para ir a la aplicación]({menu_item})')

if __name__ == '__main__':
   main()
