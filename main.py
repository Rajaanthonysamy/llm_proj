import streamlit as st
import langchain_service

st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","Mexican","Arabic","Italian","Arabic"))

if cuisine:
    res=langchain_service.generate_restaurant_name_and_items(cuisine)
    st.header(res["restaurant"].strip())
    menu_items=res["menu_items"].strip().split(",")
    st.write("**** Menu Items ****")
    for item in menu_items:
        st.write("-", item)
