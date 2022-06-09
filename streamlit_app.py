import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parents new healthy diner')


streamlit.header('Breakfast Menu 🥣 ')
streamlit.text('Omega 3 & Blueberry Oatmeal🥗 ')
streamlit.text('🥑 kale, spinach and rocket smoothie 🍞')
streamlit.text('Hard Boiled free-range egg 🐔 ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#lets put a picklist so users can pcik the fruit they want
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice ')
try:
  fruit_choice =streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information:")
  else:
      back_from_function = get_fruitvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
   

except URLError as e:
  streamlit.error(1)

#import snowflake.connector

streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()
#add a button to the load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx = close()
    streamlit.dataframe(my_data_rows)

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice ')


#new Allow the end user to add the fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
        return('Thanks for adding', new_fruit)

add_my_fruit =streamlit.text_input('what fruit would you like to add?') 
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_frunction = insert_row_snowflake(add_my_fruit)
    stremlit.text(back_from_function)
    
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ add_my_fruit)

#This will not work correctly, but go with it for now


