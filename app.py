import streamlit as st
import lang_chain_helper
st.title("Restaurant Name Suggestion App")
cusine=st.sidebar.selectbox('Pick a cuisine type:', ['Italian', 'Chinese', 'Indian', 'Mexican'])

if cusine:
    response = lang_chain_helper.generate_restaruant_name(cusine)
    st.header(response['restaurant_name'])
    menu_items = response.get('menu_items', '')
    menu_items = menu_items.split(',') if menu_items else []

    st.write("Menu Items:")
    for item in menu_items:
        st.write(item.strip())
