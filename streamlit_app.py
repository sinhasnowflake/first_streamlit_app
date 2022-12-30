import streamlit
import pandas
streamlit.title('My parents healthy diner');
streamlit.header('Breakfast Menu');
streamlit.text('almond flour pancake');
streamlit.text('almond flour waffle with kale and almond');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)



