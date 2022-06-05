import streamlit

streamlit.title('my parents new healthy diner')


streamlit.header('Breakfast Menu 🥣 ')
streamlit.text('Omega 3 & Blueberry Oatmeal🥗 ')
streamlit.text('🥑 kale, spinach and rocket smoothie 🍞')
streamlit.text('Hard Boiled free-range egg 🐔 ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
