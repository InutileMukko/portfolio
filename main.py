import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images\photo.png')

with col2:
    st.title('Ivan Donati')
    content = '''
    my info here\n
    more infos\n
    other things
    '''
    st.info(content)

intro = 'Below you can find some apps I built using Python. Please contact me if you like!'
st.write(intro)
