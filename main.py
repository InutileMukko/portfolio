import streamlit as st
import pandas

# st.set_page_config(layout='wide') # rende a video tutte le immagini più grandi

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

# col3, col4 = st.columns(2) # due colonne, si dividono equamente lo spazio
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
# tre colonne, quella di mezzo vuota, i numeri sono le dimensioni relative, quelle ai lati 3 volte quella in mezzo

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images\\{row['image']}")
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images\\{row['image']}")
        st.write(f"[Source code]({row['url']})")
