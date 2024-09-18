import streamlit as st
from snowflake.snowpark.functions import col
import pandas as pd

st.title(":cup_with_straw: Customize Your Smoothie  :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie")

cnx = st.connection("snowflake")
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)
order_name = st.text_input('Name on Smoothie:')
ingredients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe, max_selections=5)


if ingredients_list and order_name:
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    #st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,NAME_ON_ORDER) values ('""" + ingredients_string + """','"""+order_name+"""')"""
    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")



