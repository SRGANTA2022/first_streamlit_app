import streamlit

streamlit.title('my parents new healthy diner')


streamlit.header('Breakfast Menu 🥣 ')
streamlit.text('Omega 3 & Blueberry Oatmeal🥗 ')
streamlit.text('🥑 kale, spinach and rocket smoothie 🍞')
streamlit.text('Hard Boiled free-range egg 🐔 ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#lets put a picklist so users can pcik the fruit they want
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice ')

fruit_choice =streamlit.text_input('what fruit would you like information about?','kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

                                   
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
